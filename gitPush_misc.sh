#!/bin/sh

git config --global user.email arkatebi@gmail.com
git config --global user.name arkatebi

git remote rm origin

git add genBlastScores.sh
git commit -m 'Script to generate BLAST scores for all evaluation sets' misc/genBlastScores.sh

git add genPrecRecCurves.sh
git commit -m 'Script to run CAFAAssess on all evaluation sets' misc/genPrecRecCurves.sh

git add gitPush_trainingSet.sh 
git commit -m 'Script to add files related to xTract_trainingSet program' misc/gitPush_trainingSet.sh

git add gitDel.sh 
git commit -m 'Script to delete a file or directory from git repo' misc/gitDel.sh

git add gitPush_assignBlastScores.sh 
git commit -m 'Script to add files related to Assign_blastScores program' misc/gitPush_assignBlastScores.sh 

git add gitPush_doc.sh 
git commit -m 'Script to add files to doc sub folder' misc/gitPush_doc.sh

git add gitPush_evalSet.sh 
git commit -m 'Script to add files related to xTract_evalSet program' misc/gitPush_evalSet.sh

git add gitPush_GT.sh 
git commit -m 'Script to add files related to Count_GOterms program' misc/gitPush_GT.sh

git add gitPush_misc.sh 
git commit -m 'Script to add files to misc directory' misc/gitPush_misc.sh

git add gitPush_reevalSet.sh 
git commit -m 'Script to add files related to xTract_revalSet program' misc/gitPush_reevalSet.sh

git add gitPush.sh 
git commit -m 'Script to add files and figures' misc/gitPush.sh

git add gitPush_trainingSet.sh 
git commit -m 'Script to add files related to xTract_trainingSet program' misc/gitPush_trainingSet.sh

git add pushGC_2010to2016.sh 
git commit -m 'Script to add figures and data files related to Count_genes program' misc/pushGC_2010to2016.sh

git add pushGC_2012to2016.sh 
git commit -m 'Script to add figures and data files related to Count_genes program' misc/pushGC_2012to2016.sh

git add run_genEvalSet-1.sh 
git commit -m 'Script to generate ES-1' misc/run_genEvalSet-1.sh

git add run_genEvalSet-2.sh 
git commit -m 'Script to generate ES-2' misc/run_genEvalSet-2.sh

git add run_genEvalSet-3.sh 
git commit -m 'Script to generate ES-3' misc/run_genEvalSet-3.sh

git add run_genEvalSet-4.sh 
git commit -m 'Script to generate ES-4' misc/run_genEvalSet-4.sh

git add run_genEvalSet-5.sh 
git commit -m 'Script to generate ES-5' misc/run_genEvalSet-5.sh

git add run_genEvalSet-6.sh 
git commit -m 'Script to generate ES-6' misc/run_genEvalSet-6.sh

git add countTerms.gawk 
git commit -m 'Script to count strings in a text file' misc/countTerms.gawk

git remote add origin https://github.com/arkatebi/OpenWorld-problem
#git pull origin master
git push origin master

# Discard unstaged changes:
git stash save --keep-index
git stash drop
