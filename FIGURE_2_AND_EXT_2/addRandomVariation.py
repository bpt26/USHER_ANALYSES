#!/usr/bin/env python3
# Name: Bryan Thornlow
# Date: 2/1/2018
# compareDatabases.py

import sys
import os
import datetime
import random
import numpy
import gzip
import math

"""
1) RANDOM MASKING:
- for each [10,20,30,40,50] percent of sites:
- add Ns to random sites in the data to be added in the missing_1000_*.fa files

note:
- to make the missing_*.fa files in combined_nicola, i took from the raw global simulated .fa.gz file
- i got the .vcfs from yatish directly
- to make the new .vcfs with masking, i will run this script here to mask the .fa 
- need to ask yatish what is being used as the reference, add that at the beginning of the file unmaksed, THEN do faToVcf on that masked .fa
- this will give us the masked .vcfs needed to run these experiments


2) RANDOM ERRORS
- randomly draw [1000,2000..10,000] genomes and positions with replacement, but ensure that no two genome-positions are the same
- THESE ARE NOT Ns. these should be, if it is A, randomly draw [C,G,T], etc.

3) SYSTEMATIC ERRORS:
- 
"""


##########################
##### MAIN FUNCTIONS #####
##########################


##############
### MASK 1 ###
##############

def addRandomVariation():
    BASE_DIR = '/public/groups/corbettlab/tRNA/COVID/LANDEN_VCF/REVIEWER_RESPONSE/YATISH_UPDATE/NICOLA/NEW_SIM/TEST/'

    myRefSeq = ''
    with open(BASE_DIR+'ref_seq.fa') as f:
        for line in f:
            if line.strip().startswith('>'):
                myRefSeq += '>1\n'
            else:
                myRefSeq += line.strip()+'\n'

    for replicateNum in range(1,101):
        strainToSeq = {}
        myMissingFa = BASE_DIR+'MISSING_FASTA_NO_REF/missing_10_'+str(replicateNum)+'.fasta'
        if os.path.exists(myMissingFa):
            with open(myMissingFa) as f:
                for line in f:
                    if line.strip().startswith('>'):
                        myStrain = line.strip()[1:]
                    else:
                        strainToSeq[myStrain] = line.strip()
                        myLen = len(line.strip())

            for pct in [10,20,30,40,50]:
                myOutString = ''
                mySampleSize = int((float(pct)/100.0)*myLen)
                for strain in strainToSeq:
                    mySeqList = list(strainToSeq[strain])
                    myNSites = random.sample(list(range(0,myLen)),mySampleSize)
                    for site in myNSites:
                        if mySeqList[site] == 'X':
                            print('X already at site '+str(site)+' in strain '+strain+'!')
                        else:
                            mySeqList[site] = 'X'
                    myOutString += '>'+strain+'\n'+''.join(mySeqList)+'\n'
                open(BASE_DIR+'MASKED_MISSING_FASTA/missing_10_'+str(replicateNum)+'_mask_'+str(pct)+'.fasta','w').write(myRefSeq+myOutString)
            print("Finished replicate "+str(replicateNum)+'!')



##############
### RAND 2 ###
##############

def addRandomErrors():
    BASE_DIR = '/public/groups/corbettlab/tRNA/COVID/LANDEN_VCF/REVIEWER_RESPONSE/YATISH_UPDATE/NICOLA/NEW_SIM/TEST/'

    myRefSeq = ''
    with open(BASE_DIR+'ref_seq.fa') as f:
        for line in f:
            if line.strip().startswith('>'):
                myRefSeq += '>1\n'
            else:
                myRefSeq += line.strip()+'\n'

    for replicateNum in range(1,101):
        strainToSeq = {}
        myMissingFa = BASE_DIR+'MISSING_FASTA_NO_REF/missing_10_'+str(replicateNum)+'.fasta'
        if os.path.exists(myMissingFa):
            with open(myMissingFa) as f:
                for line in f:
                    if line.strip().startswith('>'):
                        myStrain = line.strip()[1:]
                    else:
                        strainToSeq[myStrain] = line.strip()
                        myLen = len(line.strip())

            for sampleSize in [10,20,30,40,50,60,70,80,90,100]:
                myOutString = ''
                myList = []
                while len(set(myList)) != sampleSize:
                    myList = []
                    myGenomes = random.choices(list(strainToSeq.keys()), k=sampleSize)
                    myPositions = random.choices(list(range(0,myLen)), k=sampleSize)
                    for i in range(0,sampleSize):
                        strainToSeq[myGenomes[i]] = mutate(strainToSeq[myGenomes[i]], myPositions[i])
                        myList.append(myGenomes[i]+':'+str(myPositions[i]))
                if len(myList) != len(set(myList)):
                    print("NO", replicateNum, sampleSize, myList)
                    raise(SystemExit)
                for k in strainToSeq.keys():
                    myOutString += '>'+str(k)+'\n'+strainToSeq[k]+'\n'
                open('RANDOM_ERRORS_FASTA/missing_10_'+str(replicateNum)+'_rand_'+str(sampleSize)+'.fasta','w').write(myRefSeq+myOutString)
            print("Finished replicate "+str(replicateNum)+'!')


