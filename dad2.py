import numpy as np
import csv as csv
import pandas as pd


def most_common(lst):
	# print list.count(lst)
	return max(set(lst), key=lst.count)

def main():
	readdata = csv.reader(open("outlookExport.CSV"))

	data = []

	for row in readdata:
	  data.append(row)

	Header = data[0]
	data.pop(0)

	Header.append("Difference")

	#for i in range(len(data)):
	 # diff = int(data[i][2]) - int(data[i][1])
	  #data[i].append(diff)


	subject = []
	fromList = []
#	toList = []
	for i in range(len(data)):
	  subject.append(data[i][0])
	  fromList.append(data[i][2])
	  #toList.append(data[i][4])

	#print "Total in 1910: %d" % len(pop1910)

	#print most_common(toList)
	print most_common(fromList)
	print most_common(subject)


main()

#print "Average in 1910: %d" % (np.mean(pop1910))
#print "Standard Deviation in 1910: %d" % (np.std(pop1910)) 


#print pd.DataFrame(data, columns = Header)
