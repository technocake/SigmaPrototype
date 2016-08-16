## POST fetchsearchdata

## Description
Builds a search-able datastructure of the users maps and links and returns it to the client.
This is meant to provide data for client-side searching. User is implied through the
session login.

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
- **searchdata** — N-Dimenisional array of topics and links.

***

## Errors
- **status** — NOT OK
- **error** — Error message

***

## Example
**Request**

    POST /fetchsearchdata

**Payload**
None


**Return**
** nb, json has no support for comments. Comments are added here to give a better overview of the data
``` json
{
  "status": "OK",
  "searchdata": [ 
                    // this is the first Map
                    ["Python", "functions", "http://example.com/python-functions"], 
                    ["Python", "functions", "http://example.com/python-use-def"], 
                    ["Python", "syntax", "http://example.com/python-syntax"],
                    ["Java", "functions", "http://example.com/java-functions"],
                    ["Java", "inventor", "http://example.com/James-gosling"]
                ],
    "linksdata": {
    "http://stackoverflow.com/questions/3768895/how-to-make-a-class-json-serializable": {
      "description": "", 
      "domain": "stackoverflow.com", 
      "favicon": "http://stackoverflow.com/favicon.ico", 
      "title": "python - How to make a class JSON serializable - Stack Overflow", 
      "topics": {
        "cls1": {
          "Arts": 3.93073e-05, 
          "Business": 1.7971e-05, 
          "Computers": 0.999878, 
          "Games": 3.37321e-05, 
          "Health": 6.84366e-06, 
          "Home": 7.5316e-06, 
          "Recreation": 5.34196e-06, 
          "Science": 8.90356e-06, 
          "Society": 8.24659e-07, 
          "Sports": 1.18447e-06
        }, 
        "errorMessage": "", 
        "statusCode": 2000, 
        "success": true, 
        "textCoverage": 0.464187, 
        "version": "1.01"
      }, 
      "url": "http://stackoverflow.com/questions/3768895/how-to-make-a-class-json-serializable", 
      "urlparts": [
        "http", 
        "stackoverflow.com", 
        "/questions/3768895/how-to-make-a-class-json-serializable", 
        "", 
        "", 
        ""
      ],
      
      ...
      
      
    }
}
```

