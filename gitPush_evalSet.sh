#!/bin/sh
git config --global user.email arkatebi@gmail.com
git config --global user.name arkatebi

git remote rm origin

git add xTract_evalSet 
git commit -m 'Simplified create_outfilename method' xTract_evalSet

git add xTract_sp_evalSet.py
git commit -m 'Updated for writing GO terms in sorted order' xTract_sp_evalSet.py

git add ArgParser_xTract_evalSet.py
git commit -m 'Simplified argument list' ArgParser_xTract_evalSet.py

git remote add origin https://github.com/arkatebi/OpenWorld-problem
#git pull origin master
git push origin master

# Discard unstaged changes:
git stash save --keep-index
git stash drop
