[Back to index](api-reference.md)

## POST /share

## Description
Shares a map. To whom? To the list of users attached to this POST request.

***

## Requires authentication
**login_required**

***

## Parameters
Essential information:

- **map_id** — the map_id of the map to share.
- **users** — a list of users to share with

### Optional attributes:

***

## Return format
Status code 200, along with a JSON array containing 
- **status** — Either OK or NOT OK
- **map_id** — the map_id of the map shared.

***

## Errors
- **status** — NOT OK
- **error** — Error message

***

## Example
**Request**

    POST /share

**Payload**
``` json
{
    "map_id": "songs-on-youtube",
    "users": ["userA", "userB"]
}

**Return**
``` json
{
  "map_id": "songs-on-youtube",  
  "status": "Share OK"
}

```
