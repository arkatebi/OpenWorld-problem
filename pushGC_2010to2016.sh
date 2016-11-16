#!/bin/sh
git config --global user.email arkatebi@gmail.com
git config --global user.name arkatebi

git remote rm origin

git add figures/geneCount_2010to2016.9606.1.png
git commit -m 'Added figure for Gene Count for Human' figures/geneCount_2010to2016.9606.1.png

git add figures/geneCount_2010to2016.10090.1.png
git commit -m 'Added figure for Gene Count for Mouse' figures/geneCount_2010to2016.10090.1.png

git add figures/geneCount_2010to2016.3702.1.png
git commit -m 'Added figure for Gene Count for Arabidopsis' figures/geneCount_2010to2016.3702.1.png

git add figures/geneCount_2010to2016.10116.1.png
git commit -m 'Added figure for Gene Count for Rat' figures/geneCount_2010to2016.10116.1.png

git add figures/geneCount_2010to2016.559292.1.png
git commit -m 'Added figure for Gene Count for S. cerevisiae' figures/geneCount_2010to2016.559292.1.png

git add figures/geneCount_2010to2016.9913.1.png
git commit -m 'Added figure for Gene Count for Bovine' figures/geneCount_2010to2016.9913.1.png

git add figures/geneCount_2010to2016.284812.1.png
git commit -m 'Added figure for Gene Count for S. pombe' figures/geneCount_2010to2016.284812.1.png

git add figures/geneCount_2010to2016.83333.1.png
git commit -m 'Added figure for Gene Count for E. coli' figures/geneCount_2010to2016.83333.1.png

git add figures/geneCount_2010to2016.224308.1.png
git commit -m 'Added figure for Gene Count for B. subtilis' figures/geneCount_2010to2016.224308.1.png

git add figures/geneCount_2010to2016.44689.1.png
git commit -m 'Added figure for Gene Count for D. discoideum' figures/geneCount_2010to2016.44689.1.png

#git add workspace/sp_list.txt 
#git commit -m 'Added default species list file species_list.txt to workspace' workspace/sp_list.txt

git add workspace/sprot_2010to2016.txt 
git commit -m 'Added default list file for SwissProt filenames sprot_files.txt to workspace' workspace/sprot_2010to2016.txt

git add workspace/geneCount_2010to2016.stat.1 
git commit -m 'Added table for frequencies of genes to workspace' workspace/geneCount_2010to2016.stat.1

git add workspace/geneCount_2010to2016.stat.1.xls 
git commit -m 'Added table for frequencies of genes to workspace' workspace/geneCount_2010to2016.stat.1.xls

git remote add origin https://github.com/arkatebi/OpenWorld-problem
#git pull origin master
git push origin master

# Discard unstaged changes:
git stash save --keep-index
git stash drop