##############
### SYST 3 ###
##############

def addSystematicErrors():
    BASE_DIR = '/public/groups/corbettlab/tRNA/COVID/LANDEN_VCF/REVIEWER_RESPONSE/YATISH_UPDATE/NICOLA/NEW_SIM/TEST/'

    myRefSeq = ''
    with open(BASE_DIR+'ref_seq.fa') as f:
        for line in f:
            if line.strip().startswith('>'):
                myRefSeq += '>1\n'
            else:
                myRefSeq += line.strip()+'\n'


    myLog = 'numSites\tpct\tnewNts'
    for replicateNum in range(1,101):
        strainToSeq = {}
        myMissingFa = BASE_DIR+'MISSING_FASTA_NO_REF/missing_10_'+str(replicateNum)+'.fasta'
        if os.path.exists(myMissingFa):
            with open(myMissingFa) as f:
                for line in f:
                    if line.strip().startswith('>'):
                        myStrain = line.strip()[1:]
                    else:
                        strainToSeq[myStrain] = line.strip()
                        myLen = len(line.strip())
            
            for numSites in [1,2]:
                for mySampleSize in range(1,11):
                    myLog += '\n'+str(replicateNum)+'\t'+str(numSites)+'\t'+str(mySampleSize)
                    myOutString = ''
                    myGenomes = random.sample(list(strainToSeq.keys()), k=mySampleSize)
                    myPositions = random.sample(list(range(0,myLen)), k=numSites)
                    for s in range(0,len(myGenomes)):
                        strain = myGenomes[s]
                        mySeq = list(strainToSeq[strain])
                        for pos in myPositions:
                            if mySeq[pos] == 'A':
                                mySeq[pos] = 'G'
                                if s == 0:
                                    myLog += '\tA'+str(pos)+'G'
                            elif mySeq[pos] == 'C':
                                mySeq[pos] = 'G'
                                if s == 0:
                                    myLog += '\tC'+str(pos)+'G'
                            elif mySeq[pos] == 'G':
                                mySeq[pos] = 'A'
                                if s == 0:
                                    myLog += '\tG'+str(pos)+'A'
                            elif mySeq[pos] == 'T':
                                mySeq[pos] = 'A'
                                if s == 0:
                                    myLog += '\tT'+str(pos)+'A'
                        strainToSeq[strain] = ''.join(mySeq)
                        if s == 0:
                            myLog += '\n'+joiner(myGenomes)
                    for k in strainToSeq.keys():
                        myOutString += '>'+str(k)+'\n'+strainToSeq[k]+'\n'
                    open('SYSTEMATIC_ERRORS_FASTA/missing_10_'+str(replicateNum)+'_samples_'+str(mySampleSize)+'_sites_'+str(numSites)+'.fasta','w').write(myRefSeq+myOutString)
            open('systematic_errors.log','w').write(myLog)
            print("Finished replicate "+str(replicateNum)+'!')


##########################
#### HELPER FUNCTIONS ####
##########################

def joiner(entry):
    newList = []
    for k in entry:
        newList.append(str(k))
    return '\t'.join(newList)

def mutate(genome, position):
    myGenome = list(genome.upper())
    if myGenome[position] == 'A':
        myGenome[position] = random.choice(['C','G','T'])
    elif myGenome[position] == 'C':
        myGenome[position] = random.choice(['A','G','T'])
    elif myGenome[position] == 'G':
        myGenome[position] = random.choice(['A','C','T'])
    elif myGenome[position] == 'T':
        myGenome[position] = random.choice(['A','C','G'])
    return(''.join(myGenome))


def main():
    if int(sys.argv[1]) == 1:
        addRandomVariation()
    elif int(sys.argv[1]) == 2:
        addRandomErrors()
    elif int(sys.argv[1]) == 3:
        addSystematicErrors()


if __name__ == "__main__":
    """
    Calls main when program is run by user.
    """
    main();
    raise SystemExit




                    





