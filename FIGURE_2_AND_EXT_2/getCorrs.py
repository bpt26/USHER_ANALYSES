#!/usr/bin/env python3
# Name: Bryan Thornlow
# Date: 2/1/2018
# createHBScripts.py

import sys
import os
import datetime
import random
import gzip
import math
import scipy
from scipy import stats
import numpy as np

##########################
##### MAIN FUNCTIONS #####
##########################

def getCoors():
	myDataDict = {}
	with open('myCorrs.txt') as f:
		for line in f:
			myDataDict[line.strip().split()[0]] = toFloat(((line.strip().split('(')[-1])[:-1]).split(','))

	print(scipy.stats.spearmanr(myDataDict['x1'], myDataDict['y1'])[1])
	print(scipy.stats.spearmanr(myDataDict['x2'], myDataDict['y2'])[1])
	print(scipy.stats.spearmanr(myDataDict['x3'], myDataDict['y3'])[1])



########################
### HELPER FUNCTIONS ###
########################

def toFloat(myList):
    myReturn = []
    for k in myList:
        myReturn.append(float(k))
    return(myReturn)

def toInt(myList):
    myReturn = []
    for k in myList:
        myReturn.append(int(k))
    return(myReturn)

def joiner(entry):
    newList = []
    for k in entry:
        newList.append(str(k))
    return '\t'.join(newList)

#######################
#### FUNCTION CALL ####
#######################

def main():
   getCoors()

if __name__ == "__main__":
    """
    Calls main when program is run by user.
    """
    main();
    raise SystemExit





            






