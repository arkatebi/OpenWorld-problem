#!/bin/sh

# Discard unstaged changes:
#git stash save --keep-index
#git stash drop

# Delete the file or the folder:

# Replace FOLDERNAME with the file or folder to be deleted from the git repository:
#git filter-branch -f --index-filter "git rm -rf --cached --ignore-unmatch FOLDERNAME" -- --all
#git filter-branch -f --index-filter "git rm -rf --cached --ignore-unmatch Ontology" -- --all

git rm -r ../workspace/benchmarks
git commit -m 'Removed folder ../workspace/benchmarks' 

# Clean up the local repository:
#rm -rf ./git/refs/original/
#git reflog expire --expire=now --all
#git gc --prune=now
#git gc --aggressive --prune=now

# Push all the changes to the remote repository: 
#git push --all --force
git push origin master 
