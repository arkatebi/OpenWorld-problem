#!/bin/sh
git config --global user.email arkatebi@gmail.com
git config --global user.name arkatebi

git remote rm origin

#git add ../CAFAAssess
#git commit -m 'Added CAFAAsses folder' ../CAFAAssess

git add ../CAFAAssess/precrec_main.py
git commit -m 'Simplified' ../CAFAAssess/precrec_main.py

git add ../CAFAAssess/precRec.py
git commit -m 'Modified method read_benchamrk' ../CAFAAssess/precRec.py

git add ../CAFAAssess/README.md
git commit -m 'Updated README file' ../CAFAAssess/README.md

#git add ../figures/prCurves
#git commit -m 'Added subfolder figures/prCurves' ../figures/prCurves

#git add ../genPRcurves.sh
#git commit -m 'Added script to generate all prCurves' ../genPRcurves.sh

#git add ../genPRcurves.txt
#git commit -m 'Added message file from cript genPRcurves.sh' ../genPRcurves.txt

git remote add origin https://github.com/arkatebi/OpenWorld-problem
git push origin master
