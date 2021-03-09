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
    strainToColor = {}
    with open('/Users/Bryan/Desktop/COVID/NEW_TREES/cogSamples.colors') as f:
        for line in f:
            splitLine = (line.strip()).split('\t')
            strainToColor[splitLine[0]] = splitLine[1]

    sampleTo6 = {}
    sampleTo131 = {}
    lineCounter = 0
    with open('6u.tip.label') as f:
        for line in f:
            sampleTo6[line.strip()] = lineCounter
            lineCounter += 1

    lineCounter = 0
    with open('131u.tip.label') as f:
        for line in f:
            sampleTo131[line.strip()] = lineCounter
            lineCounter += 1


    myRealOutString = ''
    myOutString = []
    lineCounter = 0
    for line in open('assoc_table.txt'):
        splitLine = (line.strip()).split('\t')
        
        if splitLine[0] in ["England/PHEC-16CB8/2020|2020-03-31","Wales/PHWC-15DA6F/2020|2020-05-15"]:
            myOutString.append("black")
        else:
            myOutString.append("white")


        # if sampleTo6[splitLine[0]] == sampleTo131[splitLine[0]]:
        #     myOutString.append("white")
        # else:
        #     if splitLine[0] in strainToColor and splitLine[1] in strainToColor:
        #         if strainToColor[splitLine[0]] == strainToColor[splitLine[1]]:
        #             myOutString.append(strainToColor[splitLine[0]])
        #         else:
        #             myOutString.append('#000000')
        #     else:
        #         myOutString.append('#000000')
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






















