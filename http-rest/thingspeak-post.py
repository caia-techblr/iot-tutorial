import requests

# Replace with your ThingSpeak Write API Key
WRITE_API_KEY = 'YOUR_WRITE_API_KEY'
# Replace with your ThingSpeak channel's URL
THINGSPEAK_URL = 'https://api.thingspeak.com/update'

# Data to send (e.g., field1, field2, etc.)
data = {
    'api_key': WRITE_API_KEY,
    'field1': 25.5,  # Example value for field1
    'field2': 60.2   # Example value for field2
}

try:
    # Send HTTP POST request
    response = requests.post(THINGSPEAK_URL, data=data)
    
    # Check response status
    if response.status_code == 200:
        print(f"Data successfully sent to ThingSpeak. Response: {response.text}")
    else:
        print(f"Failed to send data. HTTP Status Code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {e}")

