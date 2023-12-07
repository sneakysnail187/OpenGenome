from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import polls.global_ as g

#functions for rendering the individual html pages 
def index(request):
    return render(request, 'index.html')

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

csvToAnalyze = ''
def upload(request):
    if request.POST.get("button_type") == "submit_files":
            input_csv = request.FILES['csvFile']
            new_csv = UserCSV(csv = input_csv, name = input_csv.name)
            new_csv.save()
    if request.POST.get("button_type") == "analyze":
            csvToAnalyze = request.POST['fileName']
            print(csvToAnalyze)
    #context dictionary for dropdown menu
    fileNames = UserCSV.objects.all().distinct()
    #for name in fileNames:
        #print(name)
    context = {"names" : fileNames}

    return render(request, 'upload.html', context)

def results(request):
    return render(request, 'results.html')
#results needs to pull from db, where postpage uploads to db
#   urlName = 'http://127.0.0.1:8000' + submittedCsvFileNames[x] <!-- x here is the index chosen from the dropdown bar-->