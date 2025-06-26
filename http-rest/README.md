# HTTP REST Tutorial

## Install curl client & python `requests` library
```
sudo apt install curl
sudo pip install requests

```

## curl command usage
* Base URL :  `http(s)://demo.thingsboard.io/api/v1/$ACCESS_TOKEN/telemetry`

```
curl -X POST -d @emp.json https://dummy.restapiexample.com/api/v1/create -header "Content-Type:application/json"
curl -X GET https://dummy.restapiexample.com/api/v1/employees | python -m json.tool

```

## GET example in Python
```
import requests

# URL to send the GET request to
url = "https://dummy.restapiexample.com/api/v1/employees"

myheaders = {
    "User-Agent": "curl/7.81.0",
    "Accept": "*/*"
}

# Sending the GET request
response = requests.get(url, headers=myheaders)

# Checking if the request was successful
if response.status_code == 200:
    # Printing the response content
    print("Response Data:", response.json())
else:
    print(f"Failed to fetch data. Status Code: {response.status_code}")
```

## POST example in Python
```
import requests
import json

# URL to send the POST request to
url = "https://dummy.restapiexample.com/api/v1/create"

# Data to be sent in the POST request
payload = {
    "status": "success",
    "data": {
        "name": "test",
        "salary": "123",
        "age": "23",
        "id": 25
    }
}

myheaders = {
    "User-Agent": "curl/7.81.0",
    "Accept": "*/*"
}


# Sending the POST request
response = requests.post(url, data=json.dumps(payload), headers=myheaders)

# Printing the response
print("Status Code:", response.status_code)
print("Response Body:", response.text)
```
## ThingSpeak Connectivity
```
WR_KEY=<<Your Write API Key>>
CHANNEL_ID=<<Your Channel ID>>
curl -X GET https://api.thingspeak.com/update?api_key=$WR_KEY&field1=24&field2=60
curl -X GET https://api.thingspeak.com/channels/$CHANNEL_ID/feeds.json?results=5
curl -X GET https://api.thingspeak.com/channels/$CHANNEL_ID/fields/1.json?results=5
```
## ThingsBoard conenctivity
```
ACCESS_TOKEN="<Access token of the device>"
curl -v -X POST --data "{"temperature":42,"humidity":73}" https://demo.thingsboard.io/api/v1/$ACCESS_TOKEN/telemetry --header "Content-Type:application/json"

curl -v -X POST -d @telemetry-data-as-object.json https://demo.thingsboard.io/api/v1/$ACCESS_TOKEN/telemetry --header "Content-Type:application/json"
```

## Skeleon code
* [Retrieve feeds from Thingspeak channel](thingspeak-get-data.py)
* [Updating Thingspeak channel using GET](thingspeak-get-update.py)
* [Updating Thingspeak channel using POST](thingspeak-post.py)
* [Updating ThingsBoard Telemetry](thingsboard-post.py)

## References
* https://www.dummy.restapiexample.com/


