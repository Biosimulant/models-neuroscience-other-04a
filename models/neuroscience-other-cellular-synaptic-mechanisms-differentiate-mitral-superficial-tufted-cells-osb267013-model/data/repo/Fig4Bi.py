import neuron
from neuron import h
import time
import numpy
from numpy import genfromtxt
import csv

start_time = time.time()

openfile2='MC_voltage.hoc'
filename2='Fig4Bi_1.csv'
filename3='Fig4Bi_2.csv'
filename4='Fig4Bi_3.csv'

#trial 1
h('ginputmono=0.00075')
h('ginputpoly=0.000625')
h('latepolyinput=0.042714844')

#define parameters
h('tau1inputmono=1.8')
h('tau2inputmono=2')
h('tau1inputpoly=32.2')
h('tau2inputpoly=124')
h('membres=0.000362')
h('restV=-54')
h('syn1onset=202')
h('syn2onset=202')
h('syn3onset=202')

h.xopen(openfile2)

csv.writer(open(filename2,'w',newline='')).writerows(zip(h.volt2))

#trial 2
h('ginputmono=0.0005')
h('ginputpoly=0.0003125')
h('latepolyinput=0.056953125')

h.xopen(openfile2)

csv.writer(open(filename3,'w',newline='')).writerows(zip(h.volt2))

#trial 3
h('ginputmono=0.00075')
h('ginputpoly=0.0003125')
h('latepolyinput=0.042714844')


h.xopen(openfile2)

csv.writer(open(filename4,'w',newline='')).writerows(zip(h.volt2))


total_time = (time.time() - start_time)
print('Total time to run ' + str(total_time) + ' seconds')



