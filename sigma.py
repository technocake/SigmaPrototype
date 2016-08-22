#!usr/bin/env python3
# -*- coding:utf-8 -*-
# sigma.py
#

"""
    Navn: sigma.py
    Prosjekt: SigmaPrototype
    Opprettet av: Robin
    Beskrivelse: sigma.py fungerer som model for hele Sigma systemet. 
                Modellen har ansvar for å holde på data, som kart og linker, 
                og eksponere et api for å kunne utføre operasjoner på dataene.
                opperere / hente / lagre / endre. 
                og. 
                 Den brukes av REST API-et som har ansvar over opptatt av å oversette
                 data fra modellen til json og snakke med klienter.
                                         ----- Robin -----"""

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


import json
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
        links = get_links(user)
    except:
        # If the file does not exist, create an empty list of links.
        codecs.open(linksfile, 'w+').close()
        links = {}

    links[id] = meta

    with codecs.open(linksfile, 'wb') as userfile: 
        pickle.dump(links, userfile) # simpler syntax
        # userfile.write(pickle.dumps(links, userfile))



def get_links(user):
    """ 
        Responsible for retrieveing the links from somewhere safe. 
        associated with the user.
    """
    # secure_filename('some.file') strips hacker attempts away from input. 
    linksfile = secure_filename('%s.links'%(user))

    # Here we should check if file exists with -> os.path.isfile(path)

    try:
        with codecs.open(linksfile, 'rb') as userfile: 
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


def update_map(user, main_topic, subtopic, url=None):
    """
        Updates and or creates a Knowledge map with id <main_topic>
        returns true if a map was created, false if not.
    """
    # does the knowledge map exists?
    new = False
    the_map = get_map(user, main_topic)

    if the_map is None:
        the_map = KnowledgeMap(main_topic)
        new = True

    the_map.update(subtopic, url)
    save_map(user, main_topic, the_map)
    return new



def save_map(user, mapid, the_map):
    """
        Saves a knowledgemap
    """
    mapsfile = secure_filename('%s.maps'%(user))
    maps = get_maps(user)

    for k,v in maps.items():
        mapdict = v.__dict__
        maps[k] = mapdict
    maps[mapid] = the_map.__dict__

    with codecs.open(mapsfile, 'wb') as userfile: 
        pickle.dump(maps, userfile) 





def get_map(user, mapid, jsonable=False):
    """
        Retrieves a requested map
    """

    maps = get_maps(user)
    the_map = maps.get(mapid, None)
    if jsonable:
        return sigmaserialize(the_map)
    return the_map


def get_maps(user, jsonable=False):
    """ 
        Retrieves all maps from user
    """
    mapsfile = secure_filename('%s.maps'%(user))
    try:
        with codecs.open(mapsfile, 'rb') as userfile: 
            dict_maps = pickle.loads(userfile.read())
            # Due to a issue with pickling a class
            # in a sub module and depickling in the flask module
            # the stored data is the __dict__ of the Knowledgemap
            # This is then converted to a Knowledgemap object.
            maps = {}
            for k,v in dict_maps.items():
                the_map = KnowledgeMap()
                the_map.__dict__ = v
                maps[k] = the_map
    except Exception as e:
        # If the file does not exist, create an empty list of links.
        maps = {}
    if jsonable:
        return sigmaserialize(maps)
    return maps


def save_permissions(user, mapid, permissions):
    """
        Saves a permissions beloning to a map.
    """
    permsfile = secure_filename('%s.permissions'%(user))
    perms = get_all_permissions(user)

    for k,v in perms.items():
        permdict = v.__dict__
        perms[k] = permdict
    perms[mapid] = permissions.__dict__

    with codecs.open(permsfile, 'wb') as userfile: 
        pickle.dump(perms, userfile) 


def get_all_permissions(user, jsonable=False):
    """
        Returns all  permissions beloning to all  maps of the user.
        PARAMS
            user:
                username string.
            jsonable:
                  True --> returns data as pure dicts.
                  False --> returns data as SharingPermission objects in a dict.
    """
    permsfile = secure_filename('%s.permissions'%(user))
    try:
        with codecs.open(permsfile, 'rb') as userfile: 
            perms_dict = pickle.loads(userfile.read())
            # Due to a issue with pickling a class
            # in a sub module and depickling in the flask module
            # the stored data is the __dict__ of the Object.
            # This is then converted to a SharingPermission object.
            perms = {}
            for k,v in perms_dict.items():
                the_perms = SharingPermissions()
                the_perms.__dict__ = v
                perms[k] = the_perms
    except Exception as e:
        # If the file does not exist, create an empty list of links.
        perms = {}
    if jsonable:
        return sigmaserialize(perms)
    return perms


