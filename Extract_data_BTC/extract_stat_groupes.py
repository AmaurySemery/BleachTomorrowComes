import requests
import requests
from bs4 import BeautifulSoup



url = "https://www.before-tomorrow-comes.fr/g3-gotei-13"
page = requests.get(url)
# Voir le code html source
# print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
titres = soup.find_all("table", class_="table1")
print(titres)
for name in titres:
    print(name.get('row1'))