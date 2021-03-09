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
import seaborn as sns

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

    maskPctToRF = {}
    maskPctToN1Ovr = {}
    maskPctToNStat = {}
    maskPctToEP = {}

    randPctToRF = {}
    randPctToN1Ovr = {}
    randPctToNStat = {}
    randPctToEP = {}

    systPctToRF = {}
    systPctToN1Ovr = {}
    systPctToNStat = {}
    systPctToEP = {}

    systPctToRF2 = {}
    systPctToN1Ovr2 = {}
    systPctToNStat2 = {}
    systPctToEP2 = {}

    rfs = []
    n1ovr = []
    nstat = []
    ep = []

    with open('regRF.txt') as f:
        for line in f:
            splitLine = line.strip().split('\t')
            if not splitLine[0] == 'Replicate':
                rfs.append(float(splitLine[1]))

    pars1 = {}
    with open('REG_LOGS.txt') as f:
        for line in f:
            splitLine = line.strip().split('\t')
            ep.append(int(splitLine[2]))
            if int(splitLine[2]) == 1:
                pars1[str(splitLine[0])+':'+str(splitLine[1])] = True

    pars1id = 0.0
    pars1total = 0.0
    with open('compareSisNew0.txt') as f:
        for line in f:
            splitLine = line.strip().split('\t')
            n1ovr.append(int(splitLine[2]))
            nstat.append(float(splitLine[3]))
            if str(splitLine[0])+':'+str(splitLine[1]) in pars1:
                pars1total += 1.0
                if int(splitLine[2]) == 1:
                    pars1id += 1.0
    print("pars1: "+str(pars1id)+' / '+str(pars1total)+' = '+str(pars1id/pars1total))

    randomAddRF = []
    with open('randomlyAddedRF.txt') as f:
        for line in f:
            splitLine = (line.strip()).split('\t')
            randomAddRF.append(float(splitLine[3]))

    maskPctToRF[0] = rfs
    randPctToRF[0] = rfs
    systPctToRF[0] = rfs
    systPctToRF2[0] = rfs
    maskPctToN1Ovr[0] = n1ovr
    randPctToN1Ovr[0] = n1ovr
    systPctToN1Ovr[0] = n1ovr
    systPctToN1Ovr2[0] = n1ovr
    maskPctToNStat[0] = nstat
    randPctToNStat[0] = nstat
    systPctToNStat[0] = nstat
    systPctToNStat2[0] = nstat
    maskPctToEP[0] = ep
    randPctToEP[0] = ep
    systPctToEP[0] = ep
    systPctToEP2[0] = ep

    ##############
    ### MASK 1 ###
    ##############

    with open('maskRF.txt') as f:
        for line in f:
            splitLine = line.strip().split('\t')
            if splitLine[0] != 'Replicate':
                if not int(splitLine[1]) in maskPctToRF:
                    maskPctToRF[int(splitLine[1])] = []
                maskPctToRF[int(splitLine[1])].append(float(splitLine[2]))

    with open('MASK_LOGS.txt') as f:
        for line in f:
            splitLine = line.strip().split('\t')
            if not int(splitLine[1]) in maskPctToEP:
                maskPctToEP[int(splitLine[1])] = []
            maskPctToEP[int(splitLine[1])].append(int(splitLine[3]))

    with open('compareSisNew1.txt')as f:
        for line in f:
            splitLine = line.strip().split('\t')
            if not int(splitLine[1]) in maskPctToNStat:
                maskPctToN1Ovr[int(splitLine[1])] = []
                maskPctToNStat[int(splitLine[1])] = []
            maskPctToN1Ovr[int(splitLine[1])].append(int(splitLine[3]))
            maskPctToNStat[int(splitLine[1])].append(float(splitLine[4]))

    ##############
    ### RAND 2 ###
    ##############

    with open('randRF.txt') as f:
        for line in f:
            splitLine = line.strip().split('\t')
            if splitLine[0] != 'Replicate':
                if not int(splitLine[1])/10 in randPctToRF:
                    randPctToRF[int(splitLine[1])/10] = []
                randPctToRF[int(splitLine[1])/10].append(float(splitLine[2]))

    with open('RAND_LOGS.txt') as f:
        for line in f:
            splitLine = line.strip().split('\t')
            if not int(splitLine[1])/10 in randPctToEP:
                randPctToEP[int(splitLine[1])/10] = []
            randPctToEP[int(splitLine[1])/10].append(int(splitLine[3]))

    with open('compareSisNew2.txt') as f:
        for line in f:
            splitLine = line.strip().split('\t')
            if not int(splitLine[1])/10 in randPctToNStat:
                randPctToN1Ovr[int(splitLine[1])/10] = []
                randPctToNStat[int(splitLine[1])/10] = []
            randPctToN1Ovr[int(splitLine[1])/10].append(int(splitLine[3]))
            randPctToNStat[int(splitLine[1])/10].append(float(splitLine[4]))

    ##############
    ### SYST 3 ###
    ##############

    with open('systRF.txt') as f:
        for line in f:
            splitLine = line.strip().split('\t')
            if str(splitLine[2]) == '1':
                if not int(splitLine[1]) in systPctToRF:
                    systPctToRF[int(splitLine[1])] = []
                systPctToRF[int(splitLine[1])].append(float(splitLine[3]))
            if str(splitLine[2]) == '2':
                if not int(splitLine[1]) in systPctToRF2:
                    systPctToRF2[int(splitLine[1])] = []
                systPctToRF2[int(splitLine[1])].append(float(splitLine[3]))

    with open('SYST_LOGS.txt') as f:
        for line in f:
            splitLine = line.strip().split('\t')
            if str(splitLine[2]) == '1':
                if not int(splitLine[1]) in systPctToEP:
                    systPctToEP[int(splitLine[1])] = []
                systPctToEP[int(splitLine[1])].append(int(splitLine[4]))
            elif str(splitLine[2]) == '2':
                if not int(splitLine[1]) in systPctToEP2:
                    systPctToEP2[int(splitLine[1])] = []
                systPctToEP2[int(splitLine[1])].append(int(splitLine[4]))

    with open('compareSisNew3.txt') as f:
        for line in f:
            splitLine = line.strip().split('\t')
            if str(splitLine[2]) == '1':
                if not int(splitLine[1]) in systPctToNStat:
                    systPctToN1Ovr[int(splitLine[1])] = []
                    systPctToNStat[int(splitLine[1])] = []
                systPctToN1Ovr[int(splitLine[1])].append(int(splitLine[4]))
                systPctToNStat[int(splitLine[1])].append(float(splitLine[5]))
            elif str(splitLine[2]) == '2':
                if not int(splitLine[1]) in systPctToNStat2:
                    systPctToN1Ovr2[int(splitLine[1])] = []
                    systPctToNStat2[int(splitLine[1])] = []
                systPctToN1Ovr2[int(splitLine[1])].append(int(splitLine[4]))
                systPctToNStat2[int(splitLine[1])].append(float(splitLine[5]))

    ##################
    ### SET PANELS ###
    ##################

    fig_width = 13
    fig_height = 14
    panel_width = 0.75/4
    panel_height = 0.75/4
    panel_total_height = (panel_height*4)
    panel_total_width = (panel_width*4)
    extra_y_space = 1 - panel_total_height
    extra_x_space = 1 - panel_total_width
    above_below = extra_y_space/5
    left_right = extra_x_space/5

    plt.figure(figsize=(fig_width, fig_height))
    panel1 = plt.axes([(left_right*1)+(panel_width*0), (above_below*4)+(panel_height*3), panel_width, panel_height], frameon=True)
    panel2 = plt.axes([(left_right*2)+(panel_width*1), (above_below*4)+(panel_height*3), panel_width, panel_height], frameon=True)
    panel3 = plt.axes([(left_right*3)+(panel_width*2), (above_below*4)+(panel_height*3), panel_width, panel_height], frameon=True)
    panel4 = plt.axes([(left_right*4)+(panel_width*3), (above_below*4)+(panel_height*3), panel_width, panel_height], frameon=True)

    panel5 = plt.axes([(left_right*1)+(panel_width*0), (above_below*3)+(panel_height*2), panel_width, panel_height], frameon=True)
    panel6 = plt.axes([(left_right*2)+(panel_width*1), (above_below*3)+(panel_height*2), panel_width, panel_height], frameon=True)
    panel7 = plt.axes([(left_right*3)+(panel_width*2), (above_below*3)+(panel_height*2), panel_width, panel_height], frameon=True)
    panel8 = plt.axes([(left_right*4)+(panel_width*3), (above_below*3)+(panel_height*2), panel_width, panel_height], frameon=True)

    panel9 = plt.axes([(left_right*1)+(panel_width*0), (above_below*2)+(panel_height*1), panel_width, panel_height], frameon=True)
    panel10 = plt.axes([(left_right*2)+(panel_width*1), (above_below*2)+(panel_height*1), panel_width, panel_height], frameon=True)
    panel11 = plt.axes([(left_right*3)+(panel_width*2), (above_below*2)+(panel_height*1), panel_width, panel_height], frameon=True)
    panel12 = plt.axes([(left_right*4)+(panel_width*3), (above_below*2)+(panel_height*1), panel_width, panel_height], frameon=True)

    panel13 = plt.axes([(left_right*1)+(panel_width*0), (above_below*1)+(panel_height*0), panel_width, panel_height], frameon=True)
    panel14 = plt.axes([(left_right*2)+(panel_width*1), (above_below*1)+(panel_height*0), panel_width, panel_height], frameon=True)
    panel15 = plt.axes([(left_right*3)+(panel_width*2), (above_below*1)+(panel_height*0), panel_width, panel_height], frameon=True)
    panel16 = plt.axes([(left_right*4)+(panel_width*3), (above_below*1)+(panel_height*0), panel_width, panel_height], frameon=True)


    ################
    ### PLOTTING ###
    ################

    ##########
    ## MASK ##
    ##########

    myData = []
    myPos = []
    for k in sorted(maskPctToRF.keys()):
        myData.append(maskPctToRF[k])
        myPos.append(k)
    myData.append(randomAddRF)
    myPos.append(60)
    panel1.boxplot(x=myData,positions=myPos,widths=5.0,showfliers=False,medianprops={'color':'black'})
    #panel1.plot([-10,60],[1701.925,1701.925],c='black',ls=':')
    panel1.set_xlim([-5,65])
    panel1.set_xticks([0,10,20,30,40,50])
    panel1.set_ylim([-3,52])
    panel1.plot([55,55],[-10,100],ls=':',color='black')
    panel1.set_xlabel('Sites Masked (%)',size=8)
    panel1.set_ylabel('Robinson-Foulds Distance to Reference',size=8)
    panel1.tick_params(bottom='on',labelbottom='on',left='on',labelleft='on',right='off',labelright='off',top='off',labeltop='off',labelsize=8)

    myData = []
    myPos = []
    myErr = [[],[]]
    for k in sorted(maskPctToN1Ovr.keys()):
        myData.append([np.mean(maskPctToN1Ovr[k])])
        myCI = get95CI(maskPctToN1Ovr[k], np.mean(maskPctToN1Ovr[k]))
        myErr[0].append(myCI[0])
        myErr[1].append(myCI[1])
        myPos.append(k)
    panel2.errorbar(x=myPos,y=myData,yerr=myErr,color='black',fmt='o')
    panel2.set_xlim([-5,55])
    panel2.set_ylim([0,1.0])
    panel2.set_xlabel('Sites Masked (%)',size=8)
    panel2.set_ylabel('Sister Node Sets Identical To Reference (%)',size=8)
    panel2.tick_params(bottom='on',labelbottom='on',left='on',labelleft='on',right='off',labelright='off',top='off',labeltop='off',labelsize=8)


    myData = []
    myPos = []
    for k in sorted(maskPctToNStat.keys()):
        myData.append(maskPctToNStat[k])
        myPos.append(k)
    histData = []
    for i in [0,1,2,3,4,5]:
        histData.append(myData[i].count(0.0)/float(len(myData[i])))
        histData.append(myData[i].count(1.0)/float(len(myData[i])))
        histData.append((len(myData[i])-(myData[i].count(0.0)+myData[i].count(1.0)))/float(len(myData[i])))
    myX = [0,1,2, 4,5,6, 8,9,10, 12,13,14, 16,17,18, 20,21,22]
    panel3.bar(myX, histData, width=0.8, align='center',edgecolor='black',color=[(0,0,0),(0.5,0.5,0.5),(0.95,0.95,0.95)]*6)
    panel3.set_xticks([1, 5, 9, 13, 17, 21])
    panel3.scatter(x=[1,2],y=[3,3],color=(0,0,0),label='0')
    panel3.scatter(x=[1,2],y=[3,3],color=(0.5,0.5,0.5),label='1')
    panel3.scatter(x=[1,2],y=[3,3],color=(0.95,0.95,0.95),label='2+')
    panel3.set_ylim([0.0,1.0])
    panel3.set_xticklabels(['0','10','20','30','40','50'])
    panel3.set_ylabel('Density',size=8)
    panel3.set_xlabel('Sites Masked (%)',size=8)
    #leg = panel3.legend(loc='upper right',fontsize=7,title=' Distance From\nTrue Placement\n       (edges)')
    #leg.get_title().set_fontsize('7')
    panel3.tick_params(bottom='on',labelbottom='on',left='on',labelleft='on',right='off',labelright='off',top='off',labeltop='off',labelsize=8)

    myData = []
    myPos = []
    for k in sorted(maskPctToEP.keys()):
        myData.append(maskPctToEP[k])
        myPos.append(k)
    histData = []
    for i in [0,1,2,3,4,5]:
        histData.append(myData[i].count(1)/float(len(myData[i])))
        histData.append(myData[i].count(2)/float(len(myData[i])))
        histData.append((len(myData[i])-(myData[i].count(1)+myData[i].count(2)))/float(len(myData[i])))
    myX = [0,1,2, 4,5,6, 8,9,10, 12,13,14, 16,17,18, 20,21,22]
    panel4.bar(myX, histData, width=0.8, align='center',edgecolor='black',color=[(0,0,0),(0.5,0.5,0.5),(0.95,0.95,0.95)]*6)
    panel4.set_xticks([1, 5, 9, 13, 17, 21])
    panel4.scatter(x=[1,2],y=[3,3],color=(0,0,0),label='1')
    panel4.scatter(x=[1,2],y=[3,3],color=(0.5,0.5,0.5),label='2')
    panel4.scatter(x=[1,2],y=[3,3],color=(0.95,0.95,0.95),label='3+')
    panel4.set_ylim([0.0,1.0])
    #leg = panel4.legend(loc='upper right',fontsize=7,title='     Equally\nParsimonious\n  Placements')
    #leg.get_title().set_fontsize('7')
    panel4.set_xticklabels(['0','10','20','30','40','50'])
    panel4.set_ylabel('Density',size=8)
    panel4.set_xlabel('Sites Masked (%)',size=8)
    panel4.tick_params(bottom='on',labelbottom='on',left='on',labelleft='on',right='off',labelright='off',top='off',labeltop='off',labelsize=8)

    ##########
    ## RAND ##
    ##########

    myData = []
    myPos = []
    for k in sorted(randPctToRF.keys()):
        myData.append(randPctToRF[k])
        myPos.append(k)
    myData.append(randomAddRF)
    myPos.append(11)
    panel5.boxplot(x=myData,positions=myPos,widths=0.5,showfliers=False,medianprops={'color':'black'})
    #panel5.plot([-10,60],[1701.925,1701.925],c='black',ls=':')
    panel5.set_xticks([0,1,2,3,4,5,6,7,8,9,10])
    panel5.set_xlim([-0.5,11.5])
    panel5.set_ylim([-3,52])
    panel5.plot([10.5,10.5],[-10,100],ls=':',color='black')
    panel5.set_xlabel('Random Errors Added Per Genome',size=8)
    panel5.set_ylabel('Robinson-Foulds Distance to Reference',size=8)
    panel5.tick_params(bottom='on',labelbottom='on',left='on',labelleft='on',right='off',labelright='off',top='off',labeltop='off',labelsize=8)

    myData = []
    myPos = []
    myErr = [[],[]]
    for k in sorted(randPctToN1Ovr.keys()):
        myData.append([np.mean(randPctToN1Ovr[k])])
        myCI = get95CI(randPctToN1Ovr[k], np.mean(randPctToN1Ovr[k]))
        myErr[0].append(myCI[0])
        myErr[1].append(myCI[1])
        myPos.append(k)
    panel6.errorbar(x=myPos,y=myData,yerr=myErr,color='black',fmt='o')
    panel6.set_xlim([-0.5,10.5])
    panel6.set_ylim([0,1.0])
    panel6.set_xlabel('Random Errors Added Per Genome',size=8)
    panel6.set_ylabel('Sister Node Sets Identical To Reference (%)',size=8)
    panel6.tick_params(bottom='on',labelbottom='on',left='on',labelleft='on',right='off',labelright='off',top='off',labeltop='off',labelsize=8)

    myData = []
    myPos = []
    for k in sorted(randPctToNStat.keys()):
        myData.append(randPctToNStat[k])
        myPos.append(k)
    histData = []
    for i in [0,2,4,6,8,10]:
        histData.append(myData[i].count(0.0)/float(len(myData[i])))
        histData.append(myData[i].count(1.0)/float(len(myData[i])))
        histData.append((len(myData[i])-(myData[i].count(0.0)+myData[i].count(1.0)))/float(len(myData[i])))
    myX = [0,1,2, 4,5,6, 8,9,10, 12,13,14, 16,17,18, 20,21,22]
    panel7.bar(myX, histData, width=0.8, align='center',edgecolor='black',color=[(0,0,0),(0.5,0.5,0.5),(0.95,0.95,0.95)]*6)
    panel7.set_xticks([1, 5, 9, 13, 17, 21])
    panel7.set_xticklabels(['0','2','4','6','8','10'])
    panel7.scatter(x=[1,2],y=[3,3],color=(0,0,0),label='0')
    panel7.scatter(x=[1,2],y=[3,3],color=(0.5,0.5,0.5),label='1')
    panel7.scatter(x=[1,2],y=[3,3],color=(0.95,0.95,0.95),label='2+')
    panel7.set_ylim([0.0,1.0])
    #leg = panel7.legend(loc='upper right',fontsize=7,title=' Distance From\nTrue Placement\n       (edges)')
    #leg.get_title().set_fontsize('7')
    #panel7.plot([-10,60],[11.14924347,11.14924347],c='black',ls=':')
    #panel7.set_xlim([-0.5,10.5])
    panel7.set_ylabel('Density',size=8)
    panel7.set_xlabel('Random Errors Added Per Genome',size=8)
    panel7.tick_params(bottom='on',labelbottom='on',left='on',labelleft='on',right='off',labelright='off',top='off',labeltop='off',labelsize=8)

    myData = []
    myPos = []
    for k in sorted(randPctToEP.keys()):
        myData.append(randPctToEP[k])
        myPos.append(k)
    histData = []
    for i in [0,2,4,6,8,10]:
        histData.append(myData[i].count(1)/float(len(myData[i])))
        histData.append(myData[i].count(2)/float(len(myData[i])))
        histData.append((len(myData[i])-(myData[i].count(1)+myData[i].count(2)))/float(len(myData[i])))
    myX = [0,1,2, 4,5,6, 8,9,10, 12,13,14, 16,17,18, 20,21,22]
    panel8.bar(myX, histData, width=0.8, align='center',edgecolor='black',color=[(0,0,0),(0.5,0.5,0.5),(0.95,0.95,0.95)]*6)
    panel8.set_xticks([1, 5, 9, 13, 17, 21])
    panel8.set_xticklabels(['0','2','4','6','8','10'])
    panel8.scatter(x=[1,2],y=[3,3],color=(0,0,0),label='1')
    panel8.scatter(x=[1,2],y=[3,3],color=(0.5,0.5,0.5),label='2')
    panel8.scatter(x=[1,2],y=[3,3],color=(0.95,0.95,0.95),label='3+')
    panel8.set_ylim([0.0,1.0])
    #leg = panel8.legend(loc='upper right',fontsize=7,title='     Equally\nParsimonious\n  Placements')
    #leg.get_title().set_fontsize('7')
    panel8.set_ylabel('Density',size=8)
    panel8.set_xlabel('Random Errors Added Per Genome',size=8)
    panel8.tick_params(bottom='on',labelbottom='on',left='on',labelleft='on',right='off',labelright='off',top='off',labeltop='off',labelsize=8)

    

    ##########
    ## SYST ##
    ##########

    myData = []
    myPos = []
    for k in sorted(systPctToRF.keys()):
        myData.append(systPctToRF[k])
        myPos.append(k)
    myData.append(randomAddRF)
    myPos.append(11)
    panel9.boxplot(x=myData,positions=myPos,widths=0.5,showfliers=False,medianprops={'color':'black'})
    # myData = []
    # myPos = []
    # for k in sorted(systPctToRF2.keys()):
    #     myData.append(systPctToRF2[k])
    #     myPos.append(k)
    # panel9.boxplot(x=myData,positions=myPos,widths=0.5,showfliers=False,medianprops={'color':'red'},flierprops={'color':'red'},boxprops={'color':'red'})
    #panel5.plot([-10,60],[1701.925,1701.925],c='black',ls=':')
    panel9.set_xticks([0,1,2,3,4,5,6,7,8,9,10])
    panel9.set_xlim([-0.5,11.5])
    panel9.set_ylim([-3,52])
    panel9.plot([10.5,10.5],[-10,100],ls=':',color='black')
    panel9.set_xlabel('Lineages With Systematic Error Added',size=8)
    panel9.set_ylabel('Robinson-Foulds Distance to Reference',size=8)
    panel9.tick_params(bottom='on',labelbottom='on',left='on',labelleft='on',right='off',labelright='off',top='off',labeltop='off',labelsize=8)


    myData = []
    myPos = []
    myErr = [[],[]]
    for k in sorted(systPctToN1Ovr.keys()):
        myData.append([np.mean(systPctToN1Ovr[k])])
        myCI = get95CI(systPctToN1Ovr[k], np.mean(systPctToN1Ovr[k]))
        myErr[0].append(myCI[0])
        myErr[1].append(myCI[1])
        myPos.append(k)
    panel10.errorbar(x=myPos,y=myData,yerr=myErr,color='black',fmt='o')
    panel10.set_xlim([-0.5,10.5])
    panel10.set_ylim([0,1.0])
    panel10.set_xlabel('Lineages With Systematic Error Added',size=8)
    panel10.set_ylabel('Sister Node Sets Identical To Reference (%)',size=8)
    panel10.tick_params(bottom='on',labelbottom='on',left='on',labelleft='on',right='off',labelright='off',top='off',labeltop='off',labelsize=8)

    myData = []
    myPos = []
    for k in sorted(systPctToNStat.keys()):
        myData.append(systPctToNStat[k])
        myPos.append(k)
    histData = []
    for i in [0,2,4,6,8,10]:
        histData.append(myData[i].count(0.0)/float(len(myData[i])))
        histData.append(myData[i].count(1.0)/float(len(myData[i])))
        histData.append((len(myData[i])-(myData[i].count(0.0)+myData[i].count(1.0)))/float(len(myData[i])))
    myX = [0,1,2, 4,5,6, 8,9,10, 12,13,14, 16,17,18, 20,21,22]
    panel11.bar(myX, histData, width=0.8, align='center',edgecolor='black',color=[(0,0,0),(0.5,0.5,0.5),(0.95,0.95,0.95)]*6)
    panel11.set_xticks([1, 5, 9, 13, 17, 21])
    panel11.set_xticklabels(['0','2','4','6','8','10'])
    panel11.scatter(x=[1,2],y=[3,3],color=(0,0,0),label='0')
    panel11.scatter(x=[1,2],y=[3,3],color=(0.5,0.5,0.5),label='1')
    panel11.scatter(x=[1,2],y=[3,3],color=(0.95,0.95,0.95),label='2+')
    panel11.set_ylim([0.0,1.0])
    #leg = panel11.legend(loc='upper right',fontsize=7,title=' Distance From\nTrue Placement\n       (edges)')
    #leg.get_title().set_fontsize('7')
    #panel7.plot([-10,60],[11.14924347,11.14924347],c='black',ls=':')
    #panel7.set_xlim([-0.5,10.5])
    panel11.set_ylabel('Density',size=8)
    panel11.set_xlabel('Lineages With Systematic Error Added',size=8)
    panel11.tick_params(bottom='on',labelbottom='on',left='on',labelleft='on',right='off',labelright='off',top='off',labeltop='off',labelsize=8)

    myData = []
    myPos = []
    for k in sorted(systPctToEP.keys()):
        myData.append(systPctToEP[k])
        myPos.append(k)
    histData = []
    for i in [0,2,4,6,8,10]:
        histData.append(myData[i].count(1)/float(len(myData[i])))
        histData.append(myData[i].count(2)/float(len(myData[i])))
        histData.append((len(myData[i])-(myData[i].count(1)+myData[i].count(2)))/float(len(myData[i])))
    myX = [0,1,2, 4,5,6, 8,9,10, 12,13,14, 16,17,18, 20,21,22]
    panel12.bar(myX, histData, width=0.8, align='center',edgecolor='black',color=[(0,0,0),(0.5,0.5,0.5),(0.95,0.95,0.95)]*6)
    panel12.set_xticks([1, 5, 9, 13, 17, 21])
    panel12.set_xticklabels(['0','2','4','6','8','10'])
    panel12.scatter(x=[1,2],y=[3,3],color=(0,0,0),label='1')
    panel12.scatter(x=[1,2],y=[3,3],color=(0.5,0.5,0.5),label='2')
    panel12.scatter(x=[1,2],y=[3,3],color=(0.95,0.95,0.95),label='3+')
    panel12.set_ylim([0.0,1.0])
    #leg = panel12.legend(loc='upper right',fontsize=7,title='     Equally\nParsimonious\n  Placements')
    #leg.get_title().set_fontsize('7')
    panel12.set_ylabel('Density',size=8)
    panel12.set_xlabel('Lineages With Systematic Error Added',size=8)
    panel12.tick_params(bottom='on',labelbottom='on',left='on',labelleft='on',right='off',labelright='off',top='off',labeltop='off',labelsize=8)


    ###########
    ## SYST2 ##
    ###########

    myData = []
    myPos = []
    for k in sorted(systPctToRF2.keys()):
        myData.append(systPctToRF2[k])
        myPos.append(k)
    myData.append(randomAddRF)
    myPos.append(11)
    panel13.boxplot(x=myData,positions=myPos,widths=0.5,showfliers=False,medianprops={'color':'black'})
    # myData = []
    # myPos = []
    # for k in sorted(systPctToRF2.keys()):
    #     myData.append(systPctToRF2[k])
    #     myPos.append(k)
    # panel9.boxplot(x=myData,positions=myPos,widths=0.5,showfliers=False,medianprops={'color':'red'},flierprops={'color':'red'},boxprops={'color':'red'})
    #panel5.plot([-10,60],[1701.925,1701.925],c='black',ls=':')
    panel13.set_xticks([0,1,2,3,4,5,6,7,8,9,10])
    panel13.set_xlim([-0.5,11.5])
    panel13.set_ylim([-3,52])
    panel13.plot([10.5,10.5],[-10,100],ls=':',color='black')
    panel13.set_xlabel('Lineages With Systematic Error Added',size=8)
    panel13.set_ylabel('Robinson-Foulds Distance to Reference',size=8)
    panel13.tick_params(bottom='on',labelbottom='on',left='on',labelleft='on',right='off',labelright='off',top='off',labeltop='off',labelsize=8)


    myData = []
    myPos = []
    myErr = [[],[]]
    for k in sorted(systPctToN1Ovr2.keys()):
        myData.append([np.mean(systPctToN1Ovr2[k])])
        myCI = get95CI(systPctToN1Ovr2[k], np.mean(systPctToN1Ovr2[k]))
        myErr[0].append(myCI[0])
        myErr[1].append(myCI[1])
        myPos.append(k)
    panel14.errorbar(x=myPos,y=myData,yerr=myErr,color='black',fmt='o')
    panel14.set_xlim([-0.5,10.5])
    panel14.set_ylim([0,1.0])
    panel14.set_xlabel('Lineages With Systematic Error Added',size=8)
    panel14.set_ylabel('Sister Node Sets Identical To Reference (%)',size=8)
    panel14.tick_params(bottom='on',labelbottom='on',left='on',labelleft='on',right='off',labelright='off',top='off',labeltop='off',labelsize=8)

    myData = []
    myPos = []
    for k in sorted(systPctToNStat2.keys()):
        myData.append(systPctToNStat2[k])
        myPos.append(k)
    histData = []
    for i in [0,2,4,6,8,10]:
        histData.append(myData[i].count(0.0)/float(len(myData[i])))
        histData.append(myData[i].count(1.0)/float(len(myData[i])))
        histData.append((len(myData[i])-(myData[i].count(0.0)+myData[i].count(1.0)))/float(len(myData[i])))
    myX = [0,1,2, 4,5,6, 8,9,10, 12,13,14, 16,17,18, 20,21,22]
    panel15.bar(myX, histData, width=0.8, align='center',edgecolor='black',color=[(0,0,0),(0.5,0.5,0.5),(0.95,0.95,0.95)]*6)
    panel15.set_xticks([1, 5, 9, 13, 17, 21])
    panel15.set_xticklabels(['0','2','4','6','8','10'])
    panel15.scatter(x=[1,2],y=[3,3],color=(0,0,0),label='0')
    panel15.scatter(x=[1,2],y=[3,3],color=(0.5,0.5,0.5),label='1')
    panel15.scatter(x=[1,2],y=[3,3],color=(0.95,0.95,0.95),label='2+')
    panel15.set_ylim([0.0,1.0])
    #leg = panel15.legend(loc='upper right',fontsize=7,title=' Distance From\nTrue Placement\n       (edges)')
    #leg.get_title().set_fontsize('7')
    #panel7.plot([-10,60],[11.14924347,11.14924347],c='black',ls=':')
    #panel7.set_xlim([-0.5,10.5])
    panel15.set_ylabel('Density',size=8)
    panel15.set_xlabel('Lineages With Systematic Error Added',size=8)
    panel15.tick_params(bottom='on',labelbottom='on',left='on',labelleft='on',right='off',labelright='off',top='off',labeltop='off',labelsize=8)

    myData = []
    myPos = []
    for k in sorted(systPctToEP2.keys()):
        myData.append(systPctToEP2[k])
        myPos.append(k)
    histData = []
    for i in [0,2,4,6,8,10]:
        histData.append(myData[i].count(1)/float(len(myData[i])))
        histData.append(myData[i].count(2)/float(len(myData[i])))
        histData.append((len(myData[i])-(myData[i].count(1)+myData[i].count(2)))/float(len(myData[i])))
    myX = [0,1,2, 4,5,6, 8,9,10, 12,13,14, 16,17,18, 20,21,22]
    panel16.bar(myX, histData, width=0.8, align='center',edgecolor='black',color=[(0,0,0),(0.5,0.5,0.5),(0.95,0.95,0.95)]*6)
    panel16.set_xticks([1, 5, 9, 13, 17, 21])
    panel16.set_xticklabels(['0','2','4','6','8','10'])
    panel16.scatter(x=[1,2],y=[3,3],color=(0,0,0),label='1')
    panel16.scatter(x=[1,2],y=[3,3],color=(0.5,0.5,0.5),label='2')
    panel16.scatter(x=[1,2],y=[3,3],color=(0.95,0.95,0.95),label='3+')
    panel16.set_ylim([0.0,1.0])
    #leg = panel16.legend(loc='upper right',fontsize=7,title='     Equally\nParsimonious\n  Placements')
    #leg.get_title().set_fontsize('7')
    panel16.set_ylabel('Density',size=8)
    panel16.set_xlabel('Lineages With Systematic Error Added',size=8)
    panel16.tick_params(bottom='on',labelbottom='on',left='on',labelleft='on',right='off',labelright='off',top='off',labeltop='off',labelsize=8)

    # panel1.text(-10, 52*1.03, 'a', ha='center', va='bottom', fontsize=20)
    # panel2.text(-10, 1.0*1.03, 'b', ha='center', va='bottom', fontsize=20)
    # panel3.text(-3.5, 1.0*1.03, 'c', ha='center', va='bottom', fontsize=20)
    # panel4.text(-3.5, 1.0*1.03, 'd', ha='center', va='bottom', fontsize=20)
    # panel5.text(-1.15, 52*1.03, 'e', ha='center', va='bottom', fontsize=20)
    # panel6.text(-1.15, 1.0*1.03, 'f', ha='center', va='bottom', fontsize=20)
    # panel7.text(-3.5, 1.0*1.03, 'g', ha='center', va='bottom', fontsize=20)
    # panel8.text(-3.5, 1.0*1.03, 'h', ha='center', va='bottom', fontsize=20)
    # panel9.text(-1.15, 52*1.03, 'i', ha='center', va='bottom', fontsize=20)
    # panel10.text(-1.15, 1.0*1.03, 'j', ha='center', va='bottom', fontsize=20)
    # panel11.text(-3.5, 1.0*1.03, 'k', ha='center', va='bottom', fontsize=20)
    # panel12.text(-3.5, 1.0*1.03, 'l', ha='center', va='bottom', fontsize=20)
    # panel13.text(-1.15, 52*1.03, 'a', ha='center', va='bottom', fontsize=20)
    # panel14.text(-1.15, 1.0*1.03, 'b', ha='center', va='bottom', fontsize=20)
    # panel15.text(-3.5, 1.0*1.03, 'c', ha='center', va='bottom', fontsize=20)
    # panel16.text(-3.5, 1.0*1.03, 'd', ha='center', va='bottom', fontsize=20)

    plt.savefig('newBoxplotsExtraRowWithoutLegend.pdf', dpi=1300)
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
    return '\t'.join(newList)

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





            






