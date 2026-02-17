from neuron import h
import math
import numpy as np
from TheNetSyn_py3 import Synapse_py3
from golgi_number_1 import number_ind_1

class Golgi_net_py3_1():
    def __init__(self):
        
        print( "golgi2016 python3")
        
        h.load_file('stdlib.hoc')
        h.load_file('import3d.hoc')
        
        cell = h.Import3d_Neurolucida3()
        cell.input('morphology/pair-140514-C2-1_split_1.asc')
            
        
        i3d = h.Import3d_GUI(cell,0)
        i3d.instantiate(self)
        
        conductvalues = np.genfromtxt("final_pop_opti_1_third.txt")
            

        indiv_number = number_ind_1['indiv']
        print( 'indiv number', indiv_number)
        
      
#Soma

        self.soma[0].nseg = 1 + (2 * int(self.soma[0].L / 40))
        self.soma[0].Ra = 122
        self.soma[0].cm = 1 
        
        self.soma[0].insert('Leak')
        self.soma[0].gmax_Leak = 0.00003
        self.soma[0].e_Leak = -55
        
        self.soma[0].insert('Nav1_6')
        self.soma[0].gbar_Nav1_6 = conductvalues[indiv_number,9]
        self.soma[0].ena = 60
	
        self.soma[0].insert('Kv1_1')
        self.soma[0].gbar_Kv1_1 = conductvalues[indiv_number,10]
	
        self.soma[0].insert('Kv3_4')
        self.soma[0].gkbar_Kv3_4 = conductvalues[indiv_number,11]
        
        self.soma[0].insert('Kv4_3')
        self.soma[0].gkbar_Kv4_3 = conductvalues[indiv_number,12]	
	  
        self.soma[0].insert('Kca1_1')
        self.soma[0].gbar_Kca1_1 = conductvalues[indiv_number,13]
	  
        self.soma[0].insert('Kca3_1')
        self.soma[0].gkbar_Kca3_1 = conductvalues[indiv_number,14]
        
        self.soma[0].insert('GRC_CA')
        self.soma[0].gcabar_GRC_CA = conductvalues[indiv_number,15]
	
        self.soma[0].insert('Cav3_1')
        self.soma[0].pcabar_Cav3_1 = conductvalues[indiv_number,16]
        
        self.soma[0].ek = -80
        
        self.soma[0].insert('cdp5StCmod')
        self.soma[0].TotalPump_cdp5StCmod = 1e-7
        
        self.soma[0].eca = 137

	
        self.whatami = "golgi2019"
        
        self.dendbasal = []
        self.dendapical = []
        self.terminal_dend = []

