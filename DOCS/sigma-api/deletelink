

## POST deletelink

## Description
updates a subtopic in a map.

***

## Requires authentication
**login_required**

***

## Parameters
Essential information:


- **map_id** — The id of the map (main topic).
- **subtopic** — the subtopic having the url.
- **url** — the url to be deleted.

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

    POST /deletelink

**Payload**
``` json
{
  "map_id": "Javascript",
  "subtopic": "arrays",
  "url": "http://example.com/array/method/bad-introduction.xhtml"
}
```


**Return**
``` json
{
  "status": "OK",
}
```
