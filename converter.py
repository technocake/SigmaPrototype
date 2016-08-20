#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sigma import KnowledgeMap
from sigma import Topic
import re #for search

class Converter():
	def __init__(self):
		print("")

	def extract(self, line):
		text = re.search('TEXT="(.+?)"', line).group()
		text = re.search('"(.+?)"', text).group()
		text = text.replace('"', "")
		text.strip()

		return text

	def convert(self, file):

		freemind_file = open(file, 'r')

		#Creates an instance of KnowledgeMap with name of KnowledgeMap as filename
		name = freemind_file.name
		new_map = KnowledgeMap(name)

		#Used to establish a maintopic
		maintopic_found = False

		#The text extracted from the file. Main variable
		text = ""
	
		#Used if the converter finds a link -> adds to the last topic
		last_topic = None

		#Used to tell the converter if the text extracted from .mm file is a link
		link = False

		#Used for long nodes in .mm files
		text_found = False
		last_line = ""

		#Reads line by line
		for line in freemind_file:
			if 'node CREATED=' in line:
				#Check if its a long node in freemind; if "TEXT=" not in line then its a long node
				if "TEXT=" in line:
					text_found = True
					#Extract text to variable text
					text = self.extract(line)

					#Temporary solution to check if the node contains link
					if "http://" or "https://" in text:
						link = True
				else:
					text_found = False

				if text_found == True:
					text_found = False
					if maintopic_found == False:
						maintopic = Topic(text)
						new_map.change_main_topic(maintopic)
						maintopic_found = True
					else:
						#Create subtopic using variable text
						#add to map
						if link == True:
							link = False
							new_map.update(last_topic, text)
							last_topic.add_url(text)
						else:
							new_topic = Topic(text)
							new_map.update(new_topic)
							last_topic = new_topic


			elif '<p>' in line:
				last_line = '<p>'

			elif last_line == '<p>':
				text = line
				#removing leading and ending spaces
				text.strip()

				#Check if its subtopic or link
				if text_found == False:
					text_found = True
					new_topic = Topic(text)
					new_map.update(new_topic)
					last_topic = new_topic

				else:
					new_map.update(last_topic, text)

				text = ""
				last_line = ""

		freemind_file.close()
		return new_map

