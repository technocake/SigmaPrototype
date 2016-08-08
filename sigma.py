#!usr/bin/env python3
# -*- coding:utf-8 -*-
import codecs
import cPickle
from werkzeug import secure_filename

# sigma.py

def save_link(url, user):
	""" 
		Responsible for putting the link somewhere safe. 
		associated with the user.
	"""
	# strips hacker attempts away from input. 
	linksfile = secure_filename('%s.links'%(user))
	

	# First, read the list of links from the users link file. 
	try:
		with codecs.open(linksfile, 'r+') as userfile: 
			links = cPickle.loads(userfile.read())
	except:
		# If the file does not exist, create an empty list of links.
		links = []

	links.append(url)

	with codecs.open(linksfile, 'w+') as userfile: 
		userfile.write(cPickle.dumps(links))




def get_links(user):
	""" 
		Responsible for retrieveing the links from somewhere safe. 
		associated with the user.
	"""
	# strips hacker attempts away from input. 
	linksfile = secure_filename('%s.links'%(user))

	try:
		with codecs.open(linksfile) as userfile: 
			links = cPickle.loads(userfile.read())
	except IOError:
		links = []
	return links


if __name__ == '__main__':
	#testing saving a linksfile:
	save_link(url="http://hw.no.com", user="technocake")

	print( get_links('technocake') )
