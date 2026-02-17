NEURON mod files from the paper:
M. Migliore, L. Messineo, M. Ferrante
Dendritic Ih selectively blocks temporal summation of 
unsynchronized distal inputs in CA1 pyramidal neurons, 
J.Comput. Neurosci. 16:5-13 (2004).

The model demonstrates how the dendritic Ih in pyramidal neurons 
could selectively suppress AP generation for a volley of excitatory afferents 
when they are asynchronously and distally activated.
See the paper for more details.

Since most of the results in the paper were obtained by
averaging the results from many (100) simulations,
rather than reproduce all the simulations from one figure,
here we have chosen to show a typical simulation
to illustrate the main prediction of the paper.

The synchro-n128.hoc file will run four 200ms simulations 
plotting the membrane potential at the soma
and a ShapePlot to show the local depolarization during each simulation.

15 identical AMPA synapses were used,
randomly distributed in the apical compartments at 0-50um or 250-300um
from the soma with or without I-h. Colored labels in the plot
indicate the various cases (proximal or distal stimulation, with or
without Ih).
The peak conductance has been chosen in such a way 
to obtain approximately the same somatic depolarization in the 
absence of I-h. To better compare the results for each case,
in each simulation the synapses were activated in the same 
(asynchronous) order. 

The simulations illustrate the typical result that without Ih 
an AP is elicited following an asynchronous stimulation
in both proximal or distal dendrites (white and blue traces), whereas
in the presence of Ih (red and green traces) an AP is elicited 
only for a proximal stimulation. Instead, a synchronous activation of the input
would generate an AP in all cases.  

The simulations are best appreciated using a black background for the graphs.
To invert the background/foreground color edit
the lib/nrn.def (windows) or share/nrn/lib/nrn.defaults (unix) file 
in the NEURON home directory, and change the two lines
 
*Scene_background: #ffffff   
*Scene_foreground: #000000   
 
to 

*Scene_background: #000000   
*Scene_foreground: #ffffff   

This change will affect all future graphs, so
do not forget to reset the values to their original values
if you do not like graphs with a black background and white lines.

Under unix systems:
to compile the mod files use the command 
nrnivmodl 
and run the simulation hoc file with the command 
nrngui synchro-n128.hoc

Under Windows systems:
to compile the mod files use the "mknrndll" command.
A double click on the simulation file
synchro-n128.hoc 
will open the simulation window.

Questions on how to use this model
should be directed to michele.migliore@pa.ibf.cnr.it
