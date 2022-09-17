import requests
import requests
from bs4 import BeautifulSoup
import html5lib
import re
import urllib3

url = "https://www.before-tomorrow-comes.fr/g3-gotei-13"

def gotei_13_id_profil(name):
    id = "0"
    if name == "Asano Shirahime":
        id = "u26"
    if name == "Chibiko Daestra":
        id = "u34"
    if name == "Furihata Tetsu":
        id = "u15"
    if name == "Hinotori Mamoru":
        id = "u11"
    if name == "Hisaishi Shūmei":
        id = "u61"
    if name == "Igarashi Sora":
        id = "u5"
    if name == "Kiryū Shinjiro":
        id = "u7"
    if name == "Komamura Jinro":
        id = "u53"
    if name == "Komamura Niji":
        id = "u52"
    if name == "Kuchiki Toshizo":
        id = "u60"
    if name == "Kyōakusei Kenshirō":
        id = "u16"
    if name == "Nagatsuki Aizome":
        id = "u9"
    if name == "Naoki Shiori":
        id = "u8"
    if name == "Sabaiba Yoko":
        id = "u36"
    if name == "Shimizu Kanō":
        id = "u30"
    if name == "Shingen Mizuki":
        id = "u28"
    if name == "Shiro Mayuri":
        id = "u31"
    if name == "Shunshō Hirō":
        id = "u27"
    if name == "Tomoe Nozomi":
        id = "u3"
    if name == "Utsunomiya Thoki":
        id = "u49"
    if name == "Yane Yoru":
        id = "u38"
    if name == "Yūko Seiichi":
        id = "u20"
    if name == "Yuta":
        id = "u22"
    return id

def get_renommee(RENOMMEE):
    print(RENOMMEE)
    LONGUEUR_LISTE = len(RENOMMEE)

    RENOMMEE = str(RENOMMEE[0])
    REPLACE_RENOMMEE_1 = RENOMMEE.replace('<div class="field_uneditable">',"")
    REPLACE_RENOMMEE_2 = REPLACE_RENOMMEE_1.replace('</div>',"")
    print(REPLACE_RENOMMEE_2)
    print(isinstance(REPLACE_RENOMMEE_2,int))
    # for i in LONGUEUR_LISTE:
    #     if str

http = urllib3.PoolManager()

url = 'https://www.before-tomorrow-comes.fr/u36'
resp = http.request('GET', url,headers=headers)
# print(resp.data.decode('utf-8'))
print(resp.data)

# page = requests.get(url)
# soup = BeautifulSoup(page.content, 'html.parser')
# MEMBRES_GOTEI_13 = soup.find_all('strong')
# LISTE_GOTEI_13 = []
# for name in MEMBRES_GOTEI_13:
#     name = str(name)
#     replace_strong_1 = name.replace("<strong>","")
#     replace_strong_2 = replace_strong_1.replace("</strong>","")
#     if replace_strong_2 != "Gotei 13" and replace_strong_2 != "Reiō" and replace_strong_2 != '<a href="https://www.forumactif.com" target="_blank">Créer un forum</a>' and replace_strong_2 != '<a href="https://www.forumactif.com/forum-gratuit" target="_blank">Forum gratuit</a>':
#         LISTE_GOTEI_13.append(replace_strong_2)
#         result_id = gotei_13_id_profil(replace_strong_2)
#
#         url_profil = "https://www.before-tomorrow-comes.fr/" + str(result_id)
#         print(url_profil)
#         request_profil = requests.get(url_profil)
#         soup_profil = BeautifulSoup(request_profil.content, 'html5lib')
#         PROFIL = str(soup_profil.prettify())
#         print(soup_profil.find_all('dt'))
        # print(soup_profil.get_text())
        # PROFIL = str(soup_profil)
        # print(PROFIL.title.string)
        #
        #
        # # print(PROFIL)
        # found = re.search('<dl id="field_id-13" class="profil-infos" style="width: 100%;"><dt>Renommée : </dt><dd><div class="field_uneditable">(.+?)</div>', PROFIL).group(1)
        #
        # print(found)
        # RENOMMEE = PROFIL.find("dl",id="field_id-13",class_="profil-infos")
        #
        # get_renommee(RENOMMEE)
        #
        # RENOMMEE = str(RENOMMEE[0])
        # REPLACE_RENOMMEE_1 = RENOMMEE.replace('<div class="field_uneditable">',"")
        # REPLACE_RENOMMEE_2 = REPLACE_RENOMMEE_1.replace('</div>',"")
        #
        #
        # print(soup_profil_gotei_13("field_id-13"))
