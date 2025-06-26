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
import time

# ThingSpeak MQTT credentials
MQTT_BROKER = "mqtt3.thingspeak.com"
MQTT_PORT = 1883
MQTT_USERNAME = "Your_ThingSpeak_MQTT_Username"
MQTT_PASSWORD = "Your_ThingSpeak_MQTT_API_Key"
CHANNEL_ID = "Your_Channel_ID"
WRITE_API_KEY = "Your_Channel_Write_API_Key"

# MQTT topic format: channels/<channel_id>/publish/<write_api_key>
MQTT_TOPIC = f"channels/{CHANNEL_ID}/publish/{WRITE_API_KEY}"

# Function to publish data
def publish_data(client, field1_value):
    payload = f"field1={field1_value}"  # Replace 'field1' with your desired field
    client.publish(MQTT_TOPIC, payload)
    print(f"Published: {payload}")

# Initialize MQTT client
client = mqtt.Client()
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

# Connect to the MQTT broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Publish data in a loop (example: sending data every 15 seconds)
try:
    while True:
        field1_value = 42  # Replace with your dynamic data
        publish_data(client, field1_value)
        time.sleep(15)  # Wait 15 seconds before sending the next value
except KeyboardInterrupt:
    print("Exiting...")
    client.disconnect()
"""
