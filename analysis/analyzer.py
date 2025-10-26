"""
Analyze backtest results and propose improvements.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

from backtest.backtester import BacktestResult
from strategies.mutator import mutate_strategy


@dataclass(slots=True)
class AnalysisReport:
    issues: List[str]
    recommendations: List[str]
    candidate_mutation: Dict


class StrategyAnalyzer:
    """
    Inspects a `BacktestResult` and synthesises improvement ideas.
    """

    def __init__(self, max_drawdown_threshold: float = -0.2, sharpe_threshold: float = 0.7):
        self.max_drawdown_threshold = max_drawdown_threshold
        self.sharpe_threshold = sharpe_threshold

    def analyze(self, result: BacktestResult) -> AnalysisReport:
        metrics = result.metrics
        issues: List[str] = []
        recommendations: List[str] = []

        if metrics["max_drawdown"] < self.max_drawdown_threshold:
            issues.append(f"High drawdown ({metrics['max_drawdown']:.2%})")
            recommendations.append("Tighten exits or blend slower trend filter.")

        if metrics["sharpe"] < self.sharpe_threshold:
            issues.append(f"Weak risk-adjusted returns (Sharpe {metrics['sharpe']:.2f})")
            recommendations.append("Consider smoothing signals or reducing leverage.")

        if metrics["profit_factor"] < 1.1:
            issues.append(f"Low profit factor ({metrics['profit_factor']:.2f})")
            recommendations.append("Adjust entry thresholds to improve selectivity.")

        if not issues:
            recommendations.append("Strategy performing within thresholds. Minor parameter tweaks only.")

        mutated = mutate_strategy(result.strategy, strength=0.15)
        candidate_mutation = mutated.to_dict()

        return AnalysisReport(
            issues=issues,
            recommendations=recommendations,
            candidate_mutation=candidate_mutation,
        )
