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
#import seaborn as sns

"""
9 panel figure:

mask1RF  mask1N1ovr  mask1N1N2-2  mask1EP

rand2RF  rand2N1ovr  rand2N1N2-2  rand2EP

syst3RF  syst3N1ovr  syst3N1N2-2  syst3EP

"""

##########################
##### MAIN FUNCTIONS #####
##########################

def plotExperiments():

    usherMaskPctToRF = {}
    iqMaskPctToRF = {}
    ftMaskPctToRF = {}
    usherRandPctToRF = {}
    iqRandPctToRF = {}
    ftRandPctToRF = {}
    usherSystPctToRF = {}
    iqSystPctToRF = {}
    ftSystPctToRF = {}

    usherRfs = []
    iqRfs = []
    ftRfs = []

    with open('usherRegRF.txt') as f:
        for line in f:
            splitLine = line.strip().split('\t')
            if not splitLine[0] == 'Replicate':
                usherRfs.append(float(splitLine[1]))

    with open('iqRegRF.txt') as f:
        for line in f:
            splitLine = line.strip().split('\t')
            if not splitLine[0] == 'Replicate':
                iqRfs.append(float(splitLine[1]))

    with open('ftRegRF.txt') as f:
        for line in f:
            splitLine = line.strip().split('\t')
            if not splitLine[0] == 'Replicate':
                ftRfs.append(float(splitLine[1]))


    usherMaskPctToRF[0] = usherRfs
    usherRandPctToRF[0] = usherRfs
    usherSystPctToRF[0] = usherRfs
    iqMaskPctToRF[0] = iqRfs
    iqRandPctToRF[0] = iqRfs
    iqSystPctToRF[0] = iqRfs
    ftMaskPctToRF[0] = ftRfs
    ftRandPctToRF[0] = ftRfs
    ftSystPctToRF[0] = ftRfs

    randomTrees = [549,604,528.5,390.5,392.5]
    
    myOutCorrs = ''

    ##############
    ### MASK 1 ###
    ##############

    with open('usherMaskRF.txt') as f:
        for line in f:
            splitLine = line.strip().split('\t')
            if splitLine[0] != 'Replicate':
                if not int(splitLine[1]) in usherMaskPctToRF:
                    usherMaskPctToRF[int(splitLine[1])] = []
                usherMaskPctToRF[int(splitLine[1])].append(float(splitLine[2]))

    with open('iqMaskRF.txt') as f:
        for line in f:
            splitLine = line.strip().split('\t')
            if splitLine[0] != 'Replicate':
                if not int(splitLine[1]) in iqMaskPctToRF:
                    iqMaskPctToRF[int(splitLine[1])] = []
                iqMaskPctToRF[int(splitLine[1])].append(float(splitLine[2]))

    with open('ftMaskRF.txt') as f:
        for line in f:
            splitLine = line.strip().split('\t')
            if splitLine[0] != 'Replicate':
                if not int(splitLine[1]) in ftMaskPctToRF:
                    ftMaskPctToRF[int(splitLine[1])] = []
                ftMaskPctToRF[int(splitLine[1])].append(float(splitLine[2]))

    with open('small_mask_results.txt') as f:
        for line in f:
            splitLine = line.strip().split('\t')
            if splitLine[0] == 'USHER':
                if not float(splitLine[2]) in usherMaskPctToRF:
                    usherMaskPctToRF[float(splitLine[2])] = []
                usherMaskPctToRF[float(splitLine[2])].append(float(splitLine[3]))
            elif splitLine[0] == 'IQ':
                if not float(splitLine[2]) in iqMaskPctToRF:
                    iqMaskPctToRF[float(splitLine[2])] = []
                iqMaskPctToRF[float(splitLine[2])].append(float(splitLine[3]))
            elif splitLine[0] == 'FT':
                if not float(splitLine[2]) in ftMaskPctToRF:
                    ftMaskPctToRF[float(splitLine[2])] = []
                ftMaskPctToRF[float(splitLine[2])].append(float(splitLine[3]))


    ##############
    ### RAND 2 ###
    ##############

    with open('usherRandRF.txt') as f:
        for line in f:
            splitLine = line.strip().split('\t')
            if splitLine[0] != 'Replicate':
                if not int(splitLine[1])/10 in usherRandPctToRF:
                    usherRandPctToRF[int(splitLine[1])/10] = []
                usherRandPctToRF[int(splitLine[1])/10].append(float(splitLine[2]))

    with open('iqRandRF.txt') as f:
        for line in f:
            splitLine = line.strip().split('\t')
            if splitLine[0] != 'Replicate':
                if not int(splitLine[1])/10 in iqRandPctToRF:
                    iqRandPctToRF[int(splitLine[1])/10] = []
                iqRandPctToRF[int(splitLine[1])/10].append(float(splitLine[2]))

    with open('ftRandRF.txt') as f:
        for line in f:
            splitLine = line.strip().split('\t')
            if splitLine[0] != 'Replicate':
                if not int(splitLine[1])/10 in ftRandPctToRF:
                    ftRandPctToRF[int(splitLine[1])/10] = []
                ftRandPctToRF[int(splitLine[1])/10].append(float(splitLine[2]))

    ##############
    ### SYST 3 ###
    ##############

    with open('usherSystRF.txt') as f:
        for line in f:
            splitLine = line.strip().split('\t')
            if str(splitLine[2]) == '1':
                if not int(splitLine[1]) in usherSystPctToRF:
                    usherSystPctToRF[int(splitLine[1])] = []
                usherSystPctToRF[int(splitLine[1])].append(float(splitLine[3]))

    with open('iqSystRF.txt') as f:
        for line in f:
            splitLine = line.strip().split('\t')
            if str(splitLine[2]) == '1':
                if not int(splitLine[1]) in iqSystPctToRF:
                    iqSystPctToRF[int(splitLine[1])] = []
                iqSystPctToRF[int(splitLine[1])].append(float(splitLine[3]))

    with open('ftSystRF.txt') as f:
        for line in f:
            splitLine = line.strip().split('\t')
            if str(splitLine[2]) == '1':
                if not int(splitLine[1]) in ftSystPctToRF:
                    ftSystPctToRF[int(splitLine[1])] = []
                ftSystPctToRF[int(splitLine[1])].append(float(splitLine[3]))

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


    ################
    ### PLOTTING ###
    ################

    myData = []
    myPos = [-3,7,17,27,37,47,57,67,77,0,10,20,30,40,50,60,70,80,3,13,23,33,43,53,63,73,83]
    for k in [0,2.5,5.0,7.5,10,20,30,40,50]:
        myData.append(np.log10(usherMaskPctToRF[k]))
        print("USHER, MASK", k, np.mean(usherMaskPctToRF[k]))
        #print('USHER/IQ MASK', k, scipy.stats.mannwhitneyu(usherMaskPctToRF[k], iqMaskPctToRF[k]), len(iqMaskPctToRF[k]))
        #print('USHER/FT MASK', k, scipy.stats.mannwhitneyu(usherMaskPctToRF[k], ftMaskPctToRF[k]), len(ftMaskPctToRF[k]))
        #print('USHER/IQ MASK', k, np.mean(usherMaskPctToRF[k]), np.mean(iqMaskPctToRF[k]), str((np.mean(usherMaskPctToRF[k])-np.mean(iqMaskPctToRF[k]))/np.mean(usherMaskPctToRF[k])*100.0)+'%')
        #print('USHER/FT MASK', k, np.mean(usherMaskPctToRF[k]), np.mean(ftMaskPctToRF[k]), str((np.mean(usherMaskPctToRF[k])-np.mean(ftMaskPctToRF[k]))/np.mean(usherMaskPctToRF[k])*100.0)+'%')
        #myPos.append(k-3)
    for k in [0,2.5,5.0,7.5,10,20,30,40,50]:
        myData.append(np.log10(iqMaskPctToRF[k]))
        print("IQ, MASK", k, np.mean(iqMaskPctToRF[k]))
        #myPos.append(k)
    for k in [0,2.5,5.0,7.5,10,20,30,40,50]:
        myData.append(np.log10(ftMaskPctToRF[k]))
        print("FT, MASK", k, np.mean(ftMaskPctToRF[k]))
        #myPos.append(k+3)
    panel1.boxplot(x=myData[:9],positions=myPos[:9],widths=2,showfliers=False,medianprops={'color':'blue'},boxprops={'color':'blue'},whiskerprops={'color':'blue'},capprops={'color':'blue'})
    panel1.boxplot(x=myData[9:18],positions=myPos[9:18], widths=2, showfliers=False, medianprops={'color':'orange'}, boxprops={'color':'orange'},whiskerprops={'color':'orange'},capprops={'color':'orange'})
    panel1.boxplot(x=myData[18:], positions=myPos[18:], widths=2, showfliers=False, medianprops={'color':'purple'}, boxprops={'color':'purple'},whiskerprops={'color':'purple'},capprops={'color':'purple'})
    panel1.boxplot(x=np.log10(randomTrees), positions=[myPos[-1]+4], widths=2, showfliers=False, medianprops={'color':'black'}, boxprops={'color':'black'},whiskerprops={'color':'black'},capprops={'color':'black'})
    panel1.set_xlim([-5.5,85.5+4])
    panel1.set_xlabel('Sites Masked (%)',size=8)
    panel1.set_ylabel('Robinson-Foulds Distance to Reference',size=8)
    for k in [5,15,25,35,45,55,65,75,85]:
        panel1.plot([k,k],[-10,800],ls=':',c='k')
    panel1.set_ylim([np.log10(25),np.log10(624)])
    panel1.set_xticks([0,10,20,30,40,50,60,70,80])
    panel1.set_xticklabels(['0','2.5','5','7.5','10','20','30','40','50'])
    panel1.set_yticks([np.log10(25.0),np.log10(100.0),np.log10(200.0),np.log10(300.0),np.log10(400.0),np.log10(500.0),np.log10(600.0)])
    panel1.set_yticklabels(['25','100','200','300','400','500','600'])
    panel1.tick_params(bottom='on',labelbottom='on',left='on',labelleft='on',right='off',labelright='off',top='off',labeltop='off',labelsize=8)
    print("RANDOM TREES,", np.mean(randomTrees))


    myData = []
    myPos = []
    for k in sorted(usherRandPctToRF.keys()):
        myData.append(np.log10(usherRandPctToRF[k]))
        #print('USHER/IQ RAND', k, scipy.stats.mannwhitneyu(usherRandPctToRF[k], iqRandPctToRF[k]), len(iqRandPctToRF[k]))
        #print('USHER/FT RAND', k, scipy.stats.mannwhitneyu(usherRandPctToRF[k], ftRandPctToRF[k]), len(ftRandPctToRF[k]))
        #print('USHER/IQ RAND', k, np.mean(usherRandPctToRF[k]), np.mean(iqRandPctToRF[k]), str((np.mean(usherRandPctToRF[k])-np.mean(iqRandPctToRF[k]))/np.mean(usherRandPctToRF[k])*100.0)+'%')
        #print('USHER/FT RAND', k, np.mean(usherRandPctToRF[k]), np.mean(ftRandPctToRF[k]), str((np.mean(usherRandPctToRF[k])-np.mean(ftRandPctToRF[k]))/np.mean(usherRandPctToRF[k])*100.0)+'%')
        myPos.append(k-0.3)
    for k in sorted(iqRandPctToRF.keys()):
        myData.append(np.log10(iqRandPctToRF[k]))
        myPos.append(k)
    for k in sorted(ftRandPctToRF.keys()):
        myData.append(np.log10(ftRandPctToRF[k]))
        myPos.append(k+0.3)
    panel2.boxplot(x=myData[:11],positions=myPos[:11],widths=0.2,showfliers=False,medianprops={'color':'blue'},boxprops={'color':'blue'},whiskerprops={'color':'blue'},capprops={'color':'blue'})
    panel2.boxplot(x=myData[11:22],positions=myPos[11:22],widths=0.2,showfliers=False,medianprops={'color':'orange'}, boxprops={'color':'orange'},whiskerprops={'color':'orange'},capprops={'color':'orange'})
    panel2.boxplot(x=myData[22:],positions=myPos[22:],widths=0.2,showfliers=False,medianprops={'color':'purple'}, boxprops={'color':'purple'},whiskerprops={'color':'purple'},capprops={'color':'purple'})
    panel2.boxplot(x=np.log10(randomTrees), positions=[myPos[-1]+0.4], widths=0.2, showfliers=False, medianprops={'color':'black'}, boxprops={'color':'black'},whiskerprops={'color':'black'},capprops={'color':'black'})
    panel2.set_xlim([-0.7,10.7+0.2])
    panel2.set_xlabel('Random Errors Added Per Genome',size=8)
    panel2.set_ylabel('Robinson-Foulds Distance to Reference',size=8)
    for k in [0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5]:
        panel2.plot([k,k],[-10,800],ls=':',c='k')
    panel2.set_ylim([np.log10(25),np.log10(624)])
    panel2.set_xticks([0,1,2,3,4,5,6,7,8,9,10])
    panel2.set_xticklabels(['0','1','2','3','4','5','6','7','8','9','10'])
    panel2.set_yticks([np.log10(25),np.log10(100.0),np.log10(200.0),np.log10(300.0),np.log10(400.0),np.log10(500.0),np.log10(600.0)])
    panel2.set_yticklabels(['25','100','200','300','400','500','600'])
    panel2.tick_params(bottom='on',labelbottom='on',left='on',labelleft='on',right='off',labelright='off',top='off',labeltop='off',labelsize=8)




    myData = []
    myPos = []
    for k in sorted(usherSystPctToRF.keys()):
        myData.append(np.log10(usherSystPctToRF[k]))
        #print('USHER/IQ SYST', k, scipy.stats.mannwhitneyu(usherSystPctToRF[k], iqSystPctToRF[k]), len(iqSystPctToRF[k]))
        #print('USHER/FT SYST', k, scipy.stats.mannwhitneyu(usherSystPctToRF[k], ftSystPctToRF[k]), len(ftSystPctToRF[k]))
        #print('USHER/IQ SYST', k, np.mean(usherSystPctToRF[k]), np.mean(iqSystPctToRF[k]), str((np.mean(usherSystPctToRF[k])-np.mean(iqSystPctToRF[k]))/np.mean(usherSystPctToRF[k])*100.0)+'%')
        #print('USHER/FT SYST', k, np.mean(usherSystPctToRF[k]), np.mean(ftSystPctToRF[k]), str((np.mean(usherSystPctToRF[k])-np.mean(ftSystPctToRF[k]))/np.mean(usherSystPctToRF[k])*100.0)+'%')
        myPos.append(k-0.3)
    for k in sorted(iqSystPctToRF.keys()):
        myData.append(np.log10(iqSystPctToRF[k]))
        myPos.append(k)
    for k in sorted(ftSystPctToRF.keys()):
        myData.append(np.log10(ftSystPctToRF[k]))
        myPos.append(k+0.3)
    panel3.boxplot(x=myData[:11],positions=myPos[:11],widths=0.2,showfliers=False,medianprops={'color':'blue'},boxprops={'color':'blue'},whiskerprops={'color':'blue'},capprops={'color':'blue'})
    panel3.boxplot(x=myData[11:22],positions=myPos[11:22],widths=0.2,showfliers=False,medianprops={'color':'orange'}, boxprops={'color':'orange'},whiskerprops={'color':'orange'},capprops={'color':'orange'})
    panel3.boxplot(x=myData[22:],positions=myPos[22:],widths=0.2,showfliers=False,medianprops={'color':'purple'}, boxprops={'color':'purple'},whiskerprops={'color':'purple'},capprops={'color':'purple'})
    panel3.boxplot(x=np.log10(randomTrees), positions=[myPos[-1]+0.4], widths=0.2, showfliers=False, medianprops={'color':'black'}, boxprops={'color':'black'},whiskerprops={'color':'black'},capprops={'color':'black'})
    panel3.set_xlim([-0.7,10.7+0.2])
    panel3.set_xlabel('Lineages With Systematic Error Added',size=8)
    panel3.set_ylabel('Robinson-Foulds Distance to Reference',size=8)
    for k in [0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5]:
        panel3.plot([k,k],[-10,800],ls=':',c='k')
    panel3.set_ylim([np.log10(50),np.log10(624)])
    panel3.set_xticks([0,1,2,3,4,5,6,7,8,9,10])
    panel3.set_xticklabels(['0','1','2','3','4','5','6','7','8','9','10'])
    panel3.set_yticks([np.log10(25),np.log10(100.0),np.log10(200.0),np.log10(300.0),np.log10(400.0),np.log10(500.0),np.log10(600.0)])
    panel3.set_yticklabels(['25','100','200','300','400','500','600'])
    panel3.tick_params(bottom='on',labelbottom='on',left='on',labelleft='on',right='off',labelright='off',top='off',labeltop='off',labelsize=8)


    plt.savefig('combinedUsherIqBoxplotsTestIncludingSmallMaskTest.pdf', dpi=1300)
    plt.close()




########################
### HELPER FUNCTIONS ###
########################

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
    return('\t'.join(newList))

def joinerC(entry):
    newList = []
    for k in entry:
        newList.append(str(k))
    return(','.join(newList))

#######################
#### FUNCTION CALL ####
#######################

def main():
   plotExperiments()

if __name__ == "__main__":
    """
    Calls main when program is run by user.
    """
    main();
    raise SystemExit





            






