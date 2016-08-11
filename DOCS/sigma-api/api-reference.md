#### Sigma API references

# Knowledge Maps
### endpoints:


## POST updatemap

## Description
updates or creates a map.

***

## Requires authentication
**login_required**

***

## Parameters
Essential information:


- **main_topic** — The main topic of the map. 
- **subtopic** — a new or old subtopic of the map. 

### Optional attributes:
- **url** — optional url associated with this subtopic.

***

## Return format
Status code 200, along with a JSON array containing 
- **status** — Either OK or NOT OK
- **new** — true if a new map was created. 

***

## Errors
- **status** — NOT OK
- **error** — Error message

***

## Example
**Request**

    POST /updateMap

**Payload**
``` json
{
  "main_topic": "Javascript",
  "subtopic": "arrays",
  "url": "http://example.com/arrays/push"
}
```


**Return**
``` json
{
  "status": "OK",
  "new": true
}
```
