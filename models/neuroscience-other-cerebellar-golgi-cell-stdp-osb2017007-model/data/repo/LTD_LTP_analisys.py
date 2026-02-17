import numpy as np
import collections, efel, h5py
import matplotlib.pyplot as plt
from statistics import mean 

syn_type = 70

time_list = [-25, 25]
MF_first = 1

for time_step in time_list:
    if MF_first == 0:
        pf_delay = 0
        mf_delay = time_step
    if MF_first == 1:
        pf_delay = time_step
        mf_delay = 0


    fixed_start_1 = 3000
    fixed_start_2 = 6000
    fixed_start_3 = 9000

    fixed_end_1 = 33000
    fixed_end_2 = 36000
    fixed_end_3 = 39000

    slots = [(fixed_start_1*40), fixed_start_2 *40, fixed_start_3*40, fixed_end_1 *40, fixed_end_2 *40, fixed_end_3 *40]


    number_syns = 20

    def read_h5(filename, syn_n, slots_list):
        print('syn_numer', syn_n)
        hf = h5py.File(filename, 'r')
        values = np.array(hf.get('_MF_ampa_' + str(syn_n)))
        total_max = []
        for slots in slots_list:
            check_max = []
            #print(slots)
            for values_internal in range(slots-5000, slots+5000):
                #print(values[values_internal])
                check_max.append(abs(values[values_internal]))
            total_max.append(max(check_max)*1000)

        percent_change = (mean(total_max[3:5]) - mean(total_max[0:2]))/mean(total_max[0:2])*100

        return mean(total_max[0:2]), mean(total_max[3:5]), percent_change

    if pf_delay < 0:
            pf_delay = 'meno' + str(abs(pf_delay))

    if mf_delay < 0:
        mf_delay = 'meno' + str(abs(mf_delay))


    start_current = []
    end_current = []
    syn_number = []
    percent_change = []

    for syn_n in range(0,number_syns):
        data_start, data_end, percent = read_h5(str(syn_type) + '_trace_indiv8_syn_pf_30_del_' + str(pf_delay) + '_mf_' + str(number_syns) + '_del_' + str(mf_delay) + '_aa_0_morfo_1_MF_ampa_' + str(syn_n) + '.h5', syn_n, slots)
        start_current.append(data_start)
        end_current.append(data_end)
        syn_number.append(syn_n)
        percent_change.append(percent)

    first_half_mat = np.column_stack((np.array(syn_number), np.array(start_current)))
    second_half_mat = np.column_stack((np.array(end_current), np.array(percent_change)))
    results_single = np.column_stack((first_half_mat, second_half_mat))
    average_mat = results_single.mean(axis=0)
    average_mat[0] = 100
    results = np.vstack([results_single, average_mat])

    print(results)
    np.savetxt('Simtype_' + str(syn_type) + '_MF_' + str(mf_delay) + '_PF_' + str(pf_delay) + '.csv', results, delimiter = ' ', fmt='%i %1.3f %1.3f %1.3f')
