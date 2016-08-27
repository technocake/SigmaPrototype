# Sigma tester
from sigma import *
import sigma

"""	###############################################
		TEST CONFIG
""" ###############################################
user = "technocake"

def test_move_url():
    """ 
        KnowledgeMap.move_url(url, from, to)
        Should move a url from one subtopic to another.
    """
    move_url = "http://example.com/move-me"
    # Building map, adding two subtopics.
    the_map  = KnowledgeMap("Python")
    the_map.update("variables", "http://example.com/variables")
    the_map.update("variables", move_url)
    the_map.update("PEPs", "http://example.com/peps-are-a-good-source-to-diving-into-python")

    # Performing the move.
    the_map.move_url(move_url, "variables", "PEPs")

    # Checking results
    assert move_url not in the_map.subtopics["variables"].urls, 'URL still in source-node.'
    assert move_url in the_map.subtopics["PEPs"].urls, 'URL not in target-node.'


def test_relabel_topic():
    """
        KnowledgeMap.relabel_topic(old_topic_text, new_topic_text)
        Relabels a subtopics text. 
    """
    the_map = KnowledgeMap("Python")
    the_map.update("variables")
    the_map.relabel_topic("variables", "data-structures")
    assert "data-structures" in the_map.subtopics, "relabel topic failed, new subtopic not made."
    assert "variables" not in the_map.subtopics, "relabel topic failed, old subtopic still there."


def test_get_searchdata():
	""" 

	"""
	print( get_searchdata(user) )



def test_scenario_one():
	 # Save the map
    our_first_map = KnowledgeMap('Python', "basic python mind map")
    map_id = our_first_map.main_topic
    save_map(user, map_id, our_first_map)
   # print(map_id, our_first_map.__dict__)
    
    our_second_map = KnowledgeMap('Java', "basic Java mind map")
    map_id = our_second_map.main_topic
    save_map(user, map_id, our_second_map)


    # Get it back
    
    
    our_first_map.update('functions', "http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/functions.html")

    update_map(user, "Python", "functions", "http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/functions.html") 

    update_map(user, "Python", "functions", "http://www.cse.msu.edu/~cse231/Online/functions.html")


    relabel_topic(user, "Python", "functions", "methods")
    python = get_map(user, "Python")
    #print (python.subtopics["methods"])    
    # Get all maps
  #  print( get_maps(user))
    relabel_topic(user, "Python", "methods", "functions")
    delete_link(user, "Python", "functions", "http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/functions.html")
    #print ( get_map(user, "Python").subtopics["functions"])


def test_delete_map():
    mapid = "TestTest"
    m = KnowledgeMap(mapid)
    save_map(user, mapid, m)

    delete_map(user, mapid)
    assert mapid not in get_maps(user), "Should be deleted"


def test_get_map():
    """
        Scenario: 
            A map is saved, retrieve it. 
    """
    make_and_save_test_map()

    # Case 1: accessing local map
    m = get_map(user, "Test")
    assert m is not None, "Getting local mapid failed."
    
    # Case 2:  accessing global id of self owned map should return local map.
    mapid = MapID("Test", user)
    m = get_map(user, str(mapid))
    assert m is not None, "Getting global mapid didnt resolve to existing local map."


def test_get_maps():
    """
        Scenario: 
            A map is saved, retrieve it. 
    """
    maps = get_maps(user)
    assert isinstance(maps, dict), "get_maps Should return dict"


def test_get_permissions():
    """
        should return a dict with default
        permissions on non-existing map. 
    """
    # Non-existing perms
    #perms = get_map_permissions(user, "THIS-MAP-DOES-NOT-EXIST")
    #assert perms is None, "Permissions on non existing map should return None."

    # Changed behavior to just create it. simplifies explorating dev.
    
    # Make sure some perms are in here
    test_save_permissions()
    perms = get_map_permissions(user, "Python")
    assert perms is not None, "Should get som perms."

    ##  Resolving mapids, there
    ##  should be only one SharingPermission object per map.
    mapid = "technocake--Python"
    mid = "Python"
    
    
    perms = get_map_permissions("technocake", mapid)
    perms2 = get_map_permissions("technocake", mid)


    assert perms == perms2, "Global mapid should resolve to local mapid: owner--mapid --> mapid data: " % (perms.mapid, perms2.mapid)

    
def test_scenario_get_perms_of_shared_map():
    ##  This also applies for shared maps.
    make_and_save_test_map()

    mapid = "technocake--Test"
    mid = "Test"
    owner = "technocake"
    user = "andre"

    share(owner, mapid, user)

    perms = get_map_permissions("andre", mapid)
    assert user in perms.shared_with, "Map not shared"
    assert perms.mapid == mid, "Permission object should be for mid not global mapid (Test instead of technocake--Test)"




