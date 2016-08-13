## POST fetchsearchdata

## Description
Builds a search-able datastructure of the users maps and links and returns it to the client.
This is meant to provide data for client-side searching. User is implicit implied through the
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
``` json
{
  "status": "OK",
  "searchdata":  [ // Map level - contains a lists of Maps data
                  [  // this is the first Map
                    [Python, functions, http://example.com/python-functions],
                    [Python, syntax, http://example.com/python-syntax],
                    
                  ]
                  
}
```

