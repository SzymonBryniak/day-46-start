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
    "client_id":"",
    "client_secret":""
  }
  response = requests.post(url="https://accounts.spotify.com/api/token", headers=header, data=params)
  print(response.json())
  return response.json()['access_token']

get_auth()
