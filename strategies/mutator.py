"""
Mutation helpers for strategy optimisation loops.
"""

from __future__ import annotations

import random
from copy import deepcopy
from typing import Callable

from .strategy_base import Strategy


def mutate_strategy(strategy: Strategy, strength: float = 0.1, rng: random.Random | None = None) -> Strategy:
    rng = rng or random.Random()
    mutated = deepcopy(strategy)
    params = mutated.config.params
    for key, value in params.items():
        if isinstance(value, (int, float)):
            jitter = 1 + rng.uniform(-strength, strength)
            new_value = value * jitter
            if isinstance(value, int):
                new_value = max(1, int(round(new_value)))
            params[key] = new_value
    return mutated


def mutate_population(strategies: list[Strategy], mutate_fn: Callable[[Strategy], Strategy] | None = None) -> list[Strategy]:
    mutate_fn = mutate_fn or mutate_strategy
    return [mutate_fn(strategy) for strategy in strategies]
