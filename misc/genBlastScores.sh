# This script runs Assign_blastScores to assign scores to the evaluation sets:
# Assign scores using BLAST model:evaluation set 1:
python Assign_blastScores -I1=evalSet-1.mfo.1.map \
                          -I2=trainingSet.mfo.map \
                          -I3=evalSet-1.mfo-blast-results.txt \
                          -O=evalSet-1.mfo.scores.txt
python Assign_blastScores -I1=evalSet-1.bpo.1.map \
                          -I2=trainingSet.bpo.map \
                          -I3=evalSet-1.bpo-blast-results.txt \
                          -O=evalSet-1.bpo.scores.txt
python Assign_blastScores -I1=evalSet-1.cco.1.map \
                          -I2=trainingSet.cco.map \
                          -I3=evalSet-1.cco-blast-results.txt \
                          -O=evalSet-1.cco.scores.txt
# Assign scores using BLAST model:evaluation set 2:
python Assign_blastScores -I1=evalSet-2.mfo.1.map \
                          -I2=trainingSet.mfo.map \
                          -I3=evalSet-2.mfo-blast-results.txt \
                          -O=evalSet-2.mfo.scores.txt
python Assign_blastScores -I1=evalSet-2.bpo.1.map \
                          -I2=trainingSet.bpo.map \
                          -I3=evalSet-2.bpo-blast-results.txt \
                          -O=evalSet-2.bpo.scores.txt
python Assign_blastScores -I1=evalSet-2.cco.1.map \
                          -I2=trainingSet.cco.map \
                          -I3=evalSet-2.cco-blast-results.txt \
                          -O=evalSet-2.cco.scores.txt
# Assign scores using BLAST model:evaluation set 3:
python Assign_blastScores -I1=evalSet-3.mfo.1.map \
                          -I2=trainingSet.mfo.map \
                          -I3=evalSet-3.mfo-blast-results.txt \
                          -O=evalSet-3.mfo.scores.txt
python Assign_blastScores -I1=evalSet-3.bpo.1.map \
                          -I2=trainingSet.bpo.map \
                          -I3=evalSet-3.bpo-blast-results.txt \
                          -O=evalSet-3.bpo.scores.txt
python Assign_blastScores -I1=evalSet-3.cco.1.map \
                          -I2=trainingSet.cco.map \
                          -I3=evalSet-3.cco-blast-results.txt \
                          -O=evalSet-3.cco.scores.txt
# Assign scores using BLAST model:evaluation set 4:
python Assign_blastScores -I1=evalSet-4.mfo.1.map \
                          -I2=trainingSet.mfo.map \
                          -I3=evalSet-4.mfo-blast-results.txt \
                          -O=evalSet-4.mfo.scores.txt
python Assign_blastScores -I1=evalSet-4.bpo.1.map \
                          -I2=trainingSet.bpo.map \
                          -I3=evalSet-4.bpo-blast-results.txt \
                          -O=evalSet-4.bpo.scores.txt
python Assign_blastScores -I1=evalSet-4.cco.1.map \
                          -I2=trainingSet.cco.map \
                          -I3=evalSet-4.cco-blast-results.txt \
                          -O=evalSet-4.cco.scores.txt
# Assign scores using BLAST model:evaluation set 5:
python Assign_blastScores -I1=evalSet-5.mfo.1.map \
                          -I2=trainingSet.mfo.map \
                          -I3=evalSet-5.mfo-blast-results.txt \
                          -O=evalSet-5.mfo.scores.txt
python Assign_blastScores -I1=evalSet-5.bpo.1.map \
                          -I2=trainingSet.bpo.map \
                          -I3=evalSet-5.bpo-blast-results.txt \
                          -O=evalSet-5.bpo.scores.txt
python Assign_blastScores -I1=evalSet-5.cco.1.map \
                          -I2=trainingSet.cco.map \
                          -I3=evalSet-5.cco-blast-results.txt \
                          -O=evalSet-5.cco.scores.txt
# Assign scores using BLAST model:evaluation set 6:
python Assign_blastScores -I1=evalSet-6.mfo.1.map \
                          -I2=trainingSet.mfo.map \
                          -I3=evalSet-6.mfo-blast-results.txt \
                          -O=evalSet-6.mfo.scores.txt
python Assign_blastScores -I1=evalSet-6.bpo.1.map \
                          -I2=trainingSet.bpo.map \
                          -I3=evalSet-6.bpo-blast-results.txt \
                          -O=evalSet-6.bpo.scores.txt
python Assign_blastScores -I1=evalSet-6.cco.1.map \
                          -I2=trainingSet.cco.map \
                          -I3=evalSet-6.cco-blast-results.txt \
                          -O=evalSet-6.cco.scores.txt

