#!/usr/bin/env python
'''
    This module has the definition of Download class which has 
    the following methods to download a set of files. 

    __init__: 
        This method intializes the necessary variables. 
     
    download_testDataset:       
        This method takes a file handle to a file name containing 
        the list of UniProtKB/SwissProt data file names.
        The method iterates over the entries in this file. 
        For each entry, it checks whether the file is already in 
        the workspace. if it does not find the file in the workspace, 
        it downlaods the file by invoking download method. 

    download: 
        Takes two input parameters: url and fname
        url: it is the URL to the file name to be downloaded. 
        fname: it is the file name that to be downloaded. 
'''
import os
import sys
from os.path import basename 
import urllib2
import Config
import ConfigParser as cp

# Default configuration file name:
config_filename = '.config' 

class Download:
    def __init__(self, work_dir, sprot_filename):
        self.ConfigParam = Config.read_config(config_filename)
        self.work_dir = (self.ConfigParam['workdir'].rstrip('/'))
#        self.work_dir = work_dir 

        self.testData_filename = sprot_filename 

        self.goa_arc = 'ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/old'
        self.sprot_arc_base = 'ftp://ftp.uniprot.org/pub/databases/uniprot/previous_releases'

        if not os.path.exists(self.work_dir):
            os.makedirs(self.work_dir)
                # Create work direcoty, if it does not exist

    def download_testDataset(self, testDataset_fh):
        '''
        This method iterates through the list of the testdata file names. 
        If it does not find any of the testdata files in workspace, it 
        downloads the data file from the UniProtKB/SwissProt archive.
        '''
        for line in testDataset_fh:
            testdata_fname = line.strip().lower()
            release_name = 'release-' + testdata_fname.split('.dat.')[1]
            folder_name = release_name + '/' + \
                          'knowledgebase'
            url = self.sprot_arc_base + '/' + folder_name
            download_fname = testdata_fname.split('.dat.')[0] + '-only' + \
                             testdata_fname.split('.dat.')[1] + '.tar.gz'
            tar_fname = download_fname.rstrip('.gz')
            zip_fname = 'uniprot_sprot.dat.gz'
            if (os.path.isfile(self.work_dir + '/' + testdata_fname)):
                pass
            elif (os.path.isfile(self.work_dir + '/' + tar_fname)):
                os.system('tar -xC ' + self.work_dir + ' -f ' + \
                          self.work_dir + '/' + tar_fname + \
                          ' ' + zip_fname)
                os.system('gzip -d ' + self.work_dir + '/' + zip_fname)
                os.system('mv ' +  self.work_dir + '/' + \
                          zip_fname.rstrip('.gz') + ' ' + \
                          self.work_dir + '/' + testdata_fname)
                #os.system('rm ' + self.work_dir + '/' + tar_fname)
            elif (os.path.isfile(self.work_dir + '/' + download_fname)):
                os.system('gzip -d ' + self.work_dir + '/' + download_fname)
                os.system('tar -xC ' + self.work_dir + ' -f ' + \
                          self.work_dir + '/' + tar_fname + \
                          ' ' + zip_fname)
                os.system('gzip -d ' + self.work_dir + '/' + zip_fname)
                os.system('mv ' +  self.work_dir + '/' + \
                          zip_fname.rstrip('.gz') + ' ' + \
                          self.work_dir + '/' + testdata_fname)
                #os.system('rm ' + self.work_dir + '/' + tar_fname)
            else:
                print('Downloading ' + download_fname + ' ...')
                if (not self.download(url, download_fname)): 
                    print('Downloading failed for ' + download_fname)
                    continue
                os.system('gzip -d ' + self.work_dir + '/' + download_fname)
                os.system('tar -xC ' + self.work_dir + ' -f ' + \
                          self.work_dir + '/' + tar_fname + \
                          ' ' + zip_fname)
                os.system('tar -xC ' + self.work_dir + ' -f ' + \
                          self.work_dir + '/' + tar_fname + \
                          ' ' + zip_fname)
                os.system('gzip -d ' + self.work_dir + '/' + zip_fname)
                os.system('mv ' +  self.work_dir + '/' + \
                          zip_fname.rstrip('.gz') + ' ' + \
                          self.work_dir + '/' + testdata_fname)
                os.system('rm ' + self.work_dir + '/' + tar_fname)
            #break
        return True 

    def download(self, url, fname):
        try:
            response = urllib2.urlopen(url + '/' + fname)
        except urllib2.HTTPError, err:
            return False
        except urllib2.URLError, err:
            return False
        out_fh = open(self.work_dir + '/' + fname, 'w')
        out_fh.write(response.read())
        out_fh.close()
        return True

if __name__ == '__main__':
    print (sys.argv[0] + ' :')
    print(__doc__)
    sys.exit(0)
