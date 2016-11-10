#!/bin/sh

git config --global user.email arkatebi@gmail.com
git config --global user.name arkatebi

git remote rm origin

git add LICENSE.md
git commit -m 'Create LICENSE.md'

git add README.md
git commit -m 'Update README.md' README.md

#git add getDataSet.md
#git commit -m 'Update getDataSet.md' getDataSet.md

git add geneCount.md
git commit -m 'Update geneCount.md' geneCount.md

git add geneCount_2012to2016.md
git commit -m 'Update geneCount_2012to2016.md' geneCount_2012to2016.md

git add geneCount_2010to2016.md
git commit -m 'Update geneCount_2010to2016.md' geneCount_2010to2016.md

git add .config
git commit -m 'Update .config configuration file'

git add figures/incomplete-knowledge-1.1.png
git commit -m 'Added figure for incomplete knowledge' figures/incomplete-knowledge-1.1.png

git add figures/experiment-design-1.3.png
git commit -m 'Added figure for experimental design' figures/experiment-design-1.3.png

git add workspace/sp_list.txt 
git commit -m 'Added default species list file species_list.txt to workspace' workspace/sp_list.txt

git add workspace/sprot_files.txt 
git commit -m 'Added default list file for SwissProt filenames sprot_files.txt to workspace' workspace/sprot_files.txt

#git add workspace/sprot_genes.stat.1 
#git commit -m 'Added table for frequencies of genes to workspace' workspace/sprot_genes.stat.1

#git add workspace/sprot_genes.stat.1.xls 
#git commit -m 'Added table for frequencies of genes to workspace' workspace/sprot_genes.stat.1.xls

git add workspace/geneCount.stat.1 
git commit -m 'Added table for frequencies of genes to workspace' workspace/geneCount.stat.1

git add workspace/geneCount.stat.1.xls 
git commit -m 'Added table for frequencies of genes to workspace' workspace/geneCount.stat.1.xls

git add Count_genes 
git commit -m 'Added a method count_genes_for_species' Count_genes 

git add Count_sp_genes.py 
git commit -m 'Corrected code: removed break' Count_sp_genes.py 

git add names.dmp
git commit -m 'Upload taxonomy file' names.dmp

git add ArgParser_count.py
git commit -m 'Updated argument options' ArgParser_count.py

git add Config.py
git commit -m 'First commit' Config.py

git add Download.py
git commit -m 'First commit' Download.py

git add FormatChecker.py
git commit -m 'First commit' FormatChecker.py

git add LocateDataset.py
git commit -m 'Added a method locate_anyfile to locate any file' LocateDataset.py

git add Plot_geneCounts
git commit -m 'Simplified code by adding methods' Plot_geneCounts

git add ArgParser_plot.py
git commit -m 'Simplified code by adding methods' ArgParser_plot.py

git remote add origin https://github.com/arkatebi/OpenWorld-problem
#git pull origin master
git push origin master

# Discard unstaged changes:
git stash save --keep-index
git stash drop
