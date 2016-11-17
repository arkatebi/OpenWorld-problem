#!/bin/awk/ -f
# This script counts the number of total terms in a file
# where comma separated terms are stored in each line.
# gawk -f countTerms.gawk termFile.txt 
BEGIN {
   FS=",";
   count=0
}

{
   split($0,a,FS)
   for (i in a) {
      terms[a[i]]=a[i]
   }
}

END { 
  #for (gt in terms){ 
  #   print gt
  #}
  n=alen(terms) 
  print(n)
}

function alen(a){
  k=0
  for (i in a) k++;
  return k
}
