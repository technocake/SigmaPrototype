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

	start_file = open(file, 'r')
	name = start_file.name
	name = name[:-2]
	name = name + "json"
	end_file = open(name, 'w')
	done = True

	for line in start_file:
		if line.startswith('<node CREATED='):
			if line.endswith('/>'):
				if done == False:
					end_file.write(', ')
					text1 = re.search('TEXT="(.+?)"', line).group()
					text2 = re.search('"(.+?)"', text1).group()
					line_towrite = '"resource":' + str(text2)
					end_file.write(line_towrite)
				else:
					text1 = re.search('TEXT="(.+?)"', line).group()
					text2 = re.search('"(.+?)"', text1).group()
					line_towrite = '{"resource":' + str(text2)
					end_file.write(line_towrite)
				
				done = False
			
			else:
				if done == False:
					end_file.write('}\n')

				text1 = re.search('TEXT="(.+?)"', line).group()
				text2 = re.search('"(.+?)"', text1).group()
				line_towrite = '{' + str(text2) + ':[\n'
				end_file.write(line_towrite)
				done = True

		elif line.startswith('</node>'):
			#How to delete last comma in end_file
			end_file.write("]},\n")

	end_file.write("]},\n")

	print(end_file.name + " created.")

convert(sys.argv[1])

