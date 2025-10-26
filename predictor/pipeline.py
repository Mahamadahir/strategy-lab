"""
High-level orchestration for the stock prediction workflow.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable, Sequence

import pandas as pd

from .data_ingestion import DataIngestor
from .feature_engineering import FeatureEngineer
from .modeling import ModelRegistry, ModelTrainer, StockPredictor
from .monitoring import MonitoringService


@dataclass
class PipelineConfig:
    """Runtime configuration for the prediction pipeline."""

    symbols: Sequence[str]
    horizon_days: int
    retrain_frequency: str
    cache_dir: Path


class PredictionPipeline:
    """Coordinates the ingestion, training, inference, and monitoring stages."""

    def __init__(
        self,
        config: PipelineConfig,
        ingestor: DataIngestor,
        engineer: FeatureEngineer,
        trainer: ModelTrainer,
        registry: ModelRegistry,
        predictor: StockPredictor,
        monitor: MonitoringService,
    ):
        self.config = config
        self.ingestor = ingestor
        self.engineer = engineer
        self.trainer = trainer
        self.registry = registry
        self.predictor = predictor
        self.monitor = monitor

    def backfill_history(self, start: str, end: str) -> None:
        """Download and cache historical data for symbols in scope."""
        raise NotImplementedError

    def run_training_cycle(self, as_of: datetime) -> str:
        """Produce a trained model and return its identifier."""
        raise NotImplementedError

    def run_inference(self, symbol: str, as_of: datetime) -> pd.Series:
        """Generate predictions for a single symbol on demand."""
        raise NotImplementedError

    def batch_inference(self, symbols: Iterable[str], as_of: datetime) -> pd.DataFrame:
        """Run batched predictions for monitoring or portfolio updates."""
        raise NotImplementedError

    def evaluate_live_performance(self, model_id: str, window: int) -> dict:
        """Summarise live-versus-expected performance for reporting."""
        raise NotImplementedError

    def schedule_jobs(self) -> None:
        """Register pipeline runs with the chosen orchestration framework."""
        raise NotImplementedError
