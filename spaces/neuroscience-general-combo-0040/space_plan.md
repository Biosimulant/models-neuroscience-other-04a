# Space Plan - neuroscience-general-combo-0040

## Scientific Scope
- Domain: neuroscience
- Theme: general
- Base models: neuroscience-other-ca2-oscillations-in-sympathetic-neurons-friel-19-247655-model, neuroscience-other-caffeine-induced-electrical-oscillations-aplysia-neurons-osb34558-model, neuroscience-other-calcium-and-potassium-currents-of-olfactory-bulb-140462-model

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
