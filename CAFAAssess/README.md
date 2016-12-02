
# A command-line interface for assessing a single prediction file using precision-recall.
##### Modified from the CAFAAssess software: https://github.com/ashleyzhou972/CAFAAssess

Default GO release is from 06/01/2014.

To use:

### 1. Download both CAFAAssess and Ontology repositories

### 2. cd to the nearest base directory that contains both CAFAAssess and Ontology

### 3. Type `python CAFAAssess/precrec_main.py -h` for the usage of this module

# Example:

```
python2 ./CAFAAssess/precrec_main.py -I1=./workspace/blastScores/evalSet-1.mfo.scores.txt.1 \
                                     -I2=./workspace/evalSets/bm-evalSet-1.mfo \
                                     -G=MFO \
                                     -O=./figures/prCurves/prCurve-evalSet-1.mfo.png
```
