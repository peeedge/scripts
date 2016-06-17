import numpy as np
import csv as csv
import pandas as pd
from collections import Counter
import pprint

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


	# subject = []
	fromList = []
	bodyList = []
	htmlText = ""
	bodyWordsList = []
	for i in range(len(data)):
	  # subject.append(data[i][0])
	  fromList.append(data[i][2])
	  # bodyList.append(data[i][1])

	  # bodyList.append(data[i][1])
	  # bodyWordsList = data[i][1].split()
	  # bodyList.extend(bodyWordsList)
	#print "Total in 1910: %d" % len(pop1910)

	# print Counter(fromList)
	# print pprint.pformat(Counter(fromList))

	for key, value in Counter(fromList).items():
		htmlText += ' %s emailed you ' % key
		htmlText += '  %d times \n' % value
	# htmlLines = []
	# for textLine in pprint.pformat(Counter(fromList)).splitlines():
	#     htmlLines.append('<br/>%s' % textLine) # or something even nicer
	# htmlText = '\n'.join(htmlLines)

	print htmlText

	# print Counter(fromList).keys()
	# print Counter(fromList).values()

	# # print most_common(bodyList)
	# print most_common(fromList)
	# print set(fromList)
	# print most_common(subject)


main()

#print "Average in 1910: %d" % (np.mean(pop1910))
#print "Standard Deviation in 1910: %d" % (np.std(pop1910)) 


#print pd.DataFrame(data, columns = Header)
