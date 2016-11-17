#!/bin/sh
# Five STEPs before running this script:  

# STEP 1: comment out the following line
#exit 0

# STEP 2: Discard unstaged changes:
git stash save --keep-index
git stash drop

# Delete the file or the folder:

# STEP 3: Replace FOLDERNAME with the file or folder to be deleted from the git repository:
#git filter-branch -f --index-filter "git rm -rf --cached --ignore-unmatch FOLDERNAME" -- --all
#git filter-branch -f --index-filter "git rm -rf --cached --ignore-unmatch Ontology" -- --all
#git filter-branch -f --index-filter "git rm -rf --cached --ignore-unmatch workspace/geneCount.stat.1.xls" -- --all

# STEP 4: Clean up the local repository:
rm -rf ./git/refs/original/
git reflog expire --expire=now --all
git gc --prune=now
git gc --aggressive --prune=now

# STEP 5: Push all the changes to the remote repository: 
git push --all --force

