import requests
from bs4 import BeautifulSoup

root = 'https://subslikescript.com'
website = f'{root}/movies'

result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')

box = soup.find('article', class_='main-article')

box.find_all('a', href=True)

for link in box.find_all('a', href=True):
    link['href']
    
links = [link['href'] for link in box.find_all('a', href=True)]
print(links)

for link in links:
    result = requests.get(f'{root}/{link}')
    content = result.text
    soup = BeautifulSoup(content, 'lxml')