import os
import json
from AzureHTTPHelper import HTTPHelper

http = HTTPHelper()

print("--- GET ---")
print(http.get)
print()

print("--- POST ---")
print(http.post)
print()

print("--- HEADERS ---")
print(http.headers)
print()

# print("--- OTHER ENVIRONMENTAL VARIABLES ---")
# for x in http.env:
#     print(x)
# print()

returnData = {
    #HTTP Status Code:
    "status": 200,
    
    #Response Body:
    "body": "<h1>hello world from " + http.get["name"] + "</h1>",
    
    # Send any number of HTTP headers
    "headers": {
        "Content-Type": "text/html",
        "X-Awesome-Header": "YesItIs"
    }
}
response = open(os.environ['res'], 'w')
response.write(json.dumps(returnData))
response.close()