def get_map_permissions(user, mapid, jsonable=False):
    """
        Returns  permissions beloning to one map.
        PARAMS
            user:
                username string.
            mapid:
                mapid string
            jsonable:
                  True --> returns data as pure dicts.
                  False --> returns data as SharingPermissions object.
    """
    
    perms = get_all_permissions(user)
    the_perms = perms.get(mapid, None)
    if jsonable:
        return sigmaserialize(the_perms)
    return the_perms



def update_permissions(user, mapid, permissions):
    """
        Updates and or creates a SharingPermissions object for the 
        map with id <mapid>
        returns true if a new object was created, false if not.

        PARAMS:
            user: string of username
            mapid: string mapid
            permissions: dict with permissions
    """
    # does the object exists?
    new = False
    the_perms = get_map_permissions(user, mapid)

    if the_perms is None:
        the_perms = SharingPermissions(mapid)
        new = True

    the_perms.update(permissions)
    save_permissions(user, mapid, the_perms)
    return new




def get_searchdata(user, filter=None):
    """
        Builds a search-able datastructure of the users maps and links 
        and returns it to the client. This is meant to provide data for
        client-side searching.
    """
    maps = get_maps(user)
    links = get_links(user)

    searchdata = []
    for the_map in maps.values():
        topic = the_map.main_topic
        for subtopic in the_map.subtopics.values():
            for url in subtopic.urls.values():
                # title from metadata
                title = links.get(url, {}).get("title", "")
                searchdata.append([topic, subtopic.text, title, url])
    return searchdata


def relabel_topic(user, map_id, old_topic_text, new_topic_text):
    """
        Renames a subtopic text in a  Knowledge map with id <map_id>
        throws KeyError if map or subtopic doesnt exist.
    """
    the_map = get_map(user, map_id)
    the_map.relabel_topic(old_topic_text, new_topic_text)
    save_map(user, map_id, the_map)


def move_url(user, map_id, url, old_topic_text, new_topic_text):
    """
        Moves a url from one subtopic to another. 
    """
    the_map = get_map(user, map_id)
    the_map.move_url(url, old_topic_text, new_topic_text)
    save_map(user, map_id, the_map)


def delete_link(user, mapid, subtopic, url): #in context of a map.
    """ 
        Deletes a link from a map at the given subtopic node.
    """
    the_map = get_map(user, mapid)
    links = the_map.subtopics[subtopic].urls
    links.pop(url)
    the_map.subtopics[subtopic].urls = links
    save_map(user, mapid, the_map)


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



#########   -----   TAGS ------ ##############


def get_tags(user):
    maps = get_maps(user)
    links = get_links(user)
    tags = []

    for the_map in maps.values():
        tags.append(the_map.main_topic)
        for topic in the_map.subtopics.keys():
            tags.append(topic)

    for linkmeta in links:
        pass #tags.append(linkmeta.title) utf-8 not json serializable...
    return tags
    

########################################
#   CLASSES
########################################
class SigmaObject():
    """ 
        General class that all other sigma objects inherits from. 
        This is to signal that the derived class is a SigmaObject.
        This is usefull when these objects are going to be serialized
        (converted into) JSON-strings or Pickle-strings. 
    """
    
    def to_json(self):
        """
            Serializes classes inherting from SigmaObject into JSON.

            example:  python_map = KnowledgeMap("Python")
            jsonmap = python_map.to_json()
            print(jsonmap) -->
        """
        return json.dumps(sigmaserialize(self), indent=4)


class LinkMeta(SigmaObject):
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
                description = meta_desc.get('content')
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



