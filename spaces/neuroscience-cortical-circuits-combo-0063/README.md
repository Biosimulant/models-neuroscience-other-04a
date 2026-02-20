# COMBO_0063 - Neuroscience Cortical Circuits

## Scientific Question
How do cortical circuit motifs transform and propagate activity?

## Biological Context
Neuronal dynamics, network signaling, and emergent circuit behavior.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `neuroscience-other-cerebellar-cortex-oscil-robustness-from-golgi-ce-139656-model`: Neuroscience: CerebellarCortexOscilRobustnessFromGolgiCe139656Model
- `neuroscience-other-cerebellar-golgi-cell-model-with-stdp-pali-et-al-2017007-model`: Neuroscience: CerebellarGolgiCellModelWithStdpPaliEtAl2017007Model
- `neuroscience-other-cerebellar-golgi-cell-solinas-et-al-2007a-2007b-112685-model`: Neuroscience: CerebellarGolgiCellSolinasEtAl2007a2007b112685Model
- `neuroscience-other-cerebellar-golgi-cell-stdp-osb2017007-model`: Neuroscience: Model20170072017007Model

## Wiring Rationale
- Comparative (non-causal) mode: no direct causal links were created.

## Visualization Strategy
- Monitor-driven visualization is required for this space.
- State streams are routed into explicit monitor ports (`state_a..state_d`) to avoid signal overwrite.
- At minimum, monitor visuals include one timeseries panel and one summary table.
- Rationale: A dedicated monitor model receives all participating model state streams (`state_a..state_d`) so trajectories can be compared in one place without claiming causal coupling when IO semantics are incomplete.

## Expected Behaviors
- Model output trajectories under shared runtime settings.
- Cross-model agreement/divergence in key state or metric signals.
- Relative behavior comparison without causal linkage claims.

## Known Limitations
- No new biology is introduced beyond what upstream models encode.
- Cross-model semantic matching is rule-based and may under-connect uncertain routes.

## Source Provenance
- neuroscience-other-cerebellar-cortex-oscil-robustness-from-golgi-ce-139656-model :: modeldb:139656 :: https://modeldb.science/139656
- neuroscience-other-cerebellar-golgi-cell-model-with-stdp-pali-et-al-2017007-model :: modeldb:2017007 :: https://modeldb.science/2017007
- neuroscience-other-cerebellar-golgi-cell-solinas-et-al-2007a-2007b-112685-model :: modeldb:112685 :: https://modeldb.science/112685
- neuroscience-other-cerebellar-golgi-cell-stdp-osb2017007-model :: opensourcebrain:2017007 :: https://github.com/OpenSourceBrain/2017007

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
