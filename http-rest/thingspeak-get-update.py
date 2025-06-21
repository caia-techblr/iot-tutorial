import requests

# Replace with your ThingSpeak Write API Key
API_KEY = "YOUR_API_KEY"

# Replace with the data you want to send
field1_value = 25.5  # Example value for Field 1
field2_value = 60.2  # Example value for Field 2

# Construct the URL for the HTTP GET request
url = f"https://api.thingspeak.com/update?api_key={API_KEY}&field1={field1_value}&field2={field2_value}"

try:
    # Send the GET request
    response = requests.get(url)

    # Check the response
    if response.status_code == 200:
        print(f"Data successfully sent to ThingSpeak. Entry ID: {response.text}")
    else:
        print(f"Failed to send data. HTTP Status Code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {e}")

