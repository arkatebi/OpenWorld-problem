#!/bin/sh

git config --global user.email arkatebi@gmail.com
git config --global user.name arkatebi

git remote rm origin

git add xTract_trainingSet 
git commit -m 'updated for three ontologies' xTract_trainingSet

git add xTract_sp_trainingSet.py
git commit -m 'updated filter methods to print GO terms in the map file' xTract_sp_trainingSet.py

git add ArgParser_xTract_trainingSet.py
git commit -m 'Firt commit' ArgParser_xTract_trainingSet.py

git remote add origin https://github.com/arkatebi/OpenWorld-problem
#git pull origin master
git push origin master

# Discard unstaged changes:
git stash save --keep-index
git stash drop
