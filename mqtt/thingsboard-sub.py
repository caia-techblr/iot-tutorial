import paho.mqtt.client as mqtt

# Define ThingsBoard MQTT broker details
THINGSBOARD_HOST = 'demo.thingsboard.io'  # Replace with your ThingsBoard server
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'        # Replace with your device's access token

# Callback when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to ThingsBoard!")
        # Subscribe to a topic (e.g., telemetry updates)
        client.subscribe('v1/devices/me/telemetry')
    else:
        print(f"Failed to connect, return code {rc}")

# Callback when a message is received
def on_message(client, userdata, msg):
    print(f"Received message from topic {msg.topic}: {msg.payload.decode()}")

# Create an MQTT client instance
client = mqtt.Client()

# Set access token for authentication
client.username_pw_set(ACCESS_TOKEN)

# Assign callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the ThingsBoard MQTT broker
client.connect(THINGSBOARD_HOST, 1883, 60)

# Start the MQTT client loop
client.loop_forever()

