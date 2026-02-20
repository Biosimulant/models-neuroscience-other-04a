# Space Plan - neuroscience-cortical-circuits-combo-0065

## Scientific Scope
- Domain: neuroscience
- Theme: cortical_circuits
- Base models: neuroscience-other-cerebellar-granular-network-osb232023-model, neuroscience-other-cerebellar-granule-cell-masoli-et-al-2020-265584-model, neuroscience-other-cerebellar-granule-cell-osb265584-model, neuroscience-other-cerebellar-ltd-including-rkip-inactivation-raf-mek-osb222732-model

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
