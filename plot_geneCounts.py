#!/usr/bin/env python
'''
   Plot gene counts in BPO, CCO, and MFO 
'''
import os
import sys
from os.path import basename 
from collections import defaultdict
from collections import OrderedDict

import Config
import ConfigParser as cp
import Count_sp_genes as csg
import Download as dl
import FormatChecker as fc
import LocateDataset as ld

import matplotlib.pyplot as plt

# Default configuration file name:
config_filename = '.config'

output_fn_prefix = 'sprot_genes.stat.1'

def convert_to_number_list(bpo_list, cco_list, mfo_list): 

    for i in range(len(bpo_list)):
        bpo_list[i] = int(bpo_list[i])
        cco_list[i] = int(cco_list[i])
        mfo_list[i] = int(mfo_list[i])
    return (bpo_list, cco_list, mfo_list)

def plot_and_save(bpo_list, cco_list, mfo_list, taxon_id, taxon_name):
    b_offset = 50
    u_offset = 50
    fig = plt.figure()
#    fig = plt.figure(figsize=(40,40) )
    x_axis = range(1,11)
    plt.subplot(3,1,1)
#    ax_1=fig.add_subplot(3,1,1)

    plt_title = '# of Annotated Genes with EXP:\n' + str(taxon_name) 
#    plt.title('# of Gene Annotations with EXP Validation')
    plt.title(plt_title)
    plt.plot(x_axis, bpo_list, 'ro', x_axis, bpo_list, 'k')
    plt.ylabel('Gene Count')
    plt.axis([0, 11, min(bpo_list)-b_offset, max(bpo_list)+u_offset])
    #ax_1.text(10, 10, 'BPO', fontsize=15)

    plt.subplot(3,1,2)
#    ax_2=fig.add_subplot(3,1,2)
    plt.plot(x_axis, cco_list, 'ro', x_axis, cco_list, 'k')
    plt.ylabel('Gene Count')
    plt.axis([0, 11, min(cco_list)-b_offset, max(cco_list)+u_offset])

    plt.subplot(3,1,3) 
#    ax_3=fig.add_subplot(3,1,3) 
    plt.plot(x_axis, mfo_list, 'ro', x_axis, mfo_list, 'k')
    plt.ylabel('Gene Count')
    plt.axis([0, 11, min(mfo_list)-b_offset, max(mfo_list)+u_offset])

    fig_fname = './figures/geneFreq.' + str(taxon_id) + '.png'
    fig.savefig(fig_fname)
    #plt.show()




ConfigParam = Config.read_config(config_filename)
work_dir = ConfigParam['workdir']

fname_sprot = work_dir + '/' + 'sprot_files.txt'
fh_sf = open(fname_sprot, 'r')

tp_list = []
for line in fh_sf:
    tp_list.append(line.strip().split('.dat.')[-1])
fh_sf.close()
print tp_list

species_fname = work_dir + '/' + 'sp_list.txt'
fh_sp = open(species_fname, 'r')
taxon_id_list = []
taxon_name_list = []
for line in fh_sp:
    taxon_id_list.append(line.strip().split('\t')[0])
    taxon_name_list.append(line.strip().split('\t')[1])

geneFreq_bpo_dict = defaultdict(list) 
geneFreq_cco_dict = defaultdict(list) 
geneFreq_mfo_dict = defaultdict(list) 

fname = work_dir + '/' + 'sprot_genes.stat'
fh_sg = open(fname, 'r')
for line in fh_sg:
    print(line.strip())
    line_values = line.strip().split('\t')
    tp = line_values[0]
    print(line_values[0])
    id_no = 0
    for i in range(1,31,3):
        geneFreq_bpo_dict[taxon_id_list[id_no]].append(line_values[i])
        geneFreq_cco_dict[taxon_id_list[id_no]].append(line_values[i+1])
        geneFreq_mfo_dict[taxon_id_list[id_no]].append(line_values[i+2])
        id_no += 1

for i in range(0, len(taxon_id_list)):
    print taxon_id_list[i] 
    print taxon_name_list[i] 
    bpo_list = list(geneFreq_bpo_dict[taxon_id_list[i]])
    cco_list = list(geneFreq_cco_dict[taxon_id_list[i]])
    mfo_list = list(geneFreq_mfo_dict[taxon_id_list[i]])
    bpo_list, cco_list, mfo_list = convert_to_number_list(bpo_list, cco_list, mfo_list)
    plot_and_save(bpo_list, cco_list, mfo_list, taxon_id_list[i], taxon_name_list[i]) 

