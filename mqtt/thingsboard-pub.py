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

