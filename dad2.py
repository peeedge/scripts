# import numpy as np
import csv as csv
# import pandas as pd
from collections import Counter
import pprint
import sys

# class WriteToOutput(object):
#     def __init__(self, filename="Default.log"):
#         self.terminal = sys.stdout
#         self.log = open(filename, "a")

#     def write(self, message):
#         self.terminal.write(message)
#         self.log.write(message)

# sys.stdout = WriteToOutput("output.html")

def most_common(lst):
	# print list.count(lst)
	return max(set(lst), key=lst.count)

def from_frequency(data):
	Header = data[0]
	data.pop(0)

	Header.append("Difference")

	fromList = []
	output = ""
	
	for i in range(len(data)):
	  fromList.append(data[i][2])

	dictionary = Counter(fromList)
	sortedDictionary = sorted(dictionary.items(), key=lambda i: i[1], reverse=True)

	output += "<table><thead><th>From</th><th>How Many Times</th></thead><tbody>"

	for key, value in sortedDictionary:
		output += '<tr><td>%s</td>' % key
		output += '<td>%d</td></tr>' % value

	output += "</tbody></table>"

	with open("output.html", "w") as my_file:
		my_file.write(output)

def main():
	readdata = csv.reader(open("outlookExport.CSV"))

	data = []

	for row in readdata:
	  data.append(row)

	from_frequency(data)


main()