# Space Plan - neuroscience-general-combo-0047

## Scientific Scope
- Domain: neuroscience
- Theme: general
- Base models: neuroscience-other-cardiac-action-potentials-pacemaker-activity-sinoatrial-node-osb144520-model, neuroscience-other-cardiac-atrial-cell-courtemanche-et-al-1998-c-79461-model, neuroscience-other-cardiac-atrial-cell-osb3800-model

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
