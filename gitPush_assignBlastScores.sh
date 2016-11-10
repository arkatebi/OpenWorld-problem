#!/bin/sh

git config --global user.email arkatebi@gmail.com
git config --global user.name arkatebi

git remote rm origin

#git add Ontology/\*.*
#git commit -m 'Added Ontology folder' Ontology

git add workspace/trainingSet.9606.mfo
git commit -m 'Added sample evaluation set' workspace/trainingSet.9606.mfo

git add workspace/evalSet-1.9606.mfo.1
git commit -m 'Added sample evaluation set' workspace/evalSet-1.9606.mfo.1

git add workspace/evalSet-1.9606.mfo.1.map
git commit -m 'Added sample evaluation set map file' workspace/evalSet-1.9606.mfo.1.map

git add workspace/evalSet-1.9606.mfo-blast-results.txt
git commit -m 'Added sample blast results' workspace/evalSet-1.9606.mfo-blast-results.txt

git add Assign_blastScores
git commit -m 'Output GO terms in sorted order' Assign_blastScores

git add ArgParser_assign_blastScores.py
git commit -m 'Added complete user argument list' ArgParser_assign_blastScores.py

git add genBlastScores.sh
git commit -m 'Script to run Assign_blastScores program' genBlastScores.sh

git remote add origin https://github.com/arkatebi/OpenWorld-problem
#git pull origin master
git push origin master

# Discard unstaged changes:
git stash save --keep-index
git stash drop
