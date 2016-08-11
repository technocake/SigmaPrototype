## GET fetchlinks

## Description
Returns a dict with the users links,  the key of the dict is the url itself, the value is 
the metadata about this link.

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
- **links** — a dict with urls as keys and  metadata about the url as value.

***

## Errors
- **status** — NOT OK
- **error** — Error message

***

## Example
**Request**

    GET /fetchlinks

**Payload**
none


**Return**
``` json
{
  "status": "OK",
  "links": {
    "http://inventwithpython.com/chapter18.html": {
      "description": "", 
      "domain": "inventwithpython.com", 
      "favicon": "http://inventwithpython.com/favicon.ico", 
      "title": "", 
      "topics": {
        "cls1": {
          "Arts": 0.0383934, 
          "Business": 0.0307659, 
          "Computers": 0.651586, 
          "Games": 0.13442, 
          "Health": 0.0215786, 
          "Home": 0.0313365, 
          "Recreation": 0.0213406, 
          "Science": 0.0436635, 
          "Society": 0.010569, 
          "Sports": 0.0163468
        }, 
        "errorMessage": "", 
        "statusCode": 2000, 
        "success": true, 
        "textCoverage": 0.415449, 
        "version": "1.01"
      }, 
      "url": "http://inventwithpython.com/chapter18.html", 
      "urlparts": [
        "http", 
        "inventwithpython.com", 
        "/chapter18.html", 
        "", 
        "", 
        ""
      ]
    }, 
    "http://jqueryui.com/autocomplete/": {
      "description": "jQuery: The Write Less, Do More, JavaScript Library", 
      "domain": "jqueryui.com", 
      "favicon": "http://jqueryui.com/favicon.ico", 
      "title": "Autocomplete | jQuery UI", 
      "topics": {
        "cls1": {
          "Arts": 1.7735e-09, 
          "Business": 2.93296e-09, 
          "Computers": 1, 
          "Games": 7.97444e-10, 
          "Health": 1.84542e-09, 
          "Home": 3.07045e-09, 
          "Recreation": 5.12697e-10, 
          "Science": 9.30302e-10, 
          "Society": 5.36648e-11, 
          "Sports": 1.25083e-10
        }, 
        "errorMessage": "", 
        "statusCode": 2000, 
        "success": true, 
        "textCoverage": 0.497059, 
        "version": "1.01"
      }, 
      "url": "http://jqueryui.com/autocomplete/", 
      "urlparts": [
        "http", 
        "jqueryui.com", 
        "/autocomplete/", 
        "", 
        "", 
        ""
      ]
    }
  }
}
```

