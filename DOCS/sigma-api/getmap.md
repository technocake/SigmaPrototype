

## POST /getmap

## Description
Returns a knowledgemap identified by it's mapid.

***

## Requires authentication
**login_required**

***

## Parameters
Essential information:

- **mapid** — the url to the link that will have it's data updated.

### Optional attributes:

***

## Return format
Status code 200, along with a JSON array containing 
- **status** — Either OK or NOT OK
- **map** — a dict containing a knowledge map.
***

## Errors
- **status** — NOT OK
- **error** — Error message

***

## Example
**Request**

    POST /getmap

**Payload**
``` json
{
 "mapid": "Python"
}
```


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
  "status": "Getmap OK"
}

```
