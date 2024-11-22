import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import spotifydev
# https://github.com/spotipy-dev/spotipy/blob/2.22.1/TUTORIAL.md
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="989c4215b8c5487f87999705299f1f4b",
                                               client_secret="4b55f515f87e4005a618bd8ea283a3ee",
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

def get_user_id():
    endpoint = "https://api.spotify.com/v1/me"
    response = requests.get(url=endpoint, headers=header)
    response.raise_for_status
    print(response.json())

def create_playlist():
    
    urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
    print(sp.user_playlist_create(user_id, "spotip pl", public=True, collaborative=False, description='test spotipy playlist'))

def add_tracks():
    tracks = spotifydev.get_tracks("Disturbia")
    sp.playlist_add_items("765JkJ9MWbmuPIS3xthnOl",[tracks])
    print(tracks)

add_tracks()

def get_test():
    for i in sp.current_user_playlists(limit=50, offset=0)['items']:
        print(i)
    print(sp.playlist("765JkJ9MWbmuPIS3xthnOl", fields=None, market=None, additional_types=('track',)))

# user id is required in the next steps

def read_cache():
    print(sp.current_user_top_tracks)
    
    with open('.cache') as cache:
       e_cache = eval(cache.read())
       print(e_cache['access_token'])


