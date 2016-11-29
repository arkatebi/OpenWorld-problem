#!/bin/sh
#git config --global user.email arkatebi@gmail.com
#git config --global user.name arkatebi

#git remote rm origin

#git add ../CAFAAssess
#git commit -m 'Added CAFAAsses folder' ../CAFAAssess

git add ../CAFAAssess/precrec_main.py
git commit -m 'Simplified' ../CAFAAssess/precrec_main.py

git add ../CAFAAssess/precRec.py
git commit -m 'Modified method read_benchamrk' ../CAFAAssess/precRec.py

#git remote add origin https://github.com/arkatebi/OpenWorld-problem
git push origin master

# Discard unstaged changes:
#git stash save --keep-index
#git stash drop
