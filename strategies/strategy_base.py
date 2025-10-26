"""
Base abstractions for trading strategies.
"""

from __future__ import annotations

import abc
from dataclasses import dataclass, field
from typing import Dict

import pandas as pd

Signal = pd.Series


@dataclass(slots=True)
class StrategyConfig:
    name: str
    params: Dict[str, float] = field(default_factory=dict)
    risk_per_trade: float = 0.01


class Strategy(abc.ABC):
    """
    All strategies must implement `generate_signals`.
    """

    def __init__(self, config: StrategyConfig | None = None):
        self.config = config or StrategyConfig(name=self.__class__.__name__)

    def __repr__(self) -> str:  # pragma: no cover - convenience
        return f"{self.__class__.__name__}(params={self.config.params})"

    @staticmethod
    def _validate_data(data: pd.DataFrame):
        required = {"Open", "High", "Low", "Close", "Volume"}
        missing = required - set(data.columns)
        if missing:
            raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")

    @abc.abstractmethod
    def generate_signals(self, data: pd.DataFrame) -> Signal:
        """
        Produce position signals (-1, 0, 1) aligning with `data.index`.
        """

    def to_dict(self) -> Dict[str, float]:
        return {"name": self.config.name, **self.config.params}
