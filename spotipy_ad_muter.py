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

#webbrowser.open("https://open.spotify.com/", new=1, autoraise=True)

scope = 'user-read-currently-playing'


'''
if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()
'''

username = "-f"

def get_token():
    return(util.prompt_for_user_token(username,
                           scope,
                           client_id='84d16a6d28d744598e19c4e1bb4923d2',
                           client_secret='73f0b495c93d4539a43ca771674f1dea',
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


def volume_low():
    if token:
        sp = spotipy.Spotify(auth=token)
        sp.volume(volume_percent = 1)
    else:
        print("Can't get token for", username)


def volume_low():
    if token:
        sp = spotipy.Spotify(auth=token)
        sp.volume(volume_percent = 50)
    else:
        print("Can't get token for", username)
        


#These keystrokes open WMC, mute the volume, and close the window

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

#    except:
    except BaseException as error:
        os.system('clear')
        print('An exception occurred: {}'.format(error))
        print("Can't connect to Spotify...")
        token = get_token()
    time.sleep(0.5)

