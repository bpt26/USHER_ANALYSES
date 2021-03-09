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
        for i in ['0','10','20','30','40','50']:        
            algToDataMask[k+'-'+i] = [0,0,0]
    with open('compareSisNewMask1a.txt') as f:
        for line in f:
            splitLine = (line.strip()).split('\t')
            myType = splitLine[2]+'-'+str(splitLine[1])
            if myType in algToDataMask:
                if int(float(splitLine[5])) == 0:
                    algToDataMask[myType][0] += 1
                elif int(float(splitLine[5])) == 1:
                    algToDataMask[myType][1] += 1
                elif int(float(splitLine[5])) >= 2:
                    algToDataMask[myType][2] += 1

    for k in ['USHER','IQ','FT']:
        for i in ['2.5','5.0','7.5']:        
            algToDataMask[k+'-'+i] = [0,0,0]
    with open('compareSisNewMask1aSmallMask.txt') as f:
        for line in f:
            splitLine = (line.strip()).split('\t')
            myType = splitLine[2]+'-'+str(splitLine[1])
            if myType in algToDataMask:
                if int(float(splitLine[5])) == 0:
                    algToDataMask[myType][0] += 1
                elif int(float(splitLine[5])) == 1:
                    algToDataMask[myType][1] += 1
                elif int(float(splitLine[5])) >= 2:
                    algToDataMask[myType][2] += 1

    algToDataRand = {}
    for k in ['USHER','IQ','FT']:
        for i in ['0','10','20','30','40','50','60','70','80','90','100']:
            algToDataRand[k+'-'+i] = [0,0,0]
    with open('compareSisNewRand2a.txt') as f:
        for line in f:
            splitLine = (line.strip()).split('\t')
            myType = splitLine[2]+'-'+str(splitLine[1])
            if int(float(splitLine[5])) == 0:
                algToDataRand[myType][0] += 1
            elif int(float(splitLine[5])) == 1:
                algToDataRand[myType][1] += 1
            elif int(float(splitLine[5])) >= 2:
                algToDataRand[myType][2] += 1

    algToDataSyst = {}
    for k in ['USHER','IQ','FT']:
        for i in ['0','1','2','3','4','5','6','7','8','9','10']:
            algToDataSyst[k+'-'+i] = [0,0,0]
    with open('compareSisNewSyst3a.txt') as f:
        for line in f:
            splitLine = (line.strip()).split('\t')
            myType = splitLine[2]+'-'+str(splitLine[1])
            if int(float(splitLine[5])) == 0:
                algToDataSyst[myType][0] += 1
            elif int(float(splitLine[5])) == 1:
                algToDataSyst[myType][1] += 1
            elif int(float(splitLine[5])) >= 2:
                algToDataSyst[myType][2] += 1

    with open('compareSisNewReal.txt') as f:
        for line in f:
            splitLine = (line.strip()).split('\t')
            myType = splitLine[1]+'-'+'0'
            if int(float(splitLine[4])) == 0:
                algToDataMask[myType][0] += 1
                algToDataRand[myType][0] += 1
                algToDataSyst[myType][0] += 1
            elif int(float(splitLine[4])) == 1:
                algToDataMask[myType][1] += 1
                algToDataRand[myType][1] += 1
                algToDataSyst[myType][1] += 1
            elif int(float(splitLine[4])) >= 2:
                algToDataMask[myType][2] += 1
                algToDataRand[myType][2] += 1
                algToDataSyst[myType][2] += 1

    for k in ['USHER','IQ','FT']:
        for i in ['0','2.5','5.0','7.5','10','20','30','40','50']:
            algToDataMask[k+'-'+i] = normalise(algToDataMask[k+'-'+i])
        for i in ['0','10','20','30','40','50','60','70','80','90','100']:
            algToDataRand[k+'-'+i] = normalise(algToDataRand[k+'-'+i])
        for i in ['0','1','2','3','4','5','6','7','8','9','10']:
            algToDataSyst[k+'-'+i] = normalise(algToDataSyst[k+'-'+i])


    ##################
    ### SET PANELS ###
    ##################

    fig_width = 18
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

    ###############
    ### PANEL 1 ###
    ###############

    histData1 = []
    posList1 = []
    pos = 0
    for i in ['0','2.5','5.0','7.5','10','20','30','40','50']:
        for k in ['USHER','IQ','FT']:
            print(k, i, 'MASK', algToDataMask[k+'-'+i])
            for e in algToDataMask[k+'-'+i]:
                histData1.append(e)
                posList1.append(pos)
                pos += 1
            pos += 1

    myColors = [(0.25,0.05,0.05),(0.5,0.15,0.15),(0.75,0.25,0.25), (0.05,0.25,0.05),(0.15,0.5,0.15),(0.25,0.75,0.25), (0.05,0.05,0.25),(0.15,0.15,0.5),(0.25,0.25,0.75)]
    panel1.bar(posList1, histData1, width=0.8, align='center',edgecolor='black',color=myColors*7)
    #panel1.scatter(x=[1,2],y=[3,3],color=(0,0,0),label='0')
    #panel1.scatter(x=[1,2],y=[3,3],color=(0.5,0.5,0.5),label='1')
    #panel1.scatter(x=[1,2],y=[3,3],color=(0.95,0.95,0.95),label='2+')
    panel1.set_ylim([0.0,1.0])
    panel1.set_xticks([5,17,29,41,53,65,77,89,101])
    for k in [11,23,35,47,59,71,83,95]:
        panel1.plot([k,k],[-0.001,1.001],ls=':',c='k')
    panel1.set_xticklabels(['0','2.5','5.0','7.5','10','20','30','40','50'])
    panel1.set_ylabel('Density',size=8)
    panel1.set_xlabel('Sites Masked (%)',size=8)
    panel1.set_xlim([-1,max(posList1)+1])
    #leg = panel1.legend(loc='upper right',fontsize=7,title=' Distance From\nTrue Placement\n       (edges)')
    #leg.get_title().set_fontsize('7')
    panel1.tick_params(bottom='on',labelbottom='on',left='on',labelleft='on',right='off',labelright='off',top='off',labeltop='off',labelsize=8)


    ###############
    ### PANEL 2 ###
    ###############


    histData1 = []
    posList1 = []
    pos = 0
    for i in ['0','10','20','30','40','50','60','70','80','90','100']:
        for k in ['USHER','IQ','FT']:
            print(k, i, 'RAND', algToDataRand[k+'-'+i])
            for e in algToDataRand[k+'-'+i]:
                histData1.append(e)
                posList1.append(pos)
                pos += 1
            pos += 1

    myColors = [(0.25,0.05,0.05),(0.5,0.15,0.15),(0.75,0.25,0.25), (0.05,0.25,0.05),(0.15,0.5,0.15),(0.25,0.75,0.25), (0.05,0.05,0.25),(0.15,0.15,0.5),(0.25,0.25,0.75)]
    panel2.bar(posList1, histData1, width=0.8, align='center',edgecolor='black',color=myColors*11)
    #panel1.scatter(x=[1,2],y=[3,3],color=(0,0,0),label='0')
    #panel1.scatter(x=[1,2],y=[3,3],color=(0.5,0.5,0.5),label='1')
    #panel1.scatter(x=[1,2],y=[3,3],color=(0.95,0.95,0.95),label='2+')
    panel2.set_ylim([0.0,1.0])
    panel2.set_xticks([5,17,29,41,53,65,77,89,101,113,125])
    for k in [11,23,35,47,59,71,83,95,107,119]:
        panel2.plot([k,k],[-10,145],ls=':',c='k')
    panel2.set_xticklabels(['0','1','2','3','4','5','6','7','8','9','10'])
    panel2.set_ylabel('Density',size=8)
    panel2.set_xlabel('Random Errors Added Per Genome',size=8)
    panel2.set_xlim([-1,max(posList1)+1])
    #leg = panel1.legend(loc='upper right',fontsize=7,title=' Distance From\nTrue Placement\n       (edges)')
    #leg.get_title().set_fontsize('7')
    panel2.tick_params(bottom='on',labelbottom='on',left='on',labelleft='on',right='off',labelright='off',top='off',labeltop='off',labelsize=8)





    ###############
    ### PANEL 3 ###
    ###############


    histData1 = []
    posList1 = []
    pos = 0
    for i in ['0','1','2','3','4','5','6','7','8','9','10']:
        for k in ['USHER','IQ','FT']:
            print(k, i, 'MASK', algToDataSyst[k+'-'+i])
            for e in algToDataSyst[k+'-'+i]:
                histData1.append(e)
                posList1.append(pos)
                pos += 1
            pos += 1

    myColors = [(0.25,0.05,0.05),(0.5,0.15,0.15),(0.75,0.25,0.25), (0.05,0.25,0.05),(0.15,0.5,0.15),(0.25,0.75,0.25), (0.05,0.05,0.25),(0.15,0.15,0.5),(0.25,0.25,0.75)]
    panel3.bar(posList1, histData1, width=0.8, align='center',edgecolor='black',color=myColors*11)
    panel3.set_ylim([0.0,1.0])
    panel3.set_xticks([5,17,29,41,53,65,77,89,101,113,125])
    for k in [11,23,35,47,59,71,83,95,107,119]:
        panel3.plot([k,k],[-10,145],ls=':',c='k')
    panel3.set_xticklabels(['0','1','2','3','4','5','6','7','8','9','10'])
    panel3.set_ylabel('Density',size=8)
    panel3.set_xlabel('Lineages With Systematic Error Added',size=8)
    panel3.set_xlim([-1,max(posList1)+1])
    #leg = panel1.legend(loc='upper right',fontsize=7,title=' Distance From\nTrue Placement\n       (edges)')
    #leg.get_title().set_fontsize('7')
    panel3.tick_params(bottom='on',labelbottom='on',left='on',labelleft='on',right='off',labelright='off',top='off',labeltop='off',labelsize=8)







    plt.savefig('testHistTrueWithSmallMask.pdf', dpi=1300)
    plt.close()






##########################
#### HELPER FUNCTIONS ####
##########################

def normalise(entry):
    myReturn = [0,0,0]
    for i in range(0,len(entry)):
        myReturn[i] = float(entry[i])/float(np.sum(entry))
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
    summarizeUIF()

if __name__ == "__main__":
    """
    Calls main when program is run by user.
    """
    main();
    raise SystemExit




                    





