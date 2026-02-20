# Space Plan - neuroscience-basal-ganglia-dopamine-combo-0069

## Scientific Scope
- Domain: neuroscience
- Theme: basal_ganglia_dopamine
- Base models: neuroscience-other-calcium-influx-during-striatal-upstates-evans-et-150912-model, neuroscience-other-calcium-influx-during-striatal-upstates-osb150912-model, neuroscience-other-calcium-response-prediction-in-the-striatal-spin-151458-model, neuroscience-other-calcium-response-prediction-striatal-spines-depending-input-timing-osb151458-model

## Wiring Plan
- Comparative mode with monitor-only routing.
- Each base model state-like output connects to monitor ports `state_a..state_d`.
- No direct causal links among base models unless explicitly upgraded later.

## Visualization Plan
- Include `StateComparisonMonitor` and `StateMetricsMonitor`.
- Require at least:
  - one timeseries visual,
  - one summary table visual.

## Validation Gates
- space schema validity
- wiring endpoint validity
- smoke run success
- repo manifest/entrypoint validators pass
