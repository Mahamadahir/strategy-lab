"""
Transforms merged datasets into model-ready features and targets.
"""

from __future__ import annotations

from typing import Iterable, Tuple

import pandas as pd


class FeatureEngineer:
    """Feature computation, labelling, and persistence."""

    def __init__(self, feature_config: dict):
        self.feature_config = feature_config

    def build_feature_matrix(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Derive model features from the raw/merged dataset.
        """
        raise NotImplementedError

    def generate_targets(self, data: pd.DataFrame, horizon: int) -> pd.Series:
        """
        Produce labels (e.g., future returns or classification buckets).
        """
        raise NotImplementedError

    def select_features(self, features: pd.DataFrame) -> pd.DataFrame:
        """Filter and reorder features based on configuration or importance."""
        raise NotImplementedError

    def persist_features(self, features: pd.DataFrame, targets: pd.Series) -> Tuple[pd.DataFrame, pd.Series]:
        """
        Store engineered features/targets and return handles for downstream steps.
        """
        raise NotImplementedError
