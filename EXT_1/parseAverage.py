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



##########################
##### MAIN FUNCTIONS #####
##########################

def parseAverage():
    uList = []
    iList = []
    fList = []
    for v in [2.5,5.0,7.5]:
        with open('compareSisNewMask1aSmallMask.txt') as f:
            for line in f:
                splitLine = (line.strip()).split('\t')
                if float(splitLine[1]) == v:
                    if splitLine[2] == 'USHER':
                        uList.append(float(splitLine[5]))
                    elif splitLine[2] == 'IQ':
                        iList.append(float(splitLine[5]))
                    elif splitLine[2] == 'FT':
                        fList.append(float(splitLine[5]))
        print(v)
        print(np.mean(uList))
        print(np.mean(iList))
        print(np.mean(fList))
        print(np.mean(uList)-np.mean(iList))
        print(np.mean(uList)-np.mean(fList))


    # uList = []
    # iList = []
    # fList = []
    # with open('compareSisNewMask1a.txt') as f:
    #     for line in f:
    #         splitLine = (line.strip()).split('\t')
    #         if int(splitLine[1]) == 30:
    #             if splitLine[2] == 'USHER':
    #                 uList.append(float(splitLine[5]))
    #             elif splitLine[2] == 'IQ':
    #                 iList.append(float(splitLine[5]))
    #             elif splitLine[2] == 'FT':
    #                 fList.append(float(splitLine[5]))
    # print(np.mean(uList))
    # print(np.mean(iList))
    # print(np.mean(fList))
    # print(np.mean(uList)-np.mean(iList))
    # print(np.mean(uList)-np.mean(fList))


##########################
#### HELPER FUNCTIONS ####
##########################

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
    parseAverage()

if __name__ == "__main__":
    """
    Calls main when program is run by user.
    """
    main();
    raise SystemExit




                    






