[Back to index](api-reference.md)

## GET /getmaps

## Description
Returns a dictionary of all the knowledgemap associated with a user.

***

## Requires authentication
**login_required**

***

## Parameters
Essential information:


### Optional attributes:

***

## Return format
Status code 200, along with a JSON array containing 
- **status** — Either OK or NOT OK
- **map** — a dict containing all knowledge maps associated with a user.
- **mapid** — the mapid of the map
***

## Errors
- **status** — NOT OK
- **error** — Error message

***

## Example
**Request**

    GET /getmaps


**Return**
``` json
{
  "map": {
    "description": "basic python mind map", 
    "main_topic": "Python", 
    "subtopics": {
      "functions": {
        "subtopics": {}, 
        "text": "functions", 
        "urls": {
          "http://www.cse.msu.edu/~cse231/Online/functions.html": "http://www.cse.msu.edu/~cse231/Online/functions.html"
        }
      }
    }
  }, 
  "map_id": "technocake/Python"
  "status": "Getmap OK"
}

```
