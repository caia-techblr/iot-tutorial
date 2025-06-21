# Install MQTT Broker
```
sudo apt install mosquitto  # on laptop/desktop
sudo netstat -ntpl          # Check port number 1883 is in use
```

# Install MQTT Clients
```
sudo apt install mosquitto-clients # On Rpi
```

# Using mosquitto client utils
```
mosquitto_sub -t gitam/demo -h <ip-of-broker>
mosquitto_pub -t gitam/demo -h <ip-of-broker> -m "Hello World"
```

# Python Example - Simple Publisher
```
import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"           # "localhost"
port = 1883
topic = "gitam/demo"

client = mqtt.Client()
client.connect(broker, port)

client.publish(topic, "Hello, MQTT!")
print(f"Message sent to topic '{topic}'")
client.disconnect()
```

# Python Example - Simple Subscriber
```
import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()} on topic {message.topic}")

broker = "broker.hivemq.com"    # "localhost"
port = 1883
topic = "gitam/demo"

client = mqtt.Client()
client.on_message = on_message

client.connect(broker, port)
client.subscribe(topic)

print(f"Subscribed to topic '{topic}'")
client.loop_forever()

```

## Activity / TODO
* Use commands / mobile Apps / Node-RED / python code to publish sensor data 
* Use commands / mobile Apps / Node-RED / python code to control LEDs (or any peripherals) using MQTT subscribe
* Modify python examples to connect with IOT Platform (thingspeak/thingsboard)

## Skeleton code
