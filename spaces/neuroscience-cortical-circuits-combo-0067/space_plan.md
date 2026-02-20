# Space Plan - neuroscience-cortical-circuits-combo-0067

## Scientific Scope
- Domain: neuroscience
- Theme: cortical_circuits
- Base models: neuroscience-other-cerebellar-stellate-cell-model-rizza-et-al-2021-2018019-model, neuroscience-other-cerebellar-stellate-cell-osb2018019-model, neuroscience-other-cerebellar-stellate-cells-changes-in-threshold-l-266718-model, neuroscience-other-cerebellar-stellate-cells-osb266718-model

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
