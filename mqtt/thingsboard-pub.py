import paho.mqtt.client as paho
import random as random
import time
import json

CLIENT_ID = "ARMPMjMSGwAOBxIlDi05HCA"
MQTT_USERNAME = "ARMPMjMSGwAOBxIlDi05HCA"
MQTT_PASSWORD = "iJEpMsKStRTxDyrPiw+XXDVx"
CHANNEL_ID = "2997635"
WRITE_API_KEY = "8XOHOKF68RRB6SLP"
 
def on_publish(client, userdata, mid):
    print("mid: "+str(mid)+":"+str(userdata))
 
client = paho.Client(client_id=CLIENT_ID, clean_session=True)
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
client.on_publish = on_publish
client.connect("mqtt3.thingspeak.com", 1883)
client.loop_start()
 
while True:
    try:
        tval = random.randint(16,40)
        hval = random.randint(50,100)
        pval = random.randint(800,1000)
        payload = f"field1={tval}&field2={hval}&field3={pval}&status=MQTTPUBLISH"
        (rc, mid) = client.publish( f"channels/{CHANNEL_ID}/publish",payload,qos=1)
        time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
        break
client.disconnect()
"""
import paho.mqtt.client as mqtt
import json
import time

# ThingsBoard MQTT broker details
THINGSBOARD_HOST = 'demo.thingsboard.io'   # Replace with your ThingsBoard host
ACCESS_TOKEN = 'YOUR_DEVICE_ACCESS_TOKEN'  # Replace with your device's access token

# Callback for connection
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to ThingsBoard!")
    else:
        print(f"Failed to connect, return code {rc}")

# Initialize MQTT client
client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.on_connect = on_connect

# Connect to ThingsBoard
client.connect(THINGSBOARD_HOST, 1883, 60)
client.loop_start()

# Publish telemetry data
try:
    while True:
        telemetry_data = {
            "temperature": 25.5,  # Example temperature value
            "humidity": 60       # Example humidity value
        }
        client.publish("v1/devices/me/telemetry", json.dumps(telemetry_data))
        print(f"Published: {telemetry_data}")
        time.sleep(5)  # Publish every 5 seconds
except KeyboardInterrupt:
    print("Stopped by user")
finally:
    client.loop_stop()
    client.disconnect()
"""

