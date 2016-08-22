[Back to index](api-reference.md)

## GET users

## Description
returns flat list of users. Useful for auto-suggesting friends to share maps with. 

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
- **users** — The list of users
***

## Errors
- **status** — NOT OK
- **error** — Error message

***

## Example
**Request**

    GET /users


**Return**
``` json
{
  "status": "OK",
  "users": [
            "Edvard Grieg",
            "Mozart",
            "Ada Lovelace",
            "Marie Curriè"
          ]
}
```
