from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from django.urls import reverse_lazy
from .models import *
import polls.GenomeAnalysis as g
from tabulate import tabulate


#functions for rendering the individual html pages 

def index(request):
    return render(request, 'index.html')

def download_result_csv(request, result_id):
    result = get_object_or_404(Result, pk=result_id)
    file_path = result.csvFile.path
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = f'attachment; filename="{result.experimentTitle}"'
    return response

def download_result_plot(request, result_id):
    result = get_object_or_404(Result, pk=result_id)
    file_path = result.plot.path
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = f'attachment; filename="{result.experimentTitle}"'
    return response

def forum(request):
    _results = Result.objects.all()

    context={'results':_results}
    return render(request, 'forum.html',context)

def about(request):
    return render(request, 'about.html')

def analytics(request):
    return render(request, 'analytics.html')

def postpage(request):
    if request.method == 'POST':
        #grabs all the stuff from the html form
        author = request.POST['name']
        experimentName = request.POST['experimentName']
        targettedGenes = request.POST['targetGenes']
        expNotes = request.POST['comment']
        inputCsvFile = request.FILES['csvFile']
        plots = request.FILES['jpegFiles']

        #stores it as a new result and saves it to the result database
        new_result = Result(authorName = author, experimentTitle = experimentName, targetGenes = targettedGenes, experimentNotes = expNotes, csvFile = inputCsvFile, plot = plots)
        new_result.save()
    return render(request, 'postpage.html')


class viewer:
    csvToAnalyze = ''
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
    tabledata = []
    pVal = 0.99
    numElements = 0
    targetGenesString = ''
    GenesList = []
    pTestPngFilePath = ''
    magTest1PngFilePath = ''
    magTest2PngFilePath = ''
    magTest3PngFilePath = ''
    finalSetPngFilePath = ''



def upload(request):
    #                   button name =     value = 
    if request.POST.get("button_type") == "submit_files":
            input_csv = request.FILES['csvFile']
            new_csv = UserCSV(csv = input_csv, name = input_csv.name)
            new_csv.save()
    if request.POST.get("button_type") == "analyze":
            viewer.csvToAnalyze = request.POST['fileName']
            finString = viewer.csvToAnalyze.replace(" ", "_")
            #print(finString)
            csvPath = './uploads/SubmittedCSV/' + finString
            print(viewer.csvToAnalyze)
            #print(g.showPath(csvPath))
            viewer.IDList,viewer.AdjP,viewer.PList,viewer.tValues,viewer.BValues,viewer.logFCs,viewer.GeneSymbols,viewer.GeneTitles,viewer.GeneIDs = g.loadCSV(csvPath)
            
            

            

    #context dictionary for dropdown menu
    fileNames = UserCSV.objects.all().distinct()
    #for name in fileNames:
        #print(name)
    context = {"names" : fileNames}

    return render(request, 'upload.html', context)

def results(request):
    return render(request, 'results.html')

def analytics(request):
    #fileNames = UserCSV.objects.all().distinct()

    #finString = viewer.csvToAnalyze.replace(" ", "_")
    #pngString = finString.replace(".csv",".png")
    #pngPath = "./uploads/Plots/" + pngString
    #viewer.FilteredIDs, viewer.FlogFCs, viewer.FGeneSymbols, viewer.FGeneTitles, viewer.tabledata = g.plotPFilteredlogs(0.99,viewer.IDList,viewer.PList,viewer.logFCs,viewer.GeneSymbols,viewer.GeneTitles, pngPath)
    #head = ["ID","logFC","Gene Symbols","Gene Titles"]
    #tableName = "uploads/Tables/" + finString.replace(".csv", ".txt")
    
    #with open(tableName, 'w') as f:
       # f.write(tabulate(viewer.tabledata, headers = head))
       # f.close()

