

## POST relabeltopic

## Description
updates a subtopic in a map. 
If a subtopic has urls, those will be moved to the new subtopic. 
If the new subtopic already exists, the urls from the old subtopic will be 
appended to the target subptopic. 


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

    POST /relabeltopic

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
