from neuron import h
import math
import numpy as np
from SC_param import SC_param
from Synapses import Synapses

class Stellate:
    def __init__(self,record_all = 1):
        h.load_file('stdlib.hoc')
        h.load_file('import3d.hoc')
        
        cell = h.Import3d_Neurolucida3()
        cell.input('morphology/stellate.ASC')
        
        i3d = h.Import3d_GUI(cell, 0)
        i3d.instantiate(self)
        
        self.soma[0].nseg = 1 + (2*int(self.soma[0].L/40))
        self.soma[0].Ra = SC_param['Ra']
        self.soma[0].cm = 1 
        
        self.soma[0].insert('Leak')
        self.soma[0].gmax_Leak = SC_param['leak_soma']
        self.soma[0].e_Leak = SC_param['Eleak']
        
        self.soma[0].insert('Nav1_1')
        self.soma[0].gbar_Nav1_1 = SC_param['Nav1.1_soma']
        self.soma[0].ena = SC_param['ena']
        
        self.soma[0].insert('Cav3_2')
        self.soma[0].gcabar_Cav3_2 = SC_param['Cav3.2_soma']
        
        self.soma[0].insert('Cav3_3')
        self.soma[0].pcabar_Cav3_3 = SC_param['Cav3.3_soma']
        
        self.soma[0].insert('Kir2_3')
        self.soma[0].gkbar_Kir2_3 = SC_param['Kir2.3_soma']
        self.soma[0].ek = -84

        self.soma[0].insert('Kv1_1')
        self.soma[0].gbar_Kv1_1= SC_param['Kv1.1_soma']
        
        self.soma[0].insert('Kv3_4')
        self.soma[0].gkbar_Kv3_4 = SC_param['Kv3.4_soma']
        
        self.soma[0].insert('Kv4_3')
        self.soma[0].gkbar_Kv4_3 = SC_param['Kv4.3_soma']
        
        self.soma[0].insert('Kca1_1')
        self.soma[0].gbar_Kca1_1 = SC_param['Kca1.1_soma']
        
        self.soma[0].insert('Kca2_2')
        self.soma[0].gkbar_Kca2_2 = SC_param['Kca2.2_soma']
        
        self.soma[0].insert('Cav2_1')
        self.soma[0].pcabar_Cav2_1 = SC_param['Cav2.1_soma']
        
        self.soma[0].insert('HCN1_PC')
        self.soma[0].gbar_HCN1_PC = SC_param['HCN1_soma']
        self.soma[0].eh = -34 
        self.soma[0].insert('cdp5StCmod')
        self.soma[0].TotalPump_cdp5StCmod = 1e-8 
        
        self.soma[0].push()
        
        self.soma[0].eca = 137.5
        
        h.pop_section()
	
	
        self.whatami = "sc"
	
        self.dendprox = []
        self.denddist = []
	
        for i in self.dend:
            if i.diam >=0.6:
                self.dendprox.append(i)
            else:
                self.denddist.append(i)
       
        for i in self.dendprox:
            i.nseg = 1 + 2*int(i.L/40)
            
         
            i.Ra = SC_param['Ra']
            i.cm = 1.5 
            
            i.insert('Cav2_1')
            i.pcabar_Cav2_1 = SC_param['Cav2.1_dendprox']
        
            i.insert('Cav3_2')
            i.gcabar_Cav3_2 = SC_param['Cav3.2_dendprox']
        
            i.insert('Cav3_3')
            i.pcabar_Cav3_3 = SC_param['Cav3.3_dendprox']
        
            i.insert('Kca1_1')
            i.gbar_Kca1_1 = SC_param['Kca1.1_dendprox']
            i.ek = -84
            
            i.insert('Kca2_2')
            i.gkbar_Kca2_2 = SC_param['Kca2.2_dendprox']
            
            i.insert('Kv4_3')
            i.gkbar_Kv4_3 = SC_param['Kv4.3_dendprox']
        
            i.insert('Kv1_1')
            i.gbar_Kv1_1= SC_param['Kv1.1_dendprox']

            i.insert('Leak')
            i.gmax_Leak = SC_param['leak_dendprox']
            i.e_Leak = SC_param['Eleak']
                    
            i.insert('cdp5StCmod')
        
            
            i.TotalPump_cdp5StCmod = 1e-9 

	    
            i.push()
            i.eca = 137.5
        
            h.pop_section()
        
        for i in self.denddist: 
            i.nseg = 1 + 2*int(i.L/40)
            i.Ra = SC_param['Ra']
            i.cm = 1.5 #0.5
                
            i.insert('Cav2_1')
            i.pcabar_Cav2_1 = SC_param['Cav2.1_denddist']
        
            i.insert('Kca1_1')
            i.gbar_Kca1_1 = SC_param['Kca1.1_denddist']
            i.ek = -84
            
            i.insert('Kca2_2')
            i.gkbar_Kca2_2 = SC_param['Kca2.2_denddist']
        
            i.insert('Kv1_1')
            i.gbar_Kv1_1= SC_param['Kv1.1_denddist']
            
            i.insert('Leak')
            i.gmax_Leak = SC_param['leak_denddist']
            i.e_Leak = SC_param['Eleak']
                    
            i.insert('cdp5StCmod')
            i.TotalPump_cdp5StCmod = 1e-9 
	  
            i.push()
            i.eca = 137.5
        
            h.pop_section()
	    
	
        self.axon[0].nseg = 1 + 2*int(self.axon[0].L/40)
        self.axon[0].Ra = SC_param['Ra']
        self.axon[0].cm = 1 
        
        self.axon[0].insert('Nav1_6')
        self.axon[0].gbar_Nav1_6 = SC_param['Nav1.6_ais']
        self.axon[0].ena = SC_param['ena']
        
        self.axon[0].insert('Kv3_4')
        self.axon[0].gkbar_Kv3_4 = SC_param['Kv3.4_ais']
        self.axon[0].ek = -88 
        
        self.axon[0].insert('Kv1_1')
        self.axon[0].gbar_Kv1_1= SC_param['Kv1.1_ais']
        
        self.axon[0].insert('HCN1_PC')
        self.axon[0].gbar_HCN1_PC = SC_param['HCN1_ais']
        self.axon[0].eh = -34  
        
        self.axon[0].insert('Leak')
        self.axon[0].gmax_Leak = SC_param['leak_ais']
        self.axon[0].e_Leak = SC_param['Eleak']
        
        self.axon[0].insert('GRC_KM')
        self.axon[0].gkbar_GRC_KM = 0.00007960307413
        
        self.axon[0].insert('cdp5StCmod')
	
        for i,d in enumerate(self.axon):
            if i == 0:
                pass
            else:
                
                self.axon[i].nseg = 1 + 2*int(self.axon[i].L/40)
                self.axon[i].cm = 1
                self.axon[i].Ra = SC_param['Ra']
                
                self.axon[i].insert('Leak')
                self.axon[i].e_Leak =  SC_param['Eleak']
                self.axon[i].gmax_Leak = SC_param['leak_axon']
                
                self.axon[i].insert('Nav1_6')
                self.axon[i].gbar_Nav1_6 = SC_param['Nav1.6_axon']
                self.axon[i].ena = 60


                self.axon[i].insert('Kv3_4')
                self.axon[i].gkbar_Kv3_4 = SC_param['Kv3.4_axon']
                self.axon[i].ek = -88
                
                self.axon[i].insert('Kv1_1')
                self.axon[i].gbar_Kv1_1= SC_param['Kv1.1_axon']
                
                self.axon[i].insert('HCN1_PC')
                self.axon[i].gbar_HCN1_PC = SC_param['HCN1_axon']
                self.axon[i].eh = -34

                self.axon[i].insert('cdp5StCmod')
                
        self.voltage = h.Vector()
        self.voltage.record(self.soma[0](0.5)._ref_v)

        self.time = h.Vector()
        self.time.record(h._ref_t)
	
        
    def createsyn(self):

        
        
	##Synapsess
                                                                                                                  
        self.pf_sc = [] 
        self.pf_scnmda = []
        self.sc_sc = []
        
        self.pf_sc_burst = [] 
        self.pf_scnmda_burst = []

        

        self.dendresearch = [8, 12, 14, 21, 22, 23, 26, 27, 28, 32, 43, 90, 100] #13 #more syn are needed... 3 are to low to do something
        self.dendinhib = [8, 12, 14, 21, 22, 23, 26, 27, 28, 31, 32, 34, 35, 43, 50, 57, 58, 66, 67, 68, 71, 73, 81, 82, 84, 86, 89, 90, 98, 100, 40, 69] #32syn

        self.pfsc = []
        self.pf_scnmda = []
        for e in self.dendresearch:
            self.pfsc.append(Synapses('pf_sc',self,self.dend[e]))
            self.pf_scnmda.append(Synapses('pfnmda',self,self.dend[e]))
	
        for e in self.dendinhib:
            self.sc_sc.append(Synapses('sc',self,self.dend[e]))
            
    
