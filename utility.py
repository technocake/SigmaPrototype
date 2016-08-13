#!/usr/bin/python
# coding:utf-8

# utility.py -- working with maps offline
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





if __name__ == '__main__':
	user = "jonas"
	for mapid, the_map in sigma.get_maps(user).items():
		print("Converting map: %s from v1 to v2..." % mapid)
		convert_v1_to_v2(user, mapid, the_map)