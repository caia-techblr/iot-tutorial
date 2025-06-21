# IOT Workshop : Outline

## Introduction
* What is IOT (what's not IOT)
* Business Scenarios
* IOT Architecture (Devices, Gateway, Platforms, End User Apps)
* Platform Connectivity Protocols (Via Internet) - MQTT and HTTP REST
* IOT Platforms - ThingSpeak / ThingsBoard

## Node-RED
* Setting up NodeRED, Simple Workflows
* Building dashboard in Node-RED
* Quick Demo : SenseHAT simulator
* NddeRED on RaspberryPi - Interfacing Sensors & Actuators

## MQTT
* Overview of MQTT Protocol
* Using CLI tools (mosquitto_pub, mosquitto_sub) and Mobile apps
* Python examples for MQTT
* MQTT Publish & Subscribe in Node-RED

## HTTP REST
* Overview of HTTP Protocol, REST APIs
* Using curl command / postman tool
* Python examples for HTTP REST
* Node-RED flows for Using HTTP REST APIs - GET & POST

## Activity
* Simple MQTT Publish, Subscribe with local broker / public broker
* Simple HTTP REST operations with a dummy server
* Communicating with IOT Platforms via MQTT, HTTP REST - ThingSpeak, ThingsBoard
* Integrate sensors, actuators (from day-1 & day-2) with MQTT, HTTP REST operations

## Gateway
* Why do we need Gateway in between (Non-IP to IP, optimal IP address usage, Security & Scalability)
* Simple Gateway Demo : Arduion as End Device sending data to RaspberryPi (Gateway) through serial interface, which in turn publish data to IOT Platform 
* Ideas on Gateway based projects (e.g. Bridging CAN Network / Bluetooth Networks with Internet)
