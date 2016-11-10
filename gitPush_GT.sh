#!/bin/sh

git config --global user.email arkatebi@gmail.com
git config --global user.name arkatebi

git remote rm origin

#git add workspace/sprot_genes.stat.1 
#git commit -m 'Added table for frequencies of genes to workspace' workspace/sprot_genes.stat.1

git add Count_GOterms 
git commit -m 'First commit' Count_GOterms 

git add Count_sprot_GOterms.py 
git commit -m 'Firt commit' Count_sprot_GOterms.py 

git remote add origin https://github.com/arkatebi/OpenWorld-problem
#git pull origin master
git push origin master

# Discard unstaged changes:
git stash save --keep-index
git stash drop
