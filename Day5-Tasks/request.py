import requests
import bs4

r = requests.get('https://github.com/nvk1152')
html = bs4.BeautifulSoup(r.text, features="html.parser")
print(html.title.text)