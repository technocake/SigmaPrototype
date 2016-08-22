#!usr/bin/env python3
# -*- coding:utf-8 -*-

# auth.py
import sigma
users = ["technocake", "jonas", "carl henrik", "andre", "kjell", "amund", "oliwia", "lars"]


def authenticate(user, password):
	""" 
		This function is responsible to handle authentication reuquests.
	"""
	return user in users


def can_access(user, mapid):
	"""
		You have no authority! (or perhaps you do.)

		Used to check if a requested map is shared with user.
		  1. if user is owner, you may access it.
	 	  2. if user is in shared_with on someone else map, you may.
	 	  3 all other cases you may not.
	"""
	owner = sigma.get_owner(user, mapid)
	if user == owner:
		o, local_mapid = sigma.parse_mapid(mapid)
		if local_mapid in sigma.get_maps(owner).keys():
			return True
	perms = sigma.get_map_permissions(owner, mapid)
	if user in perms.shared_with:
		return True
	return False


if __name__ == '__main__':
	def test_can_access():
		assert can_access("technocake", "technocake/Test") == True, "Not worky."

	test_can_access()
	

