## Gene Annotations with Exp evidences in UniProtKB/SwissProt 
* Creates a table of gene counts for a set of species in UniProtKB/SwissProt 
  whose annotations have experimental evidence codes. 
* Creates graphs of the gene counts for all speceis over a set of time points.

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

#### Generate Counts of Annotated Genes with EXP Evidence

This program will create a file with the number of genes whose annotations
are experimentally validated for a set of organism over a series of time
points. The simplest way to run the program:

python Count_genes --input1 filename_listing_species_taxon_ids --input2 filename_listing_sprot_filenames 

input1 is a TWO column text file containing the list of species: the first
column has the taxon id and the second column has the organism name. input2
is a list of UniprotKB/SwissProt filenames over a series of time points.

```
python Count_genes -I1=sp_list.txt -I2=sprot_files.txt
```

It creates an output file: sprot_genes.stat.1
The output file has one row for each SwissProt file listed in
sprot_files.txt. Each row has THREE columns for each organism,
according to the organisms listed in sp_list.txt file.

#### Generate Graphs for the Gene Counts 

This program will create a graph for the gene count of each organism 
that is found in the above step. The simplest way to run the program:

python Count_genes --input1 filename_listing_species_taxon_ids --input2 filename_listing_sprot_filenames --input3 filename_gene_counts 

input1 is a TWO column text file containing the list of species: the first
column has the taxon id and the second column has the organism name. input2
is a list of UniprotKB/SwissProt filenames over a series of time points. 
input3 is the gene count file generated in the previous step.  

One specific example run with input1 file sp_list.txt, input2 file 
sprot_files.txt, and input3 file sprot_genes.stat.1:

```
python plot_geneCounts -I1=sp_list.txt -I2=sprot_files.txt -I3=sprot_genes.stat.1
```

This command takes the species list from sp_list.txt file, the time points from
the filenames listed in the sprot_files.txt file, and gene counts from the 
sprot_genes.stat.1 file and draw a graph of gene count for each speceis over 
those time points extracted sprot_files.txt. For this specific example, it 
generates the following figure files (one figure for each speceis):

geneFreq.9606.1.png
geneFreq.10090.1.png
geneFreq.3702.1.png
geneFreq.10116.1.png
geneFreq.559292.1.png
geneFreq.9913.1.png
geneFreq.284812.1.png
geneFreq.44689.1.png

Repeated run of the program creates subsequent version of the figure file for
each speceis. 

The following section shows the figures produced by running this program. 

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

