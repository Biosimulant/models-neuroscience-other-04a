# Space Plan - neuroscience-general-combo-0043

## Scientific Scope
- Domain: neuroscience
- Theme: general
- Base models: neuroscience-other-calcium-waves-neuroblastoma-cells-osb125745-model, neuroscience-other-calciumimagingdriftinggrating-calciumimagingdriftinggrating-model, neuroscience-other-calculating-the-consequences-of-left-shifted-nav-234111-model

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
