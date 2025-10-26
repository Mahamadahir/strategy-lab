"""
CLI orchestrator for the strategy lab pipeline.
"""

from __future__ import annotations

import argparse
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import List

import pandas as pd
import yfinance as yf

from analysis.analyzer import StrategyAnalyzer
from backtest.backtester import BacktestConfig, Backtester, BacktestResult
from strategies import Strategy, StrategyGenerator, mutate_population

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
)
logger = logging.getLogger("strategy-lab")


def fetch_history(symbol: str, start: str | None, end: str | None) -> pd.DataFrame:
    ticker = yf.Ticker(symbol)
    df = ticker.history(start=start, end=end, interval="1d", auto_adjust=False, actions=False)
    if df.empty:
        raise RuntimeError(f"No data downloaded for {symbol}")
    df.index.name = "Datetime"
    return df


@dataclass
class StrategyScore:
    strategy: Strategy
    backtest: BacktestResult
    score: float


def score_result(result: BacktestResult) -> float:
    metrics = result.metrics
    return metrics["total_return"] - abs(metrics["max_drawdown"])


def run_iteration(
    strategies: List[Strategy],
    data: pd.DataFrame,
    backtester: Backtester,
    analyzer: StrategyAnalyzer,
) -> List[StrategyScore]:
    scored: List[StrategyScore] = []
    for strategy in strategies:
        bt_result = backtester.run(strategy, data)
        analysis = analyzer.analyze(bt_result)
        logger.info(
            "%s -> return %.2f%%, sharpe %.2f, drawdown %.2f%%",
            strategy.config.name,
            bt_result.metrics["total_return"] * 100,
            bt_result.metrics["sharpe"],
            bt_result.metrics["max_drawdown"] * 100,
        )
        if analysis.issues:
            logger.info("  Issues: %s", "; ".join(analysis.issues))
        logger.info("  Recommendation: %s", "; ".join(analysis.recommendations))
        scored.append(StrategyScore(strategy=strategy, backtest=bt_result, score=score_result(bt_result)))
    return scored


def parse_args(argv: list[str] | None = None):
    parser = argparse.ArgumentParser(description="Strategy lab pipeline.")
    parser.add_argument("--symbol", default="AAPL")
    parser.add_argument("--start", default="2020-01-01")
    parser.add_argument("--end", default=None)
    parser.add_argument("--population", type=int, default=5, help="Strategies per generation")
    parser.add_argument("--iterations", type=int, default=2, help="Evolution cycles")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--initial-capital", type=float, default=10000.0)
    parser.add_argument("--cache", default="strategy-lab/data", help="Optional CSV cache location")
    return parser.parse_args(argv)


def maybe_cache_data(df: pd.DataFrame, cache_path: Path | None):
    if cache_path is None:
        return
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(cache_path)
    logger.info("Cached data to %s", cache_path)


def main(argv: list[str] | None = None):
    args = parse_args(argv)
    cache_path = Path(args.cache) / f"{args.symbol}.csv" if args.cache else None

    if cache_path and cache_path.exists():
        data = pd.read_csv(cache_path, parse_dates=["Datetime"], index_col="Datetime")
        logger.info("Loaded cached data from %s", cache_path)
    else:
        data = fetch_history(args.symbol, args.start, args.end)
        maybe_cache_data(data, cache_path)

    generator = StrategyGenerator(seed=args.seed)
    backtester = Backtester(BacktestConfig(initial_capital=args.initial_capital))
    analyzer = StrategyAnalyzer()

    population = generator.generate(args.population)
    for iteration in range(args.iterations):
        logger.info("=== Iteration %d ===", iteration + 1)
        scored = run_iteration(population, data, backtester, analyzer)
        scored.sort(key=lambda item: item.score, reverse=True)
        top = scored[: max(1, len(scored) // 2)]
        logger.info("Top strategy: %s -> metrics %s", top[0].strategy.config.name, top[0].backtest.metrics)
        population = [entry.strategy for entry in top]
        mutated = mutate_population(population)
        population.extend(mutated)


if __name__ == "__main__":  # pragma: no cover
    main()
