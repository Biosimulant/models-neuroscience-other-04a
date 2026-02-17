import matplotlib.pyplot as plt
from neuron import h,gui 
from golgi2019_net_py3_1 import Golgi_net_py3_1
import multiprocessing
import random as rnd
import numpy as np
import h5py

from golgi_number_1 import number_ind_1
import sys


mf_delay = 0
pf_delay = -25

cell = Golgi_net_py3_1()

Hines = h.CVode()
Hines.active(0) #0 fixed step, 1 variable time step

cpu = multiprocessing.cpu_count()
h.load_file("parcom.hoc")
p = h.ParallelComputeTool()
p.change_nthread(16,1)
p.multisplit(1)


h.nrncontrolmenu()

stimdata = dict()
stimdata['timeglobal'] =  40000

synapsesdata = dict()

#parallel fiber
#syn properties
synapsesdata['syninterval_pf'] = 10
synapsesdata['synnumber_pf'] = 1
synapsesdata['synnoise_pf'] = 0
#timing
synapsesdata['main_delay_pf'] = 10000
synapsesdata['burst_repeat_pf'] = 250
synapsesdata['burst_delay_pf'] = pf_delay
synapsesdata['final_empty_pf'] = 10000


#mossy fiber
#syn properties
synapsesdata['syninterval_mf'] = 10
synapsesdata['synnumber_mf'] = 1
synapsesdata['synnoise_mf'] = 0
#timing
synapsesdata['main_delay_mf'] = 10000
synapsesdata['burst_repeat_mf'] = 250
synapsesdata['burst_delay_mf'] = mf_delay
synapsesdata['final_empty_mf'] = 10000


#ascending axon
#syn properties
synapsesdata['syninterval_aa'] = 10
synapsesdata['synnumber_aa'] = 1
synapsesdata['synnoise_aa'] = 0
#timing
synapsesdata['main_delay_aa'] = 0
synapsesdata['burst_repeat_aa'] = 0
synapsesdata['burst_delay_aa'] = 0
synapsesdata['final_empty_aa'] = 0


#inib fiber
#syn properties
synapsesdata['syninterval_inib'] = 10
synapsesdata['synnumber_inib'] = 1
synapsesdata['synnoise_inib'] = 0
#timing
synapsesdata['main_delay_inib'] = 0
synapsesdata['burst_repeat_inib'] = 0
synapsesdata['burst_delay_inib'] = 0
synapsesdata['final_empty_inib'] = 0

#Stimulation repeat.
#Parallel fibers
if synapsesdata['main_delay_pf'] == 0 and synapsesdata['final_empty_pf'] == 0 and synapsesdata['burst_repeat_pf'] == 0:
    totalstim_pf = 0
    print('Number of stim PF: ', 0)
else:
    totalstim_pf = int((stimdata['timeglobal'] - synapsesdata['main_delay_pf'] - synapsesdata['final_empty_pf'])/  synapsesdata['burst_repeat_pf'])
    print('Number of stim PF: ', totalstim_pf)

#Mossy fibers
if synapsesdata['main_delay_mf'] == 0 and synapsesdata['final_empty_mf'] == 0 and synapsesdata['burst_repeat_mf'] == 0:
    totalstim_mf = 0
    print('Number of stim MF: ', 0)
else:
    totalstim_mf = int((stimdata['timeglobal'] - synapsesdata['main_delay_mf'] - synapsesdata['final_empty_mf'])/  synapsesdata['burst_repeat_mf'])
    print('Number of stim MF: ', totalstim_mf)




#Number of synapses each types
pf_syn = 30
mf_syn = 20

aa_syn = 0

fixed_dend_pf = 1 # 1 deactivate this part
start_dend_pf = 30
end_dend_pf = 50

fixed_dend_mf = 1
start_dend_mf = 0
end_dend_mf = 0


stimdata['stim0del'] = 10000
stimdata['stim0dur'] = 20000
stimdata['stim0amp'] = -0.052

stim = [h.IClamp(0.5,sec=cell.soma[0])]

stim[0].delay = stimdata['stim0del']
stim[0].dur = stimdata['stim0dur']
stim[0].amp = stimdata['stim0amp']

stim2 = [h.Clamp_mod(0.5,sec=cell.soma[0])]

stim2[0].dur2 = 20000

cell.createsyn(pf_syn, mf_syn, fixed_dend_pf, start_dend_pf, end_dend_pf, fixed_dend_mf, start_dend_mf, end_dend_mf, aa_syn)


#PF syn # to be updated
spk_stim_pf_total = []

