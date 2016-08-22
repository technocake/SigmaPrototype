# Sigma tester
from sigma import *


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



def test_get_map():
    """
        Scenario: 
            A map is saved, retrieve it. 
    """
    m = get_map(user, "Python")



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
    m = KnowledgeMap("Test")
    m.update("subtopic1")
    m.update("subtopic2")
    m.update("subtopic2", "http://komsys.org")

    save_map(user, "Test", m)



def test_share_and_unshare():
    """
        Share a map from User A with user B.
    """
    mapid = "Test"
    
    # test share
    share(user, mapid, "jonas")
    perms = get_map_permissions(user, mapid)
    assert "jonas" in perms.shared_with, "Map permissions not updated after shareing."

    # test unshare
    unshare(user, mapid, "jonas")
    perms = get_map_permissions(user, mapid)
    assert "jonas" not in perms.shared_with, "Map permissions not updated after un-shareing."


def test_get_owner():
    """
        who owns the map?
        assumes make_and_save_test_map has been run.
    """
    
    # test 1)   symbolic mapid of format <user>/mapid
    mapid = "%s/Test" % user
    owner = get_owner(user, mapid)
    assert owner == user, "SYMBOLIC mapid failed"

    
    # test 2)   getting owner from a map not existing
    error = ""
    try:
        mapid = "NOT-exists"
        owner = get_owner(user, mapid)
    except Exception as e:
        error = str(e)
    assert error == "Unknown Owner", "non existing map returned owner."


    # test 3)   getting a users map.
    mapid="Test"
    owner = get_owner(user, mapid)
    assert owner == user, "mapid failed"


def cleanup():
    """
        removes test data
    """
    # delete_map(user, "Test")
    pass


if __name__ == '__main__':
    # setup
    make_and_save_test_map()
    
    test_get_map()
    test_move_url()
    test_relabel_topic()
    test_get_searchdata()
    test_scenario_one()
    test_get_searchdata()
    # Permissions
    test_get_permissions()
    test_save_permissions()
    test_update_permissions()
    test_get_all_permissions()

    # Sharing
    test_share_and_unshare()
    test_get_owner()
    cleanup()