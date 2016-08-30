#!usr/bin/env python3
# -*- coding:utf-8 -*-

# auth.py
import sigma
robin_invited = ["amund", "oliwia", "lars", "lasseeli", "roverelk", "fredrik", "hatland", "vegar", "Myhres", "knutovsthus", "kim", "confusus", "per", "janne"]
jonas_invited = ["kjell"]
users = ["technocake", "jonas", "carl henrik", "andre"] + robin_invited + jonas_invited


def authenticate(user, password):
	""" 
		This function is responsible to handle authentication reuquests.
	"""
	return user in users


def can_create(user, mapid):
	"""
		jaup..
	"""
	owner, local_mapid = sigma.parse_mapid(mapid, user)
	return owner == user


def can_access(user, mapid):
	"""
		You have no authority! (or perhaps you do.)

		Used to check if a requested map is shared with user.
		  1. if user is owner, you may access it.
	 	  2. if user is in shared_with on someone else map, you may.
	 	  3 all other cases you may not.
	"""
	owner, local_mapid = sigma.parse_mapid(mapid, user)
	if user == owner:
		if local_mapid in sigma.get_maps(owner).keys():
			return True
	perms = sigma.get_map_permissions(owner, mapid)
	if user in perms.shared_with:
		return True
	return False


def can_update(user, mapid):
	"""
		Determines edit rights of a map.
		For now this is the same as read rights. 
		We like to be open in alfa prototypes.

		the first if handles the case when the map is not existing yet.
	"""
	
	if can_create(user, mapid) and sigma.is_new_map(user, mapid):
		return True
	else:
		return can_access(user, mapid)


if __name__ == '__main__':
	def test_can_access():
		assert can_access("technocake", "technocake/Test") == True, "Not worky."

	def test_can_create():
		assert can_create("technocake", "doesnotexist") == True, "Should be able to create new maps"

	def test_can_update():
		assert can_update("technocake", "doesnotexist") == True, "Should be able to create new maps"

	test_can_access()
	test_can_create()
	test_can_update()
	