for burst in range(-3, (int(totalstim_pf) + 1)):
    if burst == -3:
        #print('burst_N°', burst)
        spk_stim_pf = h.NetStim()
        spk_stim_pf.interval = 1
        spk_stim_pf.number = 1
        spk_stim_pf.noise = 0
        spk_stim_pf.start = 3000 + synapsesdata['burst_delay_pf']

        spk_stim_pf_total.append(spk_stim_pf)

    if burst == -2:
        #print('burst_N°', burst)
        spk_stim_pf = h.NetStim()
        spk_stim_pf.interval = 1
        spk_stim_pf.number = 1
        spk_stim_pf.noise = 0
        spk_stim_pf.start = 6000 + synapsesdata['burst_delay_pf']

        spk_stim_pf_total.append(spk_stim_pf)

    if burst == -1:
        #print('burst_N°', burst)
        spk_stim_pf = h.NetStim()
        spk_stim_pf.interval = 1
        spk_stim_pf.number = 1
        spk_stim_pf.noise = 0
        spk_stim_pf.start = 9000 + synapsesdata['burst_delay_pf']

        spk_stim_pf_total.append(spk_stim_pf)

    if burst > 0 and burst < int(totalstim_pf) -4:
        print('burst_stim_N°', burst)
        spk_stim_pf = h.NetStim()
        spk_stim_pf.interval = synapsesdata['syninterval_pf']
        spk_stim_pf.number = synapsesdata['synnumber_pf']
        spk_stim_pf.noise = synapsesdata['synnoise_pf']
        spk_stim_pf.start = synapsesdata['main_delay_pf'] + (synapsesdata['burst_repeat_pf'] * burst) + synapsesdata['burst_delay_pf']

        spk_stim_pf_total.append(spk_stim_pf)
        #print('new_code', synapsesdata['main_delay_pf'] + (synapsesdata['burst_repeat_pf'] * burst) + synapsesdata['burst_delay_pf'])

    if burst == int(totalstim_pf) - 3:
        print('burst_post_N°', burst)
        spk_stim_pf = h.NetStim()
        spk_stim_pf.interval = 1
        spk_stim_pf.number = 1
        spk_stim_pf.noise = 0
        spk_stim_pf.start = 33000 + synapsesdata['burst_delay_pf']

        spk_stim_pf_total.append(spk_stim_pf)

    if burst == int(totalstim_pf) -2:
        print('burst_post_N°', burst)
        spk_stim_pf = h.NetStim()
        spk_stim_pf.interval = 1
        spk_stim_pf.number = 1
        spk_stim_pf.noise = 0
        spk_stim_pf.start = 36000 + synapsesdata['burst_delay_pf']

        spk_stim_pf_total.append(spk_stim_pf)

    if burst == int(totalstim_pf) - 1:
        print('burst_post_N°', burst)
        spk_stim_pf = h.NetStim()
        spk_stim_pf.interval = 1
        spk_stim_pf.number = 1
        spk_stim_pf.noise = 0
        spk_stim_pf.start = 39000 + synapsesdata['burst_delay_pf']

        spk_stim_pf_total.append(spk_stim_pf)



spk_nc_pfsyn = []

print('len pf', len(cell.L_PF))

for m in range(int(totalstim_pf) + 1):
    spk_nc_pfsyn.append([h.NetCon(spk_stim_pf_total[m],PF.input,0,0.1,1) for PF in cell.L_PF])


#MF syn
spk_stim_mf_total = []

