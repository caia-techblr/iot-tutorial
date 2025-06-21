import requests

# Replace with your ThingSpeak channel's Read API Key and Channel ID
API_KEY = "YOUR_READ_API_KEY"
CHANNEL_ID = "YOUR_CHANNEL_ID"

# Construct the URL for the GET request
url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={API_KEY}&results=5"

try:
    # Send the GET request
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Parse the JSON response
    data = response.json()

    # Access and print the retrieved data
    feeds = data.get("feeds", [])
    for feed in feeds:
        print(f"Entry ID: {feed['entry_id']}, Field 1: {feed.get('field1')}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

