#!usr/bin/env python3
# -*- coding:utf-8 -*-
import codecs
import cPickle
from werkzeug import secure_filename
import requests
import requests_cache
from bs4 import BeautifulSoup
# This will make outguing web requests be cached. 
# if a url is downloaded twice, only the first time will grab it off the internet.
# the second time from a local stored cache.
requests_cache.install_cache("sigma-dev-0.1")


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


def fetch_title(url):
	""" 
			Responsible for retrieveing the  title of a url. 
	"""
	r = requests.get(url)
	if r:
		soup = BeautifulSoup(r.text, 'html.parser')
		try:
			title = soup.select("title")[0].string
		except:
			self.title=""
	else:
		self.title=""
	return title


if __name__ == '__main__':
	#testing saving a linksfile:
	#save_link(url="http://hw.no.com", user="technocake")

	print( get_links('technocake') )

	# Schumanns Sonate
	print( fetch_title("https://www.youtube.com/watch?v=ruV4V5mPwW8"))
