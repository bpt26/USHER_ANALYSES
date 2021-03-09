#!/usr/bin/env python3
# Name: Bryan Thornlow
# Date: 2/1/2018
# compareDatabases.py

import sys
import os
import datetime
import random
import numpy as np
import gzip
import math


##########################
##### MAIN FUNCTIONS #####
##########################

def parseLogs():
    myOutString = ''
    for rep in range(1,101):
        with open(str(rep)+'.log') as f:
            for line in f:
                splitLine = line.strip().split('\t')
                if len(splitLine) > 3 and splitLine[3].startswith('Number of parsimony-optimal placements'):
                    mySample = splitLine[1].split()[-1]
                    myOutString += joiner([rep,mySample,int(splitLine[3].split()[-1])])+'\n'
    open('REAL_LOGS.txt','w').write(myOutString)



##########################
#### HELPER FUNCTIONS ####
##########################

def joiner(entry):
    newList = []
    for k in entry:
        newList.append(str(k))
    return('\t'.join(newList))


def main():
    parseLogs()

if __name__ == "__main__":
    """
    Calls main when program is run by user.
    """
    main();
    raise SystemExit




                    




