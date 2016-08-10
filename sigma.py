#!usr/bin/env python3
# -*- coding:utf-8 -*-
# sigma.py
#
############################################################
#   This module functions as the Sigma engine. 
#   It fasciliates functionality to make meaning 
#   out of urls. 
#
#   The Sigma Engine is currently used by the webinterface (__init__.py), 
#   but it is designed such that it is independent of it's 
#   user interface. One could integrate this module in 
#   other programs, even those without a user interface.
#
#   -- Robin
#############################################################
import codecs

try:
    import cPickle as pickle
except:
    import pickle

from werkzeug import secure_filename
import requests
import requests_cache
from bs4 import BeautifulSoup
import classification

try:
    ## Python 3
    from urllib.parse import urlparse
except:
    ## Python 2
    from urlparse import urlparse

# from urlparse import urlparse

# This will make outguing web requests be cached. 
# if a url is downloaded twice, only the first time will grab it off the internet.
# the second time from a local stored cache.
requests_cache.install_cache("sigma-dev-0.1")
# Builds a topic classifier
api_key = classification.get_api_key()
# Make it
classifier = classification.TopicsClassifier(api_key)




#####################################
#       API / INTERFACE
#   These methods are the interface 
#   between the flask(webinterface) 
#   and the sigma engine.
#####################################

def save_link(id, meta, user):
    """ 
        Responsible for putting the link somewhere safe. 
        associated with the user.

        id:
            the id of the url (currently the id IS the url)
        meta:
            a dict full of metadata about this url.
        user:
            the username string.
    """
    # strips hacker attempts away from input. 
    linksfile = secure_filename('%s.links'%(user))
    

    # First, read the list of links from the users link file. 
    try:
        with codecs.open(linksfile, 'r+') as userfile: 
            links = pickle.loads(userfile.read())
    except:
        # If the file does not exist, create an empty list of links.
        links = {}

    links[id] = meta

    with codecs.open(linksfile, 'w+') as userfile: 
        userfile.write(pickle.dumps(links))




def get_links(user):
    """ 
        Responsible for retrieveing the links from somewhere safe. 
        associated with the user.
    """
    # secure_filename('some.file') strips hacker attempts away from input. 
    linksfile = secure_filename('%s.links'%(user))

    # Here we should check if file exists with -> os.path.isfile(path)

    try:
        with codecs.open(linksfile) as userfile: 
            links = pickle.loads(userfile.read())
    except IOError:
        links = {}
    return links


def fetch_meta(url, filter=None):
    """ 
            Responsible for scraping all the metadata from a given url.
            
            filter:
                a list of data-fields to return:
                example:
                    filter=['title', 'favicon']
                    filter=['all']

            List of fields:
            
                title
                favicon
                domain
                description
                topics

            Symbolic filter list:
                all:  returns all fields

    """

    link = LinkMeta(url)
    link.parse()

    # returns the local variables in this functions scope as a 
    # dict.
    return link







def fetch_title(url):
    """ 
            Responsible for retrieveing the  title of a url. 
            based on graph.py.
    """
    # validate url.
    if "http" not in url or len(url) <= 11:
       return ""
    r = requests.get(url)
    if r:
        soup = BeautifulSoup(r.text, 'html.parser')
        try:
            title = soup.select("title")[0].string
        except:
            title=""
    else:
        title=""
    return title





########################################
#   CLASSES
########################################

class LinkMeta():
    """ A class to hold meta info about a link """
    def  __init__(self, url):
        self.url = url
        self.urlparts = urlparse(url)


    def classify_topics(self):
        topics = classifier.classify(self.url)
        #topics = classifier.classify(self.url, depth=2)
        return topics


    def parse(self):
        """ Extracting intels about ze link for you madamme / sir. """
        
        r = requests.get(self.url)
        if r:
            self.title = fetch_title(self.url)
            self.domain = self.fetch_domain()
            self.favicon = self.fetch_favicon()
            self.topics = self.classify_topics()
            self.description = self.fetch_description()
        return self


    def fetch_domain(self):
        return self.urlparts.netloc.split(":")[0]


    def fetch_description(self):
        description = ""

        r = requests.get(self.url)
        if r:
            soup = BeautifulSoup(r.text, 'html.parser')
            # First get the meta description tag
            meta_desc = soup.find('meta', attrs={'name':'og:description'}) or soup.find('meta', attrs={'property':'description'}) or soup.find('meta', attrs={'name':'description'})

            # If description meta tag was found, then get the content attribute and save it to db entry
            if meta_desc:
                description = meta_desc.get('content').encode('utf-8')
        return description


    def fetch_favicon(self):
        """ 
            favicons.ico are supposed to be at the top folder of a websites domain.
            forexample http://komsys.org/favicon.ico

            This is also the case if the url in question is deeper down, as in the
            example:
            http://komsys.org/15/26/how-to-be-a-cool-engineer

            So this function does the following:
            1. Attempts to fetch the favicon on http://<domain>/favicon.ico
            2. returns this url if it got an icon, or an empty string if not.
        """    
        favurl = "%s://%s/favicon.ico" % (self.urlparts.scheme, self.domain)
        r = requests.get(favurl)
        if r:
            return favurl
        else:
            return ""




    def __repr__(self):
        """ Defaults to textual representation """
        return self.textual_representation().encode("utf-8")


    def textual_representation(self):
        if self.urlparts.fragment is not "":
            return "%s - %s\n%s" % (self.title, self.urlparts.fragment, self.domain)
        else:
            return "%s\n%s" % (self.title,  self.domain)







if __name__ == '__main__':
    #testing saving a linksfile:
    #save_link(url="http://hw.no.com", user="technocake")

    #print( get_links('technocake') )

    # Schumanns Sonate
    #print( fetch_title("https://www.youtube.com/watch?v=ruV4V5mPwW8"))


    link = fetch_meta("https://www.youtube.com/watch?v=ruV4V5mPwW8")
    print( link.title )
    print( link.domain )
    print( link.favicon )
    print( link.topics )
    print( link.description )