class KnowledgeMap(SigmaObject):
    """ The class to hold a knowledge map """
    def __init__(self, main_topic=None, description=None):
        self.main_topic = main_topic
        self.description = description
        self.subtopics = {} # expects a dict of Topic instances


    def update(self, subtopic, url=None):
        """ 
            Adds or updates a subtopic node
            optional url associated with subtopic.
        """
        if isinstance(subtopic, Topic):
            # This makes it possible to send in
            # Topic instances in addition to plain 
            # strings.
            self.subtopics[subtopic.text] = subtopic
            return
        if subtopic in self.subtopics.keys():
            links = self.subtopics[subtopic].urls
        else:
            links = {}
            # Creating a new subtopic
            self.subtopics[subtopic] = Topic(text=subtopic, urls=links)
        if url is not None:
            links[url] = url
        # Updating the subtopic
        self.subtopics[subtopic].urls = links


    def relabel_topic(self, old_topic_text, new_topic_text):
        """
            Relabels a topic. 

        """
        topic = self.subtopics.pop(old_topic_text)
        topic.text = new_topic_text
        if new_topic_text in self.subtopics:
            # new subtopic already exists,
            # Appending the links.
            for k, v in topic.urls.items():
                self.subtopics[new_topic_text].urls[k] = v
        else:
            self.subtopics[new_topic_text] = topic


    def change_main_topic(self, main_topic):
        """
            Changes the main topic of this map.
            PARAMS:
                - main_topic:
                    string containing the main topic.
        """
        self.main_topic = main_topic


    def move_url(self, url, from_node, to_node):
        """
            Moves a url belonging to a node to another node, 
            leaving other stuff intact. 

            PARAMS:
                      url = string url to be moved
                from_node = subtopic string of the source node
                  to_node = subtopic string of the target node
        """
        link = self.subtopics[from_node].urls.pop(url)
        self.update(to_node, link)


    def create_subtopic(self, subtopic):
        """
            Creates a new subtopic. 

            PARAMS:
                subtopic: string
        """
        self.subtopics[subtopic] = Topic(subtopic)


    #For testing purposes with the converter
    def to_string(self):
        result = 'Main topic : ' + self.main_topic.text + "\n"

        for topic in self.subtopics:
            result += 'Sub topic :' + self.subtopics[topic].text + "\n"
            for link in self.subtopics[topic].urls:
                result += 'Resource : ' + link + "\n"
    

        return result


   # All classes inheriting from SigmaObject will 
   # get a to_json() method for free. Removed the custom
   # to_json method. However, I got to notice it had 
   # a powerfull "direct to the point" approach, like it.




class Topic(SigmaObject):
    """ 
        Representing a topic or subtopic. 
        contains - 
        
        text
            the textual value of the topic
            example: "Variables", "running-shoes"
        urls
            dictionary of urls associated to this node
            example: {"http://example.com": "http://example.com"}
        subtopics
            dictionary of subTopic's 
            example: {
                Topic(text="Integer", urls={"http://example.com/integers"}), 
                Topic(text="Floats", urls={"http://example.com/float"}), 
            }
    """
    def __init__(self, text, urls=None, subtopics=None):
        self.text = text
        self.urls = {} if urls is None else urls
        self.subtopics = {} if subtopics is None else subtopics


    def add_url(self, url):
        self.urls[url] = url
    


class SharingPermissions(SigmaObject):
    """
        Holding sharing permisions for a users' map. 

        Currently only public/private is beeing used.
    """
    def __init__(self, mapid=None, global_permissions=None):
        """
            Builds a permissions object for a map. 
            basically now it is - "Is the map private or public?"
            More finegrained access control can be added later, like:
                - "has user A access to this map? "
        """
        self.mapid = mapid
        if global_permissions is None:
            self.permissions = {"global": "private"}
        else:
            self.permissions = global_permissions


    def update(self, permissions):
        """ 
            Updates a sharing permissions for a map.
        """
        # Updating the subtopic
        self.permissions = permissions


    def __getitem__(self, permissiontype):
        """ 
            makes it possible to do  perms = SharingPermissions()
            perms["global"] --> "private"
        """
        return self.permissions[permissiontype]



#   ----    HACKS   -------

def sigmaserialize(obj):
    """
        This function makes it possible to use
        json.dumps() to take an object with nested classes 
        and turn it into a json string.

        For example, a KnowledgeMap object contains 
        Topic objects in the subtopics field. json.dumps
        won't by default know how to take a custom class 
        and turn it into json. This function converts the
        object and all objects within it to pure python
        dictionaries. json.dumps knows how to translate
        python dicts into json strings by default. 

        Therefore it should be used as an intermediary 
        step into converting an SigmaObject into json:

        0.  import json
        1.  m = KnowledgeMap()
        2.  map_as_dict = sigmaserialize(m)
        3.  map_as_json_string = json.dumps(map_as_dict)


        However, all SigmaObject inheriting classes have a 
        to_json() method, that does this. So this simplifies
        the syntax for the above KnowledgeMap example to:

        map_as_json_string = m.to_json()

    """
    if isinstance(obj, SigmaObject):
        obj = obj.__dict__

    if isinstance(obj, dict):
        for k,v in obj.items():
            obj[k] = sigmaserialize(v)
    #if isinstance(obj, list) or isinstance(obj, tuple):
    #   for i, v in enumerate(obj):
    #       obj[i] = sigmaserialize(v)


    return obj


if __name__ == '__main__':
    from test_sigma import *
    test_get_searchdata()