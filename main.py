import requests
from bs4 import BeautifulSoup
import spotipy

question = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')
question1 = '2007-08-30'
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}


response = requests.get(f'https://www.billboard.com/charts/hot-100/{question}/', headers=header)
response.raise_for_status
billboard100 = response.text
soup = BeautifulSoup(billboard100, 'html.parser')

# top100 = soup.find_all('div', class_="chart-results-list // lrv-u-padding-t-150 lrv-u-padding-t-050@mobile-max")
top100 = soup.find_all('div', class_="o-chart-results-list-row-container")
counter = 1
for i in top100:
  title = i.find('h3')
  print(counter, end=".")
  print(title.text.strip())
  counter += 1
