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

def getLinkColor():
    myRealOutString = ''
    for repNum in range(1,7):
        strainToColor = {}
        for line in open('missing-'+str(repNum)+'.txt'):
            strainToColor[line.strip()] = 'red'

        myOutString = []
        for line in open('t'+str(repNum)+'_assoc_table.txt'):
            splitLine = (line.strip()).split('\t')
            if splitLine[0] in strainToColor and splitLine[1] in strainToColor:
                myOutString.append('red')
            else:
                myOutString.append('black')
        myRealOutString += 'link.col = c('+joinerC(myOutString)+')\n'
    open('linkerVectorNew.txt','w').write(myRealOutString)



##########################
#### HELPER FUNCTIONS ####
##########################

def joinerC(entry):
    newList = []
    for k in entry:
        newList.append('"'+str(k)+'"')
    return ','.join(newList)


def joiner(entry):
    newList = []
    for k in entry:
        newList.append(str(k))
    return('\t'.join(newList))


def main():
   getLinkColor()

if __name__ == "__main__":
    """
    Calls main when program is run by user.
    """
    main();
    raise SystemExit






















