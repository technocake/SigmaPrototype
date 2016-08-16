#### Sigma API references


#  Sigma API urls 
These urls are used by clients to speak with the sigma engine. These are not meant to be used by users directly.
Data is represented in JSON, both in requests by clients and responses from the server. 

### Things that are about knowledgemaps
- /[getmap](getmap.md) -- returns a knowledgemap by its mapid
- /[mapnames](mapnames.md) -- Gives a list of the users maps, map names only.
- /[updatemap](updatemap.md) -- Used to add a subtopic and or urls in a map.
- /[relabeltopic](relabeltopic.md) -- Changes a subtopics text in a map.

### Things that are for searching and autosuggestions
- /[tags](tags.md)  -- returns a flat list of the users tags( topics / subtopics from maps)
- /[fetchsearchdata](fetchsearchdata.md)  -- returns a nested list of searchable data + links. Grouped per link.


### Things that are about links
- /[postmeta](postmeta.md) -- updates a url's metadata    
- /[deletelink](deletelink.md) -- removes a url from the system.
- /[fetchtitle](fetchtitle.md) -- returns the title belonging to  a URL.
- /[fetchmeta](fetchmeta.md)  -- returns alot of metadata beloning to a URL.
- /[fetchlinks](fetchlinks.md) -- returns the list of all links belonging to a user.


##  Web user-interface urls
 These urls are part of the built-in web-client of the sigma prototype. This is what users are directly seeing and using.
-  /    
-  /logout 
-  /login
-  /meny 
-  /inputurl
-  /maps
-  /<user>/map/<mapid>
-  /<user>/map/<mapid>/thumbnail
-  /postuser
    
