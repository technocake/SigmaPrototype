## POST fetchsearchdata

## Description
Builds a search-able datastructure of the users maps and links and returns it to the client.
This is meant to provide data for client-side searching. User is implied through the
session login.

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
- **searchdata** — N-Dimenisional array of topics and links.

***

## Errors
- **status** — NOT OK
- **error** — Error message

***

## Example
**Request**

    POST /fetchsearchdata

**Payload**
None


**Return**
** nb, json has no support for comments. Comments are added here to give a better overview of the data
``` json
{
  "status": "OK",
  "searchdata": [ 
                    // this is the first Map
                    ["Python", "functions", "http://example.com/python-functions"], // subtopic funtions has two links,
                    ["Python", "functions", "http://example.com/python-use-def"], // second link in subtopic functions
                    ["Python", "syntax", "http://example.com/python-syntax"] // only one link on subtopic syntax
                    // this is another map
                    ["Java", "functions", "http://example.com/java-functions"],
                    ["Java", "inventor", "http://example.com/James-gosling"]
                ]
}
```
