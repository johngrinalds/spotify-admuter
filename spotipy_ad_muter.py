#pip install spotipy
#pip install pynput

import sys
import spotipy
import spotipy.util as util
from pynput.keyboard import Key, Controller
keyboard = Controller()
import time
import webbrowser
import os
import json

#webbrowser.open("https://open.spotify.com/", new=1, autoraise=True)

scope = 'user-read-currently-playing'

username = "-f"

# Load your credentials here
with open("/Users/johngrinalds/Documents/GitHub/spotify-admuter/creds.json") as f:
  creds = json.load(f)

def get_token():
    return(util.prompt_for_user_token(username,
                           scope,
                           client_id=creds['id'],
                           client_secret=creds['secret'],
                           redirect_uri='http://localhost')
           )

#Get Spotify Current Playing Song

def get_playing():
    if token:
        sp = spotipy.Spotify(auth=token)
        result = sp.currently_playing()
        playing_type = result["currently_playing_type"]
    else:
        print("Can't get token for", username)
    return playing_type

#These keystrokes are for the keyboard-based volume mute key

def mute_toggle():
    keyboard.press(Key.media_volume_mute)
    keyboard.release(Key.media_volume_mute)


#This runs in a loop until cancelled

 
print("Be sure Spotify is open and playing.\nRunning... Press Ctrl+C to cancel")
state = 0 #not playing ad
token = get_token()


while True:
    try:
        song_status = get_playing()
        #print("song_status: ", song_status)
        #print("state: ", state)
        if (song_status == 'ad')&(state == 0):
            state = 1
            mute_toggle()
            os.system('clear')
            print("Spotify Playing\nMuting in progress.")
        if (song_status != 'ad')&(state == 1):
            state = 0
            mute_toggle()
            os.system('clear')
            print("Spotify Playing\nMuting in progress.")

    except BaseException as error:
        os.system('clear')
        print('An exception occurred: {}'.format(error))
        print("Can't connect to Spotify...")
        token = get_token()
    time.sleep(0.5)

