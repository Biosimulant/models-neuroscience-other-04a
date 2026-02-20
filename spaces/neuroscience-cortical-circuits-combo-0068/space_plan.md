# Space Plan - neuroscience-cortical-circuits-combo-0068

## Scientific Scope
- Domain: neuroscience
- Theme: cortical_circuits
- Base models: neuroscience-other-cerebellar-thalamo-cortical-brain-network-for-se-2019877-model, neuroscience-other-cerebellum-granule-cell-fhf-dover-et-al-2016-206267-model, neuroscience-other-cerebellum-granule-cell-fhf-osb206267-model, neuroscience-other-cerebellum-purkinje-cell-osb244679-model

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
