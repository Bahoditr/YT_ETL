import requests
import json
API_KEY = 'AIzaSyDqkY2PANzLKiSW0fY9UpXcgpgVbMmzVXM'
CHANNEL_HANDLE = 'MrBeast'
url = f'https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}'

response = requests.get(url)
print(response)

data = response.json()
print(json.dumps(data, indent=4))