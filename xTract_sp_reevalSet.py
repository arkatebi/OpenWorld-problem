#!/usr/bin/env python
'''
    This module has the following methods. create_testSet_allSpecies 
    and create_testSet_singSpecies are the entry points for these methods.
    create_testSet_allSpecies(fh_sprot_t1, fh_sprot_t2,
                              testSet_LK_mfo_handle, 
                              testSet_LK_mfo_map_handle,
                              testSet_LK_bpo_handle,
                              testSet_LK_bpo_map_handle,
                              testSet_LK_cco_handle,
                              testSet_LK_cco_map_handle,
                              EXP_default=set([]))
        This method invokes filter_testSet_allSpecies() 
        to generate test sequences on each of three ontologies:
        MFO, BPO, and CCO. 
   
    create_testSet_singleSpecies(fh_sprot_t1, fh_sprot_t2, taxon_id,
                                 testSet_LK_mfo_handle, 
                                 testSet_LK_mfo_map_handle,
                                 testSet_LK_bpo_handle,
                                 testSet_LK_bpo_map_handle,
                                 testSet_LK_cco_handle,
                                 testSet_LK_cco_map_handle,
                                 EXP_default=set([]))
        This methods is similar to create_testSet_allSpecies but works 
        for single species by invoking filter_testSet_singleSpecies 
        method.

    filter_testSet_allSpecies(fh_sprot_t1, fh_sprot_t2, fh_test_seq, 
                              fh_map, ontType, EXP_default=set([]))
        This method takes five input arguments:
            (1) a file handle for the UniprotKB/SwissProt file at t1 
            (2) a file handle for the UniprotKB/SwissProt file at t2 
            (3) an file handle for writing test sequences,
            (4) an file handle for writing the mapping between
                target id and protein name, and
            (5) the ontology type for which the test data is generated, and 
            (6) the set of EXP codes.
        This method invokes get_NEXP_accession_list to obtain the list of
        proteins that did not have EXP evidence codes at t1 but had
        no-EXP evidence codes at t1. Then the method uses this list to
        filter the proteins whose annotations gained EXP evidence codes
        at t2. It then writes the sequences to the output file. It also
        writes the mapping between the protein name, sequence id, and 
        the corresponding GO term(s) to the map file.

    filter_testSet_singleSpecies(fh_sprot_t1, fh_sprot_t2, taxon_id, fh_test_seq,
                                 fh_map, ontType, EXP_default=set([]))
        This method is similar to filter_testSet_allSpecies but works on single
        species.
 
    get_NEXP_accession_list(fh_sprot, taxon_id, ontType, EXP_default=set([]))
        This method calls build_NEXP_accession_allSpecies when taxon_id is
        an empty string and calls build_NEXP_accession_singleSpecies when
        taxon_id is a valid taxonomic id to obtain the list of accessions
        of the proteins that did not have EXP evidence codes but had
        non-EXP evidence codes in the SwissProt file fh_sprot for
        a specific ontology type ontType.

    build_NEXP_accession_allSpecies(fh_sprot, ontType, EXP_default=set([]))
        This method builds a list of accessions for the proteins in the
        file (with handle fh_sprot) such that those proteins do not have
        EXP evidence codes but do have non-EXP evidence codes. This method
        builds this list for the proteins in a specific ontology.

    build_NEXP_accession_singleSpecies(fh_sprot, taxon_id, ontType, EXP_default=set([]))
       This method is similar to build_NEXP_accession_allSpecies but works 
       for only specific species.
'''
import sys
from collections import defaultdict
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SwissProt as sp

