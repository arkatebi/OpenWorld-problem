## Species growth in UniProtKB/SwissProt database over time 

#### Some informative sites 

#### UniProtKB/SwissProt
This is a non-redundant protein sequence database. Each entry in this database
is manually annotated involving detailed analysis of the protein sequence and
of the scientific literature. The database is recognized as the central access
point of the extensive curated protein information, classification, and
cross-reference.

* UniProtKB/SwissProt dataset current release:
  ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/
* UniProtKB/SwissProt dataset archive (release 46 and greater):
  ftp://ftp.uniprot.org/pub/databases/uniprot/previous_releases/
* UniProtKB/SwissProt dataset archive (release 9 to 45):
  ftp://ftp.ebi.ac.uk/pub/databases/swissprot/sw_old_releases/
* Detailed release statistics:
  http://web.expasy.org/docs/relnotes/relstat.html
* UniProtKB/SwissProt file format:
  http://arep.med.harvard.edu/labgc/jong/Fetch/SwissProtAll.html

### Requirements
* Python 2.7 
* Biopython 1.66 or greater 

### Software Usage 

The details of the usage description of the CAFA Toolset are as follows. 

### Statistics Generation 
This tool will create a file for the target set, containing the protein
sequences in the fasta file format. The simplest way to run the program 
for target generation:

python Filter_genes  --input1 UniProtKB/SwissProt-annotation-at-t0 -G taxon_id

input1 is a UniProtKB/SwissProt annotation file at a certain time point (on
CAFA time-line, this is time t0, the sequence release date for the CAFA 
community challenge), taxon_id is the taxonomy id for the specific species
whose protein sequences are being filtered. Here is an example with
uniprot_sprot.dat.38 as the UniProtKB/SwissProt annotation file and
559292 as taxon id for Saccharomyces cerevisiae.

```
python Count_genes -I1=uniprot_sprot.dat.2014_09 -G=559292
```

It will create the following two output files - one for the target sequences
and one for the target id and protein name mapping used in the target sequence
output file:

uniprot_sprot.dat.2014_09.559292.tfa.1

uniprot_sprot.dat.2014_09.559292.tfa.1.map

* The target sequence output file name is created by adding an extension with
the name of the input file where the extension is formed in the following way:
[taxon id].[tfa].[version #].

* The map file name is created by adding '.map' at the end of the target sequence
output file name: [taxon id].[tfa].[version #].map

* Multiple run of this program with the same input file will create
subsequent versions of the output file where the file name will end with
subsequent version number, such as 2, 3, 4, etc.

The program can also take an output file name as a command line argument:

python Count_genes --input1 UniProtKB/SwissProt-annotation-at-t0 -G taxon_id -output output_filename

### Source Code
This is an open source project and the source code is publicly available on 
GitHub through the following URL: https://github.com/arkatebi/CAFA-Toolset.
For questions, please email either of us: Iddo Friedberg (idoerg@gmail.com),  
Ataur Katebi (arkatebi@gmail.com).

### References
[1] Radivojac P, Clark WT, Oron TR, et al. (2013). A large-scale evaluation of 
computational protein function prediction, Nature Methods 10(3), pp 221-227, 
PMID 23353650.
