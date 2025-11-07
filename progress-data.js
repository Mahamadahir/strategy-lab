window.progressData = {
  "generatedAt": "2026-04-07T00:00:00Z",
  "features": [
    {
      "id": "feature-foundations",
      "title": "Foundations & Tooling",
      "start": "2026-04-01",
      "due": "2026-04-08",
      "state": "in-progress",
      "methods": [
        {
          "id": "method-dockerize-stack",
          "title": "Containerize Strategy Lab stack",
          "start": "2026-04-01",
          "due": "2026-04-04",
          "state": "in-progress",
          "tests": [
            {
              "id": "test-docker-build",
              "title": "tests/infra/test_docker_image.py::test_builds_clean",
              "start": "2026-04-03",
              "due": "2026-04-04",
              "state": "pending"
            },
            {
              "id": "test-docker-devcontainer",
              "title": "tests/infra/test_devcontainer.py::test_smoke_bootstrap",
              "start": "2026-04-03",
              "due": "2026-04-04",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-ci-pipeline",
          "title": "Provision CI for lint, tests, and backtests",
          "start": "2026-04-02",
          "due": "2026-04-07",
          "state": "pending",
          "tests": [
            {
              "id": "test-ci-required-jobs",
              "title": "tests/infra/test_ci_matrix.py::test_required_jobs",
              "start": "2026-04-05",
              "due": "2026-04-07",
              "state": "pending"
            },
            {
              "id": "test-ci-backtest-cache",
              "title": "tests/infra/test_ci_matrix.py::test_backtest_cache",
              "start": "2026-04-05",
              "due": "2026-04-07",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-dev-onboarding-docs",
          "title": "Document onboarding and Docker workflows",
          "start": "2026-04-03",
          "due": "2026-04-08",
          "state": "pending",
          "tests": [
            {
              "id": "test-docs-onboarding",
              "title": "docs/review/dev_onboarding_checklist",
              "start": "2026-04-06",
              "due": "2026-04-08",
              "state": "pending"
            },
            {
              "id": "test-docs-runbook",
              "title": "docs/review/docker_runbook_signoff",
              "start": "2026-04-06",
              "due": "2026-04-08",
              "state": "pending"
            }
          ]
        }
      ]
    },
    {
      "id": "feature-data-foundations",
      "title": "Data Foundations",
      "start": "2026-04-08",
      "due": "2026-04-19",
      "state": "pending",
      "methods": [
        {
          "id": "method-fetch-price-history",
          "title": "Implement DataIngestor.fetch_price_history",
          "start": "2026-04-08",
          "due": "2026-04-12",
          "state": "pending",
          "tests": [
            {
              "id": "test-fetch-price-history",
              "title": "tests/predictor/test_data_ingestion.py::test_fetch_price_history",
              "start": "2026-04-11",
              "due": "2026-04-12",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-fetch-fundamentals",
          "title": "Implement DataIngestor.fetch_fundamental_snapshot",
          "start": "2026-04-09",
          "due": "2026-04-13",
          "state": "pending",
          "tests": [
            {
              "id": "test-fetch-fundamentals",
              "title": "tests/predictor/test_data_ingestion.py::test_fetch_fundamental_snapshot",
              "start": "2026-04-12",
              "due": "2026-04-13",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-fetch-alt-signals",
          "title": "Implement DataIngestor.fetch_alternative_signals",
          "start": "2026-04-10",
          "due": "2026-04-15",
          "state": "pending",
          "tests": [
            {
              "id": "test-fetch-alt-signals",
              "title": "tests/predictor/test_data_ingestion.py::test_fetch_alternative_signals",
              "start": "2026-04-13",
              "due": "2026-04-15",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-merge-sources",
          "title": "Implement DataIngestor.merge_sources",
          "start": "2026-04-11",
          "due": "2026-04-17",
          "state": "pending",
          "tests": [
            {
              "id": "test-merge-sources",
              "title": "tests/predictor/test_data_ingestion.py::test_merge_sources",
              "start": "2026-04-15",
              "due": "2026-04-17",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-cache-dataset",
          "title": "Implement DataIngestor.cache_dataset",
          "start": "2026-04-12",
          "due": "2026-04-18",
          "state": "pending",
          "tests": [
            {
              "id": "test-cache-dataset",
              "title": "tests/predictor/test_data_ingestion.py::test_cache_dataset",
              "start": "2026-04-16",
              "due": "2026-04-18",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-ingestion-tests",
          "title": "Ship ingestion unit + integration tests",
          "start": "2026-04-13",
          "due": "2026-04-19",
          "state": "pending",
          "tests": [
            {
              "id": "test-ingestion-unit-suite",
              "title": "tests/predictor/test_data_ingestion.py::test_ingestion_matrix",
              "start": "2026-04-15",
              "due": "2026-04-19",
              "state": "pending"
            },
            {
              "id": "test-ingestion-integration",
              "title": "integration/test_data_pipeline.py::test_vendor_fallbacks",
              "start": "2026-04-15",
              "due": "2026-04-19",
              "state": "pending"
            }
          ]
        }
      ]
    },
    {
      "id": "feature-feature-engineering",
      "title": "Feature Engineering",
      "start": "2026-04-15",
      "due": "2026-04-26",
      "state": "pending",
      "methods": [
        {
          "id": "method-build-feature-matrix",
          "title": "Implement FeatureEngineer.build_feature_matrix",
          "start": "2026-04-15",
          "due": "2026-04-20",
          "state": "pending",
          "tests": [
            {
              "id": "test-feature-matrix-shape",
              "title": "tests/predictor/test_feature_engineer.py::test_feature_matrix_shape",
              "start": "2026-04-18",
              "due": "2026-04-20",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-generate-targets",
          "title": "Implement FeatureEngineer.generate_targets",
          "start": "2026-04-16",
          "due": "2026-04-21",
          "state": "pending",
          "tests": [
            {
              "id": "test-generate-targets",
              "title": "tests/predictor/test_feature_engineer.py::test_generate_targets",
              "start": "2026-04-19",
              "due": "2026-04-21",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-select-features",
          "title": "Implement FeatureEngineer.select_features",
          "start": "2026-04-17",
          "due": "2026-04-23",
          "state": "pending",
          "tests": [
            {
              "id": "test-select-features",
              "title": "tests/predictor/test_feature_engineer.py::test_select_features",
              "start": "2026-04-20",
              "due": "2026-04-23",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-persist-features",
          "title": "Implement FeatureEngineer.persist_features",
          "start": "2026-04-18",
          "due": "2026-04-24",
          "state": "pending",
          "tests": [
            {
              "id": "test-persist-features",
              "title": "tests/predictor/test_feature_engineer.py::test_persist_features",
              "start": "2026-04-21",
              "due": "2026-04-24",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-feature-tests",
          "title": "FeatureEngineer regression tests",
          "start": "2026-04-19",
          "due": "2026-04-26",
          "state": "pending",
          "tests": [
            {
              "id": "test-feature-regression",
              "title": "tests/predictor/test_feature_engineer.py::test_regression_suite",
              "start": "2026-04-22",
              "due": "2026-04-26",
              "state": "pending"
            },
            {
              "id": "test-feature-persistence",
              "title": "integration/test_feature_pipeline.py::test_persistence_contract",
              "start": "2026-04-22",
              "due": "2026-04-26",
              "state": "pending"
            }
          ]
        }
      ]
    },
    {
      "id": "feature-training-eval",
      "title": "Training & Evaluation",
      "start": "2026-04-22",
      "due": "2026-05-03",
      "state": "pending",
      "methods": [
        {
          "id": "method-build-model",
          "title": "Implement ModelTrainer.build_model",
          "start": "2026-04-22",
          "due": "2026-04-26",
          "state": "pending",
          "tests": [
            {
              "id": "test-build-model",
              "title": "tests/predictor/test_model_trainer.py::test_build_model",
              "start": "2026-04-25",
              "due": "2026-04-26",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-train",
          "title": "Implement ModelTrainer.train",
          "start": "2026-04-23",
          "due": "2026-04-29",
          "state": "pending",
          "tests": [
            {
              "id": "test-train",
              "title": "tests/predictor/test_model_trainer.py::test_train_loop",
              "start": "2026-04-27",
              "due": "2026-04-29",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-evaluate",
          "title": "Implement ModelTrainer.evaluate",
          "start": "2026-04-24",
          "due": "2026-04-30",
          "state": "pending",
          "tests": [
            {
              "id": "test-evaluate",
              "title": "tests/predictor/test_model_trainer.py::test_evaluate_metrics",
              "start": "2026-04-28",
              "due": "2026-04-30",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-save-artifacts",
          "title": "Implement ModelTrainer.save_artifacts",
          "start": "2026-04-25",
          "due": "2026-05-01",
          "state": "pending",
          "tests": [
            {
              "id": "test-save-artifacts",
              "title": "tests/predictor/test_model_trainer.py::test_save_artifacts",
              "start": "2026-04-29",
              "due": "2026-05-01",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-training-tests",
          "title": "Training/evaluation regression tests",
          "start": "2026-04-26",
          "due": "2026-05-03",
          "state": "pending",
          "tests": [
            {
              "id": "test-trainer-regression",
              "title": "integration/test_training_loop.py::test_regression_metrics",
              "start": "2026-04-30",
              "due": "2026-05-03",
              "state": "pending"
            }
          ]
        }
      ]
    },
    {
      "id": "feature-registry-serving",
      "title": "Registry & Serving",
      "start": "2026-04-29",
      "due": "2026-05-10",
      "state": "pending",
      "methods": [
        {
          "id": "method-registry-register",
          "title": "Implement ModelRegistry.register",
          "start": "2026-04-29",
          "due": "2026-05-03",
          "state": "pending",
          "tests": [
            {
              "id": "test-registry-register",
              "title": "tests/predictor/test_model_registry.py::test_register",
              "start": "2026-05-02",
              "due": "2026-05-03",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-registry-load",
          "title": "Implement ModelRegistry.load",
          "start": "2026-04-30",
          "due": "2026-05-06",
          "state": "pending",
          "tests": [
            {
              "id": "test-registry-load",
              "title": "tests/predictor/test_model_registry.py::test_load",
              "start": "2026-05-04",
              "due": "2026-05-06",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-registry-latest",
          "title": "Implement ModelRegistry.latest",
          "start": "2026-05-01",
          "due": "2026-05-07",
          "state": "pending",
          "tests": [
            {
              "id": "test-registry-latest",
              "title": "tests/predictor/test_model_registry.py::test_latest",
              "start": "2026-05-05",
              "due": "2026-05-07",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-predictor-load-model",
          "title": "Implement StockPredictor.load_model",
          "start": "2026-05-02",
          "due": "2026-05-08",
          "state": "pending",
          "tests": [
            {
              "id": "test-predictor-load-model",
              "title": "tests/predictor/test_stock_predictor.py::test_load_model",
              "start": "2026-05-06",
              "due": "2026-05-08",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-predictor-predict",
          "title": "Implement StockPredictor.predict",
          "start": "2026-05-03",
          "due": "2026-05-09",
          "state": "pending",
          "tests": [
            {
              "id": "test-predictor-predict",
              "title": "tests/predictor/test_stock_predictor.py::test_predict",
              "start": "2026-05-07",
              "due": "2026-05-09",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-predictor-explain",
          "title": "Implement StockPredictor.explain",
          "start": "2026-05-04",
          "due": "2026-05-10",
          "state": "pending",
          "tests": [
            {
              "id": "test-predictor-explain",
              "title": "tests/predictor/test_stock_predictor.py::test_explain",
              "start": "2026-05-08",
              "due": "2026-05-10",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-serving-tests",
          "title": "Registry & serving functional tests",
          "start": "2026-05-04",
          "due": "2026-05-10",
          "state": "pending",
          "tests": [
            {
              "id": "test-serving-regression",
              "title": "integration/test_serving_stack.py::test_end_to_end",
              "start": "2026-05-08",
              "due": "2026-05-10",
              "state": "pending"
            }
          ]
        }
      ]
    },
    {
      "id": "feature-pipeline",
      "title": "Prediction Pipeline & Scheduling",
      "start": "2026-05-06",
      "due": "2026-05-17",
      "state": "pending",
      "methods": [
        {
          "id": "method-pipeline-backfill",
          "title": "Implement PredictionPipeline.backfill_history",
          "start": "2026-05-06",
          "due": "2026-05-10",
          "state": "pending",
          "tests": [
            {
              "id": "test-pipeline-backfill",
              "title": "tests/predictor/test_prediction_pipeline.py::test_backfill_history",
              "start": "2026-05-09",
              "due": "2026-05-10",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-pipeline-training-cycle",
          "title": "Implement PredictionPipeline.run_training_cycle",
          "start": "2026-05-07",
          "due": "2026-05-12",
          "state": "pending",
          "tests": [
            {
              "id": "test-pipeline-training-cycle",
              "title": "tests/predictor/test_prediction_pipeline.py::test_run_training_cycle",
              "start": "2026-05-10",
              "due": "2026-05-12",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-pipeline-run-inference",
          "title": "Implement PredictionPipeline.run_inference",
          "start": "2026-05-08",
          "due": "2026-05-13",
          "state": "pending",
          "tests": [
            {
              "id": "test-pipeline-run-inference",
              "title": "tests/predictor/test_prediction_pipeline.py::test_run_inference",
              "start": "2026-05-11",
              "due": "2026-05-13",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-pipeline-batch",
          "title": "Implement PredictionPipeline.batch_inference",
          "start": "2026-05-09",
          "due": "2026-05-14",
          "state": "pending",
          "tests": [
            {
              "id": "test-pipeline-batch",
              "title": "tests/predictor/test_prediction_pipeline.py::test_batch_inference",
              "start": "2026-05-12",
              "due": "2026-05-14",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-pipeline-live-eval",
          "title": "Implement PredictionPipeline.evaluate_live_performance",
          "start": "2026-05-10",
          "due": "2026-05-15",
          "state": "pending",
          "tests": [
            {
              "id": "test-pipeline-live-eval",
              "title": "tests/predictor/test_prediction_pipeline.py::test_evaluate_live_performance",
              "start": "2026-05-13",
              "due": "2026-05-15",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-pipeline-schedule",
          "title": "Implement PredictionPipeline.schedule_jobs",
          "start": "2026-05-11",
          "due": "2026-05-16",
          "state": "pending",
          "tests": [
            {
              "id": "test-pipeline-schedule",
              "title": "tests/predictor/test_prediction_pipeline.py::test_schedule_jobs",
              "start": "2026-05-14",
              "due": "2026-05-16",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-pipeline-tests",
          "title": "Pipeline integration tests",
          "start": "2026-05-12",
          "due": "2026-05-17",
          "state": "pending",
          "tests": [
            {
              "id": "test-pipeline-integration",
              "title": "integration/test_prediction_pipeline.py::test_end_to_end",
              "start": "2026-05-14",
              "due": "2026-05-17",
              "state": "pending"
            }
          ]
        }
      ]
    },
    {
      "id": "feature-monitoring",
      "title": "Monitoring & Reporting",
      "start": "2026-05-13",
      "due": "2026-05-24",
      "state": "pending",
      "methods": [
        {
          "id": "method-monitor-log",
          "title": "Implement MonitoringService.log_predictions",
          "start": "2026-05-13",
          "due": "2026-05-16",
          "state": "pending",
          "tests": [
            {
              "id": "test-monitor-log",
              "title": "tests/predictor/test_monitoring_service.py::test_log_predictions",
              "start": "2026-05-15",
              "due": "2026-05-16",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-monitor-drift",
          "title": "Implement MonitoringService.detect_drift",
          "start": "2026-05-14",
          "due": "2026-05-18",
          "state": "pending",
          "tests": [
            {
              "id": "test-monitor-drift",
              "title": "tests/predictor/test_monitoring_service.py::test_detect_drift",
              "start": "2026-05-16",
              "due": "2026-05-18",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-monitor-alerts",
          "title": "Implement MonitoringService.trigger_alerts",
          "start": "2026-05-15",
          "due": "2026-05-20",
          "state": "pending",
          "tests": [
            {
              "id": "test-monitor-alerts",
              "title": "tests/predictor/test_monitoring_service.py::test_trigger_alerts",
              "start": "2026-05-17",
              "due": "2026-05-20",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-monitor-report",
          "title": "Implement MonitoringService.compile_report",
          "start": "2026-05-16",
          "due": "2026-05-22",
          "state": "pending",
          "tests": [
            {
              "id": "test-monitor-report",
              "title": "tests/predictor/test_monitoring_service.py::test_compile_report",
              "start": "2026-05-19",
              "due": "2026-05-22",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-monitor-tests",
          "title": "Monitoring regression suite",
          "start": "2026-05-17",
          "due": "2026-05-24",
          "state": "pending",
          "tests": [
            {
              "id": "test-monitoring-regression",
              "title": "integration/test_monitoring_pipeline.py::test_alert_thresholds",
              "start": "2026-05-20",
              "due": "2026-05-24",
              "state": "pending"
            }
          ]
        }
      ]
    },
    {
      "id": "feature-launch-readiness",
      "title": "Launch Readiness",
      "start": "2026-05-20",
      "due": "2026-05-31",
      "state": "pending",
      "methods": [
        {
          "id": "method-launch-harden-ops",
          "title": "Harden operations & on-call playbooks",
          "start": "2026-05-20",
          "due": "2026-05-24",
          "state": "pending",
          "tests": [
            {
              "id": "test-launch-ops-playbook",
              "title": "runbooks/tests/oncall_playbook_walkthrough",
              "start": "2026-05-23",
              "due": "2026-05-24",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-launch-docs",
          "title": "Finalize documentation + API references",
          "start": "2026-05-21",
          "due": "2026-05-27",
          "state": "pending",
          "tests": [
            {
              "id": "test-launch-docs-review",
              "title": "docs/review/predictor_api_signoff",
              "start": "2026-05-25",
              "due": "2026-05-27",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-launch-dry-run",
          "title": "Dry-run release + rollback rehearsal",
          "start": "2026-05-22",
          "due": "2026-05-28",
          "state": "pending",
          "tests": [
            {
              "id": "test-launch-dry-run",
              "title": "operations/tests/release_dry_run",
              "start": "2026-05-26",
              "due": "2026-05-28",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-launch-freeze",
          "title": "Freeze v1.0 model candidate",
          "start": "2026-05-23",
          "due": "2026-05-29",
          "state": "pending",
          "tests": [
            {
              "id": "test-launch-freeze",
              "title": "integration/test_model_freeze.py::test_candidate_snapshot",
              "start": "2026-05-27",
              "due": "2026-05-29",
              "state": "pending"
            }
          ]
        },
        {
          "id": "method-launch-signoff",
          "title": "Executive + compliance sign-off",
          "start": "2026-05-24",
          "due": "2026-05-31",
          "state": "pending",
          "tests": [
            {
              "id": "test-launch-signoff",
              "title": "reviews/checklists/launch_signoff_board",
              "start": "2026-05-29",
              "due": "2026-05-31",
              "state": "pending"
            }
          ]
        }
      ]
    }
  ]
};
