#!/bin/sh

git config --global user.email arkatebi@gmail.com
git config --global user.name arkatebi

git remote rm origin

git add README.md
git commit -m 'Update README.md' README.md

git add doc/getDataSet.md
git commit -m 'Update getDataSet.md' doc/getDataSet.md

git add doc/geneCount.md
git commit -m 'Update geneCount.md' doc/geneCount.md

git add doc/geneCount_2012to2016.md
git commit -m 'Update geneCount_2012to2016.md' doc/geneCount_2012to2016.md

git add doc/geneCount_2010to2016.md
git commit -m 'Update geneCount_2010to2016.md' doc/geneCount_2010to2016.md

git remote add origin https://github.com/arkatebi/OpenWorld-problem
#git pull origin master
git push origin master

# Discard unstaged changes:
git stash save --keep-index
git stash drop
