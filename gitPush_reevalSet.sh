#!/bin/sh

git config --global user.email arkatebi@gmail.com
git config --global user.name arkatebi

git remote rm origin

git add xTract_reevalSet 
git commit -m 'Output filename automated' xTract_reevalSet

git add xTract_sp_reevalSet.py
git commit -m 'Added method to filter out sequnces' xTract_sp_reevalSet.py

git add ArgParser_xTract_reevalSet.py
git commit -m 'Added argument for ontology' ArgParser_xTract_reevalSet.py

git remote add origin https://github.com/arkatebi/OpenWorld-problem
#git pull origin master
git push origin master

# Discard unstaged changes:
git stash save --keep-index
git stash drop