def build_NEXP_accession_allSpecies(fh_sprot, ontType, EXP_default=set([])):
    '''
    This method builds a list of accessions of the proteins whose annotations 
    have non-EXP evidence but no EXP evidence codes in a specific 
    UniProtKB/SwissProt file (file pointer fh_sprot) for some ontology 
    type (ontType). The method returns the list. 
    '''
    # nexp_accessions: Initialize a list to store the accessions of the 
    # proteins that meet the criteria: (1) the protein whose annotation 
    # is supported some Non-EXP evidence code in the specific ontology 
    # ontType, but (2) the annotation is NOT supported by any EXP 
    # evidence code.
    nexp_accessions = []
    print('      Building the accession list with the proteins ' + \
          'that have only non-EXP evidence codes at time t1 ...')
    for rec in sp.parse(fh_sprot):
        # ont_specific_code_exist: this varilable is initialized to False
        # at the beginning of each iteration. If an evidence code (either 
        # EXP or Non-EXP) for the current record is found, this varilable 
        # will be set to True
        ont_specific_code_exist = False
        # exp_code: this variable is initialized to False at the beginning 
        # of each iteration. If an EXP evidence for the current record is 
        # found, this variable will be set to True.
        exp_code = False
        # Going over the list of DB reference entries:
        for crossRef in rec.cross_references:
            # Consider the cross_reference entries
            # that relate to GO DB:
            if crossRef[0] == 'GO':
                goList = [crossRef[1],
                         (crossRef[3].split(':'))[0],
                          crossRef[2][0]]
                if not ont_specific_code_exist and goList[2] == ontType:
                    ont_specific_code_exist = True
                if goList[2] == ontType and \
                    (crossRef[3].split(':'))[0] in EXP_default:
                    exp_code = True
                    break
        # If the protein's annotation is supported by some Non-EXP evidence
        # code but is not supported by any EXP evidence code, append the 
        # protein's accessions list to the nexp_accessions list:
        if ont_specific_code_exist and not exp_code:
            nexp_accessions.append(rec.accessions)
    return nexp_accessions

def build_NEXP_accession_singleSpecies(fh_sprot, taxon_id, ontType, EXP_default=set([])):
    '''
    This method builds a list of accessions of the proteins whose annotations 
    have non-EXP evidence but no EXP evidence codes in a specific 
    UniProtKB/SwissProt file (file pointer fh_sprot) for some ontology 
    type (ontType). The method returns the list. 
    '''
    # nexp_accessions: Initialize a list to store the accessions of the 
    # proteins that meet the criteria: (1) the protein whose annotation 
    # is supported some Non-EXP evidence code in the specific ontology 
    # ontType, but (2) the annotation is NOT supported by any EXP 
    # evidence code.
    nexp_accessions = []
    print('      Building the accession list with the proteins ' + \
          'that have only non-EXP evidence codes at time t1 ...')
    for rec in sp.parse(fh_sprot):
        # Selects records that are related to a specific
        # taxonomy id taxon_id:
        if taxon_id in rec.taxonomy_id:
            # ont_specific_code_exist: this varilable is initialized to False
            # at the beginning of each iteration. If an evidence code (either 
            # EXP or Non-EXP) for the current record is found, this varilable 
            # will be set to True
            ont_specific_code_exist = False
            # exp_code: this variable is initialized to False at the beginning 
            # of each iteration. If an EXP evidence for the current record is 
            # found, this variable will be set to True.
            exp_code = False
            # Going over the list of DB reference entries:
            for crossRef in rec.cross_references:
            # Consider the cross_reference entries
            # that relate to GO DB:
                if crossRef[0] == 'GO':
                    goList = [crossRef[1],
                              (crossRef[3].split(':'))[0],
                              crossRef[2][0]]
                    if not ont_specific_code_exist and goList[2] == ontType:
                        ont_specific_code_exist = True
                    if goList[2] == ontType and \
                        (crossRef[3].split(':'))[0] in EXP_default:
                        exp_code = True
                        break
            # If the protein's annotation is supported by some Non-EXP evidence
            # code but is not supported by any EXP evidence code, append the 
            # protein's accessions list to the nexp_accessions list:
            if ont_specific_code_exist and not exp_code:
                nexp_accessions.append(rec.accessions)
    return nexp_accessions

def get_NEXP_accession_list(fh_sprot, taxon_id, ontType, EXP_default=set([])):
    # Initialize a list to store the accessions of the proteins 
    # that meet certain criteria: 
    if not taxon_id: # if taxon_id is empty, invoke the method for all species
        nexp_accessions = build_NEXP_accession_allSpecies(fh_sprot,
                                                          ontType, 
                                                          EXP_default)
    else: # if taxon_id is supplied, invoke the method for single species 
        nexp_accessions = build_NEXP_accession_singleSpecies(fh_sprot,
                                                             taxon_id,
                                                             ontType, 
                                                             EXP_default)
    return nexp_accessions

