import requests
import bs4

r = requests.get('https://pypi.org/project/beautifulsoup4/')
html = bs4.BeautifulSoup(r.text, features="html.parser")
print(html.title.text)