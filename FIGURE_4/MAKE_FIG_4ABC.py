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
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

"""
9 panel figure:

RF  N1ID  N1N2-2  EP

"""

##########################
##### MAIN FUNCTIONS #####
##########################

def plotRealHists():
    rf = []
    n1id = []
    nstat = []
    ep = []

    with open('realRFs.txt') as f:
        for line in f:
            splitLine = line.strip().split('\t')
            if splitLine[0] != 'Replicate':
                rf.append(float(splitLine[1]))

    with open('compareSisNewReal.txt') as f:
        for line in f:
            splitLine = line.strip().split('\t')
            n1id.append(int(splitLine[3]))
            nstat.append(float(splitLine[4]))

    with open('REAL_LOGS.txt') as f:
        for line in f:
            splitLine = line.strip().split('\t')
            ep.append(int(splitLine[2]))
            if int(splitLine[2]) > 10:
                ep.append(10)


    fig_width = 10
    fig_height = 3
    panel_width = 0.75/3
    panel_height = 0.7
    panel_total_height = (panel_height*1)
    panel_total_width = (panel_width*3)
    extra_y_space = 1 - panel_total_height
    extra_x_space = 1 - panel_total_width
    above_below = extra_y_space/2
    left_right = extra_x_space/4

    plt.figure(figsize=(fig_width, fig_height))
    panel1 = plt.axes([(left_right*1)+(panel_width*0), (above_below*1)+(panel_height*0), panel_width, panel_height], frameon=True)
    panel2 = plt.axes([(left_right*2)+(panel_width*1), (above_below*1)+(panel_height*0), panel_width, panel_height], frameon=True)
    panel3 = plt.axes([(left_right*3)+(panel_width*2), (above_below*1)+(panel_height*0), panel_width, panel_height], frameon=True)

    myX = [0,1,2,3,4,5,6,7,8,9,10]
    myY = makeHist(rf, myX)
    panel1.bar(myX, myY, edgecolor='black', facecolor='gray', linewidth=1)
    print(rf)
    panel1.set_ylabel('Proportion of Trees',size=8)
    panel1.set_xlabel('Robinson-Foulds Distance',size=8)
    panel1.tick_params(bottom='on',labelbottom='on',left='on',labelleft='on',right='off',labelright='off',top='off',labeltop='off',labelsize=8)

    myX = [0,1,2,3,4,5]
    myY = makeHist(nstat, myX)
    panel2.bar(myX, myY, edgecolor='black', facecolor='gray', linewidth=1)
    print(max(nstat))
    panel2.set_ylabel('Proportion of Samples',size=8)
    panel2.set_xlabel('Distance From Reference Placement (edges)',size=8)
    panel2.tick_params(bottom='on',labelbottom='on',left='on',labelleft='on',right='off',labelright='off',top='off',labeltop='off',labelsize=8)

    myX = [1,2,3,4,5,6,7,8,9,10]
    myY = makeHist(ep, myX)
    panel3.bar(myX, myY, edgecolor='black', facecolor='gray', linewidth=1)
    print(ep)
    panel3.set_ylabel('Proportion of Samples',size=8)
    panel3.set_xlabel('Equally Parsimonious Placements',size=8)
    panel3.set_xticks([1,2,3,4,5,6,7,8,9,10])
    panel3.set_xticklabels(['1','2','3','4','5','6','7','8','9','10+'])
    panel3.tick_params(bottom='on',labelbottom='on',left='on',labelleft='on',right='off',labelright='off',top='off',labeltop='off',labelsize=8) 

    plt.savefig('realHists.pdf', dpi=1300)
    plt.close()















########################
### HELPER FUNCTIONS ###
########################

def makeHist(myY, myX):
    myReturn = [0]*len(myX)
    for k in myY:
        myAdd = -1
        for i in range(0,len(myX)):
            if k >= myX[i]:
                myAdd += 1
        myReturn[myAdd] += 1
    myRealReturn = []
    for k in myReturn:
        myRealReturn.append(k/float(sum(myReturn)))
    return(myRealReturn)

def get95CI(myList, myMean):
    myReturn = []
    for i in range(0,1000):
        myReturn.append(np.mean(random.choices(myList,k=len(myList))))
    x = sorted(myReturn)
    return([myMean-x[24],x[974]-myMean])

def getColor(myDict):
    myReturn = []
    for k in myDict:
        myReturn += myDict[k]
    return(myReturn)

def makeJitterXY(myDict):
    myX, myY = [], []
    for k in myDict:
        myX += addJitter([k]*len(myDict[k]))
        myY += myDict[k]
    return(myX, myY)

def makeJitterXY2(myDict):
    myX, myY = [], []
    for k in myDict:
        myX += addJitter2([k]*len(myDict[k]))
        myY += myDict[k]
    return(myX, myY)

def myLog(myList):
    myReturn = []
    for k in myList:
        if k != 0:
            myReturn.append(np.log10(k))
    return(myReturn)

def toInt(myList):
    myReturn = []
    for k in myList:
        myReturn.append(int(k))
    return(myReturn)

def addJitter(myList):
    myReturn = []
    for k in myList:
        myXNum = k*100
        myReturn.append(random.randint(myXNum-90, myXNum+91)/100.0)
    return(myReturn)

def addJitter2(myList):
    myReturn = []
    for k in myList:
        myXNum = k*100
        myReturn.append(random.randint(myXNum-10, myXNum+11)/100.0)
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
   plotRealHists()

if __name__ == "__main__":
    """
    Calls main when program is run by user.
    """
    main();
    raise SystemExit





            






