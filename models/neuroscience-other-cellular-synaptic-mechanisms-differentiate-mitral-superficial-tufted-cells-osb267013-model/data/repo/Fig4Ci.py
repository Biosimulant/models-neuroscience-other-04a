import neuron
from neuron import h
import time
import numpy
from numpy import genfromtxt
import csv

start_time = time.time()
openfile2='sTC_voltage.hoc'

filename2='Fig4Ci_1.csv'
filename3='Fig4Ci_2.csv'
filename4='Fig4Ci_3.csv'

#define parameters

h('ginputmono=0.00759375')
h('ginputpoly=0.00025')
h('latepolyinput=0.02883252')



h('tau1inputmono=1.9')
h('tau2inputmono=2.7')
h('tau1inputpoly=10')
h('tau2inputpoly=24.5')
h('membres=0.000269')
h('restV=-56')
h('syn1onset=202')
h('syn2onset=202')
h('syn3onset=202')
h.xopen(openfile2)


csv.writer(open(filename2,'w',newline='')).writerows(zip(h.volt2))


h('ginputmono=0.003796875')
h('ginputpoly=0.001125')
h('latepolyinput=0.025628906')

h.xopen(openfile2)
csv.writer(open(filename3,'w',newline='')).writerows(zip(h.volt2))



h('ginputmono=0.003796875')
h('ginputpoly=0.00075')
h('latepolyinput=0.025628906')

h.xopen(openfile2)
csv.writer(open(filename4,'w',newline='')).writerows(zip(h.volt2))

total_time = (time.time() - start_time)
print('Total time to run ' + str(total_time) + ' seconds')



