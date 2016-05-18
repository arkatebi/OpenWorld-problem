#!/usr/bin/env python
'''
    This module has the following method:

    count_genes_with_EXP:
        This method takes four input arguments:
            (1) a uniprot-swissProt file handle,
            (2) a taxonomy id,
            (3) the set of EXP codes.
            
        This method counts the number of proteins whose annotations 
        have experimental evidences, in each of BPO, CCO, and MFO ontological 
        categories, for an organism with the supplied taxon id.
          
        Finally, it returns these THREE counts.
'''
from Bio import SwissProt as sp

def count_genes_with_EXP(fh_sprot, taxon_id, EXP_default=set([])):
    gene_count = {} 
    gene_count['MFO'] = 0
    gene_count['BPO'] = 0
    gene_count['CCO'] = 0

    for rec in sp.parse(fh_sprot):
        # SELECT records that are related to a specific
        # taxon_id such as 559292 for yeast:
        if taxon_id in rec.taxonomy_id:
            # Three flags to check whether an Exp evidence is found
            # in any of BPO, CCO, and MFO ontological categories:
            exp_flag = {}
            exp_flag['MFO'] = False
            exp_flag['BPO'] = False
            exp_flag['CCO'] = False

            # Go over the list of DB cross references:
            for crossRef in rec.cross_references:
                # Consider the cross_reference entries that
                # relate to GO DB:
                if crossRef[0] == 'GO':
                    goList = [crossRef[1],
                              (crossRef[3].split(':'))[0],
                              crossRef[2][0]]
                    if (crossRef[3].split(':'))[0] in EXP_default:
                        if goList[-1].upper() == 'F':
                            exp_flag['MFO'] = True
                        elif goList[-1].upper() == 'P':
                            exp_flag['BPO'] = True
                        elif goList[-1].upper() == 'C':
                            exp_flag['CCO'] = True
                # Whenever an exp evidence for all three ontological 
                # categories are found, break out the loop:
                if (exp_flag['MFO'] and exp_flag['BPO'] and exp_flag['CCO']):
                    break
            # Increase gene counts in BPO, CCO, and MFO categories
            # depending on the corresponding flag values:
            if exp_flag['MFO']:
                gene_count['MFO'] += 1
            if exp_flag['BPO']:
                gene_count['BPO'] += 1
            if exp_flag['CCO']:
                gene_count['CCO'] += 1
    return gene_count

def count_genes_with_EXP_old(fh_sprot, taxon_id, EXP_default=set([])):
    # The exp_bpo_ct variable counts total number of genes in
    # the sprot file related to the taxonomy id taxon_id whose
    # annotations have EXP evidence and in BPO ontological category:
    exp_bpo_ct = 0

    # The exp_cco_ct variable counts total number of genes in
    # the sprot file related to the taxonomy id taxon_id whose
    # annotations have EXP evidence and in CCO ontological category:
    exp_cco_ct = 0

    # The exp_mfo_ct variable counts total number of genes in
    # the sprot file related to the taxonomy id taxon_id whose
    # annotations have EXP evidence and in MFO ontological category:
    exp_mfo_ct = 0

    for rec in sp.parse(fh_sprot):
        # SELECT records that are related to a specific
        # taxon_id such as 559292 for yeast:
        if taxon_id in rec.taxonomy_id:
            bpo_exp_flag = cco_exp_flag = mfo_exp_flag = False
            # Go over the list of GO information:
            for crossRef in rec.cross_references:
                # Consider the cross_reference entries that
                # relate to GO DB:
                if crossRef[0] == 'GO':
                    goList = [crossRef[1],
                              (crossRef[3].split(':'))[0],
                              crossRef[2][0]]
                    if (crossRef[3].split(':'))[0] in EXP_default:
                        if goList[-1].upper() == 'P':
                            bpo_exp_flag = True
                        elif goList[-1].upper() == 'C':
                            cco_exp_flag = True
                        elif goList[-1].upper() == 'F':
                            mfo_exp_flag = True
                if (bpo_exp_flag and cco_exp_flag and mfo_exp_flag):
                    break
            # Increase gene counts in BPO, CCO, and MFO categories
            # depending on the corresponding flag values:
            if bpo_exp_flag:
                exp_bpo_ct += 1
            if cco_exp_flag:  
                exp_cco_ct += 1
            if mfo_exp_flag:  
                exp_mfo_ct += 1
    return (exp_bpo_ct, exp_cco_ct, exp_mfo_ct)

if __name__ == '__main__':
    print (sys.argv[0] + ':')
    print(__doc__)
    sys.exit(0)
