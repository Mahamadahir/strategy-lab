"""
Vectorised backtesting utilities.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

import numpy as np
import pandas as pd

from strategies.strategy_base import Strategy


@dataclass(slots=True)
class BacktestConfig:
    initial_capital: float = 10000.0
    trading_cost_bps: float = 5.0  # round-trip commission
    slippage_bps: float = 1.0


@dataclass(slots=True)
class BacktestResult:
    strategy: Strategy
    equity_curve: pd.Series
    metrics: Dict[str, float]
    trades: pd.DataFrame
    signals: pd.Series


def _compute_drawdown(equity: pd.Series) -> pd.Series:
    cumulative_max = equity.cummax()
    drawdown = equity / cumulative_max - 1
    return drawdown


def _build_trade_log(position: pd.Series, equity: pd.Series) -> pd.DataFrame:
    trades = []
    current = None
    prev_pos = 0.0
    for timestamp, pos in position.items():
        pos = float(pos)
        sign = np.sign(pos)

        if prev_pos == 0 and sign != 0:
            current = {
                "entry": timestamp,
                "direction": sign,
                "entry_equity": equity.loc[timestamp],
            }
        elif prev_pos != 0 and sign == 0:
            if current:
                current["exit"] = timestamp
                current["exit_equity"] = equity.loc[timestamp]
                current["pnl"] = current["exit_equity"] - current["entry_equity"]
                trades.append(current)
                current = None
        elif prev_pos != 0 and sign != 0 and np.sign(prev_pos) != sign:
            if current:
                current["exit"] = timestamp
                current["exit_equity"] = equity.loc[timestamp]
                current["pnl"] = current["exit_equity"] - current["entry_equity"]
                trades.append(current)
            current = {
                "entry": timestamp,
                "direction": sign,
                "entry_equity": equity.loc[timestamp],
            }
        prev_pos = pos

    if current:
        current["exit"] = position.index[-1]
        current["exit_equity"] = equity.iloc[-1]
        current["pnl"] = current["exit_equity"] - current["entry_equity"]
        trades.append(current)

    if not trades:
        return pd.DataFrame(columns=["entry", "exit", "direction", "pnl", "entry_equity", "exit_equity"])

    df = pd.DataFrame(trades)
    return df[["entry", "exit", "direction", "pnl", "entry_equity", "exit_equity"]]


class Backtester:
    def __init__(self, config: BacktestConfig | None = None):
        self.config = config or BacktestConfig()

    def run(self, strategy: Strategy, market_data: pd.DataFrame) -> BacktestResult:
        strategy._validate_data(market_data)
        signals = strategy.generate_signals(market_data)
        signals = signals.astype(float).clip(-1, 1).reindex(market_data.index).fillna(0)
        position = signals.shift(1).fillna(0)

        returns = market_data["Close"].pct_change().fillna(0)
        gross = position * returns

        turnover = position.diff().abs().fillna(0)
        cost_rate = (self.config.trading_cost_bps + self.config.slippage_bps) / 10000
        costs = turnover * cost_rate
        net_returns = gross - costs

        equity = (1 + net_returns).cumprod() * self.config.initial_capital

        metrics = self._compute_metrics(equity, net_returns)
        trades = _build_trade_log(position, equity)

        return BacktestResult(
            strategy=strategy,
            equity_curve=equity,
            metrics=metrics,
            trades=trades,
            signals=signals,
        )

    def _compute_metrics(self, equity: pd.Series, returns: pd.Series) -> Dict[str, float]:
        total_return = equity.iloc[-1] / equity.iloc[0] - 1
        daily_ret = returns
        ann_factor = 252
        cagr = (1 + total_return) ** (ann_factor / len(daily_ret)) - 1 if len(daily_ret) else 0.0
        volatility = daily_ret.std() * np.sqrt(ann_factor)
        sharpe = (daily_ret.mean() * ann_factor) / (volatility + 1e-9)
        drawdown = _compute_drawdown(equity)
        max_drawdown = drawdown.min()
        positive = daily_ret[daily_ret > 0].sum()
        negative = -daily_ret[daily_ret < 0].sum()
        profit_factor = positive / (negative + 1e-9)

        return {
            "total_return": float(total_return),
            "cagr": float(cagr),
            "volatility": float(volatility),
            "sharpe": float(sharpe),
            "max_drawdown": float(max_drawdown),
            "profit_factor": float(profit_factor),
        }
