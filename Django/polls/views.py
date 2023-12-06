from django.shortcuts import render
from django.http import HttpResponse
from .models import *

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

def analysis(request):
    if request.method == 'POST':
        input_csv = request.FILES['csvFile']
        new_csv = UserCSV(csv = input_csv)
        new_csv.save()

    return render(request, 'analysis.html')


#results needs to pull from db, where postpage uploads to db
#