# HTTP REST Tutorial

## Install curl client
```
sudo apt install curl
```

## curl command usage
* Base URL :  `http(s)://demo.thingsboard.io/api/v1/$ACCESS_TOKEN/telemetry`

```
ACCESS_TOKEN="<Access token of the device>"
curl -v -X POST --data "{"temperature":42,"humidity":73}" https://demo.thingsboard.io/api/v1/$ACCESS_TOKEN/telemetry --header "Content-Type:application/json"

curl -v -X POST -d @telemetry-data-as-object.json https://demo.thingsboard.io/api/v1/$ACCESS_TOKEN/telemetry --header "Content-Type:application/json"

```

## GET example in Python

## POST example in Python

## Skeleon code
* [Retrieve feeds from Thingspeak channel](thingspeak-get-data.py)
* [Updating Thingspeak channel using GET](thingspeak-get-update.py)
* [Updating Thingspeak channel using POST](thingspeak-post.py)
* [Updating ThingsBoard Telemetry[(thingsboard-post.py)