# POST --> grab the images --> viewer
# if exists pos.png --> render image
    #for magTest
    if request.method == 'POST':
        if request.POST.get("button_type") =="pTest":
            viewer.pVal = float(request.POST.get('pValue'))
            finString = viewer.csvToAnalyze.replace(" ", "_")
            pngString = finString.replace(".csv",".png")
            pngPath = "./uploads/Plots/" + pngString
            viewer.pTestPngFilePath = pngString
            viewer.FilteredIDs, viewer.FlogFCs, viewer.FGeneSymbols, viewer.FGeneTitles, viewer.tabledata = g.plotPFilteredlogs(viewer.pVal,viewer.IDList,viewer.PList,viewer.logFCs,viewer.GeneSymbols,viewer.GeneTitles, pngPath)
            head = ["ID","logFC","Gene Symbols","Gene Titles"]
            tableName = "./uploads/Tables/" + finString.replace(".csv", "Test.txt")
            with open(tableName, 'w') as f:
                 f.write(tabulate(viewer.tabledata, headers = head))
                 f.close()
        if request.POST.get("button_type")=='magTest':
            finString = viewer.csvToAnalyze.replace(" ", "_")
            viewer.numElements = int(request.POST.get('numElmentsInput'))
            if request.POST.get('radio') == '1':
                notsaveDestination=finString.replace(".csv","MagTest1.png")
                viewer.magTest1PngFilePath = notsaveDestination
                saveDestination = "./uploads/Plots/"+ notsaveDestination
                g.logMag(1, viewer.numElements, viewer.FlogFCs, viewer.tabledata, saveDestination)
            if request.POST.get("radio") == "2":
                notsaveDestination=finString.replace(".csv","MagTest2.png")
                viewer.magTest2PngFilePath = notsaveDestination
                saveDestination = "./uploads/Plots/"+ notsaveDestination
                g.logMag(2, viewer.numElements, viewer.FlogFCs, viewer.tabledata, saveDestination)
            if request.POST.get("radio") == "3":
                notsaveDestination=finString.replace(".csv","MagTest3.png")
                viewer.magTest3PngFilePath = notsaveDestination
                saveDestination = "./uploads/Plots/"+ notsaveDestination
                g.logMag(3, viewer.numElements, viewer.FlogFCs, viewer.tabledata, saveDestination)
        if request.POST.get("button_type") == 'targetGene':
             finString = viewer.csvToAnalyze.replace(" ", "_")
             viewer.finalSetPngFilePath = finString.replace(".csv","FinalSet.png")
             savePlace = "./uploads/Plots/" + finString.replace(".csv","FinalSet.png")
             viewer.targetGenesString = request.POST.get('targetGenes')
             viewer.GenesList = list(viewer.targetGenesString.split(", "))
             viewer.interesttable = g.shortCSV(viewer.GenesList,viewer.IDList,viewer.GeneSymbols,viewer.logFCs,viewer.GeneTitles,viewer.AdjP,viewer.PList,viewer.tValues,viewer.BValues,savePlace)
             interesthead = ["ID","Adj.P.Val","P.Value","t","B","logFC","Gene.Symbol","Gene.Title"]
             interesttableName = "./uploads/Tables/" + finString.replace(".csv", "Test2.txt")
             with open(interesttableName, 'w') as fi:
                 fi.write(tabulate(viewer.interesttable, headers=interesthead))
                 fi.close()

#
#
#
    context = {"csvName" : viewer.csvToAnalyze,
               "pTest" : viewer.pTestPngFilePath,
               "magTest1" : viewer.magTest1PngFilePath,
               "magTest2" : viewer.magTest2PngFilePath,
               "magTest3" : viewer.magTest3PngFilePath,
               "finalSet": viewer.finalSetPngFilePath}
    #print(viewer.csvToAnalyze)
    return render(request, 'analytics.html', context)


    #results needs to pull from db, where postpage uploads to db
    #   urlName = 'http://127.0.0.1:8000' + submittedCsvFileNames[x] <!-- x here is the index chosen from the dropdown bar-->