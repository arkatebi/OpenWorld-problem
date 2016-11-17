#!/bin/sh
# Five STEPs before running this script:  

# STEP 1: comment out the following line
#exit 0

# STEP 2: Discard unstaged changes:
git stash save --keep-index
git stash drop

# STEP 3: Delete the file (s):
# List all the file names to be deleted with the comparative path:

#git rm ../genPrecRecCurves.sh
#git commit -m "remove ../genPrecRecCurves.sh"

#git rm ../gitDel.sh
#git commit -m "remove ../gitDel.sh"

# STEP 4: Push all the changes to the remote repository: 
git push origin master 

