import http.client
import json

conn = http.client.HTTPSConnection("")
payload = json.dumps({
   "authorizationValue": {
      "keyName": "string",
      "type": "string",
      "value": "string"
   },
   "options": {
      "property1": "string",
      "property2": "string"
   },
   "securityDefinition": {
      "description": "string",
      "type": "string"
   },
   "spec": {},
   "swaggerUrl": "http://petstore.swagger.io/v2/swagger.json"
})
headers = {
   'User-Agent': 'Apidog/1.0.0 (https://apidog.com)',
   'Content-Type': 'application/json'
}
conn.request("POST", "/api/gen/clients/", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))