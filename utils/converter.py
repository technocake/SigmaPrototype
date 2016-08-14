#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
	File       : converter.py
	Description: This is a converter. 

"""

import sys
import re

def convert(file):

	#Have to figure out how to delete last comma in end_file

	freemind_file = open(file, 'r')
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
					json_file.write("]},\n")
			else:
				json_file.write("]},\n")

	print(json_file.name + " created.")

convert(sys.argv[1])

