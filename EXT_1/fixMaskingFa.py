#!/usr/bin/env python3
# Name: Bryan Thornlow
# Date: 2/1/2018
# compareDatabases.py

import sys
import os
import datetime
import random
import numpy
import gzip
import math

##########################
##### MAIN FUNCTIONS #####
##########################

def fixMasking():
    for r in range(1,6):
        for s in [2.5,5.0,7.5]:
            myOutString = ''
            with open('MASKED_MISSING_FASTA/missing_1000_subtree_'+str(r)+'_mask_'+str(s)+'.fasta') as f:
                for line in f:
                    splitLine = line.strip()
                    if not splitLine.startswith('>'):
                        splitLine = splitLine.replace('X','N')
                    myOutString += splitLine+'\n'
            open('FIXED_MASKED_MISSING_FASTA/missing_1000_subtree_'+str(r)+'_mask_'+str(s)+'.fasta','w').write(myOutString)



##########################
#### HELPER FUNCTIONS ####
##########################

def joiner(entry):
    newList = []
    for k in entry:
        newList.append(str(k))
    return '\t'.join(newList)


def main():
    fixMasking()


if __name__ == "__main__":
    """
    Calls main when program is run by user.
    """
    main();
    raise SystemExit




                    







