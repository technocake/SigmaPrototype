#### Sigma API references


#  Sigma API urls 
These urls are used by clients to speak with the sigma engine. These are not meant to be used by users directly.
Data is represented in JSON, both in requests by clients and responses from the server. 

    10. /[postmeta](postmeta.md) -- updates a url's metadata
    11. /[getmap](getmap.md) -- returns a knowledgemap by its mapid
    12. /[mapnames](mapnames.md) -- Gives a list of the users maps, map names only.
    13. /[updatemap](updatemap.md) -- Used to add a subtopic and or urls in a map.
    14. /[relabeltopic](relabeltopic.md) -- Changes a subtopics text in a map.
    15. /[tags](tags.md)  -- returns a flat list of the users tags( topics / subtopics from maps)
    16. /[deletelink](deletelink.md) -- removes a url from the system.
    17. /[fetchtitle](fetchtitle.md) -- returns the title belonging to  a URL.
    18. /[fetchmeta](fetchmeta.md)  -- returns alot of metadata beloning to a URL.
    19. /[fetchlinks](fetchlinks.md) -- returns the list of all links belonging to a user.


##  Web user-interface urls
 These urls are part of the built-in web-client of the sigma prototype. This is what users are directly seeing and using.
    1.  /    
    2.  /logout 
    3.  /login
    4.  /meny 
    5.  /inputurl
    6.  /maps
    7.  /<user>/map/<mapid>
    8.  /<user>/map/<mapid>/thumbnail
    9.  /postuser
    
