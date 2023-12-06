from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import polls.global_ as g

#functions for rendering the individual html pages 
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

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

def upload(request):
    if request.method == 'POST':
        input_csv = request.FILES['csvFile']
        new_csv = UserCSV(csv = input_csv)
        new_csv.save()
        #g.submittedCSVFileNames.append(new_result.csvFile.name)
        #files = g.submittedCSVFileNames
        new_csv_name = CSVNames(csvName = input_csv.name)
    fileNames = list(CSVNames.objects.all().distinct())
    for name in fileNames:
        print(name)
    context = {"name" : fileNames}

    return render(request, 'upload.html', context)

#results needs to pull from db, where postpage uploads to db
#   urlName = 'http://127.0.0.1:8000' + submittedCsvFileNames[x] <!-- x here is the index chosen from the dropdown bar-->