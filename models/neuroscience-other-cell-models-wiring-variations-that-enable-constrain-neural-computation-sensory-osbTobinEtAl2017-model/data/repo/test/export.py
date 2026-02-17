from pyneuroml.swc.ExportSWC import convert_to_swc

files = ['bask.cell.nml', 'pyr_4_sym.cell.nml']

for f in files:
    convert_to_swc(f, add_comments=True)