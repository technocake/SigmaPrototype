# Sigma tester
from sigma import *


"""	###############################################
		TEST CONFIG
""" ###############################################
user = "technocake"



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



if __name__ == '__main__':
	test_get_searchdata()
	test_scenario_one()
	test_get_searchdata()