#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
	File       : converter.py
	Description: This is a converter. 

"""

import sys
import re
import os # Needed to check if the file exist and get the file extension

def convert(file):

	#Have to figure out how to delete last comma in end_file

	freemind_file = open(file, 'r')
	
	# Split the filename into name incl. path, and the file extension
	# Just assumes the file format is correct if the file extension is ".mm"
	#if os.path.ntsplitext(freemind_file)[1] == ".mm":  This does not work on my machine (Win.7 x64), variable type error? Commented out for now
	print(freemind_file.name)
	name = freemind_file.name
	name = name[:-2]
	name = name + "json"
	json_file = open(name, 'w')
	done = True
	just = False

	for line in freemind_file:
		if line.startswith('<node CREATED='):
			text1 = re.search('TEXT="(.+?)"', line).group()
			text2 = re.search('"(.+?)"', text1).group()

			if "/>" in line:
				if done == False:
					json_file.write(',\n')
				
				line_towrite = '{"resource":' + str(text2) + "}"
				json_file.write(line_towrite)
				
				done = False
			
			else:
				line_towrite = '{' + str(text2) + ':[\n'
				json_file.write(line_towrite)
				done = True
				just = False

		elif line.startswith('</node>'):
			#How to delete last comma in end_file
			if done == False:
				if just == False:
					json_file.write("\n]},\n")
					just = True
				else:
					#if done==False:
					json_file.write("]},\n") # This is the call that creates the last comma & newline
			else:
				json_file.write("]},\n")

	print(json_file.name + " created.")


	# Når en fil åpnes i Python så er det
	#  viktig å stenge den også.
	#   Dette er ikke noe Python gjør automatisk.
	#                     --- Jonas ---
	# ---------------------------------

	freemind_file.close()
	json_file.close()
	
	# ---------------------------------
#else:
#	print("Sorry, unknown file type")


# Check if the argument array has the required length (argv[0] is the application name, argv[1] is the added file's name)
if len(sys.argv) > 1:
	argument = sys.argv[1]
	
	# Check if the argument points to an existing file.
	# We risk a "No such file or directory" error otherwise
	if os.path.exists(argument):
		convert(sys.argv[1])
	else:
		print("Status 2: File does not exist") # Sounds ok?
else:
	print("Status 1: No file is defined") # Sounds ok?