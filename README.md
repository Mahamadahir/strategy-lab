# Strategy Lab

Modular experimentation environment for generating, backtesting, and improving trading strategies, now expanding into a production-ready stock predictor.

## Vision
- Provide an end-to-end research-to-production workflow that transforms raw market data into actionable stock predictions.
- Maintain a modular architecture so data ingestion, feature engineering, modeling, and monitoring can evolve independently.
- Ship a reliable predictor that can be scheduled, audited, and continuously improved through the Strategy Lab toolchain.

## Current Modules
- `strategies/` - randomisable building blocks (MA crossover, RSI mean reversion, MACD) plus mutation utilities.
- `backtest/` - vectorised backtester that factors in slippage and commissions.
- `analysis/` - post-run analyser that highlights weaknesses and proposes parameter tweaks.
- `main.py` - CLI orchestrator for running iterative optimisation loops.

## Project Skeleton
```text
strategy-lab/
├── analysis/
│   ├── __init__.py
│   └── analyzer.py
├── backtest/
│   ├── __init__.py
│   └── backtester.py
├── predictor/
│   ├── __init__.py
│   ├── data_ingestion.py
│   ├── feature_engineering.py
│   ├── modeling.py
│   ├── monitoring.py
│   └── pipeline.py
├── strategies/
│   ├── __init__.py
│   ├── generator.py
│   ├── mutator.py
│   └── strategy_base.py
├── data/
├── main.py
└── requirements.txt
```

### Key Contracts
- `DataIngestor`: connectors for market, fundamental, and alternative data plus raw cache management.
- `FeatureEngineer`: transforms merged datasets into model-ready features and labels.
- `ModelTrainer` and `ModelRegistry`: build, evaluate, and version models; persist artifacts for inference.
- `StockPredictor`: wraps feature prep and prediction-time logic.
- `PredictionPipeline`: orchestrates ingestion, training, inference, and scheduling.
- `MonitoringService`: captures prediction telemetry, drift checks, and reporting hooks.

## 10-Week Roadmap
| Week | Focus | Milestones |
| ---- | ----- | ---------- |
| 1 | Foundations | Finalise prediction scope, audit data vendors, create ingestion config stub. |
| 2 | Data Ingestion | Implement price/fundamental collectors, establish caching, smoke-test merges. |
| 3 | Feature Engineering | Define labelling strategy, prototype feature set, document feature config. |
| 4 | Dataset Management | Stand up dataset versioning, add splitting utilities, write EDA notebooks. |
| 5 | Baseline Modeling | Implement baseline model, run first training loop, capture initial metrics. |
| 6 | Model Quality | Add cross-validation, hyperparameter sweeps, and model comparison reports. |
| 7 | Registry & Pipeline | Persist artifacts, wire `PredictionPipeline.run_training_cycle`, automate retrains. |
| 8 | Inference Service | Implement batch/on-demand inference, integrate with CLI/API, add explainability. |
| 9 | Monitoring & Alerts | Ship logging, drift checks, alert routing, and executive reporting templates. |
| 10 | Launch Readiness | Harden ops, add documentation, dry-run release, and freeze v1.0 model candidate. |

## Feature Implementation Checklist
<details>
<summary><strong>Data Foundations</strong></summary>

- [ ] Implement `DataIngestor.fetch_price_history`
- [ ] Implement `DataIngestor.fetch_fundamental_snapshot`
- [ ] Implement `DataIngestor.fetch_alternative_signals`
- [ ] Implement `DataIngestor.merge_sources`
- [ ] Implement `DataIngestor.cache_dataset`

</details>

<details>
<summary><strong>Feature Engineering</strong></summary>

- [ ] Implement `FeatureEngineer.build_feature_matrix`
- [ ] Implement `FeatureEngineer.generate_targets`
- [ ] Implement `FeatureEngineer.select_features`
- [ ] Implement `FeatureEngineer.persist_features`

</details>

<details>
<summary><strong>Training & Evaluation</strong></summary>

- [ ] Implement `ModelTrainer.build_model`
- [ ] Implement `ModelTrainer.train`
- [ ] Implement `ModelTrainer.evaluate`
- [ ] Implement `ModelTrainer.save_artifacts`

</details>

<details>
<summary><strong>Registry & Serving</strong></summary>

- [ ] Implement `ModelRegistry.register`
- [ ] Implement `ModelRegistry.load`
- [ ] Implement `ModelRegistry.latest`
- [ ] Implement `StockPredictor.load_model`
- [ ] Implement `StockPredictor.predict`
- [ ] Implement `StockPredictor.explain`

</details>

<details>
<summary><strong>Pipeline Orchestration</strong></summary>

- [ ] Implement `PredictionPipeline.backfill_history`
- [ ] Implement `PredictionPipeline.run_training_cycle`
- [ ] Implement `PredictionPipeline.run_inference`
- [ ] Implement `PredictionPipeline.batch_inference`
- [ ] Implement `PredictionPipeline.evaluate_live_performance`
- [ ] Implement `PredictionPipeline.schedule_jobs`

</details>

<details>
<summary><strong>Monitoring & Reporting</strong></summary>

- [ ] Implement `MonitoringService.log_predictions`
- [ ] Implement `MonitoringService.detect_drift`
- [ ] Implement `MonitoringService.trigger_alerts`
- [ ] Implement `MonitoringService.compile_report`

</details>

## Usage
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py --symbol AAPL --start 2020-01-01 --population 6 --iterations 3
```

The script downloads data (cached under `data/`), generates a population of strategies, backtests them, and feeds the results into the analyser. The highest-scoring strategies are mutated and evolved over subsequent iterations.

To integrate the forthcoming predictor, the CLI will be extended to accept `predict` subcommands once the pipeline is implemented.
