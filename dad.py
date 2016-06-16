import numpy as np
import csv as csv
import pandas as pd

readdata = csv.reader(open("outlookExport.CSV"))

#for row in readdata:
  #print row

data = []

for row in readdata:
  data.append(row)

Header = data[0]
data.pop(0)

print pd.DataFrame(data, columns=Header)

