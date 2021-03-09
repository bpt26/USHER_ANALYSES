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


t1 = read.newick("current-tree.nh")
write.table(t1$edge,file='current-tree.edge',quote=F,sep='\t',col.names=F)
write.table(t1$tip.label,file='current-tree.tip.label',quote=F,sep='\t',col.names=F,row.names=F)
"""

##########################
##### MAIN FUNCTIONS #####
##########################

def subSampleTreeR():
	tipToParsScore = {}
	with open('current-tree.tip.label') as f:
		for line in f:
			tipToParsScore[line.strip()] = 99

	toPrune = []
	with open('parsScoresWa.tsv') as f:
		for line in f:
			splitLine = (line.strip()).split('\t')
			if splitLine[1] in tipToParsScore:
				tipToParsScore[splitLine[1]] = int(splitLine[2])
				if int(splitLine[2]) > 2:
					toPrune.append(splitLine[1])


	randomChoices = np.random.choice(toPrune, 13276-1000, replace=False)
	myOutString = 'library(ape)\nsetwd("/Users/Bryan/Desktop/COVID/NEW_SIM/ZOOM_FIG/REDO")\nmyTree = read.tree("current-tree.nh")\n'
	for k in randomChoices:
		myOutString += 'myTree = drop.tip(myTree, "'+k+'")\n'
	open('subsample_1000.R','w').write(myOutString+'write.tree(myTree, file="subsample_1000.nh")\n')

	randomChoices = np.random.choice(toPrune, 13276-5000, replace=False)
	myOutString = 'library(ape)\nsetwd("/Users/Bryan/Desktop/COVID/NEW_SIM/ZOOM_FIG/REDO")\nmyTree = read.tree("current-tree.nh")\n'
	for k in randomChoices:
		myOutString += 'myTree = drop.tip(myTree, "'+k+'")\n'
	open('subsample_5000.R','w').write(myOutString+'write.tree(myTree, file="subsample_5000.nh")\n')

	randomChoices = np.random.choice(toPrune, 13276-250, replace=False)
	myOutString = 'library(ape)\nsetwd("/Users/Bryan/Desktop/COVID/NEW_SIM/ZOOM_FIG/REDO")\nmyTree = read.tree("current-tree.nh")\n'
	for k in randomChoices:
		myOutString += 'myTree = drop.tip(myTree, "'+k+'")\n'
	open('subsample_250.R','w').write(myOutString+'write.tree(myTree, file="subsample_250.nh")\n')







##########################
#### HELPER FUNCTIONS ####
##########################

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

def joinerX(entry):
    newList = []
    for k in entry:
        newList.append(str(k))
    return ','.join(newList)

def main():
   subSampleTreeR()

if __name__ == "__main__":
    """
    Calls main when program is run by user.
    """
    main();
    raise SystemExit






