##dend #to be redone
    
        
        for en_index, d_sec in enumerate(self.dend):
            #print('number, len', en_index, d_sec.L)
            if en_index >= 0 and en_index <= 3 or en_index >= 16 and en_index <= 17 or en_index >= 33 and en_index <= 41 or en_index == 84 or en_index >= 105 and en_index <= 150:
                self.dendbasal.append(d_sec)
                
            if en_index >= 4 and en_index <= 15 or en_index >= 18 and en_index <= 32 or en_index >= 42 and en_index <= 83 or en_index >= 85 and en_index <= 104:
                self.dendapical.append(d_sec)

        final_sec = [1, 17, 38, 40, 41, 105, 106, 109, 111, 112, 115, 117, 118, 120, 121, 123, 124, 127, 128, 129, 131, 132, 133, 135, 137, 139, 140, 144, 145, 147, 148, 150]
        for en_index, d_sec in enumerate(self.dend):
            if en_index in final_sec:
                self.terminal_dend.append(d_sec)
        
        #Dend apical	    
        for r in self.dendapical:
                r.nseg = 1 + (2 * int(r.L / 40))
                r.Ra = 122
                r.cm = 2.5
                
                r.insert('Leak')
                r.gmax_Leak = 0.00003
                r.e_Leak = -55
                
                r.insert('Nav1_6')
                r.gbar_Nav1_6 = conductvalues[indiv_number,0]
                r.ena = 60
                
                r.insert('Kca1_1')
                r.gbar_Kca1_1 = conductvalues[indiv_number,1]
                
                r.insert('Kca2_2')
                r.gkbar_Kca2_2 = conductvalues[indiv_number,2]
                r.ek = -80
                
                r.insert('Cav2_3')
                r.gcabar_Cav2_3 = conductvalues[indiv_number,3]
                
                r.insert('Cav3_1')
                r.pcabar_Cav3_1 = conductvalues[indiv_number,4]
                
                r.insert('cdp5StCmod')
                r.TotalPump_cdp5StCmod = 5e-9
                
               
                r.push()
                r.eca = 137
                h.pop_section()   
	
	
        #Dend basal
        for i in self.dendbasal:
                i.nseg = 1 + (2 * int(i.L / 40))
                i.Ra = 122
                i.cm = 2.5
                
                i.insert('Leak')
                i.gmax_Leak = 0.00003
                i.e_Leak = -55	
                
                i.insert('Nav1_6')
                i.gbar_Nav1_6 = conductvalues[indiv_number,5]
                i.ena = 60
                
                i.insert('Kca1_1')
                i.gbar_Kca1_1 = conductvalues[indiv_number,6]
                
                i.insert('Kca2_2')
                i.gkbar_Kca2_2 = conductvalues[indiv_number,7]
                i.ek = -80

                i.insert('GRC_CA')
                i.gcabar_GRC_CA = conductvalues[indiv_number,8]

                i.insert('cdp5StCmod')
                i.TotalPump_cdp5StCmod = 2e-9
                
                i.push()
                i.eca = 137
                h.pop_section()   

    #final dend
        self.dend_final = [h.Section(name='final_dend'+str(x)) for x in range(32)]
 
        for i in self.dend_final:
                i.L = 2.5
                i.diam = 0.58
                i.nseg = 1
                i.Ra = 122
                i.cm = 2.5
                
                i.insert('Leak')
                i.gmax_Leak = 0.00003
                i.e_Leak = -55	
                
                i.insert('Nav1_6')
                i.gbar_Nav1_6 = conductvalues[indiv_number,5]
                i.ena = 60

                i.insert('Kca1_1')
                i.gbar_Kca1_1 = conductvalues[indiv_number,6]

                i.insert('Kca2_2')
                i.gkbar_Kca2_2 = conductvalues[indiv_number,7]
                i.ek = -80

                i.insert('GRC_CA')
                i.gcabar_GRC_CA = conductvalues[indiv_number,8]
# 
                i.insert('cdp5StCmod')
                i.TotalPump_cdp5StCmod = 2e-9
                
                i.insert('cdp5_nmdaCa')
                i.TotalPump_cdp5_nmdaCa = 1e-9
                
                i.push()
                i.eca = 137
                h.pop_section()  
                
        for sec in range(len(self.dend_final)):
            self.dend_final[sec].connect(self.terminal_dend[sec],1,0)
            print(self.dend_final[sec], self.terminal_dend[sec])
           
           
 
