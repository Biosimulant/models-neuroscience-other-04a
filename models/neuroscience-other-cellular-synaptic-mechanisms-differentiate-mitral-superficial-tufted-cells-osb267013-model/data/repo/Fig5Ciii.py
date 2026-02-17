import neuron
from neuron import h
import time
import numpy
from numpy import genfromtxt
import csv

start_time = time.time()

openfile='MC_voltage.hoc'
filename='testspikes.csv'

#define parameters
h('ginputmono=0')
h('ginputpoly=0.0019')
h('latepolyinput=0.0156')
h('tau1inputpoly=4.7')
h('tau2inputpoly=25.7')
h('syn2onset=202.7')
h('tau1inputmono=2.2')
h('tau2inputmono=9.5')
h('membres=0.000272')
h('restV=-54')
h('syn1onset=202')
h('syn3onset=202')

h.xopen(openfile)

csv.writer(open(filename,'w',newline='')).writerows(zip(h.volt2))

total_time = (time.time() - start_time)
print('Total time to run ' + str(total_time) + ' seconds')



