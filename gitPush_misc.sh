#!/bin/sh

git config --global user.email arkatebi@gmail.com
git config --global user.name arkatebi

git remote rm origin

git add genBlastScores.sh
git commit -m 'Script to generate BLAST scores for all evaluation sets' genBlastScores.sh

git add genPrecRecCurves.sh
git commit -m 'Script to run CAFAAssess on all evaluation sets' genPrecRecCurves.sh

git add gitPush_trainingSet.sh 
git commit -m 'Script to add files related to xTract_trainingSet program' gitPush_trainingSet.sh

git add gitDel.sh 
git commit -m 'Script to delete a file or directory from git repo' gitDel.sh

git add gitPush_assignBlastScores.sh 
git commit -m 'Script to add files related to Assign_blastScores program' gitPush_assignBlastScores.sh 

git add gitPush_doc.sh 
git commit -m 'Script to add files to doc sub folder' gitPush_doc.sh

git add gitPush_evalSet.sh 
git commit -m 'Script to add files related to xTract_evalSet program' gitPush_evalSet.sh

git add gitPush_GT.sh 
git commit -m 'Script to add files related to Count_GOterms program' gitPush_GT.sh

git add gitPush_misc.sh 
git commit -m 'Script to add files to misc directory' gitPush_misc.sh

git add gitPush_reevalSet.sh 
git commit -m 'Script to add files related to xTract_revalSet program' gitPush_reevalSet.sh

git add gitPush.sh 
git commit -m 'Script to add files and figures' gitPush.sh

git add gitPush_trainingSet.sh 
git commit -m 'Script to add files related to xTract_trainingSet program' gitPush_trainingSet.sh

git add pushGC_2010to2016.sh 
git commit -m 'Script to add figures and data files related to Count_genes program' pushGC_2010to2016.sh

git add pushGC_2012to2016.sh 
git commit -m 'Script to add figures and data files related to Count_genes program' pushGC_2012to2016.sh

git add run_genEvalSet-1.sh 
git commit -m 'Script to generate ES-1' run_genEvalSet-1.sh

git add run_genEvalSet-2.sh 
git commit -m 'Script to generate ES-2' run_genEvalSet-2.sh

git add run_genEvalSet-3.sh 
git commit -m 'Script to generate ES-3' run_genEvalSet-3.sh

git add run_genEvalSet-4.sh 
git commit -m 'Script to generate ES-4' run_genEvalSet-4.sh

git add run_genEvalSet-5.sh 
git commit -m 'Script to generate ES-5' run_genEvalSet-5.sh

git add run_genEvalSet-6.sh 
git commit -m 'Script to generate ES-6' run_genEvalSet-6.sh

git add run_genEvalSet-1-sp.sh 
git commit -m 'Script to generate ES-1 for species' run_genEvalSet-1-sp.sh

git add run_genEvalSet-2-sp.sh 
git commit -m 'Script to generate ES-2 for species' run_genEvalSet-2-sp.sh

git add run_genEvalSet-3-sp.sh 
git commit -m 'Script to generate ES-3 for species' run_genEvalSet-3-sp.sh

git add run_genEvalSet-4-sp.sh 
git commit -m 'Script to generate ES-4 for species' run_genEvalSet-4-sp.sh

git add run_genEvalSet-5-sp.sh 
git commit -m 'Script to generate ES-5 for species' run_genEvalSet-5-sp.sh

git add run_genEvalSet-6-sp.sh 
git commit -m 'Script to generate ES-6 for species' run_genEvalSet-6-sp.sh

git add countTerms.gawk 
git commit -m 'Script to count strings in a text file' countTerms.gawk



git remote add origin https://github.com/arkatebi/OpenWorld-problem
#git pull origin master
git push origin master

# Discard unstaged changes:
git stash save --keep-index
git stash drop
