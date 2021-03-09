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

def get138ColorVectors():

    fileToEdges = {}
    fileToEdges['current-tree.edge'] = 17815
    fileToEdges['subsample_1000.edge'] = 1153
    fileToEdges['subsample_5000.edge'] = 5926
    fileToEdges['subsample_250.edge'] = 290
    tipNumToColor = {}
    nodeToPars = {'hCoV-19/USA/WA-UW96/2020|EPI_ISL_416452|2020-03-10':1}
    with open('parsScoresWa.tsv') as f:
        for line in f:
            splitLine = (line.strip()).split('\t')
            if not splitLine[0].startswith('#'):
                if splitLine[1].startswith('hCoV') or splitLine[1].startswith('node'):
                    nodeToPars[splitLine[1]] = int(splitLine[2])
                else:
                    tipNumToColor[(1000+int(splitLine[1]))] = int(splitLine[2])

    myOutString = 'library(phytools)\nlibrary(inlmisc)\nsetwd("/Users/Bryan/Desktop/COVID/NEW_SIM/ZOOM_FIG/REDO/")\n'
    myOutString += 't1000 = read.newick("subsample_1000.nh")\nt5000 = read.newick("subsample_5000.nh")\nt250 = read.newick("subsample_250.nh")\n'


    #############
    ### S1000 ###
    #############

    myLineNumber = 0
    sampleToNum = {}

    for line in open('subsample_250.tip.label'):
        myLineNumber += 1
        sampleToNum[line.strip()] = myLineNumber
        if line.strip() in nodeToPars:
            tipNumToColor[myLineNumber] = nodeToPars[line.strip()]
        else:
            print(line.strip())

    print(min(tipNumToColor.values()), max(tipNumToColor.values())) # 2, 23
    #print(tipNumToColor)

    """
    pal = colorRamp(c("red","orange","yellow","green","cyan","blue","violet"))
    write.table(x=pal(seq(0, 1, len=23)),file='23.color',quote=FALSE,col.names=FALSE,row.names=FALSE)
    """

    parsToColor = {}
    lineNum = 0
    myColVec = []
    with open('28.alt.color') as f:
        for line in f:
            myColVec.append(line.strip())
            splitLine = (line.strip()).split()
            parsToColor[lineNum] = splitLine[0]
            lineNum += 1

    for k in tipNumToColor:
        temp = tipNumToColor[k]
        tipNumToColor[k] = parsToColor[temp]
    #print(tipNumToColor)

    myEdgeColors = ['"black"']*fileToEdges['subsample_250.edge'] # total number of edges in t1
    nodeToDescendants = {}
    for line in open('subsample_250.edge'):
        splitLine = (line.strip()).split('\t')
        if int(splitLine[2]) in tipNumToColor:
            myEdgeColors[int(splitLine[0])-1] = tipNumToColor[int(splitLine[2])]

    myOutString += 'edge.col = c('+joinerX(myEdgeColors)+')\n'

    #print(myOutString)

    myOutString += 'pdf("subsample_250.pdf",height=90,width=150)'+'\n'
    myOutString += 'pal = colorRampPalette(c('+joinerX(myColVec)+'))\n'
    myOutString += 'plot.phylo(x=t250,show.tip.label=FALSE,show.node.label=FALSE,edge.color=edge.col,edge.width=0.1)'+'\n'
    myOutString += 'AddGradientLegend(seq(1,'+str(len(myColVec))+'), pal = pal, at = NULL, n = '+str(len(myColVec))+', labels = TRUE, scientific = FALSE,title = NULL, strip.dim = c(2, 8), loc="bottomleft")\n'
    myOutString += 'add.scale.bar(cex=100,length=1.0,lwd=10,font=50)\n'
    myOutString += 'dev.off()'+'\n'
    myOutString += 'warnings()'+'\n\n\n'















    # #############
    # ### S1000 ###
    # #############

    # myLineNumber = 0
    # sampleToNum = {}

    # for line in open('subsample_1000.tip.label'):
    #     myLineNumber += 1
    #     sampleToNum[line.strip()] = myLineNumber
    #     if line.strip() in nodeToPars:
    #         tipNumToColor[myLineNumber] = nodeToPars[line.strip()]
    #     else:
    #         print(line.strip())

    # print(min(tipNumToColor.values()), max(tipNumToColor.values())) # 2, 23
    # #print(tipNumToColor)

    # """
    # pal = colorRamp(c("red","orange","yellow","green","cyan","blue","violet"))
    # write.table(x=pal(seq(0, 1, len=23)),file='23.color',quote=FALSE,col.names=FALSE,row.names=FALSE)
    # """

    # parsToColor = {}
    # lineNum = 0
    # myColVec = []
    # with open('26.alt.color') as f:
    #     for line in f:
    #         myColVec.append(line.strip())
    #         splitLine = (line.strip()).split()
    #         parsToColor[lineNum] = splitLine[0]
    #         lineNum += 1

    # for k in tipNumToColor:
    #     temp = tipNumToColor[k]
    #     tipNumToColor[k] = parsToColor[temp]
    # #print(tipNumToColor)

    # myEdgeColors = ['"black"']*fileToEdges['subsample_1000.edge'] # total number of edges in t1
    # nodeToDescendants = {}
    # for line in open('subsample_1000.edge'):
    #     splitLine = (line.strip()).split('\t')
    #     if int(splitLine[2]) in tipNumToColor:
    #         myEdgeColors[int(splitLine[0])-1] = tipNumToColor[int(splitLine[2])]

    # myOutString += 'edge.col = c('+joinerX(myEdgeColors)+')\n'

    # #print(myOutString)

    # myOutString += 'pdf("subsample_1000.pdf",height=90,width=150)'+'\n'
    # myOutString += 'pal = colorRampPalette(c('+joinerX(myColVec)+'))\n'
    # myOutString += 'plot.phylo(x=t1000,show.tip.label=FALSE,show.node.label=FALSE,edge.color=edge.col,edge.width=0.1)'+'\n'
    # myOutString += 'AddGradientLegend(seq(1,'+str(len(myColVec))+'), pal = pal, at = NULL, n = '+str(len(myColVec))+', labels = TRUE, scientific = FALSE,title = NULL, strip.dim = c(2, 8), loc="bottomleft")\n'
    # myOutString += 'add.scale.bar(cex=100,length=1.0,lwd=10,font=50)\n'
    # myOutString += 'dev.off()'+'\n'
    # myOutString += 'warnings()'+'\n\n\n'


    # #############
    # ### S1000 ###
    # #############

    # myLineNumber = 0
    # sampleToNum = {}
    # tipNumToColor = {}

    # for line in open('subsample_5000.tip.label'):
    #     myLineNumber += 1
    #     sampleToNum[line.strip()] = myLineNumber
    #     if line.strip() in nodeToPars:
    #         tipNumToColor[myLineNumber] = nodeToPars[line.strip()]
    #     else:
    #         print(line.strip())

    # print(min(tipNumToColor.values()), max(tipNumToColor.values())) # 2, 23
    # #print(tipNumToColor)

    # """
    # pal = colorRamp(c("red","orange","yellow","green","cyan","blue","violet"))
    # write.table(x=pal(seq(0, 1, len=23)),file='23.color',quote=FALSE,col.names=FALSE,row.names=FALSE)
    # """

    # parsToColor = {}
    # lineNum = 1
    # myColVec = []
    # with open('29.alt.color') as f:
    #     for line in f:
    #         myColVec.append(line.strip())
    #         splitLine = (line.strip()).split()
    #         parsToColor[lineNum] = splitLine[0]
    #         lineNum += 1

    # for k in tipNumToColor:
    #     temp = tipNumToColor[k]
    #     tipNumToColor[k] = parsToColor[temp]
    # #print(tipNumToColor)

    # myEdgeColors = ['"black"']*fileToEdges['subsample_5000.edge'] # total number of edges in t1
    # nodeToDescendants = {}
    # for line in open('subsample_5000.edge'):
    #     splitLine = (line.strip()).split('\t')
    #     if int(splitLine[2]) in tipNumToColor:
    #         myEdgeColors[int(splitLine[0])-1] = tipNumToColor[int(splitLine[2])]
    #     if not int(splitLine[1]) in nodeToDescendants:
    #         nodeToDescendants[int(splitLine[1])] = []
    #     nodeToDescendants[int(splitLine[1])].append(int(splitLine[2]))

    # #print(myEdgeColors)

    # myUnresolvedNodes = list(sorted(nodeToDescendants.keys()))
    # # go through all nodes with descendents
    # # if all descendents have colors, add node into tipNumToColor, will recolor that edge later
    # # else, add it onto the end of myUnresolvedNodes
    # for k in myUnresolvedNodes:
    #     #print(k, nodeToDescendants[k])
    #     unresolveds = 0
    #     myColors = []
    #     for d in nodeToDescendants[k]:
    #         if d in tipNumToColor:
    #             #print(d, tipNumToColor[d])
    #             myColors.append(tipNumToColor[d])
    #         else:
    #             unresolveds += 1
    #             #print(d)
    #     if unresolveds == 0:
    #         if len(set(myColors)) == 1:
    #             tipNumToColor[k] = myColors[0]
    #         else:
    #             tipNumToColor[k] = '"black"'
    #         #print("resolved "+str(k))
    #     else:
    #         myUnresolvedNodes.append(k)
    #         #print("adding "+str(k)+" back to end")

    # # now that every node has a color, go through again
    # for line in open('subsample_5000.edge'):
    #     splitLine = (line.strip()).split('\t')
    #     if int(splitLine[2]) in tipNumToColor:
    #         myEdgeColors[int(splitLine[0])-1] = tipNumToColor[int(splitLine[2])]
    #     else:
    #         print(int(splitLine[2]))

    # myOutString += 'edge.col = c('+joinerX(myEdgeColors)+')\n'

    # #print(myOutString)

    # myOutString += 'pdf("subsample_5000.pdf",height=90,width=150)'+'\n'
    # myOutString += 'pal = colorRampPalette(c('+joinerX(myColVec)+'))\n'
    # myOutString += 'plot.phylo(x=t5000,show.tip.label=FALSE,show.node.label=FALSE,edge.color=edge.col,edge.width=0.1)'+'\n'
    # myOutString += 'AddGradientLegend(seq(1,'+str(len(myColVec))+'), pal = pal, at = NULL, n = '+str(len(myColVec))+', labels = TRUE, scientific = FALSE,title = NULL, strip.dim = c(2, 8), loc="bottomleft")\n'
    # myOutString += 'add.scale.bar(cex=100,length=1.0,lwd=10,font=50)\n'
    # myOutString += 'dev.off()'+'\n'
    # myOutString += 'warnings()'+'\n\n\n'














    open('make_subsample_tree_figs_editor.R','w').write(myOutString)









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

def joinerX(entry):
    newList = []
    for k in entry:
        newList.append(str(k))
    return ','.join(newList)

def main():
   get138ColorVectors()

if __name__ == "__main__":
    """
    Calls main when program is run by user.
    """
    main();
    raise SystemExit






















