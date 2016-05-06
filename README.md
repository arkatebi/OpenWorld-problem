## Gene Annotations with Exp Evidences in UniProtKB/SwissProt 
* Creates a table of gene counts for a set of species in UniProtKB/SwissProt 
  whose annotations have experimental evidence codes. 
* Creates graphs of the gene counts for those speceis over a series of time 
  points.

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

#### Experimental Evidence Codes 

* Guide to GO evidence codes: 
  http://geneontology.org/page/guide-go-evidence-codes
* Evidence code decision tree: 
  http://geneontology.org/page/evidence-code-decision-tree  

### Requirements
* Python 2.7 
* Biopython 1.66 or greater 

### Software Usage 

The details of the usage description of this software are as follows.

#### Generate Counts of Genes Annotated with Exp Evidence Codes

This program will create a file with the number of genes whose annotations
have experimental evidence codes in the UniProtKB/SwissProt files for a set 
of organismis over a series of time points. The simplest way to run the 
program:

```
python Count_genes --input1 filename_listing_species_taxon_ids --input2 filename_listing_sprot_filenames 
```

input1 is a TWO column text file containing the list of species to be 
considered: the first column has the taxon id and the second column has 
the organism name. input2 is a file containing the UniprotKB/SwissProt 
filenames over a series of time points. The file file format is one filename
in each line. Blank lines are allowed. 

One specific example run with input1 file sp_list.txt and input2 file 
sprot_files.txt:  

```
python Count_genes -I1=sp_list.txt -I2=sprot_files.txt
```

This command will extract the species names from the sp_list.txt file
and the UniprotKB/SwissProt file names from the sprot_files.txt file,
and then will calculate the gene counts for all species over the 
UniProtKB/SwissProt files found in the sprot_files.txt file. If the 
UniProtKB/SwissProt files are not found in the current directory or the 
workspace, the program will automatically download these files. 
 
Successful run of this program will create an output file: sprot_genes.stat.1
This output has two header lines: first line has the taxonomy id and 
the second line has BPO, CCO, and MFO names for each taxonomy id. 
Subsequent lines are for gene counts: one row for each timepoint, 
containing gene counts for each organism, in the same seqeuence as 
they are found in the sp_list.txt file. For each organism, the file 
has THREE columns, for gene counts in BPO, CCO, and MFO ontological 
categories.

Repeated run of the program, will create subsequent version of the 
output file. 

The program can also take an optional output filename prefix as an 
additional argument which is shown below: 

```
python Count_genes -I1=sp_list.txt -I2=sprot_files.txt -O=sprot_genes.stat
```
It will behave the same way as described above. 

#### Generate Graphs for the Gene Counts 

This program will create a graph for the gene count of each organism 
that is found in the above step. One can run the program as follows:

```
python Count_genes --input1 filename_listing_species_taxon_ids --input2 filename_listing_sprot_filenames --input3 filename_gene_counts 
```

input1 is a TWO column text file containing the list of species: the first
column has the taxon id and the second column has the organism name. input2
is a list of UniprotKB/SwissProt filenames over a series of time points. 
input3 is the gene count file generated in the previous step.  

One specific example run with input1 file sp_list.txt, input2 file 
sprot_files.txt, and input3 file sprot_genes.stat.1:

```
python Plot_geneCounts -I1=sp_list.txt -I2=sprot_files.txt -I3=sprot_genes.stat.1
```

This command takes the species list from sp_list.txt file, the time points from
the filenames listed in the sprot_files.txt file, and gene counts from the 
sprot_genes.stat.1 file and draw a graph of gene count for each speceis over 
those time points extracted from sprot_files.txt. For this specific example, it 
generates the following figure files (one figure for each speceis):
```
geneFreq.9606.1.png
geneFreq.10090.1.png
geneFreq.3702.1.png
geneFreq.10116.1.png
geneFreq.559292.1.png
geneFreq.9913.1.png
geneFreq.83333.1.png
geneFreq.284812.1.png
geneFreq.44689.1.png
```
Repeated run of the program creates the subsequent versions of each figure file. 

The following section shows the figures produced by running this program with
the above input files.

#### Graphical View of Gene Counts 

####  Homo sapiens (taxon id 9606) 
![Alt Gene Frequencey of Human] (/figures/geneFreq.9606.1.png?raw=true “Gene Frequency of Human”)

####  Mus musculus (taxon id 10090) 
![Alt Gene Frequency of Mouse] (/figures/geneFreq.10090.1.png?raw=true “Gene Frequency of Mouse”)

####  Arabidopsis thaliana (taxon id 3702) 
![Alt Gene Frequency of Arabidopsis] (/figures/geneFreq.3702.1.png?raw=true “Gene Frequency of Arabidopsis”)


####  Rattus norvegicus (taxon id 10116) 
![Alt Gene Frequency of Rat] (/figures/geneFreq.10116.1.png?raw=true “Gene Frequency of Rat”)

####  Saccharomyces cerevisiae (taxon id 559292) 
![Alt Gene Frequency of Baker's yeast] (/figures/geneFreq.559292.1.png?raw=true “Gene Frequency of Baker's yeast”)

####  Bos taurus (taxon id 9913) 
![Alt Gene Frequency of Bovine] (/figures/geneFreq.9913.1.png?raw=true “Gene Frequency of Bovine”)

####  Schizosaccharomyces pombe (taxon id 284812) 
![Alt Gene Frequency of Fission yeast] (/figures/geneFreq.284812.1.png?raw=true “Gene Frequency of Fission yeast”)

####  Echerichia coli (taxon id 83333) 
![Alt Gene Frequency of E. coli] (/figures/geneFreq.83333.1.png?raw=true “Gene Frequency of E. coli”)

####  Bacillus subtilis (taxon id 224308) 
![Alt Gene Frequency of B. subtilis] (/figures/geneFreq.224308.1.png?raw=true “Gene Frequency of B. subtilis”)

####  Dictyostelium discoideum (taxon id 44689) 
![Alt Gene Frequency of Slime mold] (/figures/geneFreq.44689.1.png?raw=true “Gene Frequency of Slime mold”)

### Source Code
This is an open source project and the source code is publicly available on 
GitHub through the following URL: https://github.com/arkatebi/CAFA-Toolset.
For questions, please email either of us: Iddo Friedberg (idoerg@gmail.com),  
Ataur Katebi (arkatebi@gmail.com).

