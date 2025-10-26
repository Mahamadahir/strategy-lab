"""
Data ingestion layer for the stock predictor.

Defines the boundary between external data providers and the internal pipeline.
Concrete implementations should provide connectors for market data vendors,
fundamental datasets, and alternative signals.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

import pandas as pd


class DataIngestor:
    """Collects and caches all raw inputs required by the predictor."""

    def __init__(self, cache_dir: Path, providers: Mapping[str, Any]):
        self.cache_dir = cache_dir
        self.providers = providers

    def fetch_price_history(self, symbol: str, start: str, end: str) -> pd.DataFrame:
        """Pull OHLCV history from the configured market data provider."""
        raise NotImplementedError

    def fetch_fundamental_snapshot(self, symbol: str) -> pd.DataFrame:
        """Retrieve balance sheet, income statement, and cash flow metrics."""
        raise NotImplementedError

    def fetch_alternative_signals(self, symbol: str) -> pd.DataFrame:
        """Load sentiment, macro indicators, or alternative datasets."""
        raise NotImplementedError

    def merge_sources(self, datasets: Mapping[str, pd.DataFrame]) -> pd.DataFrame:
        """Align and join disparate data sources into a unified frame."""
        raise NotImplementedError

    def cache_dataset(self, name: str, df: pd.DataFrame) -> Path:
        """
        Persist the raw dataset for reproducibility and offline development.
        """
        raise NotImplementedError
