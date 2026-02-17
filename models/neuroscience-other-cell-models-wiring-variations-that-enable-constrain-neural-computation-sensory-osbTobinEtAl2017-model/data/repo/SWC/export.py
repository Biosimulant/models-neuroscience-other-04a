from pyneuroml.swc.ExportSWC import convert_to_swc

from neuroml import *
from pyneuroml import pynml
import random

# This is same as ../nC_projects_lite/PN1LS_allORNs/generatedNeuroML2/neuron_PN1_LS_sk_419138.cell.nml
files = ['../nC_projects_lite/PN1LS_allORNs_Rinput/generatedNeuroML2/neuron_PN1_LS_sk_419138.cell.nml']

files = ['../nC_projects_lite/PN1LS_allORNs/generatedNeuroML2/neuron_PN1_LS_sk_419138.cell.nml',
         '../nC_projects_lite/PN1RS_allORNs/generatedNeuroML2/neuron_PN1_RS_sk_638603.cell.nml',
         '../nC_projects_lite/PN2LS_allORNs/generatedNeuroML2/neuron_PN2_LS_sk_427345.cell.nml',
         '../nC_projects_lite/PN2RS_allORNs/generatedNeuroML2/neuron_PN2_RS_sk_480245.cell.nml',
         '../nC_projects_lite/PN3LS_allORNs/generatedNeuroML2/neuron_PN3_LS_sk_668267.cell.nml']
         
         
net_ref = "AllCells"
net_doc = NeuroMLDocument(id=net_ref)

net = Network(id=net_ref)
net_doc.networks.append(net)

count = 0

cells = {}

for f in files:
    print('Processing %s'%f)
    import os 
    cwd = os.path.dirname(os.path.realpath(__file__))
    convert_to_swc(f, add_comments=True, target_dir=cwd)
    
    net_doc.includes.append(IncludeType(f))
    
    cell_id = f.split('/')[-1].split('.')[0]

    pop = Population(id="Pop_%s"%cell_id, component=cell_id, type="populationList")

    net.populations.append(pop)

    for i in [0]:
        inst = Instance(id=i)
        pop.instances.append(inst)
        p = Property(tag='color', value='%s %s %s'%(random.random(),random.random(),random.random()))
        pop.properties.append(p)

        X=count*50
        Y=0
        Z=0

        inst.location = Location(x=X, y=Y, z=Z)

        count+=1
        
net_file = '../NeuroML2/%s.net.nml'%(net_ref)
writers.NeuroMLWriter.write(net_doc, net_file)

print("Written network with %i cells in network to: %s"%(count,net_file))

pynml.nml2_to_png(net_file, max_memory="2G")