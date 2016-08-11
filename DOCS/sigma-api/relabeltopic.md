

## POST relabeltopic

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
