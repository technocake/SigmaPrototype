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

	for line in freemind_file:
		if line.startswith('<node CREATED='):
			if "/>" in line:
				if done == False:
					json_file.write(', ')
					text1 = re.search('TEXT="(.+?)"', line).group()
					text2 = re.search('"(.+?)"', text1).group()
					line_towrite = '"resource":' + str(text2)
					json_file.write(line_towrite)
				else:
					text1 = re.search('TEXT="(.+?)"', line).group()
					text2 = re.search('"(.+?)"', text1).group()
					line_towrite = '{"resource":' + str(text2)
					json_file.write(line_towrite)
				
				done = False
			
			else:
				if done == False:
					json_file.write('}\n')

				text1 = re.search('TEXT="(.+?)"', line).group()
				text2 = re.search('"(.+?)"', text1).group()
				line_towrite = '{' + str(text2) + ':[\n'
				json_file.write(line_towrite)
				done = True

		elif line.startswith('</node>'):
			#How to delete last comma in end_file
			json_file.write("]},\n")

	json_file.write("]},\n")

	print(json_file.name + " created.")

convert(sys.argv[1])

