#!/usr/bin/env python

'''
    The entry point of this module is parse_args() method which calls
    other methods to collect user supplied arguments, parses and
    verifies them. Description of these methods are the following:
   
    collect_args: This method collects the user supplied arguments and 
        returns them as an aprgparse ArgumentParser object. 

    extract_args: This method puts the user supplied arguments into an 
        ordered dictionary and returns it at the end.

    check_args: This method verifies the correctness of the user supplied
        arguments and puts them into an ordered dictionary which it returns
        at the end. 

    parse_args: This method calls the above methods and returns the final 
        dictionary of the user supplied arguments to the calling point.
'''

import os
import sys
import argparse
import re
from collections import OrderedDict

def collect_args():
    """ 
    This method collects the user supplied arguments and returns them 
    at the end.
    """
    parser = argparse.ArgumentParser(description='Generate prediction scores ' + \
        'according to BLAST model.')
    parser.add_argument('-I1', '--input1', help=' Specifies path to the ' + \
        'target protein id file. This opton is mandatory.')
    parser.add_argument('-I2', '--input2', help=' Specifies path to the ' + \
        'map fiel between training protein ids and GO terms. ' + \
        'This opton is mandatory.')
    parser.add_argument('-I3', '--input3', help=' Specifies path to the ' + \
        'blast results file. This opton is mandatory.')
    parser.add_argument('-O', '--output', default='', help='Provides user ' + \
        'an option to specify an output filename prefix. When not ' + \
        'specified, the program will create an output file name.')
    return parser

def extract_args(args):
    """
     This method builds a dictionary from the user supplied arguments
     and returns the constructed dictionary at the end.
    """
    args_dict = OrderedDict() 
    args_dict['target_fname'] = args.input1
    args_dict['GOterm_fname'] = args.input2
    args_dict['blast_result'] = args.input3
    args_dict['outfile'] = args.output
    return args_dict
    
def check_args(args_dict,parser):
    """
    This method checks the user arguments for consistency. It builds a new 
    dictionary from these arguments and finally returns this newly created 
    dictionary. 
    """
    user_dict = OrderedDict() 
    for arg in args_dict:
        if arg == 'target_fname':
            if args_dict[arg] == None:
                print ('Missing target protein id list file\n')
                print (parser.parse_args(['--help']))
            else:
                user_dict['target_fname'] = args_dict[arg]
        elif arg == 'GOterm_fname':
            if args_dict[arg] == None:
                print ('Missing training protein id and GO term map file\n')
                print (parser.parse_args(['--help']))
            else:
                user_dict['GOterm_fname'] = args_dict[arg]
        elif arg == 'blast_result':
            if args_dict[arg] == None:
                print ('Missing blast result file\n')
                print (parser.parse_args(['--help']))
            else:
                user_dict['blast_result'] = args_dict[arg]
        elif arg == 'outfile':
            user_dict[arg] = args_dict[arg]
    return user_dict

def parse_args():
    """ 
    This is the entry point for the other methods in this module. It
      1. invokes collect_args to collect the user arguments.
      2. invokes extract_args to put those arguments into an 
         ordered dictionary. 
      3. checks the consistency of those arguments by invoking 
         check_args which returns an ordered dictionary of correct 
         arguments.
      4. returns the dictionary at the end.
    """

    # Collect user arguments:
    parser = collect_args() 
    args_dict = {}
    args, unknown = parser.parse_known_args()
    if len(unknown) > 0:
        print ('\n*********************************')
        print ("Invalid Arguments")
        print ('*********************************\n')
        print (parser.parse_args(['--help']))
    # Places the user arguments into a dictionary:
    args_dict = extract_args(args) 
    # Checks the consistency of the user args:
    user_dict = check_args(args_dict,parser) 
    return user_dict

if __name__ == '__main__':
    print (sys.argv[0] + ':')
    print (__doc__)
    sys.exit(0)
