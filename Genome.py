import numpy as np
import matplotlib.pyplot as plt
import csv
from tabulate import tabulate

IDList = []
AdjP = []
PList = []
tValues = []
BValues = []
logFCs = []
GeneSymbols = []
GeneTitles = []
GeneIDs = []
FilteredIDs = []
FlogFCs = []
FGeneSymbols = []
FGeneTitles = []
tabledata = []
SortedIDs = []
SortedGenes = []
SortedTitles = []
logssorted = []
completeinterestset = []
FAdjP = []
FPList = []
FtValues = []
FBValues = []
sortedtabledata = []
savefigpath = ""
savefigpath2 = ""
savefigpath3 = ""
saveinfopath = ""

def initArrays():
    IDList = []
    AdjP = []
    PList = []
    tValues = []
    BValues = []
    logFCs = []
    GeneSymbols = []
    GeneTitles = []
    GeneIDs = []
    with open(r"Data from GEO2R - One Experimental Group.csv", newline='') as cfile: ##replace filepath
        genomedata = csv.DictReader(cfile)
        for row in genomedata:
            if (row['Gene.symbol']!=""):
                IDList.append(row['ID'])
                AdjP.append(float(row['adj.P.Val']))
                PList.append(float(row['P.Value']))
                tValues.append(float(row['t']))
                BValues.append(float(row['B']))
                logFCs.append(float(row['logFC']))
                GeneSymbols.append(row['Gene.symbol'])
                GeneTitles.append(row['Gene.title'])
                GeneIDs.append(row['Gene.ID'])
            
def initFilteredArrays():
    FilteredIDs = []
    FlogFCs = []
    FGeneSymbols = []
    FGeneTitles = []
    for p in range(len(PList)):
        if (PList[p]>0.99):
            FilteredIDs.append(IDList[p])
            FlogFCs.append(logFCs[p])
            FGeneSymbols.append(GeneSymbols[p])
            FGeneTitles.append(GeneTitles[p])
            
def plotFilteredArrays():            
    plt.bar(FilteredIDs, FlogFCs, width = 0.4)
    plt.xlabel("ID")
    plt.ylabel("logFC")
    plt.savefig(saveinfopath)

def printTableData():
    tabledata = []
    for i in range(len(FilteredIDs)):
        tabledata.append([FilteredIDs[i],FlogFCs[i],FGeneSymbols[i],FGeneTitles[i]])
    head = ["ID","logFC","Gene Symbols","Gene Titles"]
    print(tabulate(tabledata, headers=head))

def SortIDs():
    logssorted = sorted(FlogFCs)[:5]+sorted(FlogFCs)[-5:]
    SortedIDs = []
    for i in range(len(logssorted)):
        for j in range(len(tabledata)):
            if((tabledata[j][1])==(logssorted[i])):
                print(tabledata[j][0],"added")
                SortedIDs.append(tabledata[j][0])
                break

def plotSortedIDs():
    plt.bar(SortedIDs,logssorted)
    plt.title("Genomes with largest magnitude logFC values")
    plt.xticks(fontsize=5)
    plt.xlabel("ID")
    plt.ylabel("logFC")
    plt.savefig(savefigpath2)

def initLogssorted():
    logssorted = [abs(element) for element in FlogFCs]
    logssorted = sorted(logssorted)
    SortedIDs = []
    SortedGenes = []
    SortedTitles = []
    for i in range(len(logssorted)):
        for j in range(len(tabledata)):
            if((abs(tabledata[j][1]))==logssorted[i]):
                SortedIDs.append(tabledata[j][0])
                SortedGenes.append(tabledata[j][2])
                SortedTitles.append(tabledata[j][3])
                tabledata[j][1] = 0 #to prevent duplicates
                break

def writeSortedTableData():
    sortedtabledata = []
    for i in range(len(FilteredIDs)):
        for j in range(len(FilteredIDs)):
            if (logssorted[i]==abs(FlogFCs[j])):
                sortedtabledata.append([SortedIDs[i],FlogFCs[j],SortedGenes[i],SortedTitles[i]])
                break
    sortedtabledata.insert(0,['ID','logFC','Gene.Symbol','Gene.Title'])

    with open('Downloads/output.csv','w', newline='') as f:
        writer=csv.writer(f)
        writer.writerows(sortedtabledata)
    
def writeSortedDataAsCSV(filepathwrite):
    with open('Downloads/output_with_shortened_list.csv', newline='') as o:
        interestgenes = csv.DictReader(o)
        SortedIDs = []
        SortedGenes = []
        SortedTitles = []
        logssorted = []
        for row in interestgenes:
            SortedIDs.append(row["ID"])
            SortedGenes.append(row["Gene.Symbol"])
            SortedTitles.append(row["Gene.Title"])
            logssorted.append(float(row["logFC"]))
        
def initFVals():
    for i in range(len(SortedIDs)):
        for j in range(len(IDList)):
            if(SortedIDs[i]==IDList[j]):
                FAdjP.append(AdjP[j])
                FPList.append(PList[j])
                FtValues.append(tValues[j])
                FBValues.append(BValues[j])
                break
        
def plotCompleteInterestSet():
    for i in range(len(SortedIDs)):
        completeinterestset.append([SortedIDs[i],FAdjP[i],FPList[i],FtValues[i],FBValues[i],logssorted[i],SortedGenes[i],SortedTitles[i]])
    plt.bar(SortedGenes[:9],logssorted[:9])
    plt.xlabel("Gene.Symbol")
    plt.xticks(fontsize=8)
    plt.ylabel("logFC")
    plt.savefig(savefigpath3)
    completeinterestset.insert(0,["ID","Adj.P.Val","P.Value","t","B","logFC","Gene.Symbol","Gene.Title"])

def writeCompleteInterestSetCSV(filepathwrite):
    with open('Downloads/InterestedOutput.csv','w', newline='') as fo:
        writer=csv.writer(fo)
        writer.writerows(completeinterestset)