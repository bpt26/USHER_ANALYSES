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

    myOutString = 'library(phytools)\nsetwd("/Users/Bryan/Desktop/COVID/MORE_TANGLEGRAMS")\n\n'

    lineCounter = 0
    numToLinkCol = {}
    for line in open('linkerVectorNew.txt'):
        lineCounter += 1
        numToLinkCol[lineCounter] = line.strip()

    fileToEdges = {}
    fileToEdges['original-1.edges'] = 119
    fileToEdges['original-2.edges'] = 129
    fileToEdges['original-3.edges'] = 120
    fileToEdges['original-4.edges'] = 122
    fileToEdges['original-5.edges'] = 123
    fileToEdges['original-6.edges'] = 171
    fileToEdges['usher-1.edges'] = 119
    fileToEdges['usher-2.edges'] = 129
    fileToEdges['usher-3.edges'] = 119
    fileToEdges['usher-4.edges'] = 122
    fileToEdges['usher-5.edges'] = 123
    fileToEdges['usher-6.edges'] = 166

    for repNum in range(1,7):
        myOutString += 't1 = read.newick("original-'+str(repNum)+'.nh")\n'
        myOutString += 't2 = read.newick("usher-'+str(repNum)+'.nh")\n'
        myOutString += 'assoc<-cbind(t1$tip.label,t2$tip.label)\n'
        myOutString += 'obj = cophylo(t1,t2,rotate=FALSE,link.lwd=0.001)\n\n'

        ################
        ### ORIGINAL ###
        ################

        myLineNumber = 0
        sampleToNum = {}
        tipNumToColor = {}
        isMissing = {}
        for line in open('missing-'+str(repNum)+'.txt'):
            isMissing[line.strip()] = True

        for line in open('original-'+str(repNum)+'.tiplabels'):
            myLineNumber += 1
            sampleToNum[line.strip()] = myLineNumber
            if line.strip() in isMissing:
                tipNumToColor[myLineNumber] = 'red'
            else:
                tipNumToColor[myLineNumber] = 'black'

        myEdgeColors = ['black']*fileToEdges['original-'+str(repNum)+'.edges'] # total number of edges in t1
        nodeToDescendants = {}
        for line in open('original-'+str(repNum)+'.edges'):
            splitLine = (line.strip()).split('\t')
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
        for line in open('original-'+str(repNum)+'.edges'):
            splitLine = (line.strip()).split('\t')
            if int(splitLine[2]) in tipNumToColor:
                myEdgeColors[int(splitLine[0])-1] = tipNumToColor[int(splitLine[2])]
            else:
                print(int(splitLine[2]))

        myOutString += 'left<-c('+joinerC(myEdgeColors)+')\n'


        #############
        ### USHER ###
        #############

        myLineNumber = 0
        sampleToNum = {}
        tipNumToColor = {}
        isMissing = {}
        for line in open('missing-'+str(repNum)+'.txt'):
            isMissing[line.strip()] = True

        for line in open('usher-'+str(repNum)+'.tiplabels'):
            myLineNumber += 1
            sampleToNum[line.strip()] = myLineNumber
            if line.strip() in isMissing:
                tipNumToColor[myLineNumber] = 'red'
            else:
                tipNumToColor[myLineNumber] = 'black'

        myEdgeColors = ['black']*fileToEdges['usher-'+str(repNum)+'.edges'] # total number of edges in t1
        nodeToDescendants = {}
        for line in open('usher-'+str(repNum)+'.edges'):
            splitLine = (line.strip()).split('\t')
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
        for line in open('usher-'+str(repNum)+'.edges'):
            splitLine = (line.strip()).split('\t')
            if int(splitLine[2]) in tipNumToColor:
                myEdgeColors[int(splitLine[0])-1] = tipNumToColor[int(splitLine[2])]
            else:
                print(int(splitLine[2]))

        myOutString += 'right<-c('+joinerC(myEdgeColors)+')\n'

        myOutString += 'edge.col<-list(left=left,right=right)\n'
        myOutString += 'myCol = rgb(0, 0, 0, max = 255, alpha = 25)\n'
        myOutString += numToLinkCol[repNum]+'\n'
        myOutString += 'pdf("original-usher-'+str(repNum)+'.pdf",height=90,width=150)\n'
        myOutString += 'plot(obj,edge.col=edge.col,pts=FALSE,tip.lty=0,tip.len=0.01,ftype="off",link.lwd=1,lwd=5,link.lty="solid",link.col=linkCol)\n'
        myOutString += 'dev.off()\n\n\n'
    open('trees.R','w').write(myOutString)


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






















