[Back to index](api-reference.md)

## POST /postmeta

## Description
Updates a links meta data information with the users potential changes / additions.
returns searchdata. (this should probably be an optional flag to return searchdata).

***

## Requires authentication
**login_required**

***

## Parameters
Essential information:

- **url** — the url to the link that will have it's data updated.
- **meta** — A dict with the same format as returned by [/fetchmeta](fetchmeta.md)

### Optional attributes:

***

## Return format
Status code 200, along with a JSON array containing 
- **status** — Either OK or NOT OK
- **searchdata** — a list of lists with searchable data, see [/fetchsearchdata](fetchsearchdata.md).
***

## Errors
- **status** — NOT OK
- **error** — Error message

***

## Example
**Request**

    POST /postmeta

**Payload**
``` json
{
  "url":"http://stackoverflow.com/questions/11536764/how-to-fix-attempted-relative-import-in-non-package-even-with-init-py",
  "meta": {
            "description":"",
            "domain":"stackoverflow.com",
            "favicon":"http://stackoverflow.com/favicon.ico",
            "title":"python - How to fix \"Attempted relative import in non-package\" even with __init__.py - Stack Overflow",
            "topics":{"cls1":{"Arts":0.00156966,"Business":0.00149015,"Computers":0.992041,"Games":0.00184698,"Health":0.000609371,"Home":0.000578662,"Recreation":0.000518582,"Science":0.00119602,"Society":0.0000908997,"Sports":0.00005845},
            "errorMessage":"",
            "statusCode":2000,"success":true,"textCoverage":0.575022,"version":"1.01"},
            "url":"http://stackoverflow.com/questions/11536764/how-to-fix-attempted-relative-import-in-non-package-even-with-init-py",
            "urlparts":[
                          "http","stackoverflow.com",
                          "/questions/11536764/how-to-fix-attempted-relative-import-in-non-package-even-with-init-py",
                          "",
                          "",
                          ""
                        ]
          }
}
```


**Return**
``` json
{
  "searchdata": [
    [
      "Python", 
      "functions", 
      "http://www.cse.msu.edu/~cse231/Online/functions.html"
    ], 
    [
      "python", 
      "jsontull", 
      "http://stackoverflow.com/questions/3768895/how-to-make-a-class-json-serializable"
    ], 
    [
      "inkscape", 
      "cli-options", 
      "https://inkscape.org/en/doc/inkscape-man.html"
    ]
  ], 
  "status": "Postmeta OK"
}

```
