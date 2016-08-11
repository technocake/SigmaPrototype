#### Sigma API references

# Knowledge Maps
### endpoints:
 * POST updatemap
 * POST relabel
 


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

    POST /updatemap

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




## POST relabel

## Description
updates a subtopic in a map.

***

## Requires authentication
**login_required**

***

## Parameters
Essential information:


- **map_id** — The id of the map (main topic).
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

    POST /relabel

**Payload**
``` json
{
  "map_id": "Javascript",
  "old": "arrays",
  "new": "array methods"
}
```


**Return**
``` json
{
  "status": "OK",
}
```
