<a name="title" />
## Obtaining datasets for assessment of predictive models

### Contents

1\. [Training and Evaluation Sets] (#genSets)

1.1\. [Training Set] (#genTrainingSet)

1.2\. [Evaluation Set 1] (#genEvalSet-1)

1.3\. [Evaluation Set 2] (#genEvalSet-2)

1.4\. [Evaluation Set 3] (#genEvalSet-3)

<a name="genSets" />
### Training and Evaluation Sets 

![alt Experiment Design] (/figures/experiment-design-1.3.png?raw=true “Experiment Design”)


The details of how to collect the training and evaluation data sets
are as follows.

<a name="genTrainingSet" />
#### Training Set (TS)

This program will extract the sequences of the proteins that have 
experimental evidence codes in a UniProt/SwissProt file at some 
time point. For TS, January 2010 is the time point.  

```
python xTract_trainingSet -I1=uniprot_sprot.dat.2010_01

```
The input file uniprot_sprot.dat.2010_01 is the UniProt/SwissProt file 
where the sequences are extracted from. The program generates the
following six output files - two files for each ontological category:

```
uniprot_sprot.dat.2010_01.tfa_LK_mfo.1
uniprot_sprot.dat.2010_01.tfa_LK_mfo.1.map
uniprot_sprot.dat.2010_01.tfa_LK_bpo.1
uniprot_sprot.dat.2010_01.tfa_LK_bpo.1.map
uniprot_sprot.dat.2010_01.tfa_LK_cco.1
uniprot_sprot.dat.2010_01.tfa_LK_cco.1.map
```

The first ouput file has the extracted training sequences in the FASTA 
file format for MFO ontology. The id for each sequence is constructed from 
a program generated string and the SwissProt name of the protein. The 
second output file records the mapping between the program generated string 
and the SwissProt protein name, corresponding to the entries in the first 
file. Subsequent files are for BPO and CCO ontological categories.

The program can also be used to extract training sequences for a specific 
organism:

```
python xTract_trainingSet -I1=uniprot_sprot.dat.2010_01 -G=9606
```

This will generate the following output files:

```
uniprot_sprot.dat.2010_01.9606.tfa_LK_mfo.1
uniprot_sprot.dat.2010_01.9606.tfa_LK_mfo.1.map
uniprot_sprot.dat.2010_01.9606.tfa_LK_bpo.1
uniprot_sprot.dat.2010_01.9606.tfa_LK_bpo.1.map
uniprot_sprot.dat.2010_01.9606.tfa_LK_cco.1
uniprot_sprot.dat.2010_01.9606.tfa_LK_cco.1.map
```

This program can also take an optional output file name: 

```
python xTract_trainingSet -I1=uniprot_sprot.dat.2010_01 -G=9606 -O=trainingSet
```

This will create the following output files:

```
trainingSet.9606.tfa_LK_mfo.1
trainingSet.9606.tfa_LK_mfo.1.map
trainingSet.9606.tfa_LK_bpo.1
trainingSet.9606.tfa_LK_bpo.1.map
trainingSet.9606.tfa_LK_cco.1
trainingSet.9606.tfa_LK_cco.1.map
```

Repeated run of the program will create the subsequent versions of each 
output file.

<a name="genEvalSet-1" />
#### Evaluation Set 1 (ES-1)

This program will extract the sequences of the proteins whose annotations
did not have experimental evidence codes in UniProt/SwissProt database at time
t1 but gained experimental evidence codes at time t2. For ES-1, t1 is set as 
January 2010 and t2 is set as January 2011.

```
python xTract_testSet -I1=uniprot_sprot.dat.2010_01 -I2=uniprot_sprot.dat.2011_01

```
The first input file uniprot_sprot.dat.2010_01 is the UniProt/SwissProt 
annotation file at t1 and the second input file uniprot_sprot.dat.2011_01 is the 
UniProt/SwissProt annotation file at t2. The name of a SwissProt file should have 
the following format: a file name prefix followed by the exact string .dat. 
followed by the time stamp (in yyyy_mm format). The program generates the 
following six output files - two files in each ontological category:

```
uniprot_sprot.dat.2010_01-2011_01.mfo.1
uniprot_sprot.dat.2010_01-2011_01.mfo.1.map
uniprot_sprot.dat.2010_01-2011_01.bpo.1
uniprot_sprot.dat.2010_01-2011_01.bpo.1.map
uniprot_sprot.dat.2010_01-2011_01.cco.1
uniprot_sprot.dat.2010_01-2011_01.cco.1.map
```

The first ouput file has the extracted test sequences in the FASTA 
file format for MFO ontology. The id for each sequence is constructed from 
a program generated string and the SwissProt name of the protein. The 
second output file records the mapping between the program generated string 
and the SwissProt protein name, corresponding to the entries in the first file.
The subsequent two pairs of files are for BPO and CCO ontological categories, 
respectively.

The program can also be used to extract sequences for a specific organism:

```
python xTract_testSet -I1=uniprot_sprot.dat.2010_01 -I2=uniprot_sprot.dat.2011_01 -O=evalSet-1
```

This will generate the following output files:

```
evalSet-1.mfo.1
evalSet-1.mfo.1.map
evalSet-1.bpo.1
evalSet-1.bpo.1.map
evalSet-1.cco.1
evalSet-1.cco.1.map
```

This program can also take an optional output file name: 

```
python xTract_testSet -I1=uniprot_sprot.dat.2010_01 -I2=uniprot_sprot.dat.2011_01 -G=9606 -O=evalSet-1
```

This will create the following output files:

```
evalSet-1.9606.mfo.1
evalSet-1.9606.mfo.1.map
evalSet-1.9606.bpo.1
evalSet-1.9606.bpo.1.map
evalSet-1.9606.cco.1
evalSet-1.9606.cco.1.map
```

Repeated run of the program will create the subsequent versions of each 
output file.

<a name="genEvalSet-2" />
#### Evaluation Set 2 (ES-2)

This program will extract the sequences of the proteins whose annotations
gained annotations that have experimental evidence codes in UniProt/SwissProt 
database at time t2. For ES-2, t1 is set as January 2011 and t2 is set as 
January 2012.

```
python xTract_reevalSet -I1=evalSet-1.mfo.1.map -I2=uniprot_sprot.dat.2012_01 -N=F -O=evalSet-2
python xTract_reevalSet -I1=evalSet-1.bpo.1.map -I2=uniprot_sprot.dat.2012_01 -N=P -O=evalSet-2
python xTract_reevalSet -I1=evalSet-1.cco.1.map -I2=uniprot_sprot.dat.2012_01 -N=C -O=evalSet-2
```
The first input argument is the map file at time t1 from ES-1. The second input
argument is the SwissProt file at t2. The third argument is the ontology 
name and the fourth argument is the prefix for the output file name. It 
generates the following output files - one sequence file in fasta format 
and one map file for each ontology:

```
evalSet-2.mfo.1
evalSet-2.mfo.1.map 
evalSet-2.bpo.1
evalSet-2.bpo.1.map 
evalSet-2.cco.1
evalSet-2.cco.1.map 
```

<a name="genEvalSet-3" />
#### Evaluation Set 3 (ES-3)

The following set of commands will generate ES-3:

```
python xTract_reevalSet -I1=evalSet-2.mfo.1.map -I2=uniprot_sprot.dat.2013_01 -N=F -O=evalSet-3
python xTract_reevalSet -I1=evalSet-2.bpo.1.map -I2=uniprot_sprot.dat.2013_01 -N=P -O=evalSet-3
python xTract_reevalSet -I1=evalSet-2.cco.1.map -I2=uniprot_sprot.dat.2013_01 -N=C -O=evalSet-3
```
ES-3 data will be stored in the following files: one sequence file in fasta 
format and one map file for each ontology:

```
evalSet-3.mfo.1
evalSet-3.mfo.1.map 
evalSet-3.bpo.1
evalSet-3.bpo.1.map 
evalSet-3.cco.1
evalSet-3.cco.1.map 
```

Similarly, ES-4, ES-5, and ES-6 can be generated. 

### Source Code
This is an open source project and the source code is publicly available on 
GitHub through the following URL: https://github.com/arkatebi/OpenWorld-problem.
For questions, please email either of us: Iddo Friedberg (idoerg@gmail.com),
Ataur Katebi (arkatebi@gmail.com).

[Go to the top] (#title)
