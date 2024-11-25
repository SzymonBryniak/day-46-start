import requests

# curl -X POST "https://accounts.spotify.com/api/token" \
#      -H "Content-Type: application/x-www-form-urlencoded" \
#      -d "grant_type=client_credentials&client_id=your-client-id&client_secret=your-client-secret"
def get_auth():
  header = {
    "Content-Type": "application/x-www-form-urlencoded"
  }
  params = {
    "grant_type":"client_credentials",
    "client_id":"989c4215b8c5487f87999705299f1f4b",
    "client_secret":"4b55f515f87e4005a618bd8ea283a3ee"
  }
  response = requests.post(url="https://accounts.spotify.com/api/token", headers=header, data=params)
  # print(response.json())
  return response.json()['access_token']


def get_tracks(song):
  # curl --request GET \
  # --url 'https://api.spotify.com/v1/search?q=Get+Ur+Freak+On&type=track&limit=1' \
  # --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
  token = get_auth()
  endpoint = 'https://api.spotify.com/v1/search'
  header = {
    "Authorization": f"Bearer {token}"
  }

  params = {
    "q": song,
    "type": "track",
    "limit": 1
  }

  response = requests.get(endpoint, headers=header, params=params)
  response.raise_for_status()
  # print(token)
  # print(response.json()['tracks']['items'][0]['id'])
  return response.json()['tracks']['items'][0]['id']
 
def get_playlist_tracks():
  token = get_auth()
  endpoint = "https://api.spotify.com/v1/playlists/765JkJ9MWbmuPIS3xthnOl/tracks"
  header = {
    'Authorization': f"Bearer {token}"
  }
  params = {
    "limit": 100
  }
  response = requests.get(url=endpoint, headers=header, params=params)
  response.raise_for_status()
  print(response.json())

  # curl --request GET \
  # --url 'https://api.spotify.com/v1/playlists/3cEYpjA9oz9GiPac4AsH4n/tracks?limit=1000' \
  # --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'

