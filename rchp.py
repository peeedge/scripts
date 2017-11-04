import os,sys,glob,pprint,build_utils

if len(sys.argv) > 1:
	root_dir = build_utils.getRootDir()    

	# Read in the input
	with open('Web.config', 'r') as input :
	  inputdata = input.read()

	replaceValue = sys.argv[1]
	# Replace the target string
	inputdata = inputdata.replace('value="http://localhost:4200"', 'value="http://localhost:' + replaceValue + '"')

	# Write the input out again
	with open('Web.config', 'w') as input:
	  input.write(inputdata)

	print
	print "***Replaced customHeaders port number with '" + replaceValue +"'***"