"""
Random strategy generation utilities.
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import List, Sequence

import pandas as pd

from .strategy_base import Signal, Strategy, StrategyConfig


def _rsi(series: pd.Series, period: int) -> pd.Series:
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1 / period, min_periods=period).mean()
    avg_loss = loss.ewm(alpha=1 / period, min_periods=period).mean()
    rs = avg_gain / (avg_loss + 1e-9)
    return 100 - (100 / (1 + rs))


class MovingAverageCrossoverStrategy(Strategy):
    def generate_signals(self, data: pd.DataFrame) -> Signal:
        self._validate_data(data)
        short = data["Close"].rolling(window=int(self.config.params["short_window"]), min_periods=1).mean()
        long = data["Close"].rolling(window=int(self.config.params["long_window"]), min_periods=1).mean()
        signal = pd.Series(0, index=data.index, dtype=float)
        signal[short > long] = 1
        signal[short < long] = -1
        return signal.ffill().fillna(0)


class RSIMeanReversionStrategy(Strategy):
    def generate_signals(self, data: pd.DataFrame) -> Signal:
        self._validate_data(data)
        rsi = _rsi(data["Close"], int(self.config.params["period"]))
        lower = self.config.params["lower"]
        upper = self.config.params["upper"]
        signal = pd.Series(0, index=data.index, dtype=float)
        signal[rsi < lower] = 1
        signal[rsi > upper] = -1
        return signal.ffill().fillna(0)


class MACDStrategy(Strategy):
    def generate_signals(self, data: pd.DataFrame) -> Signal:
        self._validate_data(data)
        fast = data["Close"].ewm(span=int(self.config.params["fast"]), adjust=False).mean()
        slow = data["Close"].ewm(span=int(self.config.params["slow"]), adjust=False).mean()
        signal_line = fast - slow
        trigger = signal_line.ewm(span=int(self.config.params["signal"]), adjust=False).mean()
        signal = pd.Series(0, index=data.index, dtype=float)
        signal[(signal_line > trigger)] = 1
        signal[(signal_line < trigger)] = -1
        return signal.ffill().fillna(0)


@dataclass
class StrategyFactory:
    rng: random.Random

    def moving_average(self) -> Strategy:
        short = self.rng.randint(5, 20)
        long = self.rng.randint(short + 5, short + 80)
        config = StrategyConfig(
            name="MA Crossover",
            params={"short_window": short, "long_window": long},
        )
        return MovingAverageCrossoverStrategy(config)

    def rsi(self) -> Strategy:
        period = self.rng.randint(10, 21)
        lower = self.rng.randint(20, 35)
        upper = self.rng.randint(65, 80)
        config = StrategyConfig(
            name="RSI Mean Reversion",
            params={"period": period, "lower": float(lower), "upper": float(upper)},
        )
        return RSIMeanReversionStrategy(config)

    def macd(self) -> Strategy:
        fast = self.rng.randint(8, 15)
        slow = self.rng.randint(fast + 5, fast + 20)
        signal = self.rng.randint(5, 10)
        config = StrategyConfig(
            name="MACD Trend",
            params={"fast": fast, "slow": slow, "signal": signal},
        )
        return MACDStrategy(config)


class StrategyGenerator:
    """
    Produce strategies via random sampling, crossover, and mutation.
    """

    def __init__(self, seed: int | None = None):
        self.rng = random.Random(seed)
        self.factory = StrategyFactory(self.rng)
        self._builders = [
            self.factory.moving_average,
            self.factory.rsi,
            self.factory.macd,
        ]

    def random_strategy(self) -> Strategy:
        return self.rng.choice(self._builders)()

    def generate(self, n: int) -> List[Strategy]:
        return [self.random_strategy() for _ in range(n)]

    def crossover(self, parents: Sequence[Strategy]) -> Strategy:
        if len(parents) != 2:
            raise ValueError("crossover expects exactly two parents")
        a, b = parents
        if a.__class__ is not b.__class__:
            return self.random_strategy()
        params = {}
        for key in a.config.params:
            params[key] = self.rng.choice([a.config.params[key], b.config.params[key]])
        config = StrategyConfig(name=f"{a.config.name} x {b.config.name}", params=params)
        return a.__class__(config=config)
