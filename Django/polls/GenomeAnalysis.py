import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
#savefigpath = "./uploads/plots/PFilteredLogFC.png"
#savefigpath2 = "./uploads/plots/LargestLogFCs.png"
#savefigpath3 = "./uploads/plots/InterestLogFCs.png"
def loadCSV(csvpath): #initial csv insert, tied to open analysis, needs csv path
    df = pd.read_csv(csvpath)#replace filepath
    IDList = []
    AdjP = []
    PList = []
    tValues = []
    BValues = []
    logFCs = []
    GeneSymbols = []
    GeneTitles = []
    GeneIDs = []
    IDList = df['ID'].tolist()
    AdjP = df['adj.P.Val'].tolist()
    PList = df['P.Value'].tolist()
    tValues = df['t'].tolist()
    BValues = df['B'].tolist()
    logFCs = df['logFC'].tolist()
    GeneSymbols = df['Gene.symbol'].tolist()
    GeneTitles = df['Gene.title'].tolist()
    GeneIDs = df['Gene.ID'].tolist()
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
    plt.bar(FilteredIDs, FlogFCs, width = 0.4)
    plt.title("P-Filtered Genomes")
    plt.xlabel("ID")
    plt.ylabel("logFC")
    #plt.show()
    plt.savefig(fileLocation)
    tabledata = []
    for i in range(len(FilteredIDs)):
        tabledata.append([FilteredIDs[i],FlogFCs[i],FGeneSymbols[i],FGeneTitles[i]])
    return FilteredIDs, FlogFCs, FGeneSymbols, FGeneTitles, tabledata

def logMag(menuOption, num, FlogFCs, tabledata):
    if (menuOption==1):
        greatestMag(num, FlogFCs, tabledata)
    if (menuOption==2):
        negLogs(num, FlogFCs, tabledata)
    if (menuOption==3):
        posLogs(num, FlogFCs, tabledata)

def greatestMag(num, FlogFCs, tabledata):
    logssorted = sorted(FlogFCs)[:(num/2)]+sorted(FlogFCs)[-(num/2):]
    SortedIDs = []
    for i in range(len(logssorted)):
        for j in range(len(tabledata)):
            if((tabledata[j][1])==(logssorted[i])):
                print(tabledata[j][0],"added")
                SortedIDs.append(tabledata[j][0])
                break
    plt.bar(SortedIDs,logssorted)
    plt.title("Genomes with largest magnitude logFC values")
    plt.xticks(fontsize=5)
    plt.xlabel("ID")
    plt.ylabel("logFC")
    plt.show()

def negLogs(num, FlogFCs, tabledata):
    logssorted = sorted(FlogFCs)[:(num/2)]
    SortedIDs = []
    for i in range(len(logssorted)):
        for j in range(len(tabledata)):
            if((tabledata[j][1])==(logssorted[i])):
                print(tabledata[j][0],"added")
                SortedIDs.append(tabledata[j][0])
                break
    plt.bar(SortedIDs,logssorted)
    plt.title("Genomes with largest negative logFC values")
    plt.xticks(fontsize=5)
    plt.xlabel("ID")
    plt.ylabel("logFC")
    plt.show()
    #plt.savefig(savefigpath2)

def posLogs(num, FlogFCs, tabledata):
    logssorted = sorted(FlogFCs)[-(num/2):]
    SortedIDs = []
    for i in range(len(logssorted)):
        for j in range(len(tabledata)):
            if((tabledata[j][1])==(logssorted[i])):
                print(tabledata[j][0],"added")
                SortedIDs.append(tabledata[j][0])
                break
    plt.bar(SortedIDs,logssorted)
    plt.title("Genomes with largest negative logFC values")
    plt.xticks(fontsize=5)
    plt.xlabel("ID")
    plt.ylabel("logFC")
    plt.show()
    #plt.savefig(savefigpath2)

def shortCSV(IDInput, IDList, GeneSymbols, logFCs, GeneTitles, AdjP, PList, tValues, BValues): #this should be reserved for user filtered csvs, prints out the Interest gene logs and tabluates full set 
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
    plt.bar(SortedGenes,logssorted)
    plt.title("Interest Gene logFCs")
    plt.xlabel("Gene.Symbol")
    plt.xticks(fontsize=8)
    plt.ylabel("logFC")
    plt.show()
    #plt.savefig(savefigpath3)
    completeinterestset = []
    for i in range(len(IDInput)):
        completeinterestset.append([IDInput[i],FAdjP[i],FPList[i],FtValues[i],FBValues[i],logssorted[i],SortedGenes[i],SortedTitles[i]])
    interesthead = ["ID","Adj.P.Val","P.Value","t","B","logFC","Gene.Symbol","Gene.Title"]
    print(tabulate(completeinterestset, headers=interesthead))