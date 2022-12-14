import requests
from bs4 import BeautifulSoup

url_gotei_groupe = "https://www.before-tomorrow-comes.fr/g3-gotei-13"
url_classement = 'https://www.before-tomorrow-comes.fr/memberlist?mode=point&order=DESC&submit=Ok&username'

page = requests.get(url_gotei_groupe)
soup = BeautifulSoup(page.content, 'html.parser')
MEMBRES_GOTEI_13 = soup.find_all('strong')
LISTE_GOTEI_13 = []
for name in MEMBRES_GOTEI_13:
    name = str(name)
    replace_strong_1 = name.replace("<strong>","")
    replace_strong_2 = replace_strong_1.replace("</strong>","")
    if replace_strong_2 != "Gotei 13" and replace_strong_2 != "Reiō" and replace_strong_2 != '<a href="https://www.forumactif.com" target="_blank">Créer un forum</a>' and replace_strong_2 != '<a href="https://www.forumactif.com/forum-gratuit" target="_blank">Forum gratuit</a>':
        LISTE_GOTEI_13.append(replace_strong_2)

# print(LISTE_GOTEI_13)

page = requests.get(url_classement)
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
CLASSEMENT = soup.find_all("div", class_='forumbg forumbg-table')
print(CLASSEMENT[0])

for name in CLASSEMENT:
    name = str(name)
    replace_strong_1 = name.replace("<strong>","")
    replace_strong_2 = replace_strong_1.replace("</strong>","")
    # print(replace_strong_2)
    # if replace_strong_2 != "Gotei 13" and replace_strong_2 != "Reiō" and replace_strong_2 != '<a href="https://www.forumactif.com" target="_blank">Créer un forum</a>' and replace_strong_2 != '<a href="https://www.forumactif.com/forum-gratuit" target="_blank">Forum gratuit</a>':
    #     LISTE_GOTEI_13.append(replace_strong_2)