#axon
        for i,d in enumerate(self.axon):
            if i == 0:
                #AIS
                self.axon[i].nseg = 1 + (2 * int(self.axon[i].L / 40))
                self.axon[i].Ra = 122
                self.axon[i].cm = 1
                
                self.axon[i].insert('Leak')
                self.axon[i].gmax_Leak = 0.00003
                self.axon[i].e_Leak = -55
                
                self.axon[i].insert('HCN1')
                self.axon[i].gbar_HCN1 = conductvalues[indiv_number,17]
                
                self.axon[i].insert('HCN2')
                self.axon[i].gbar_HCN2 = conductvalues[indiv_number,18]
            
                self.axon[i].insert('Nav1_6')
                self.axon[i].gbar_Nav1_6 = conductvalues[indiv_number,19]
                self.axon[i].ena = 60
            
                self.axon[i].insert('GRC_KM')
                self.axon[i].gkbar_GRC_KM = conductvalues[indiv_number,20]
                
                self.axon[i].insert('Kca1_1')
                self.axon[i].gbar_Kca1_1 = conductvalues[indiv_number,21]               

                self.axon[i].insert('GRC_CA')
                self.axon[i].gcabar_GRC_CA = conductvalues[indiv_number,22]

                self.axon[i].ek = -80                 
                self.axon[i].insert('cdp5StCmod')	
                self.axon[i].TotalPump_cdp5StCmod = 1e-8
                
                self.axon[i].push()
                self.axon[i].eca = 137
                h.pop_section()  
                    
            elif i >= 1:
                #axon
                    
                self.axon[i].nseg = 1 + (2 * int(self.axon[i].L / 40))
                self.axon[i].cm = 1
                self.axon[i].Ra = 122
                
                
                self.axon[i].insert('Leak')
                self.axon[i].e_Leak = -55
                self.axon[i].gmax_Leak = 0.000001
                
                self.axon[i].insert('Nav1_6')
                self.axon[i].gbar_Nav1_6 = 0.0115
                self.axon[i].ena = 60

                self.axon[i].insert('Kv3_4')
                self.axon[i].gkbar_Kv3_4 = 0.0091
                self.axon[i].ek = -80  
                

                self.axon[i].insert('cdp5StCmod')	    
                self.axon[i].TotalPump_cdp5StCmod = 1e-8
                
                self.axon[i].push()
                self.axon[i].eca = 137
                h.pop_section()   
        

        
        self.time_vector = h.Vector()
        self.time_vector.record(h._ref_t)

        self.vm = h.Vector()
        self.vm.record(self.soma[0](0.5)._ref_v)
        
        self.vm_dend_apic = h.Vector()
        self.vm_dend_apic.record(self.dend[48](0.5)._ref_v)
        
        self.vm_dend_basal = h.Vector()
        self.vm_dend_basal.record(self.dend[3](0.5)._ref_v)
        

        
#calcium dendrites activated        
        
        self.cai_nmda_dend_0 = h.Vector()
        self.cai_nmda_dend_0.record(self.dend_final[0](0.5)._ref_ca_nmdai)
        
        self.cai_nmda_dend_1 = h.Vector()
        self.cai_nmda_dend_1.record(self.dend_final[1](0.5)._ref_ca_nmdai)
        
        self.cai_nmda_dend_2 = h.Vector()
        self.cai_nmda_dend_2.record(self.dend_final[2](0.5)._ref_ca_nmdai)
        
        self.cai_nmda_dend_3 = h.Vector()
        self.cai_nmda_dend_3.record(self.dend_final[3](0.5)._ref_ca_nmdai)
        
        self.cai_nmda_dend_4 = h.Vector()
        self.cai_nmda_dend_4.record(self.dend_final[4](0.5)._ref_ca_nmdai)
        
        self.cai_nmda_dend_5 = h.Vector()
        self.cai_nmda_dend_5.record(self.dend_final[5](0.5)._ref_ca_nmdai)

        self.cai_nmda_dend_6 = h.Vector()
        self.cai_nmda_dend_6.record(self.dend_final[6](0.5)._ref_ca_nmdai)
        
        self.cai_nmda_dend_7 = h.Vector()
        self.cai_nmda_dend_7.record(self.dend_final[7](0.5)._ref_ca_nmdai) 
        
        
        self.cai_nmda_dend_8 = h.Vector()
        self.cai_nmda_dend_8.record(self.dend_final[8](0.5)._ref_ca_nmdai)
        
        self.cai_nmda_dend_9 = h.Vector()
        self.cai_nmda_dend_9.record(self.dend_final[9](0.5)._ref_ca_nmdai) 
        
        self.cai_nmda_dend_10 = h.Vector()
        self.cai_nmda_dend_10.record(self.dend_final[10](0.5)._ref_ca_nmdai)
        
        self.cai_nmda_dend_11 = h.Vector()
        self.cai_nmda_dend_11.record(self.dend_final[11](0.5)._ref_ca_nmdai)
        
        self.cai_nmda_dend_12 = h.Vector()
        self.cai_nmda_dend_12.record(self.dend_final[12](0.5)._ref_ca_nmdai)
        
        self.cai_nmda_dend_13 = h.Vector()
        self.cai_nmda_dend_13.record(self.dend_final[13](0.5)._ref_ca_nmdai)
        
        self.cai_nmda_dend_14 = h.Vector()
        self.cai_nmda_dend_14.record(self.dend_final[14](0.5)._ref_ca_nmdai)
        
        self.cai_nmda_dend_15 = h.Vector()
        self.cai_nmda_dend_15.record(self.dend_final[15](0.5)._ref_ca_nmdai)

        self.cai_nmda_dend_16 = h.Vector()
        self.cai_nmda_dend_16.record(self.dend_final[16](0.5)._ref_ca_nmdai)
        
        self.cai_nmda_dend_17 = h.Vector()
        self.cai_nmda_dend_17.record(self.dend_final[17](0.5)._ref_ca_nmdai) 
        
        
        self.cai_nmda_dend_18 = h.Vector()
        self.cai_nmda_dend_18.record(self.dend_final[18](0.5)._ref_ca_nmdai)
        
        self.cai_nmda_dend_19 = h.Vector()
        self.cai_nmda_dend_19.record(self.dend_final[19](0.5)._ref_ca_nmdai) 

        
            
            
    def createsyn(self, pf_n, mf_n, fixed_pf, dend_start_pf, dend_end_pf, fixed_mf, dend_start_mf, dend_end_mf, aa_n):
