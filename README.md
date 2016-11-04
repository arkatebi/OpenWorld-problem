<a name="title" />
## Impact of 'Open World Assumption' on assessment of predictive models
* The open-world problem arises from the open-world assumption: 'the 
  absence of evidence does not amount to the evidence of absence'.
* In this project, I investigate this problem by taking advantage 
  of the growth of the curated protein annotation database, 
  UniProtKB/SwissProt.
* I update this repository with the new tools that I develop to 
  facilitate the research. 

### Contents
1\. [Introduction] (#intro)

2\. [Experiment Design] (#expDesign)

3\. [Requirements to use the tools] (#requirements)

4\. [Gene Count Statistics] (#geneCounts)

5\. [Training and Evaluation Sets] (#genSets)

6\. [Predictive Models] (#modelSet)


<a name="intro">
### Introduction
Models for functional predictions of proteins are developed based on the
current state of the functional annotation databases. However, the
annotations of most proteins are incomplete. Therefore, the question arises
whether the assigned strengths and weaknesses of the predictive models based
on the current knowledge still hold when new annotations become 
available through additional experiments. The situation can be depicted in the
following figure.

![alt Incomplete Knowledge] (/figures/incomplete-knowledge-1.1.png?raw=true “Incomplete Knowledge”)

Suppose, T is the set of experimentally annotated functions for some protein, 
according to the current state of knowledge. Some model A predicts this 
set to be P. Therefore, tp (true positive) = |P∩T|, fp (false positive) = 
|P-T|, and fn (false negative) = |T-P|. The performance will be measured 
according to these values. Because of new experiments, if T expands to 
become T′ as shown in the figure above, then tp, fp, and fn will change. We 
want to address the following question: how can this change of knowledge 
impact the performance evaluation of the predictive model A?

<a name="expDesign" />
### Experimental Design 
The following figure shows the time points for collecting the training and 
evaluation sets. 

![alt Experiment Design] (/figures/experiment-design-1.3.png?raw=true “Experiment Design”)

<a name="requirements" />
### Requirements
* Python 3.5 or greater
* Biopython 1.66 or greater

<a name="geneCounts" />
### Gene Count Statistics 
The statistics for gene counts in the UniProtKB/SwissProt can 
be found by following the link below: 

https://github.com/arkatebi/OpenWorld-problem/blob/master/doc/geneCount.md

<a name="genSets" />
### Training and Evaluation Sets 

The details of how to collect the training and evaluation data sets
can be found by following the link below: 

https://github.com/arkatebi/OpenWorld-problem/blob/master/doc/getDataSet.md


<a name="modelSet" />
### Predictive Models 

#### BLAST 

The Assign_blastScores program assign scores to the association between 
GO terms and proteins according to the scoring criteria described in [1].

```
python Assign_blastScores -I1=evalSet-1.9606.mfo.1.map \
                          -I2=trainingSet.9606.mfo.map \
                          -I3=evalSet-1.9606.mfo-blast-results.txt \
                          -O=evalSet-1.9606.mfo.scores.txt
```

The first and second input files are map files related to evaluation set
and training set, respectively. A map file has three columns: the first
column records program generated protein id (for details, see (#genSet)),
the second column records protein name, and the third column records the
GO term that defines the function of this protein. The third input file
contains the blast results of evaluation set against the training set.
The fourth input is the output filename where the program records scores:
the first column has the target id, the second column has the protein name,
and the third column has the assigned score.

#### HMMER 
See reference [2].

### Source Code
This is an open source project and the source code is publicly available on 
GitHub through the following URL: https://github.com/arkatebi/OpenWorld-problem.
For questions, please email either of us: Iddo Friedberg (idoerg@gmail.com),
Ataur Katebi (arkatebi@gmail.com).

<a name="refSet" />
### References 

[1] Altschul SF, Gish W, Miller W, Myers EW & Lipman DJ (1990). Basic local alignment search tool. J. Mol. Biol. 215:403-410
[2] HMMER 3.1b2 (February 2015); http://hmmer.org/

[Go to the top] (#title)
