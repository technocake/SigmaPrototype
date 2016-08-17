from sigma import KnowledgeMap

python_map = KnowledgeMap("Python")
jsonmap = python_map.to_json()
print(jsonmap)


# Adding a subtopic without url
python_map.update("variables")
# with a url
python_map.update("code-conventions", "https://www.python.org/dev/peps/pep-0020/")

#add another url to already existing subtopic
python_map.update("variables", "http://usingpython.com/python-variables/")
#result:

print(python_map.to_json())