"""
Model management, training, and inference contracts.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

import pandas as pd

from .feature_engineering import FeatureEngineer


class ModelTrainer:
    """Handles model instantiation, training, validation, and persistence."""

    def __init__(self, model_config: Mapping[str, Any], registry: "ModelRegistry"):
        self.model_config = model_config
        self.registry = registry

    def build_model(self) -> Any:
        """Create an untrained model instance according to the config."""
        raise NotImplementedError

    def train(self, model: Any, features: pd.DataFrame, targets: pd.Series) -> Any:
        """Fit the model using the provided dataset."""
        raise NotImplementedError

    def evaluate(self, model: Any, features: pd.DataFrame, targets: pd.Series) -> Mapping[str, float]:
        """Return validation metrics for model selection."""
        raise NotImplementedError

    def save_artifacts(self, model: Any, metrics: Mapping[str, float]) -> Path:
        """Persist the trained model and metadata via the registry."""
        raise NotImplementedError


class ModelRegistry:
    """Simple registry for versioned models and metadata."""

    def __init__(self, storage_path: Path):
        self.storage_path = storage_path

    def register(self, model_path: Path, metrics: Mapping[str, float]) -> str:
        """Store metadata and return the registered model identifier."""
        raise NotImplementedError

    def load(self, model_id: str) -> Any:
        """Load a model artifact by identifier."""
        raise NotImplementedError

    def latest(self) -> str:
        """Return the identifier for the most recent production candidate."""
        raise NotImplementedError


class StockPredictor:
    """Wraps inference-time concerns."""

    def __init__(self, registry: ModelRegistry, preprocessor: FeatureEngineer):
        self.registry = registry
        self.preprocessor = preprocessor

    def load_model(self, model_id: str | None = None) -> Any:
        """Eagerly load the requested model (or default to the latest)."""
        raise NotImplementedError

    def predict(self, model: Any, data: pd.DataFrame) -> pd.Series:
        """Generate predictions for the supplied dataset."""
        raise NotImplementedError

    def explain(self, model: Any, data: pd.DataFrame) -> Mapping[str, float]:
        """Return feature attributions or other explainability outputs."""
        raise NotImplementedError
