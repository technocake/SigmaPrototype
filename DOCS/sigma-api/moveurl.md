[Back to index](api-reference.md)


## POST moveurl

## Description
 Moves a url from one subtopic to another. 


***

## Requires authentication
**login_required**

***

## Parameters
Essential information:


- **map_id** — The id of the map (main topic).
- **url** — the url to be moved.
- **old** — the old subtopic text.
- **new** — the new subtopic text.

### Optional attributes:

***

## Return format
Status code 200, along with a JSON array containing 
- **status** — Either OK or NOT OK

***

## Errors
- **status** — NOT OK
- **error** — Error message

***

## Example
**Request**

    POST /moveurl

**Payload**
``` json
{
  "map_id": "Javascript",
  "url": "http://example.com/tralala",
  "old": "arrays",
  "new": "array methods"
}
```


**Return**
``` json
{
  "status": "Moveurl OK",
}
```
