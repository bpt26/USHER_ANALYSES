#!/usr/bin/env python3
# Name: Bryan Thornlow
# Date: 2/1/2018
# compareDatabases.py

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
import seaborn as sns


##########################
##### MAIN FUNCTIONS #####
##########################

def summarizeUIF():
    algToDataMask = {}
    for k in ['USHER','IQ','FT']:
        for i in ['0','10','20','30']:        
            algToDataMask[k+'-'+i] = [0,0,0]
    with open('compareSisNewMask1a.txt') as f:
        for line in f:
            splitLine = (line.strip()).split('\t')
            myType = splitLine[2]+'-'+str(splitLine[1])
            if myType in algToDataMask:
                if int(splitLine[5]) == 0:
                    algToDataMask[myType][0] += 1
                elif int(splitLine[5]) == 1:
                    algToDataMask[myType][1] += 1
                elif int(splitLine[5]) >= 2:
                    algToDataMask[myType][2] += 1

    algToDataRand = {}
    for k in ['USHER','IQ','FT']:
        for i in ['0','10','20','30','40','50','60','70','80','90','100']:
            algToDataRand[k+'-'+i] = [0,0,0]
    with open('compareSisNewRand2a.txt') as f:
        for line in f:
            splitLine = (line.strip()).split('\t')
            myType = splitLine[2]+'-'+str(splitLine[1])
            if int(splitLine[5]) == 0:
                algToDataRand[myType][0] += 1
            elif int(splitLine[5]) == 1:
                algToDataRand[myType][1] += 1
            elif int(splitLine[5]) >= 2:
                algToDataRand[myType][2] += 1

    algToDataSyst = {}
    for k in ['USHER','IQ','FT']:
        for i in ['0','1','2','3','4','5','6','7','8','9','10']:
            algToDataSyst[k+'-'+i] = [0,0,0]
    with open('compareSisNewSyst3a.txt') as f:
        for line in f:
            splitLine = (line.strip()).split('\t')
            myType = splitLine[2]+'-'+str(splitLine[1])
            if int(splitLine[5]) == 0:
                algToDataSyst[myType][0] += 1
            elif int(splitLine[5]) == 1:
                algToDataSyst[myType][1] += 1
            elif int(splitLine[5]) >= 2:
                algToDataSyst[myType][2] += 1

    with open('compareSisNewReal.txt') as f:
        for line in f:
            splitLine = (line.strip()).split('\t')
            myType = splitLine[1]+'-'+'0'
            if int(splitLine[4]) == 0:
                algToDataMask[myType][0] += 1
                algToDataRand[myType][0] += 1
                algToDataSyst[myType][0] += 1
            elif int(splitLine[4]) == 1:
                algToDataMask[myType][1] += 1
                algToDataRand[myType][1] += 1
                algToDataSyst[myType][1] += 1
            elif int(splitLine[4]) >= 2:
                algToDataMask[myType][2] += 1
                algToDataRand[myType][2] += 1
                algToDataSyst[myType][2] += 1

    for k in ['USHER','IQ','FT']:
        for i in ['0','10','20','30']:
            algToDataMask[k+'-'+i] = normalise(algToDataMask[k+'-'+i])
        for i in ['0','10','20','30','40','50','60','70','80','90','100']:
            algToDataRand[k+'-'+i] = normalise(algToDataRand[k+'-'+i])
        for i in ['0','1','2','3','4','5','6','7','8','9','10']:
            algToDataSyst[k+'-'+i] = normalise(algToDataSyst[k+'-'+i])


    ##################
    ### SET PANELS ###
    ##################

    fig_width = 6
    fig_height = 10
    panel_width = 0.8
    panel_height = 0.75/3
    panel_total_height = (panel_height*3)
    panel_total_width = (panel_width*1)
    extra_y_space = 1 - panel_total_height
    extra_x_space = 1 - panel_total_width
    above_below = extra_y_space/4
    left_right = extra_x_space/2

    plt.figure(figsize=(fig_width, fig_height))
    panel1 = plt.axes([(left_right*1)+(panel_width*0), (above_below*3)+(panel_height*2), panel_width, panel_height], frameon=True)
    panel2 = plt.axes([(left_right*1)+(panel_width*0), (above_below*2)+(panel_height*1), panel_width, panel_height], frameon=True)
    panel3 = plt.axes([(left_right*1)+(panel_width*0), (above_below*1)+(panel_height*0), panel_width, panel_height], frameon=True)

    histData1 = []
    posList1 = []
    pos = 0
    for i in ['0','10','20','30']:
        for k in ['USHER','IQ','FT']:
            for e in algToDataMask[k+'-'+i]:
                histData1.append(e)
                posList1.append(pos)
                pos += 1
            pos += 1
    myColors = [(0.25,0.05,0.05),(0.5,0.15,0.15),(0.75,0.25,0.25), (0.05,0.25,0.05),(0.15,0.5,0.15),(0.25,0.75,0.25), (0.05,0.05,0.25),(0.15,0.15,0.5),(0.25,0.25,0.75)]
    panel1.bar(posList1, histData1, width=0.8, align='center',edgecolor='black',color=myColors*4)
    panel1.set_xticks([1, 5, 9, 13, 17, 21])
    panel1.scatter(x=[1,2],y=[3,3],color=(0,0,0),label='0')
    panel1.scatter(x=[1,2],y=[3,3],color=(0.5,0.5,0.5),label='1')
    panel1.scatter(x=[1,2],y=[3,3],color=(0.95,0.95,0.95),label='2+')
    panel1.set_ylim([0.0,1.0])
    #panel1.set_xticklabels(['0','10','20','30'])
    panel1.set_ylabel('Density',size=8)
    panel1.set_xlabel('Sites Masked (%)',size=8)
    leg = panel1.legend(loc='upper right',fontsize=7,title=' Distance From\nTrue Placement\n       (edges)')
    leg.get_title().set_fontsize('7')
    panel1.tick_params(bottom='on',labelbottom='on',left='on',labelleft='on',right='off',labelright='off',top='off',labeltop='off',labelsize=8)

    plt.savefig('testHistTrue.pdf', dpi=1300)
    plt.close()







##########################
#### HELPER FUNCTIONS ####
##########################

def normalise(entry):
    myReturn = [0,0,0]
    for i in range(0,len(entry)):
        myReturn[i] = float(i)/float(np.sum(entry))
    return(myReturn)

def getOverlap(list1, list2):
    myReturn = 0
    for k in list1:
        if k in list2:
            myReturn+= 1
    if myReturn == min(len(list1.keys()), len(list2.keys())):
        return(1)
    else:
        return(0)

def joinerN(entry):
    newList = []
    for k in entry:
        newList.append(str(k))
    return '\n'.join(newList)

def joiner(entry):
    newList = []
    for k in entry:
        newList.append(str(k))
    return '\t'.join(newList)


def main():
    parseCompareNew()

if __name__ == "__main__":
    """
    Calls main when program is run by user.
    """
    main();
    raise SystemExit




                    