#PF       
        self.L_PF = []
        self.dend_pf = []
        
        for sec_index, sec_sec in enumerate(self.dend):
            if sec_index >= 4 and sec_index <= 15 or sec_index >= 18 and sec_index <= 32 or sec_index >= 42 and sec_index <= 83 or sec_index >= 85 and sec_index <= 104:
                self.dend_pf.append(sec_sec)   

        print('self.dend_pf', len(self.dend_pf))
        
        
#PF location
        if fixed_pf == 0:
            for fix_i in range(dend_start_pf, dend_end_pf):
                self.L_PF.append(Synapse_py3('PF',self,self.dend_pf[fix_i])) 
        
        elif fixed_pf == 1:
            for i in range(0, pf_n):
                self.L_PF.append(Synapse_py3('PF',self,self.dend_pf[i])) 
                
            
#MOSSY        
        self.L_MF = []
        self.L_MF_NMDA_B = []
        self.dend_mf = []
        self.dend_aa = []
        
        for sec_index, sec_sec in enumerate(self.dend):
            if sec_index >= 108 and sec_index <= 112 or sec_index >= 114 and sec_index <= 121 or sec_index >= 128 and sec_index <= 129 or sec_index >= 131 and sec_index <= 132 or sec_index >= 135 and sec_index <= 140 or sec_index >= 144 and sec_index <= 145 or sec_index >= 147 and sec_index <= 150:
                self.dend_mf.append(sec_sec)   
                self.dend_aa.append(sec_sec) 

        print('self.dend_mf', len(self.dend_mf))
        

        
#MF location        
        

        for i in range(0, mf_n):
            self.L_MF.append(Synapse_py3('MF',self,self.dend_final[i]))
            self.L_MF_NMDA_B.append(Synapse_py3('MF_nmda_B',self,self.dend_final[i]))





#AA
        self.L_AA = []
        self.L_AA_NMDA_B = []

        for i in range(0, aa_n):
                self.L_AA.append(Synapse_py3('AA',self,self.dend_aa[i]))
                self.L_AA_NMDA_B.append(Synapse_py3('MF_nmda_B',self,self.dend_aa[i]))




