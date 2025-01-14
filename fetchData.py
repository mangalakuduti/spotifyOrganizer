import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth


def authenticate():
    load_dotenv()
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=os.getenv("SPOTIPY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
            redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
            scope=os.getenv("SCOPE")
        ))
    return sp

def get_playlists(sp):
    playlists = sp.current_user_playlists()
    for playlist in playlists['items']:
        print(f"Name: {playlist['name']}, ID: {playlist['id']}")
    return playlists


if __name__ == "__main__":
    sp = authenticate()
    playlists = get_playlists(sp)
