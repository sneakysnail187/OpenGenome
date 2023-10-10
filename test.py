import numpy as np
from numpy import loadtxt
from Bio.Affy import CelFile
import csv

#with open ("GSM7585785_31116_HF-30512_RA_SPR856_HGU133P.CEL", "r") as handle:
#   c = CelFile.read(handle)

#print(c.ncols, c.nrows)
#print(c.intensities)
#print(c.stdevs)
#print(c.npix)


#puts everything into the array numbers
numbers = []
f = open('GSE236924_series_matrix.txt', 'r')
for line in f:
    line = line.strip()
    line.replace(r"\t", ' ')
    words = line.split()
    for w in words:
        if any(c.isdigit() for c in w):
            numbers.append(w)
f.close

#testing to see what is in numbers at certain points
A = numbers[10000:10010]
#print(A)

#writes every index of numbers into csv in excel format
with open ('test.csv', 'w', newline= '') as g:
  writer = csv.writer(g, dialect= 'excel')
  for lines in numbers:
      JD = lines
      writer.writerow([JD])

# so far this gets every single thing with numbers in it and puts that shit in a csv
#does not tell you what any of the values are or are related to and just makes one HUUUGE column of every single value (over 7 mill)