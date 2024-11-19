import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
# https://github.com/spotipy-dev/spotipy/blob/2.22.1/TUTORIAL.md
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="",
                                               client_secret="",
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-public"))
user_id = "1124705280"
taylor_uri = 'spotify:artist:06HL4z0CvFAxyc27GXpf02'
endpoint = "https://api.spotify.com/v1/users/{user_id}/playlists"

header = {"Authorization": "Bearer "}

def artist_alubums():
    results = sp.artist_albums(taylor_uri, album_type='album')
    albums = results['items']
    while results['next']:
        results = sp.next(results)
        albums.extend(results['items'])

    for album in albums:
        print(album['name'])

def create_playlist():
    
    urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
    print(sp.user_playlist_create(user_id, "spotip pl", public=True, collaborative=False, description='test spotipy playlist'))

def get_test():
    print(sp.user(user_id))

get_test()


# user id is required in the next steps
def get_user_id():
    endpoint = "https://api.spotify.com/v1/me"
    response = requests.get(url=endpoint, headers=header)
    response.raise_for_status
    print(response.json())

get_test()
def create_playlist():
    body = {
    "name": "New Playlist",
    "description": "New playlist description",
    "public": "false"
}
    response = requests.post(url=endpoint, json=body, headers=header)
    response.aise_for_status
    print(response)


    
def read_cache():
    print(sp.current_user_top_tracks)
    
    with open('.cache') as cache:
       e_cache = eval(cache.read())
       print(e_cache['access_token'])


