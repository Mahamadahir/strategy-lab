"""
Skeleton package for the forthcoming stock predictor workflow.

Each module defines the boundaries for data collection, feature engineering,
model training, inference serving, and monitoring. Implementations are left
intentionally blank so future iterations can slot in concrete logic while
re-using the shared interfaces.
"""

from .data_ingestion import DataIngestor
from .feature_engineering import FeatureEngineer
from .modeling import ModelRegistry, ModelTrainer, StockPredictor
from .pipeline import PredictionPipeline
from .monitoring import MonitoringService

__all__ = [
    "DataIngestor",
    "FeatureEngineer",
    "ModelRegistry",
    "ModelTrainer",
    "StockPredictor",
    "PredictionPipeline",
    "MonitoringService",
]
