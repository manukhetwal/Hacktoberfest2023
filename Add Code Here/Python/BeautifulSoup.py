import requests
from bs4 import BeautifulSoup

url = 'https://www.example.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Example: Extract all links from the webpage
links = soup.find_all('a')
for link in links:
    print(link.get('href'))
