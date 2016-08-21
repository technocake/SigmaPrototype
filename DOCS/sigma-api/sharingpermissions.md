[Back to index](api-reference.md)

## GET /sharingpermissions  or 
## POST /sharingpermissions

## Description
Shows or changes sharing permissions on a map. If a GET request is sent with mapid the current
sharing permissions is returned for that map. if a POST request is sent with mapid and new 
permissions the sharing permissions of the map will change.

This endpoint is meant to be used by user clients to show sharing permissions or to change them. 
The actual access control of a map is done serverside.  

***

## Requires authentication
**login_required**

***

## Parameters
Essential information:


- **map_id** — The id of the map (main topic). Both GET and POST.
- **permissions** — a dict with the new permissions for this map POST only.
- **new** — the new subtopic text.

### Optional attributes:

***

## Return format
Status code 200, along with a JSON array containing 
- **status** — Either OK or NOT OK
- **permissions** — Dict containing sharing access permissions of the map.
***

## Errors
- **status** — NOT OK
- **error** — Error message

***

## Example
**Request**

    GET /sharingpermissions

**Payload**
``` json
{
  "map_id": "Javascript"
}
```


**Return**
``` json
{
  "status": "OK",
  "permissions": {
    "global": "public"
  }
}
```
This first example is retrieving the permissions of the map Javascript. It has a public access.

The next example shows how to change the map from  public access to private.

**Request**

    POST /sharingpermissions

**Payload**
``` json
{
  "map_id": "Javascript",
  "permissions": {
    "global": "private"
  }
}
```


**Return**
``` json
{
  "status": "OK",
}
