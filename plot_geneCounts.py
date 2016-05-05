#!/usr/bin/env python
'''
   Plot gene counts in BPO, CCO, and MFO 
'''
import os
import sys
from os.path import basename 
from collections import defaultdict

import ArgParser_plot as ap
import Config
import ConfigParser as cp
import FormatChecker as fc
import LocateDataset as ld

import matplotlib.pyplot as plt

# Default configuration file name:
config_filename = '.config'
no_of_organisms = 10 

class plot_geneCounts:
    def __init__(self):
        # Collect user arguments into a dictionary:
        self.parsed_dict = ap.parse_args() 

        # Collect config file entries:
        self.ConfigParam = Config.read_config(config_filename) 
        self.work_dir = self.ConfigParam['workdir']
        self.figure_dir = './figures'
        # Look for workspace, and if none exists create one:
        if not os.path.exists(self.work_dir):
            os.makedirs(self.work_dir) # Create work space

        # Extract species list file name: 
        t1 = self.parsed_dict['t1'] 
        # Locate file for the species list file:
        self.species_filename = ld.locate_anyfile(t1, self.work_dir)

        # Extract filename containing the list of SwissProt file names:
        t2 = self.parsed_dict['t2'] 
        # Locate the file containing the list of the UniProtKB/SwissProt
        # file names over a series of time points:
        self.sprot_fnList_filename = ld.locate_anyfile(t2, self.work_dir)

        # Extract the filename containing the gene counts:  
        t3 = self.parsed_dict['t3'] 
        # Locate the gene count file:
        self.geneCount_filename = ld.locate_anyfile(t3, self.work_dir)
        return None

    def create_fig_name(self, fname_prefix):
        """ 
        Creates an output filename based on the output file prefix
        provided by the user and at the end returns the newly
        created output filename.
        """
        ob = fname_prefix
        index = 1
        while os.path.exists(self.figure_dir + '/' + ob + '.' + str(index) + '.png'):
            index = index + 1
        output_filename = self.figure_dir + '/' + ob + '.' + str(index) + '.png'
        return output_filename

    def convert_str2num_list(self, bpo_list, cco_list, mfo_list):
        for i in range(len(bpo_list)):
            bpo_list[i] = int(bpo_list[i])
            cco_list[i] = int(cco_list[i])
            mfo_list[i] = int(mfo_list[i])
        return (bpo_list, cco_list, mfo_list)

    def plot_and_save(self, bpo_list, cco_list, mfo_list, taxon_id, taxon_name):
        # Extract the time point list from the sprot file name list: 
        tp_lst = self.extract_timepoint_info(
                       open(self.sprot_fnList_filename, 'r'))

        print tp_lst
        print len(tp_lst)
#        raise SystemExit

        b_offset = 50
        u_offset = 50
        fig = plt.figure()
    #    fig = plt.figure(figsize=(40,40) )
        x_axis = range(1,11)
#        plt.subplot(3,1,1)
        ax_1=fig.add_subplot(3,1,1)
        plt_title = '# of Annotated Genes with EXP:\n' + str(taxon_name) 
    #    plt.title('# of Gene Annotations with EXP Validation')
        plt.title(plt_title)
        plt.plot(x_axis, bpo_list, 'ro', x_axis, bpo_list, 'k')
        plt.ylabel('Gene Count')
        plt.axis([0, 11, min(bpo_list)-b_offset, max(bpo_list)+u_offset])
#        plt.xticks(x_axis, tp_lst, size='small', horizontalalignment='center')
        plt.xticks(x_axis, tp_lst, horizontalalignment='center')

        ax_1.text(10, 10, 'BPO', fontsize=15)

        plt.subplot(3,1,2)
    #    ax_2=fig.add_subplot(3,1,2)
        plt.plot(x_axis, cco_list, 'ro', x_axis, cco_list, 'k')
        plt.ylabel('Gene Count')
        plt.axis([0, 11, min(cco_list)-b_offset, max(cco_list)+u_offset])
