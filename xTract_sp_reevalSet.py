#!/usr/bin/env python
'''
    This module has the following main method create_reevalSet_allSpecies
    which is the entry point of this module:
    create_reevalSet_allSpecies(fh_mapFile_t1, fh_sprot_t2,
                                reevalSet_handle, 
                                reevalSet_map_handle,
                                ontType,
                                EXP_default=set([])):
        This method goes over the records in the SwissProt file 
        at time t2. It checks whether a the protein in this 
        record matches any of the entries in the map file from 
        time point t1. The map file at time point t1 has three 
        columns: 1st column has the target id, second column 
        has protein name, and the third column has the GO term.  
        It checks whether for a protein, new GO terms are gained 
        at time t2. If it does, it write out the sequence to the 
        output file. It also writes out the gained GO terms to 
        the output map file in the same format as the map file 
        at time t1. 
   
    The module also has a few other internal methods: 
        __collect_prevES(fh_mapFile): 
        This method creates a dictionary from the map file. 
        It constructs the keys of the dictionary by 
        combining columns 1 and 2 with a separator ":" 
        between them. And the values are the corresponding 
        GO terms.   

       __print_prevES_dict(GOterm_dict)
       This method prints the keys and the values of the dictionary
       that __collect_prevES creates. 

       __is_accession_found(accession_t2, prevES_dict):
       This method checks whether the protein in the accession field 
       of the SwissProt record mathes any of the keys in the prevES_dict. 
       If it does, it returns the key; otherwise, it returns None. 
'''

import sys
from collections import defaultdict
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SwissProt as sp

def __collect_prevES(fh_mapFile): 
    GOterm_dict = defaultdict(set)
    for line in fh_mapFile:
        fields = line.strip().split('\t')
        k=fields[0] + ':' + fields[1]
        GOterm_dict[k].add(fields[2])
    return GOterm_dict
    
def __print_prevES_dict(GOterm_dict): 
    for k in sorted(GOterm_dict.keys()): 
        print('>' + k + '\t', ','.join(str(t) for t in GOterm_dict[k]))
    return None

def __is_accession_found(accession_t2, prevES_dict):
    for k in sorted(prevES_dict.keys()):
        protName = k.split(':')[1]
        accession_t2 = [x.upper() for x in accession_t2]
        if protName.upper() in accession_t2:
            return k 
    return None 

def create_reevalSet_allSpecies(fh_mapFile_t1, fh_sprot_t2,
                                reevalSet_handle, 
                                reevalSet_map_handle,
                                ontType,
                                EXP_default=set([])):
    prevES_dict = __collect_prevES(fh_mapFile_t1)

    # Counter for the number of proteins that had also annotations at t1: 
    countMatch = 0 
    # Counter for the number of proteins that gained annotations at t2: 
    countFunctionGain = 0
    for rec in sp.parse(fh_sprot_t2):
        # Checks whether the protein had annotation at t1: 
        retVal = __is_accession_found(rec.accessions, prevES_dict)
        if (retVal):
            countMatch+=1
            exp_code = False
            goTerms = set()
            # Going over the list of GO information:
            for crossRef in rec.cross_references:
                # Consider the cross_reference entries
                # that relate to GO DB:
                if crossRef[0] == 'GO':
                    goList = [crossRef[1],
                             (crossRef[3].split(':'))[0],
                             crossRef[2][0]]
                    if goList[2] == ontType and \
                       (crossRef[3].split(':'))[0] in EXP_default:
                        goTerms.add(goList[0])
                        exp_code = True
                        #break
            # If the current protein's annotation gains EXP evidence
            # code at t2, write the sequence to the output file:
            # GO terms from t1: 
            curGOterms=prevES_dict[retVal]
            # Gained GO terms between t1 and t2: 
            newGOterms = goTerms-curGOterms
            if exp_code and newGOterms:
                countFunctionGain += 1
                target_id=retVal.split(':')[0]
                protName=retVal.split(':')[1]
                outseq = SeqRecord(Seq(rec.sequence),
                                   id=str(target_id),
                                   description = "%s" %
                                   (protName))
                outseq_list = [outseq]
                # Write out the sequence to fasta file:
                SeqIO.write(outseq_list, reevalSet_handle, "fasta")

                # Write out the mapping to the map file:
                # (protein sequence id, protein name, new GO term(s))
                for gt in newGOterms:
                    #mapStr = "T" + str(target_id) + '\t' + \
                    #           str(gt) + '\n'
                    mapStr = str(target_id) + '\t' + \
                             str(protName) + '\t' + \
                             str(gt) + '\n'
                    reevalSet_map_handle.write("%s" % mapStr)
                return None
                #sys.exit(0)
    print('countMatch at t2: ' + str(countMatch))
    print('countFunctionGain at t2: ' + str(countFunctionGain))
    return None

if __name__ == '__main__':
    print (sys.argv[0] + ':')
    print(__doc__)
    sys.exit(0)