def is_accession_found(accession_t2, nexp_accessions_t1):
    '''
    This method checks whether any accession represented by the first 
    list accession_t2 is found in any of the lists in the second list 
    nexp_accessions_t1. 
    If accession (first argument) is found in the accession list 
    (second argument), then the function returns True
    else it returns False
    '''
    for l in nexp_accessions_t1:
        if (set(accession_t2) & set(l)): 
            return True
    return False

def filter_testSet_allSpecies(fh_sprot_t1, fh_sprot_t2, fh_test_seq, 
                              fh_map, ontType, EXP_default=set([])):
    '''
    This method filters the protein sequences from a SwissProt file
    at time point t2 such that the annotations of those proteins
    did not have experimental evidence codes at time t1 but obtained
    experimental evidence codes at time t2. The SwissProt files at time
    points t1 and t2 are represented by the file pointers fh_sprot_t1
    and fh_sprot_t2, respectively.
    This method is repeatedly invoked by create_testSet_allSpecies to create
    test sequences for different ontologies.
    '''
    # Initializes the target_id:
    target_id = int("1"+"0000001")
    outseq_list = []
    # nexp_accessions_t1: Obtain the list of accessions of the proteins 
    # whose annotations were supproted by non-EXP evidence codes but not 
    # by any EXP evidence codes at time t1. In fact, nexp_accessions_t1 
    # is a list of lists.
    nexp_accessions_t1 = get_NEXP_accession_list(fh_sprot_t1, '',
                                                   ontType, EXP_default)
    print('      Number of entries in the accession list: ' + \
                 str(len(nexp_accessions_t1)))
    print('      Writing the sequences of the proteins whose annotations ' + \
          'gained EXP evidence at time t2 to the ouput file ...')
    for rec in sp.parse(fh_sprot_t2):
        # Selects records that are related to a specific
        # taxonomy id taxon_id:
        # print(is_accession_found(nexp_accessions_t1[0], nexp_accessions_t1))
        # if taxon_id in rec.taxonomy_id:

        # if the protein's annotation was supported by non-EXP evidence code 
        # but not by any EXP evidence code at t1, check whether it gained EXP 
        # evidece code at t2 for the same ontology ontType:
        if (is_accession_found(rec.accessions, nexp_accessions_t1)):
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
            if exp_code:
                #goTerms = ','.join(list(goTerms))
                outseq = SeqRecord(Seq(rec.sequence),
                                   id="T"+str(target_id),
                                   description = "%s" %
                                   (rec.accessions[0]))
                outseq_list = [outseq]
                # Write out the sequence to fasta file:
                SeqIO.write(outseq_list,fh_test_seq, "fasta")

                # Write out the mapping to the map file:
                # (protein sequence id, protein name, GO term(s))
                for gt in goTerms:
                    #mapStr = "T" + str(target_id) + '\t' + \
                    #               str(rec.accessions[0]) + '\n'
                    #mapStr = "T" + str(target_id) + '\t' + \
                    #           str(gt) + '\n'
                    mapStr = "T" + str(target_id) + '\t' + \
                                   str(rec.accessions[0]) + '\t' + \
                                   str(gt) + '\n'
                    fh_map.write("%s" % mapStr)
                target_id += 1
    return None


def __collect_prevES(fh_mapFile): 

    GOterm_dict = defaultdict(set)
    for line in fh_mapFile:
        #print(line)
        fields = line.strip().split('\t')
        #print(fields)
        k=fields[0] + ':' + fields[1]
        GOterm_dict[k].add(fields[2])
        #print(k)
        #print(GOterm_dict[k])
    return GOterm_dict
    
def __print_preES_dict(GOterm_dict): 
    for k in sorted(GOterm_dict.keys()): 
        print('>' + k + '\t', ','.join(str(t) for t in GOterm_dict[k]))
        #print('>' + k)
    return None

