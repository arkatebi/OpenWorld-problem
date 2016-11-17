#!/bin/sh
# Four STEPs before running this script:  

# STEP 1: comment out the following line
#exit 0

# STEP 2: Discard unstaged changes:
git stash save --keep-index
git stash drop

# STEP 3: Delete the file (s):
# List all the file names to be deleted with the comparative path:
# To delete file from both git repo and the file system: 
# git rm filename
# git commit "-m filename"

# To delete file from only git repo and not remove it from the file system: 
# git rm --cached filename
# git commit "-m filename"

#git rm ../genPrecRecCurves.sh
#git commit -m "remove ../genPrecRecCurves.sh"

# STEP 4: Push all the changes to the remote repository: 
git push origin master 
