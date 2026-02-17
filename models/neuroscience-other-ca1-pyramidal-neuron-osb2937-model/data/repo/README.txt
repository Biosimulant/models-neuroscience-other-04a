Model files from the paper: 
M. Migliore, Modeling the attenuation and failure of action potentials in 
the dendrites of hippocampal neurons, Biophys. J. 71:2394-403 (1996).
 
The paper proposed (and experiments later confirmed) a slow inactivation 
of the Na channels as the mechanism responsible for the progressive 
reduction of action potentials amplitude, observed in the dendrites of 
CA1 hippocampal pyramidal neurons during a train.  This mechanism was 
modeled using an additional gate variable in the Na+ conductance. The 
gate variable and its kinetics are now included in the updated Na+ 
conductance (na3.mod) of the 1999 CA1 model.


Under unix systems:
===================
to compile the mod files use the command 
nrnivmodl 
and run the simulation hoc file with the command 
nrngui figs.hoc

Under Windows:
==============
to compile the mod files use the "mknrndll DOS box" and 
follow on-screen instructions.
A double click on the simulation file
figs.hoc 
will open the simulation window.

This CA1 model can be used to run three related simulations, 
corresponding to the simulations shown in Fig.3 (right), Fig.4bc, 
and Fig.4bd of the paper.

"run Fig.3" will show somatic and dendritic membrane potential during
a 450ms suprathreshold dendritic current injection on a distal
compartment, followed by a 70ms current pulse after a 250ms delay.

To demonstrate the recovery from slow inactivation, "run Fig.4bc" will 
show membrane potential of a distal compartment from 4 overlapping 
simulations with the same initial 450ms dendritic current injection 
followed by a short 70 pulse after different delays.

To demonstrate that hyperpolarization increases the rate of recovery
as observed in the experiments,"run Fig.4bd" will show the same simulation
as in "run Fig.3", but with a -0.5nA dendritic current injection during 
the 250ms delay.

Questions on how to use this model should be directed to
michele.migliore@pa.ibf.cnr.it





