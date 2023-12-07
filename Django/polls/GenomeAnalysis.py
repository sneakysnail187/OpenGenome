import csv
from tabulate import tabulate
import matplotlib.pyplot as plt
#savefigpath = "./uploads/plots/PFilteredLogFC.png"
#savefigpath2 = "./uploads/plots/LargestLogFCs.png"
#savefigpath3 = "./uploads/plots/InterestLogFCs.png"
def loadCSV(csvpath): #initial csv insert, tied to open analysis, needs csv path
    IDList = []
    AdjP = []
    PList = []
    tValues = []
    BValues = []
    logFCs = []
    GeneSymbols = []
    GeneTitles = []
    GeneIDs = []
    with open(csvpath, newline='') as cfile: ##replace filepath
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
    return IDList,AdjP,PList,tValues,BValues,logFCs,GeneSymbols,GeneTitles,GeneIDs
    

def plotPFilteredlogs(pDesired, IDList, PList, logFCs, GeneSymbols, GeneTitles, fileLocation):
    FilteredIDs = []
    FlogFCs = []
    FGeneSymbols = []
    FGeneTitles = []
    for p in range(len(PList)):
        if (PList[p]>pDesired): #maybe make this editable? setting statistical threshold
            FilteredIDs.append(IDList[p])
            FlogFCs.append(logFCs[p])
            FGeneSymbols.append(GeneSymbols[p])
            FGeneTitles.append(GeneTitles[p])
    plt.figure()
    plt.bar(FilteredIDs, FlogFCs, width = 0.4)
    plt.title("P-Filtered Genomes")
    plt.xlabel("ID")
    plt.ylabel("logFC")
    plt.savefig(fileLocation)
    tabledata = []
    for i in range(len(FilteredIDs)):
        tabledata.append([FilteredIDs[i],FlogFCs[i],FGeneSymbols[i],FGeneTitles[i]])
    return FilteredIDs, FlogFCs, FGeneSymbols, FGeneTitles, tabledata

def logMag(menuOption, num, FlogFCs, tabledata, saveDestination):
    if (menuOption==3):
        greatestMag(num, FlogFCs, tabledata,saveDestination)
    if (menuOption==2):
        negLogs(num, FlogFCs, tabledata,saveDestination)
    if (menuOption==1):
        posLogs(num, FlogFCs, tabledata,saveDestination)

def greatestMag(num, FlogFCs, tabledata,saveDestination):
    logssorted = sorted(FlogFCs)[:num]+sorted(FlogFCs)[-num:]
    SortedIDs = []
    for i in range(len(logssorted)):
        for j in range(len(tabledata)):
            if((tabledata[j][1])==(logssorted[i])):
                print(tabledata[j][0],"added")
                SortedIDs.append(tabledata[j][0])
                break
    plt.figure()
    plt.bar(SortedIDs,logssorted)
    plt.title("Genomes with largest magnitude logFC values")
    plt.xticks(fontsize=5)
    plt.xlabel("ID")
    plt.ylabel("logFC")
    plt.savefig(saveDestination)

def negLogs(num, FlogFCs, tabledata,saveDestination):
    logssorted = sorted(FlogFCs)[:num]
    SortedIDs = []
    for i in range(len(logssorted)):
        for j in range(len(tabledata)):
            if((tabledata[j][1])==(logssorted[i])):
                print(tabledata[j][0],"added")
                SortedIDs.append(tabledata[j][0])
                break
    plt.figure()
    plt.bar(SortedIDs,logssorted)
    plt.title("Genomes with largest negative logFC values")
    plt.xticks(fontsize=5)
    plt.xlabel("ID")
    plt.ylabel("logFC")
    plt.savefig(saveDestination)

def posLogs(num, FlogFCs, tabledata,saveDestination):
    logssorted = sorted(FlogFCs)[-num:]
    SortedIDs = []
    for i in range(len(logssorted)):
        for j in range(len(tabledata)):
            if((tabledata[j][1])==(logssorted[i])):
                print(tabledata[j][0],"added")
                SortedIDs.append(tabledata[j][0])
                break
    plt.figure()
    plt.bar(SortedIDs,logssorted)
    plt.title("Genomes with largest positive logFC values")
    plt.xticks(fontsize=5)
    plt.xlabel("ID")
    plt.ylabel("logFC")
    plt.savefig(saveDestination)

def shortCSV(IDInput, IDList, GeneSymbols, logFCs, GeneTitles, AdjP, PList, tValues, BValues,savePlace): #this should be reserved for user filtered csvs, prints out the Interest gene logs and tabluates full set 
    SortedGenes = []
    SortedTitles = []
    logssorted = []
    FAdjP = []
    FPList = []
    FtValues = []
    FBValues = []
    for i in range(len(IDInput)):
        for j in range(len(IDList)):
            if(IDInput[i]==IDList[j]):
                SortedGenes.append(GeneSymbols[j])
                SortedTitles.append(GeneTitles[j])
                logssorted.append(logFCs[j])
                FAdjP.append(AdjP[j])
                FPList.append(PList[j])
                FtValues.append(tValues[j])
                FBValues.append(BValues[j])
                break
    print(SortedGenes)
    plt.figure()
    plt.bar(SortedGenes,logssorted)
    plt.title("Interest Gene logFCs")
    plt.xlabel("Gene.Symbol")
    plt.xticks(fontsize=8)
    plt.ylabel("logFC")
    plt.savefig(savePlace)
    completeinterestset = []
    for i in range(len(IDInput)):
        completeinterestset.append([IDInput[i],FAdjP[i],FPList[i],FtValues[i],FBValues[i],logssorted[i],SortedGenes[i],SortedTitles[i]])
    return completeinterestset