def create_reevalSet_allSpecies(fh_mapFile_t1, fh_sprot_t2,
                              reevalSet_handle, 
                              reevalSet_map_fname_handle,
                              ontType,
                              EXP_default=set([])):
    
    print('MFO ontology:')
    prevES_dict = __collect_prevES(fh_mapFile_t1)
    #__print_preES_dict(prevES_dict) 
 



    sys.exit(0)
    filter_testSet_allSpecies(fh_sprot_t1, fh_sprot_t2,
                                  testSet_LK_mfo_handle,
                                  testSet_LK_mfo_map_handle,
                                  'F', EXP_default)
    testSet_LK_mfo_handle.flush()
    testSet_LK_mfo_map_handle.flush()
    print('BPO ontology:')
    # Reposition the file pointer to the beginning:
    fh_sprot_t1.seek(0)
    fh_sprot_t2.seek(0)
    filter_testSet_allSpecies(fh_sprot_t1, fh_sprot_t2,
                       testSet_LK_bpo_handle,
                       testSet_LK_bpo_map_handle,
                       'P', EXP_default)
    testSet_LK_bpo_handle.flush()
    testSet_LK_bpo_map_handle.flush()
    print('CCO ontology:')
    # Reposition the file pointer to the beginning:
    fh_sprot_t1.seek(0)
    fh_sprot_t2.seek(0)
    filter_testSet_allSpecies(fh_sprot_t1, fh_sprot_t2,
                       testSet_LK_cco_handle,
                       testSet_LK_cco_map_handle,
                       'C', EXP_default)
    testSet_LK_cco_handle.flush()
    testSet_LK_cco_map_handle.flush()
    return None

def create_testSet_allSpecies_old(fh_sprot_t1, fh_sprot_t2,
                              testSet_LK_mfo_handle, 
                              testSet_LK_mfo_map_handle,
                              testSet_LK_bpo_handle,
                              testSet_LK_bpo_map_handle,
                              testSet_LK_cco_handle,
                              testSet_LK_cco_map_handle,
                              EXP_default=set([])):
    print('MFO ontology:')
    filter_testSet_allSpecies(fh_sprot_t1, fh_sprot_t2,
                                  testSet_LK_mfo_handle,
                                  testSet_LK_mfo_map_handle,
                                  'F', EXP_default)
    testSet_LK_mfo_handle.flush()
    testSet_LK_mfo_map_handle.flush()
    print('BPO ontology:')
    # Reposition the file pointer to the beginning:
    fh_sprot_t1.seek(0)
    fh_sprot_t2.seek(0)
    filter_testSet_allSpecies(fh_sprot_t1, fh_sprot_t2,
                       testSet_LK_bpo_handle,
                       testSet_LK_bpo_map_handle,
                       'P', EXP_default)
    testSet_LK_bpo_handle.flush()
    testSet_LK_bpo_map_handle.flush()
    print('CCO ontology:')
    # Reposition the file pointer to the beginning:
    fh_sprot_t1.seek(0)
    fh_sprot_t2.seek(0)
    filter_testSet_allSpecies(fh_sprot_t1, fh_sprot_t2,
                       testSet_LK_cco_handle,
                       testSet_LK_cco_map_handle,
                       'C', EXP_default)
    testSet_LK_cco_handle.flush()
    testSet_LK_cco_map_handle.flush()
    return None