for burst in range(-3, int(totalstim_mf) + 1):
    if burst == -3:
        #print('burst_N°', burst)
        spk_stim_mf = h.NetStim()
        spk_stim_mf.interval = 1
        spk_stim_mf.number = 1
        spk_stim_mf.noise = 0
        spk_stim_mf.start = 3000 + synapsesdata['burst_delay_mf']

        spk_stim_mf_total.append(spk_stim_mf)

    if burst == -2:
        #print('burst_N°', burst)
        spk_stim_mf = h.NetStim()
        spk_stim_mf.interval = 1
        spk_stim_mf.number = 1
        spk_stim_mf.noise = 0
        spk_stim_mf.start = 6000 + synapsesdata['burst_delay_mf']

        spk_stim_mf_total.append(spk_stim_mf)

    if burst == -1:
        #print('burst_N°', burst)
        spk_stim_mf = h.NetStim()
        spk_stim_mf.interval = 1
        spk_stim_mf.number = 1
        spk_stim_mf.noise = 0
        spk_stim_mf.start = 9000 + synapsesdata['burst_delay_mf']

        spk_stim_mf_total.append(spk_stim_mf)

    if burst > 0 and burst < int(totalstim_mf) -4:
        #print('burst_N°', burst)
        spk_stim_mf = h.NetStim()
        spk_stim_mf.interval = synapsesdata['syninterval_mf']
        spk_stim_mf.number = synapsesdata['synnumber_mf']
        spk_stim_mf.noise = synapsesdata['synnoise_mf']
        spk_stim_mf.start = synapsesdata['main_delay_mf'] + (synapsesdata['burst_repeat_mf'] * burst) + synapsesdata['burst_delay_mf']

        spk_stim_mf_total.append(spk_stim_mf)

    if burst == int(totalstim_mf) - 3:
        print('burst_post_N°', burst)
        spk_stim_mf = h.NetStim()
        spk_stim_mf.interval = 1
        spk_stim_mf.number = 1
        spk_stim_mf.noise = 0
        spk_stim_mf.start = 33000 + synapsesdata['burst_delay_mf']

        spk_stim_mf_total.append(spk_stim_mf)

    if burst == int(totalstim_mf) -2:
        print('burst_post_N°', burst)
        spk_stim_mf = h.NetStim()
        spk_stim_mf.interval = 1
        spk_stim_mf.number = 1
        spk_stim_mf.noise = 0
        spk_stim_mf.start = 36000 + synapsesdata['burst_delay_mf']

        spk_stim_mf_total.append(spk_stim_mf)

    if burst == int(totalstim_mf) - 1:
        print('burst_post_N°', burst)
        spk_stim_mf = h.NetStim()
        spk_stim_mf.interval = 1
        spk_stim_mf.number = 1
        spk_stim_mf.noise = 0
        spk_stim_mf.start = 39000 + synapsesdata['burst_delay_mf']

        spk_stim_mf_total.append(spk_stim_mf)

spk_nc_mfsyn = []
spk_nc_mfsyn_B = []

print('len mf', len(cell.L_MF))


for v in range(int(totalstim_mf) + 1):
    spk_nc_mfsyn.append([h.NetCon(spk_stim_mf_total[v],MF.input,0,0.1,1) for MF in cell.L_MF])
    spk_nc_mfsyn_B.append([h.NetCon(spk_stim_mf_total[v],MF_nmda_B.input,0,0.1,1) for MF_nmda_B in cell.L_MF_NMDA_B])




#initialize
h.dt = 0.025
h.celsius = 32
h.tstop = stimdata['timeglobal']
h.v_init = -65

def initialize():
    h.finitialize()
    h.run()

initialize()


stimdata['i'] = number_ind_1['indiv']

if synapsesdata['burst_delay_pf'] < 0:
        synapsesdata['burst_delay_pf'] = 'meno' + str(abs(synapsesdata['burst_delay_pf']))

if synapsesdata['burst_delay_mf'] < 0:
    synapsesdata['burst_delay_mf'] = 'meno' + str(abs(synapsesdata['burst_delay_mf']))


def save_me(time_vec, vm_vec, pf_n, aa_n, mf_n, del_pf, del_mf, what, which):

    hf = h5py.File('70_trace_indiv' + str(stimdata['i']) + '_syn_pf_' + str(pf_n) + '_del_' + del_pf + '_mf_' + str(mf_n) + '_del_' + del_mf + '_aa_' + str(aa_n) + '_morfo_' + str(number_ind_1['morfo_n']) + what + '.h5', 'w')
    hf.create_dataset('time_vec', data=time_vec)
    hf.create_dataset(what, data = vm_vec)
    hf.close()

    fig, ax = plt.subplots()
    ax.plot(time_vec, vm_vec, 'b', label='spikes')

    legend = ax.legend(loc='upper right', shadow=True)

    frame = legend.get_frame()
    frame.set_facecolor('0.90')

    plt.xlabel("time (ms)")
    plt.ylabel(which)

    plt.savefig('70_trace_indiv' + str(stimdata['i']) + '_syn_pf_' + str(pf_n) + '_del_' + del_pf + '_mf_' + str(mf_n) + '_del_' + del_mf + '_aa_' + str(aa_n) + '_morfo_' + str(number_ind_1['morfo_n']) + what + '.eps')
    plt.close()


save_me(np.array(cell.time_vector), np.array(cell.vm), pf_syn, aa_syn, mf_syn, str(synapsesdata['burst_delay_pf']), str(synapsesdata['burst_delay_mf']), '_VM_soma', "Voltage")


#total

#W
for syn_type in range(0, mf_syn):
    #AMPA_MF
    save_me(np.array(cell.time_vector), np.array(cell.L_MF[syn_type].i['AMPA'][0]), pf_syn, aa_syn, mf_syn, str(synapsesdata['burst_delay_pf']), str(synapsesdata['burst_delay_mf']), '_MF_ampa_' + str(syn_type), "current")

quit()
