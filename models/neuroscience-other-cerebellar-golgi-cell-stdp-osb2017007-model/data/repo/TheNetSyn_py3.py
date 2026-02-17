from neuron import h

class Synapse_py3:
    def __init__(self,source,target,section,nrel = 0,syntype = 'ANK',record_all = 0,weight = 1):
        self.record_all = record_all
        if record_all:
            print("Recording all in Synapse")
		
        self.input = h.NetStim(0.5)
        self.input.start = -10
        self.input.number = 1
        self.input.interval = 1e9
        self.weight = weight

        self.nrel = nrel
        self.syntype = syntype

        self.postsyns = {}

        if (type(source) == type('s')):
            sourcetype = source
        else:
            sourcetype = source.whatami

        if self.record_all:
            self.SpikeTrain_input = [h.Vector(),h.Vector()]
            self.netcon_in = h.NetCon(self.input,None, 0, 0.1, 1)
            self.netcon_in.record(self.SpikeTrain_input[1], self.SpikeTrain_input[0], 1)

                
                
                
                
#GOLGI
        if sourcetype == 'PF':
            if target.whatami == 'golgi2019':
                # Make a parallel fiber synapse onto a Golgi cell
                # Use deterministic synapses
                self.whatami = "syn_PF2GoC_det"
                self.postsyns['AMPA'] = [h.Golgi_PF_syn(0.5, sec=section)]
                self.postsyns['AMPA'][0].tau_facil=10.8*5
                self.postsyns['AMPA'][0].tau_rec=35.1
                self.postsyns['AMPA'][0].tau_1=30
                self.postsyns['AMPA'][0].gmax = 1200
                self.postsyns['AMPA'][0].U=0.4

                self.nc_syn = [h.NetCon(self.input,receptor[0],0,0.1,1) for receptor in self.postsyns.values()]


        elif sourcetype == 'MF':
            if target.whatami == 'golgi2019':
                # Make a mossy fiber synapse onto a Golgi cell
                # Use deterministic synapses
                self.whatami = "syn_MF2GoC_det"
                self.postsyns['AMPA'] = [h.Golgi_MF_syn(0.5, sec=section)]
                self.postsyns['AMPA'][0].tau_facil=8
                self.postsyns['AMPA'][0].tau_rec=5
                self.postsyns['AMPA'][0].tau_1=1
                self.postsyns['AMPA'][0].gmax = 1200
                self.postsyns['AMPA'][0].U = 0.42

                self.nc_syn = [h.NetCon(self.input,receptor[0],0,0.1,1) for receptor in self.postsyns.values()]

        elif sourcetype == 'MF_nmda_B':
            if target.whatami == 'golgi2019':
                # Make a  mossy fiber NMDAB onto a Golgi cell
                # Use deterministic synapses*
                self.whatami = "syn_MFB2GoC_det"
                self.postsyns['NMDA'] = [h.PC_NMDA_NR2B(0.5, sec=section)]
                self.postsyns['NMDA'][0].tau_facil=8
                self.postsyns['NMDA'][0].tau_rec=8
                self.postsyns['NMDA'][0].tau_1=1
                self.postsyns['NMDA'][0].gmax = 2100
                self.postsyns['NMDA'][0].U=0.42
                #print 'nmda'
                self.nc_syn = [h.NetCon(self.input,receptor[0],0,0.1,1) for receptor in self.postsyns.values()]

        elif sourcetype == 'AA':
            if target.whatami == 'golgi2019':
                # Make a AA synapse onto a Golgi cell
                # Use deterministic synapses*
                self.whatami = "syn_AA2GoC_det"
                self.postsyns['AMPA'] = [h.Golgi_PF_syn(0.7, sec=section)]
                self.postsyns['AMPA'][0].tau_facil=54
                self.postsyns['AMPA'][0].tau_rec=35.1
                self.postsyns['AMPA'][0].tau_1=30
                self.postsyns['AMPA'][0].gmax = 1200
                self.postsyns['AMPA'][0].U=0.4

                self.nc_syn = [h.NetCon(self.input,receptor[0],0,0.1,1) for receptor in self.postsyns.values()]

        else:
            print('SOURCE TYPE DOES NOT EXIST SOMETHING WRONG!!!!!!!!!')



        if len(self.postsyns) > 0:
            self.i = {}
            for (post_type,post) in self.postsyns.items():
                for p in post:
                    self.i[post_type] = []
                    self.i[post_type].append(h.Vector())
                    self.i[post_type][-1].record(p._ref_i)
            print(self.i)






