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
- for each file, how many samples have identical N1 sister clades between usher tree and sim tree
- for each lineage, if N1 != N1, compare N2s, then N3s, adn if they are not identical, go back one more and compare,
record N for each lineage, then take the average for each file.
- write a separate script to parse logs for each.


# sim: 15.n1.sister_clades
# reg: missing_10_52.n1.sister_clades
# mask: missing_10_52_mask_10.n1.sister_clade
# rand: missing_10_52_rand_100.n1.sister_clade
# sys: missing_10_52_samples_10_sites_1.n1.sister_clade
"""


##########################
##### MAIN FUNCTIONS #####
##########################

def compareSisterClades():

    ###########
    ### REG ###
    ###########

    myOutString = ''
    for rep in range(1,101):

        lineageToSimTreeN1 = {}
        lineageToSimTreeN2 = {}
        lineageToSimTreeN3 = {}
        lineageToUsherTreeN1 = {}
        lineageToUsherTreeN2 = {}
        lineageToUsherTreeN3 = {}

        with open('SIM_TREE_N1/'+str(rep)+'.n1.sister_clades') as f:
            for line in f:
                if (line.strip()).endswith(':'):
                    myStrain = line.strip()[:-1]
                    lineageToSimTreeN1[myStrain] = {}
                elif len(line.strip()) > 1:
                    (lineageToSimTreeN1[myStrain])[line.strip()] = True


        with open('SIM_TREE_N2/'+str(rep)+'.n2.sister_clades') as f:
            for line in f:
                if (line.strip()).endswith(':'):
                    myStrain = line.strip()[:-1]
                    lineageToSimTreeN2[myStrain] = {}
                elif len(line.strip()) > 1:
                    (lineageToSimTreeN2[myStrain])[line.strip()] = True

        with open('SIM_TREE_N3/'+str(rep)+'.n3.sister_clades') as f:
            for line in f:
                if (line.strip()).endswith(':'):
                    myStrain = line.strip()[:-1]
                    lineageToSimTreeN3[myStrain] = {}
                elif len(line.strip()) > 1:
                    (lineageToSimTreeN3[myStrain])[line.strip()] = True


        with open('N1/missing_10_'+str(rep)+'.n1.sister_clades') as f:
            for line in f:
                if (line.strip()).endswith(':'):
                    myStrain = line.strip()[:-1]
                    lineageToUsherTreeN1[myStrain] = {}
                elif len(line.strip()) > 1:
                    (lineageToUsherTreeN1[myStrain])[line.strip()] = True


        with open('N2/missing_10_'+str(rep)+'.n2.sister_clades') as f:
            for line in f:
                if (line.strip()).endswith(':'):
                    myStrain = line.strip()[:-1]
                    lineageToUsherTreeN2[myStrain] = {}
                elif len(line.strip()) > 1:
                    (lineageToUsherTreeN2[myStrain])[line.strip()] = True

        with open('N3/missing_10_'+str(rep)+'.n3.sister_clades') as f:
            for line in f:
                if (line.strip()).endswith(':'):
                    myStrain = line.strip()[:-1]
                    lineageToUsherTreeN3[myStrain] = {}
                elif len(line.strip()) > 1:
                    (lineageToUsherTreeN3[myStrain])[line.strip()] = True

        for l in lineageToSimTreeN1:
            NStat = 0.0
            N1Idetical = 0
            notAtRoot = 0
            if (max(len(set(lineageToSimTreeN1[l].keys())), len(set(lineageToUsherTreeN1[l].keys()))) < 39332):
                notAtRoot = 1
                
            simDicts = [lineageToSimTreeN1[l], lineageToSimTreeN2[l], lineageToSimTreeN3[l]]
            usherDicts = [lineageToUsherTreeN1[l], lineageToUsherTreeN2[l], lineageToUsherTreeN3[l]]

            if lineageToSimTreeN1[l] == lineageToUsherTreeN1[l]:
                N1Idetical = 1
                NStat = 0.0
            else:
                minN = 999                    
                for s in range(0,len(simDicts)):
                    for u in range(0,len(usherDicts)):
                        if simDicts[s] == usherDicts[u] and (float(s+1)+float(u+1)-2.0) < minN:
                            minN = (float(s+1)+float(u+1)-2.0)
                if minN == 999:
                    NStat = 5.0
                else:
                    NStat = minN

            myOutString += (str(rep)+'\t'+l+'\t'+str(N1Idetical)+'\t'+str(NStat)+'\t'+str(notAtRoot))+'\n'
        print("Finished rep "+str(rep))
    open('compareSisNew0.txt','w').write(myOutString)




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
    compareSisterClades()

if __name__ == "__main__":
    """
    Calls main when program is run by user.
    """
    main();
    raise SystemExit




                    




