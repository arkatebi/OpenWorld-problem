#!/usr/bin/env python
'''
    This module has the following method:

    count_GOterms_with_EXP:
        This method takes four input arguments:
            (1) a uniprot-swissProt file handle,
            (2) a taxonomy id,
            (3) the set of EXP codes.
            
        This method counts the number of proteins whose annotations 
        have experimental evidences, in each of BPO, CCO, and MFO ontological 
        categories, for an organism with the supplied taxon id.
          
        Finally, it returns these THREE counts.
'''
from collections import OrderedDict
from Bio import SwissProt as sp

def count_GOterms_with_EXP(fh_sprot, taxon_id, EXP_default=set([])):
    '''
    This method extract the distinct GO terms for each gene that 
    have validation with any of the experimental evidence codes.
    A set is created for these GO terms for each gene and then 
    are placed in a dictionary of each ontological categories. 
    At the end, these THREE dictionaries are returned.
    '''
    mfo_terms = OrderedDict()
    bpo_terms = OrderedDict()
    cco_terms = OrderedDict()
    count = 0
    for rec in sp.parse(fh_sprot):
        # SELECT records that are related to a specific
        # taxon_id such as 559292 for yeast:
        if taxon_id in rec.taxonomy_id:
            protName = rec.accessions[0]
            # Initialize lists for adding GO terms:
            terms_mfo = set()
            terms_bpo = set()
            terms_cco = set()
            # Go over the list of DB cross references:
            for crossRef in rec.cross_references:
                # Consider the cross_reference entries that
                # relate to GO DB:
                if crossRef[0] == 'GO':
                    goList = [crossRef[1],
                              (crossRef[3].split(':'))[0],
                              crossRef[2][0]]
                    if (crossRef[3].split(':'))[0] in EXP_default:
#                        print goList
                        if goList[-1].upper() == 'F':
                            terms_mfo.add(goList[0])
                        elif goList[-1].upper() == 'P':
                            terms_bpo.add(goList[0])
                        elif goList[-1].upper() == 'C':
                            terms_cco.add(goList[0])
            # Increase gene counts in BPO, CCO, and MFO categories
            # depending on the corresponding flag values:
            mfo_terms[protName] = terms_mfo
            bpo_terms[protName] = terms_bpo
            cco_terms[protName] = terms_cco
            count += 1
            if count > 20: 
                break
            #break
    return (mfo_terms, bpo_terms, cco_terms) 

def count_GOterms_with_EXP_old(fh_sprot, taxon_id, EXP_default=set([])):
    '''
    This method counts the distinct GO terms for each gene that 
    have validation with any of the experimental evidence codes. 
    It calculates these numbers for MFO, BPO, and CCO ontological 
    categories and then returns them.
    '''
    count_mfo = OrderedDict()
    count_bpo = OrderedDict()
    count_cco = OrderedDict()

    for rec in sp.parse(fh_sprot):
        # SELECT records that are related to a specific
        # taxon_id such as 559292 for yeast:
        if taxon_id in rec.taxonomy_id:
            protName = rec.accessions[0]
            # Initialize lists for adding GO terms:
            terms_mfo = set()
            terms_bpo = set()
            terms_cco = set()
            # Go over the list of DB cross references:
            for crossRef in rec.cross_references:
                # Consider the cross_reference entries that
                # relate to GO DB:
                if crossRef[0] == 'GO':
                    goList = [crossRef[1],
                              (crossRef[3].split(':'))[0],
                              crossRef[2][0]]
                    if (crossRef[3].split(':'))[0] in EXP_default:
#                        print goList
                        if goList[-1].upper() == 'F':
                            terms_mfo.add(goList[0])
                        elif goList[-1].upper() == 'P':
                            terms_bpo.add(goList[0])
                        elif goList[-1].upper() == 'C':
                            terms_cco.add(goList[0])
            # Increase gene counts in BPO, CCO, and MFO categories
            # depending on the corresponding flag values:
            count_mfo[protName]=len(list(terms_mfo))
            count_bpo[protName]=len(list(terms_bpo))
            count_cco[protName]=len(list(terms_cco))
            print(protName)
            print(terms_mfo) 
            print(terms_bpo) 
            print(terms_cco)
            print(count_mfo[protName]) 
            print(count_bpo[protName]) 
            print(count_cco[protName]) 
            break
#    print count_mfo
#    print count_bpo
#    print count_cco

    print(len(list(count_mfo.keys())))
#    print len(count_bpo.keys())
#    print len(count_cco.keys())
#    print count_mfo.values()
    print(max(count_mfo.values()))
    count_list = list(count_mfo.values())
    count_list.sort()
    l = len(count_list)
#    print(count_list[l-100:l])
#    print count_bpo.values() 
#    print count_cco.values() 
    return None 

def count_genes_with_EXP_old(fh_sprot, taxon_id, EXP_default=set([])):
    gene_count = {} 
    gene_count['BPO'] = 0
    gene_count['CCO'] = 0
    gene_count['MFO'] = 0

    for rec in sp.parse(fh_sprot):
        # SELECT records that are related to a specific
        # taxon_id such as 559292 for yeast:
        if taxon_id in rec.taxonomy_id:
            # Three flags to check whether an Exp evidence is found
            # in any of BPO, CCO, and MFO ontological categories: 
            bpo_exp_flag = cco_exp_flag = mfo_exp_flag = False
            # Go over the list of DB cross references:
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
                # Whenever an exp evidence for all three ontological 
                # categories are found, break out the loop:
                if (bpo_exp_flag and cco_exp_flag and mfo_exp_flag):
                    break
            # Increase gene counts in BPO, CCO, and MFO categories
            # depending on the corresponding flag values:
            if bpo_exp_flag:
                gene_count['BPO'] += 1
            if cco_exp_flag:  
                gene_count['CCO'] += 1
            if mfo_exp_flag:  
                gene_count['MFO'] += 1
    return gene_count

if __name__ == '__main__':
    print(sys.argv[0] + ':')
    print(__doc__)
    sys.exit(0)
