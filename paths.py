import requests
from bs4 import BeautifulSoup

def find_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]
    for link in links:
        print(link)

find_links('http://google.com')
