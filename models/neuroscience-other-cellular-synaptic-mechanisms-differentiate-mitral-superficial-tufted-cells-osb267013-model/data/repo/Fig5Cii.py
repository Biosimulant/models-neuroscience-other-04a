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
h('ginputmono=0.0047')
h('tau1inputmono=1.4')
h('tau2inputmono=4.3')
h('ginputpoly=0.0003515625')
h('latepolyinput=0.0225')
h('tau1inputpoly=6.2')
h('tau2inputpoly=28.5')
h('membres=0.00027')
h('restV=-54')
h('syn1onset=202')
h('syn2onset=202')
h('syn3onset=202')

h.xopen(openfile)

csv.writer(open(filename,'w',newline='')).writerows(zip(h.volt2))

total_time = (time.time() - start_time)
print('Total time to run ' + str(total_time) + ' seconds')



