import requests
import requests
from bs4 import BeautifulSoup
import json

url = "https://www.before-tomorrow-comes.fr/g3-gotei-13"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
MEMBRES_GOTEI_13 = soup.find_all('strong')
LISTE_GOTEI_13 = []
for name in MEMBRES_GOTEI_13:
    name = str(name)
    replace_strong_1 = name.replace("<strong>","")
    replace_strong_2 = replace_strong_1.replace("</strong>","")
    if replace_strong_2 != "Gotei 13" and replace_strong_2 != "Reiō" and replace_strong_2 != '<a href="https://www.forumactif.com" target="_blank">Créer un forum</a>' and replace_strong_2 != '<a href="https://www.forumactif.com/forum-gratuit" target="_blank">Forum gratuit</a>':
        LISTE_GOTEI_13.append(replace_strong_2)

print(LISTE_GOTEI_13)
LISTE_ID_PROFIL = {"liste_gotei13": [{"Asano Shirahime":"u26",
"Chibiko Daestra":"u34",
"Furihata Tetsu":"u15",
"Hinotori Mamoru":"u11",
"Hisaishi Shūmei":"u61",
"Igarashi Sora":"u5",
"Kiryū Shinjiro":"u7",
"Komamura Jinro":"u53",
"Komamura Niji":"u52",
"Kuchiki Toshizo":"u60",
"Kyōakusei Kenshirō":"u16",
"Nagatsuki Aizome":"u9",
"Naoki Shiori":"u8",
"Sabaiba Yoko":"u36",
"Shimizu Kanō":"u30",
"Shingen Mizuki":"u28",
"Shiro Mayuri":"u31",
"Shunshō Hirō":"u27",
"Tomoe Nozomi":"u3",
"Utsunomiya Thoki":"u49",
"Yane Yoru":"u38",
"Yūko Seiichi":"u20",
"Yuta":"u22"}]
}

JSON_ID_PROFIL = json.loads(LISTE_ID_PROFIL)
print(JSON_ID_PROFIL)