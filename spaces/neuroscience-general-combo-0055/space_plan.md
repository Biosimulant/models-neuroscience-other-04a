# Space Plan - neuroscience-general-combo-0055

## Scientific Scope
- Domain: neuroscience
- Theme: general
- Base models: neuroscience-other-cerebellar-cortex-oscil-osb139656-model, neuroscience-other-cerebellar-gain-and-timing-control-model-yamazak-144416-model, neuroscience-other-cerebellar-gain-timing-control-osb144416-model

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
