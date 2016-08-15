#!/usr/bin/python
# coding:utf-8

# utility.py -- working with maps offline
import os
import sigma
from sigma import KnowledgeMap, Topic

def convert_v1_to_v2(user, mapid, the_map):
	"""
		Converts from map structure v1 to v2 
	"""
	new_dict = {}
	for subtopic, links in the_map.subtopics.items():
		if "urls" in links:
			print("Already converted from v1. skipping.")
			return
		new_dict[subtopic] = {'urls': links, 'subtopics': {}}
	the_map.subtopics = new_dict
	sigma.save_map(user, mapid, the_map)


def make_minimum_configuration():
	"""
		Generates the minimum required configuration to run
		the web-interface out of the box
	"""

	try:
		SECRET_KEY = ''.join('%02x' % ord(x) for x in os.urandom(16)) # python2
	except:
		SECRET_KEY = ''.join('%02x' % x for x in os.urandom(16)) # python3

	with open("config.py", "w") as configfile:
		configfile.write("SECRET_KEY='%s'\n"%SECRET_KEY)


def load_config(app):
	"""
		Loads or creates and loads configuration from config.py. 
	"""
	try:
		app.config.from_object('config')
	except:
		make_minimum_configuration()
		app.config.from_object('config')


	if "WEBROOT" in app.config:
		import os
		# Changes the running directory of
		# the application to the same folder
		# as the python files.  This way
		# import statements will work. 
		os.chdir(app.config["WEBROOT"])
	return app





if __name__ == '__main__':
	make_minimum_configuration()
	#user = "jonas"
	#for mapid, the_map in sigma.get_maps(user).items():
	#	print("Converting map: %s from v1 to v2..." % mapid)
	#	convert_v1_to_v2(user, mapid, the_map)