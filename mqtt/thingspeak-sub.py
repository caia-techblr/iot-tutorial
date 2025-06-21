import paho.mqtt.client as mqtt

# Define your MQTT credentials and channel details
MQTT_BROKER = "mqtt3.thingspeak.com"
MQTT_PORT = 1883
MQTT_USERNAME = "Your_ThingSpeak_MQTT_Username"
MQTT_PASSWORD = "Your_ThingSpeak_MQTT_API_Key"
CHANNEL_ID = "Your_Channel_ID"
SUBSCRIBE_TOPIC = f"channels/{CHANNEL_ID}/subscribe/fields/field1"

# Callback when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully!")
        client.subscribe(SUBSCRIBE_TOPIC)
        print(f"Subscribed to topic: {SUBSCRIBE_TOPIC}")
    else:
        print(f"Connection failed with code {rc}")

# Callback when a message is received
def on_message(client, userdata, msg):
    print(f"Message received on topic {msg.topic}: {msg.payload.decode()}")

# Create an MQTT client instance
client = mqtt.Client()

# Set username and password for authentication
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

# Assign callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Start the MQTT client loop to process network traffic
client.loop_forever()