def filter_testSet_singleSpecies(fh_sprot_t1, fh_sprot_t2, taxon_id, fh_test_seq, 
                                 fh_map, ontType, EXP_default=set([])):
    '''
    This method filters the protein sequences from a SwissProt file
    at time point t2 such that the annotations of those proteins
    did not have EXP evidence codes at time t1 but obtained
    experimental evidence codes at time t2. The SwissProt files at time
    points t1 and t2 are represented by the file pointers fh_sprot_t1
    and fh_sprot_t2, respectively.
    This method is repeatedly invoked by create_testSet_singleSpecies to create
    test sequences for different ontologies.
    '''
    # Initializes the target_id:
    target_id = int(taxon_id+"0000001")
    outseq_list = []
    # nexp_accessions_t1: Obtain the list of accessions of the proteins 
    # whose annotations were supproted by non-EXP evidence codes but not 
    # by any EXP evidence codes at time t1. In fact, nexp_accessions_t1 
    # is a list of lists.
    nexp_accessions_t1 = get_NEXP_accession_list(fh_sprot_t1, taxon_id,
                                                   ontType, EXP_default)
    print('      Number of entries in the accession list: ' + \
                 str(len(nexp_accessions_t1)))
    print('      Writing the sequences of the proteins whose annotations ' + \
          'gained EXP evidence at time t2 to the ouput file ...')

    for rec in sp.parse(fh_sprot_t2):
        # Selects records that are related to a specific
        # taxonomy id taxon_id:
        # print(is_accession_found(nexp_accessions_t1[0], nexp_accessions_t1))
        # if taxon_id in rec.taxonomy_id:

        # if the protein's annotation was supported by non-EXP evidence code 
        # but not by any EXP evidence code at t1, check whether it gained EXP 
        # evidece code at t2 for the same ontology ontType:
        if (taxon_id in rec.taxonomy_id and \
            is_accession_found(rec.accessions, nexp_accessions_t1)):
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
            if exp_code:
                #goTerms = ','.join(list(goTerms))
                outseq = SeqRecord(Seq(rec.sequence),
                                   id="T"+str(target_id),
                                   description = "%s" %
                                   (rec.accessions[0]))
                outseq_list = [outseq]
                # Write out the sequence to fasta file:
                SeqIO.write(outseq_list,fh_test_seq, "fasta")
                # Write the mapping to the map file
                # (protein sequence id, protein name, GO term(s))
                for gt in goTerms:
                    #mapStr = "T" + str(target_id) + '\t' + \
                    #               str(rec.accessions[0]) + '\n'
                    #mapStr = "T" + str(target_id) + '\t' + \
                    #           str(gt) + '\n'
                    mapStr = "T" + str(target_id) + '\t' + \
                                   str(rec.accessions[0]) + '\t' + \
                                   str(gt) + '\n'
                    fh_map.write("%s" % mapStr)
                target_id += 1
    return None

def create_testSet_singleSpecies(fh_sprot_t1, fh_sprot_t2, taxon_id,
                                 testSet_LK_mfo_handle, 
                                 testSet_LK_mfo_map_handle,
                                 testSet_LK_bpo_handle,
                                 testSet_LK_bpo_map_handle,
                                 testSet_LK_cco_handle,
                                 testSet_LK_cco_map_handle,
                                 EXP_default=set([])):
    '''
    This method calls other methods to filter protein sequences that 
    are experimentally annotated. It calls three different methods - 
    one separate method for each ontological category.
    '''
    print('MFO ontology:')
    filter_testSet_singleSpecies(fh_sprot_t1, fh_sprot_t2, taxon_id,
                                  testSet_LK_mfo_handle,
                                  testSet_LK_mfo_map_handle,
                                  'F', EXP_default)
    testSet_LK_mfo_handle.flush()
    testSet_LK_mfo_map_handle.flush()
    # Reposition the file pointer to the beginning:
    fh_sprot_t1.seek(0)
    fh_sprot_t2.seek(0)
    print('BPO ontology:')
    filter_testSet_singleSpecies(fh_sprot_t1, fh_sprot_t2, taxon_id,
                                  testSet_LK_bpo_handle,
                                  testSet_LK_bpo_map_handle,
                                  'P', EXP_default)
    testSet_LK_bpo_handle.flush()
    testSet_LK_bpo_map_handle.flush()
    # Reposition the file pointer to the beginning:
    fh_sprot_t1.seek(0)
    fh_sprot_t2.seek(0)
    print('CCO ontology:')
    filter_testSet_singleSpecies(fh_sprot_t1, fh_sprot_t2, taxon_id,
                                  testSet_LK_cco_handle,
                                  testSet_LK_cco_map_handle,
                                  'C', EXP_default)
    testSet_LK_cco_handle.flush()
    testSet_LK_cco_map_handle.flush()
if __name__ == '__main__':
    print (sys.argv[0] + ':')
    print(__doc__)
    sys.exit(0)
