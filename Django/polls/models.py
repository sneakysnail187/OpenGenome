from django.db import models

class Result(models.Model):
    authorName = models.CharField(max_length=30,null = False, blank = False)
    experimentTitle = models.CharField(max_length = 200,null = False, blank = False, primary_key=True)
    targetGenes = models.CharField(max_length = 200,null = False, blank = False)
    experimentNotes = models.TextField()
    csvFile = models.FileField(upload_to = 'ResultsCSV', blank = True, null = True)
    plot = models.ImageField(upload_to = 'Plots', blank = True, null = True)
    def __str__(self):
        return self.experimentTitle


class Comment(models.Model):
    post = models.ForeignKey(Result, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length = 30,null = False, blank = False)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    #meta data to order comments
    class Meta:
        ordering = ['created_on']
    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.name)


class Plots(models.Model):
    plot = models.ImageField()

class UserCSV(models.Model):
    csv = models.FileField(upload_to = 'SubmittedCSV', blank = True, null = True)
    name = models.CharField(max_length = 200,null = True, blank = True)
    def __str__ (self):
        return '{}'.format(self.name)

class CSVNames(models.Model):
    csvName = models.CharField(max_length = 200, null = True, blank = True)
    def __str__(self):
        return self.csvName
    