def test_scenario_shared_map_gets_more_links():
    """
        Both owner and the new user update of the map
        should be synced. 
    """
    test_scenario_get_perms_of_shared_map()
    mapid = "technocake--Test"
    mid = "Test"
    owner = "technocake"
    user = "andre"
    url1 = "http://funkify.it"
    url2 = "http://funkify.it/lol"
    # Case 1 . owner adds a link
    update_map(owner, mid, "added-by-owner", url1)

    # user B
    assert url1 in get_map(user, mapid).urls, "Added link to shared map did not propagate to shared users."
    assert url1 in get_links(user), "Added link to shared map did not propagate to shared users."
    # user B
    assert url1 in get_map(owner, mid).urls, "Added link to shared map did not propagate to shared users."
    assert url1 in get_links(owner), " Added link to shared map did not propagate to shared users."


def test_make_default_perms():
    """
        Should generate a SharingPermissions object for a map adn save it. 
    """
    sigma._make_default_perms("technocake", "Does-not-exist-really")
    assert get_map_permissions("technocake", "Does-not-exist-really") is not None, "Did not make default object for perms."


def test_save_permissions():
    """
        Makes some global permissions and save it.
    """
    mapid= "Python"
    perms = SharingPermissions(mapid, {"global": "public"})
    save_permissions(user, mapid, perms)
    

def test_update_permissions():
    """
        Change some global permissions 
    """
    mapid= "Python"
    update_permissions(user, mapid, {"global": "public"})
    perms = get_map_permissions(user, mapid)
    assert perms["global"] == "public", "Update permissions failed." 


def test_get_all_permissions():
    """
        Should return a dict.
    """
    # make sure there is perms in here:
    test_save_permissions()

    perms = get_all_permissions(user)
    perms = get_all_permissions(user, True)
    print( perms )


def make_and_save_test_map():
    """ 
        Used to build mock-data
    """
    update_map(user, "Test", "subtopic1")
    update_map(user, "Test", "subtopic2")
    update_map(user, "Test", "subtopic2",   "http://komsys.org")


def test_mapid():
    the_id = MapID("technocake--Test")
    assert str(the_id) == "technocake--Test", "representation of mapid is wrong."



def test_mapid_is_global():
    the_id = MapID("technocake--Test")
    assert the_id.is_global(), "Should be flagged as global"
    the_id = MapID("Test")
    assert the_id.is_global() is not True, "Should not be flagged as global"


def test_share_and_unshare():
    """
        Share a map from User A with user B.
    """
    owner = "technocake"
    user = "jonas"
    mid = "Test"
    mapid = str(MapID(mid, owner)) # technocake--Test

    # test share
    share(owner, mid, user)
    
    perms = get_map_permissions(owner, mid)
    assert user in perms.shared_with, "Map permissions not updated after shareing."

    # owner gets own local map
    the_map = get_map(owner, mid)
    assert the_map is not None, "Local Map retrieve failed for owner"

    # owner gets own global map
    the_map = get_map(owner, mapid)
    assert the_map is not None, "Global Map retrieve failed for owner"

    # shared map retrieved by global id by the user that was shared with.
    the_map = get_map(user, mapid)
    assert the_map is not None, "Global Map retrieve failed for shared user"

    # user wont get by local id.  
    # should resolv in a non-existent map. 
    # (since user B does not have a map with the same name as the one
    # from user A)
    the_map = get_map(user, mid)
    assert the_map is None, "Local Map retrieve of owners map should fail for shared user "


    #### Dont save username--maps
    ###
    #
    maps = get_maps(user)
    _id = MapID("use-me-for-delim-character")

    for mid, m in maps.items():
        if _id.delim in mid:
            if MapID(mid).owner != user:
                assert m == "SYMBOLIC",  "Stored a symbolic map, oh noes. data: %s "%(mid, m.__dict__) 

    # test unshare
    unshare(user, mapid, "jonas")
    perms = get_map_permissions(user, mapid)
    assert "jonas" not in perms.shared_with, "Map permissions not updated after un-shareing."




def test_is_new_map():
    assert is_new_map(user, "doesnotexist") == True, "Should be new"


def cleanup():
    """
        removes test data
    """
    # delete_map(user, "Test")
    pass




if __name__ == '__main__':
    # setup
    make_and_save_test_map()
    
    # MapID
    test_mapid()
    test_mapid_is_global()

    test_get_map()
    test_get_maps()
    test_move_url()
    test_relabel_topic()
    test_get_searchdata()
    test_scenario_one()
    test_get_searchdata()
    test_is_new_map()
    test_delete_map()
    
    # Permissions
    test_make_default_perms()
    test_get_permissions()
    test_save_permissions()
    test_update_permissions()
    test_get_all_permissions()

    # Sharing
    test_share_and_unshare()
    cleanup()
    test_scenario_get_perms_of_shared_map()
    test_scenario_shared_map_gets_more_links()