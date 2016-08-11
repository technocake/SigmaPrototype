

## GET tags

## Description
Builds and returns a list of tags from the users maps and links. 
Can be usefull for autocomplete: see: http://jqueryui.com/autocomplete/

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
- **tags** — The list of user tags
***

## Errors
- **status** — NOT OK
- **error** — Error message

***

## Example
**Request**

    GET /tags

**Payload**
``` json
{}
```


**Return**
``` json
{
  "status": "OK",
  "tags": [
            "Python",
            "functions",
            "methods",
            "Computer Programming",
            "Games programming",
            "gfx",
            "awesome"
          ]
}
```
