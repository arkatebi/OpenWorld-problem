#!/bin/bash
# Evaluation Set 1
echo 'Evaluation Set 1'
python2 ./CAFAAssess/precrec_main.py -I1=./workspace/blastScores/evalSet-1.mfo.scores.txt.1 \
                                     -I2=./workspace/evalSets/bm-evalSet-1.mfo \
                                     -G=MFO \
                                     -O=./figures/prCurves/prCurve-evalSet-1.mfo.png 
python2 ./CAFAAssess/precrec_main.py -I1=./workspace/blastScores/evalSet-1.bpo.scores.txt.1 \
                                     -I2=./workspace/evalSets/bm-evalSet-1.bpo \
                                     -G=BPO \
                                     -O=./figures/prCurves/prCurve-evalSet-1.bpo.png 
python2 ./CAFAAssess/precrec_main.py -I1=./workspace/blastScores/evalSet-1.cco.scores.txt.1 \
                                     -I2=./workspace/evalSets/bm-evalSet-1.cco \
                                     -G=CCO \
                                     -O=./figures/prCurves/prCurve-evalSet-1.cco.png 
# Evaluation set 2
echo 'Evaluation Set 2'
python2 ./CAFAAssess/precrec_main.py -I1=./workspace/blastScores/evalSet-2.mfo.scores.txt.1 \
                                     -I2=./workspace/evalSets/bm-evalSet-2.mfo \
                                     -G=MFO \
                                     -O=./figures/prCurves/prCurve-evalSet-2.mfo.png 
python2 ./CAFAAssess/precrec_main.py -I1=./workspace/blastScores/evalSet-2.bpo.scores.txt.1 \
                                     -I2=./workspace/evalSets/bm-evalSet-2.bpo \
                                     -G=BPO \
                                     -O=./figures/prCurves/prCurve-evalSet-2.bpo.png 
python2 ./CAFAAssess/precrec_main.py -I1=./workspace/blastScores/evalSet-2.cco.scores.txt.1 \
                                     -I2=./workspace/evalSets/bm-evalSet-2.cco \
                                     -G=CCO \
                                     -O=./figures/prCurves/prCurve-evalSet-2.cco.png 
#exit 0
# Evaluation set 3
echo 'Evaluation Set 3'
python2 ./CAFAAssess/precrec_main.py -I1=./workspace/blastScores/evalSet-3.mfo.scores.txt.1 \
                                     -I2=./workspace/evalSets/bm-evalSet-3.mfo \
                                     -G=MFO \
                                     -O=./figures/prCurves/prCurve-evalSet-3.mfo.png 
python2 ./CAFAAssess/precrec_main.py -I1=./workspace/blastScores/evalSet-3.bpo.scores.txt.1 \
                                     -I2=./workspace/evalSets/bm-evalSet-3.bpo \
                                     -G=BPO \
                                     -O=./figures/prCurves/prCurve-evalSet-3.bpo.png 
python2 ./CAFAAssess/precrec_main.py -I1=./workspace/blastScores/evalSet-3.cco.scores.txt.1 \
                                     -I2=./workspace/evalSets/bm-evalSet-3.cco \
                                     -G=CCO \
                                     -O=./figures/prCurves/prCurve-evalSet-3.cco.png 
# Evaluation set 4
echo 'Evaluation Set 4'
python2 ./CAFAAssess/precrec_main.py -I1=./workspace/blastScores/evalSet-4.mfo.scores.txt.1 \
                                     -I2=./workspace/evalSets/bm-evalSet-4.mfo \
                                     -G=MFO \
                                     -O=./figures/prCurves/prCurve-evalSet-4.mfo.png 
python2 ./CAFAAssess/precrec_main.py -I1=./workspace/blastScores/evalSet-4.bpo.scores.txt.1 \
                                     -I2=./workspace/evalSets/bm-evalSet-4.bpo \
                                     -G=BPO \
                                     -O=./figures/prCurves/prCurve-evalSet-4.bpo.png 
python2 ./CAFAAssess/precrec_main.py -I1=./workspace/blastScores/evalSet-4.cco.scores.txt.1 \
                                     -I2=./workspace/evalSets/bm-evalSet-4.cco \
                                     -G=CCO \
                                     -O=./figures/prCurves/prCurve-evalSet-4.cco.png 
# Evaluation set 5
echo 'Evaluation Set 5'
python2 ./CAFAAssess/precrec_main.py -I1=./workspace/blastScores/evalSet-5.mfo.scores.txt.1 \
                                     -I2=./workspace/evalSets/bm-evalSet-5.mfo \
                                     -G=MFO \
                                     -O=./figures/prCurves/prCurve-evalSet-5.mfo.png 
python2 ./CAFAAssess/precrec_main.py -I1=./workspace/blastScores/evalSet-5.bpo.scores.txt.1 \
                                     -I2=./workspace/evalSets/bm-evalSet-5.bpo \
                                     -G=BPO \
                                     -O=./figures/prCurves/prCurve-evalSet-5.bpo.png 
python2 ./CAFAAssess/precrec_main.py -I1=./workspace/blastScores/evalSet-5.cco.scores.txt.1 \
                                     -I2=./workspace/evalSets/bm-evalSet-5.cco \
                                     -G=CCO \
                                     -O=./figures/prCurves/prCurve-evalSet-5.cco.png
# Evaluation set 6
echo 'Evaluation Set 6'
python2 ./CAFAAssess/precrec_main.py -I1=./workspace/blastScores/evalSet-6.mfo.scores.txt.1 \
                                     -I2=./workspace/evalSets/bm-evalSet-6.mfo \
                                     -G=MFO \
                                     -O=./figures/prCurves/prCurve-evalSet-6.mfo.png 
python2 ./CAFAAssess/precrec_main.py -I1=./workspace/blastScores/evalSet-6.bpo.scores.txt.1 \
                                     -I2=./workspace/evalSets/bm-evalSet-6.bpo \
                                     -G=BPO \
                                     -O=./figures/prCurves/prCurve-evalSet-6.bpo.png 
python2 ./CAFAAssess/precrec_main.py -I1=./workspace/blastScores/evalSet-6.cco.scores.txt.1 \
                                     -I2=./workspace/evalSets/bm-evalSet-6.cco \
                                     -G=CCO \
                                     -O=./figures/prCurves/prCurve-evalSet-6.cco.png
