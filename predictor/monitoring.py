"""
Monitoring and observability hooks for the stock predictor.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Mapping

import pandas as pd


@dataclass
class MonitoringEvent:
    """Simple container for prediction outputs and metadata."""

    symbol: str
    timestamp: datetime
    prediction: float
    actual: float | None


class MonitoringService:
    """Surface key metrics, quality checks, and alerts."""

    def __init__(self, sink: str):
        self.sink = sink

    def log_predictions(self, batch: pd.DataFrame) -> None:
        """Persist raw predictions and metadata for auditing."""
        raise NotImplementedError

    def detect_drift(self, features: pd.DataFrame, predictions: pd.Series) -> Mapping[str, float]:
        """Compute drift metrics for features and residuals."""
        raise NotImplementedError

    def trigger_alerts(self, message: str, severity: str) -> None:
        """Send alerts to the configured sink."""
        raise NotImplementedError

    def compile_report(self, window: int) -> Mapping[str, float]:
        """Aggregate metrics into an executive-friendly dashboard."""
        raise NotImplementedError
