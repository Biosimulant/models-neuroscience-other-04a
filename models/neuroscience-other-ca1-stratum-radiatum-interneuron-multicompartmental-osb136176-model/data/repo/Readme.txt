This is the readme file for the NEURON simulation demonstrating NMDA spikes in interneurons

Instructions to run the model under Windows Xp or Win7:

1. Start mknrndll
2. Select as working directory the folder "Katona_et_al"
3. press the button "Make nrnmech.dll"
4. start Neuron
5. Select as working directory the folder "Katona_et_al"
6. type Enter
7. copy the following line to oc> command prompt: load_file("basal.hoc")
8. Please remove nmda synapses one by one from the PointProcessGroupManager window using the remove button

Graph[1] demonstrates NMDA spikes in a reconstructed CA1 stratum radiatum interneuron
Graph[2] shows the enlarged view of the initiation phase of the spike