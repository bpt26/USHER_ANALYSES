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

"""
see getColorVectors.py in /Users/Bryan/Desktop/COVID/NEW_TREES/ for notes
"""

##########################
##### MAIN FUNCTIONS #####
##########################

def get138ColorVectors():

    myOutString = 'library(phytools)\nsetwd("/Users/Bryan/Desktop/COVID/NEW_SIM/DENSITREE")\n\n'

    myOutString += 't1 = read.newick("6u.rot.ultrametric")\n'
    myOutString += 't2 = read.newick("131u.rot.ultrametric")\n'
    myOutString += 'assoc<-cbind(t1$tip.label,t2$tip.label)\n'
    myOutString += 'obj = cophylo(t1,t2,rotate=FALSE,link.lwd=0.001)\n\n'

    ##############
    ##### T1 #####
    ##############

    myLineNumber = 0
    sampleToNum = {}
    tipNumToColor = {}
    for line in open('6u.tip.label'):
        myLineNumber += 1
        sampleToNum[line.strip()] = myLineNumber
        tipNumToColor[myLineNumber] = 'black'

    for line in open('/Users/Bryan/Desktop/COVID/NEW_TREES/cogSamples.colors'):
        splitLine = (line.strip()).split('\t')
        if splitLine[0] in sampleToNum:
            myTipNum = sampleToNum[splitLine[0]]
            tipNumToColor[myTipNum] = splitLine[1]

    myEdgeColors = ['black']*588 # total number of edges in t1
    nodeToDescendants = {}
    for line in open('6u.edge'):
        splitLine = (line.strip()).split()
        if int(splitLine[2]) in tipNumToColor:
            myEdgeColors[int(splitLine[0])-1] = tipNumToColor[int(splitLine[2])]
        if not int(splitLine[1]) in nodeToDescendants:
            nodeToDescendants[int(splitLine[1])] = []
        nodeToDescendants[int(splitLine[1])].append(int(splitLine[2]))

    myUnresolvedNodes = list(sorted(nodeToDescendants.keys()))
    for k in myUnresolvedNodes:
        unresolveds = 0
        myColors = []
        for d in nodeToDescendants[k]:
            if d in tipNumToColor:
                myColors.append(tipNumToColor[d])
            else:
                unresolveds += 1
        if unresolveds == 0:
            if len(set(myColors)) == 1:
                tipNumToColor[k] = myColors[0]
            else:
                tipNumToColor[k] = 'black'
            # print("resolved "+str(k))
        else:
            myUnresolvedNodes.append(k)
            # print("adding "+str(k)+" back to end")

    # now that every node has a color, go through again
    for line in open('6u.edge'):
        splitLine = (line.strip()).split()
        if int(splitLine[2]) in tipNumToColor:
            myEdgeColors[int(splitLine[0])-1] = tipNumToColor[int(splitLine[2])]
        else:
            print(int(splitLine[2]))

    myOutString += 'left<-c('+joinerC(myEdgeColors)+')\n'
    print(myEdgeColors[184])


    ##############
    ##### T2 #####
    ##############

    myLineNumber = 0
    sampleToNum = {}
    tipNumToColor = {}
    for line in open('131u.tip.label'):
        myLineNumber += 1
        sampleToNum[line.strip()] = myLineNumber
        tipNumToColor[myLineNumber] = 'black'

    for line in open('/Users/Bryan/Desktop/COVID/NEW_TREES/cogSamples.colors'):
        splitLine = (line.strip()).split('\t')
        if splitLine[0] in sampleToNum:
            myTipNum = sampleToNum[splitLine[0]]
            tipNumToColor[myTipNum] = splitLine[1]

    myEdgeColors = ['black']*587 # total number of edges in t2
    nodeToDescendants = {}
    for line in open('131u.edge'):
        splitLine = (line.strip()).split()
        if int(splitLine[2]) in tipNumToColor:
            myEdgeColors[int(splitLine[0])-1] = tipNumToColor[int(splitLine[2])]
        if not int(splitLine[1]) in nodeToDescendants:
            nodeToDescendants[int(splitLine[1])] = []
        nodeToDescendants[int(splitLine[1])].append(int(splitLine[2]))

    myUnresolvedNodes = list(sorted(nodeToDescendants.keys()))
    # go through all nodes with descendents
    # if all descendents have colors, add node into tipNumToColor, will recolor that edge later
    # else, add it onto the end of myUnresolvedNodes
    for k in myUnresolvedNodes:
        unresolveds = 0
        myColors = []
        for d in nodeToDescendants[k]:
            if d in tipNumToColor:
                myColors.append(tipNumToColor[d])
            else:
                unresolveds += 1
        if unresolveds == 0:
            if len(set(myColors)) == 1:
                tipNumToColor[k] = myColors[0]
            else:
                tipNumToColor[k] = 'black'
            # print("resolved "+str(k))
        else:
            myUnresolvedNodes.append(k)
            # print("adding "+str(k)+" back to end")

    # now that every node has a color, go through again
    for line in open('131u.edge'):
        splitLine = (line.strip()).split()
        if int(splitLine[2]) in tipNumToColor:
            myEdgeColors[int(splitLine[0])-1] = tipNumToColor[int(splitLine[2])]
        else:
            print(int(splitLine[2]))

    with open('linkerVectorNew.txt') as f:
        for line in f:
            linkCol = line.strip()+'\n'

    myOutString += 'right<-c('+joinerC(myEdgeColors)+')\n'
    print(myEdgeColors[211])

    myOutString += 'edge.col<-list(left=left,right=right)\n'
    myOutString += linkCol
    myOutString += 'pdf("densitree_cophylo_new_rot.pdf",height=90,width=150)\n'
    myOutString += 'plot(obj,edge.col=edge.col,pts=FALSE,tip.lty=0,tip.len=0.01,ftype="off",link.lwd=1,lwd=5,link.lty="solid",link.col=link.col)\n'
    myOutString += 'dev.off()\n\n'

    open('make_cophylo_rot.R','w').write(myOutString)


##########################
#### HELPER FUNCTIONS ####
##########################

def recursiveGetDescendents():
    myReturn = []
    for t in nodeToDescendants[myNode]:
        if t in tipNumToColor:
            myReturn.append(tipNumToColor[t])
        elif t in nodeToDescendants:
            myTemp = recursiveGetDescendents

def replaceSymbols(myEntry):
    myEntry = myEntry.replace('|', '_')
    myEntry = myEntry.replace('/', '_')
    return(myEntry)

def joiner(entry):
    newList = []
    for k in entry:
        newList.append(str(k))
    return '\t'.join(newList)

def joinerC(entry):
    newList = []
    for k in entry:
        newList.append('"'+str(k)+'"')
    return ','.join(newList)

def main():
   get138ColorVectors()

if __name__ == "__main__":
    """
    Calls main when program is run by user.
    """
    main();
    raise SystemExit






















