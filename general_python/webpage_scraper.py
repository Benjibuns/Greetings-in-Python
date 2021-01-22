import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.dailysmarty.com/topics/python')
html = r.text
soup = BeautifulSoup(html, 'html.parser')

for link in soup.find_all('a'):
    if link.get("href") == None:
        continue
    elif link.get("href").startswith("/posts/"):
        return link.get('href')