#        plt.xticks(x_axis, tp_lst, size='small', horizontalalignment='center')
        plt.xticks(x_axis, tp_lst, horizontalalignment='center')

        plt.subplot(3,1,3) 
    #    ax_3=fig.add_subplot(3,1,3) 
        plt.plot(x_axis, mfo_list, 'ro', x_axis, mfo_list, 'k')
        plt.ylabel('Gene Count')
        plt.axis([0, 11, min(mfo_list)-b_offset, max(mfo_list)+u_offset])
        fig_fname = self.create_fig_name('geneFreq.' + str(taxon_id))
#        plt.xticks(x_axis, tp_lst, size='small', horizontalalignment='center')
        plt.xticks(x_axis, tp_lst, horizontalalignment='center')

        print fig_fname
#        fig.savefig(fig_fname)
        plt.show()

    def plot_and_save_old(self, bpo_list, cco_list, mfo_list, taxon_id, taxon_name):
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
        fig_fname = self.create_fig_name('geneFreq.' + str(taxon_id))
        print fig_fname
        fig.savefig(fig_fname)
        plt.show()

    def extract_taxon_info(self, fh): 
        taxon_id_list = []
        taxon_name_list = []
        for line in fh:
            taxon_id_list.append(line.strip().split('\t')[0])
            taxon_name_list.append(line.strip().split('\t')[1])
        return (taxon_id_list, taxon_name_list) 

    def extract_timepoint_info(self, fh): 
        tp_list = []
        for line in fh:
            tp_list.append(line.strip().split('.dat.')[-1])
        return tp_list 

    def extract_gene_count(self, tax_id_lst, fh): 
        # Initialize dictionary for gene count in BPO ontological group: 
        gc_bpo_dict = defaultdict(list) 
        # Initialize dictionary for gene count in CCO ontological group: 
        gc_cco_dict = defaultdict(list) 
        # Initialize dictionary for gene count in MFO ontological group: 
        gc_mfo_dict = defaultdict(list) 
        for line in fh:
            line_values = line.strip().split('\t')
            tp = line_values[0]
            id_no = 0
            for i in range(1,no_of_organisms*3+1,3):
                gc_bpo_dict[tax_id_lst[id_no]].append(line_values[i])
                gc_cco_dict[tax_id_lst[id_no]].append(line_values[i+1])
                gc_mfo_dict[tax_id_lst[id_no]].append(line_values[i+2])
                id_no += 1
        return (gc_bpo_dict, gc_cco_dict, gc_mfo_dict)

    def process_data(self): 
        # Extract time points from the sprot file name list:  
        tp_lst = self.extract_timepoint_info(
                       open(self.sprot_fnList_filename, 'r'))
        print tp_lst
        # Extract taxon id list and taxon name list:
        tax_id_lst, tax_name_lst = self.extract_taxon_info(
                                        open(self.species_filename, 'r'))

         # Extract gene count from the gene count file:
        gc_bpo_dict, gc_cco_dict, gc_mfo_dict = self.extract_gene_count(
                                                     tax_id_lst, 
                                                     open(self.geneCount_filename, 'r'))

        # Extract gene counts for each organism and plot and save graphs:  
        for i in range(0, len(tax_id_lst)):
            # Convert the gene counts from a list of 
            # strings to a list of numbers: 
            bpo_list, cco_list, mfo_list = self.convert_str2num_list(
                                                gc_bpo_dict[tax_id_lst[i]], 
                                                gc_cco_dict[tax_id_lst[i]],
                                                gc_mfo_dict[tax_id_lst[i]])
            # Plot the gene counts in BPO, CCO, and MFO ontological categories
            # and save them to the files:
            self.plot_and_save(bpo_list, 
                               cco_list, 
                               mfo_list, 
                               tax_id_lst[i], 
                               tax_name_lst[i])
#            break
        return None
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print (sys.argv[0] + ':')
        print(__doc__)
    else:
        pg = plot_geneCounts() # Create an instance of plot_geneCount class
        pg.process_data()      # Process data
    sys.exit(0)


