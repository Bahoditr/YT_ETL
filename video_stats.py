import requests
import json
import os
from dotenv import load_dotenv


load_dotenv(dotenv_path='./.env', override = True)
API_KEY = os.getenv("API_KEY")
CHANNEL_HANDLE = 'MrBeast'



def get_playlist():

    try:
        url = f'https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}'
        response = requests.get(url)
        #print(response)
        data = response.json()
        #print(data)
        #print(json.dumps(data, indent=4))
        #print(data["items"][0]["contentDetails"]["relatedPlaylists"]['uploads'])
        channal_playlistId = data["items"][0]["contentDetails"]["relatedPlaylists"]['uploads']
        return channal_playlistId
    except requests.exceptions.RequestException as e:
        raise e
    

if __name__ == "__main__":
    print("get_playlist will be executed")
    print(get_playlist())
else:
    print("get_playlist will not be executed")
    

get_playlist()
#test_bb.hh()