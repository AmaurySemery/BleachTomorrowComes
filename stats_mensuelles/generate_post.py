#!/usr/bin/env python
# coding: utf8

import csv
import os
import requests
from bs4 import BeautifulSoup

__file__ = 'statistiques.csv'
CHEMIN = os.path.dirname(os.path.realpath(__file__))
CHEMIN_CONVERT = CHEMIN.replace('\\','/')

chemin_csv = str(CHEMIN_CONVERT) + '/Documents/python/BTC/stats_mensuelles/statistiques.csv'

def web_scraping(url,header):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    MEMBRES = soup.find_all('strong')
    LISTE = []
    for name in MEMBRES:
        name = str(name)
        replace_strong_1 = name.replace("<strong>","")
        replace_strong_2 = replace_strong_1.replace("</strong>","")
        if replace_strong_2 != header and replace_strong_2 != "Reiō" and replace_strong_2 != '<a href="https://www.forumactif.com" target="_blank">Créer un forum</a>' and replace_strong_2 != '<a href="https://www.forumactif.com/forum-gratuit" target="_blank">Forum gratuit</a>':
            LISTE.append(replace_strong_2)
    return LISTE

def change(membre,liste_membre_gotei,liste_membre_acuerdo,liste_membre_UN,liste_membre_indep):
    COLOR_GOTEI_13 = '[color=#344b99]'
    COLOR_ACUERDO = '[color=#929291]'
    COLOR_ULTIMA_NECAT = '[color=#a23d3c]'
    COLOR_INDEP = '[color=#a2783c]'
    if membre in liste_membre_gotei:
        data = '[*][b]' + str(COLOR_GOTEI_13) + str(membre) + '[/color][/b]'
    elif membre in liste_membre_acuerdo:
        data = '[*][b]' + str(COLOR_ACUERDO) + str(membre) + '[/color][/b]'
    elif membre in liste_membre_UN:
        data = '[*][b]' + str(COLOR_ULTIMA_NECAT) + str(membre) + '[/color][/b]'
    elif membre in liste_membre_indep:
        data = '[*][b]' + str(COLOR_INDEP) + str(membre) + '[/color][/b]'
    else:
        data = '[*][b]' + str(membre) + '[/b]'
    return data

if __name__=='__main__':
    url_gotei_groupe = "https://www.before-tomorrow-comes.fr/g3-gotei-13"
    url_acuerdo_groupe = "https://www.before-tomorrow-comes.fr/g4-acuerdo"
    url_UN_groupe = "https://www.before-tomorrow-comes.fr/g5-ultima-necat"
    url_indep_groupe = "https://www.before-tomorrow-comes.fr/g6-independants"

    LISTE_MEMBRES_GOTEI_13 = web_scraping(url_gotei_groupe,"Gotei 13")
    LISTE_MEMBRES_ACUERDO = web_scraping(url_acuerdo_groupe,"Acuerdo")
    LISTE_MEMBRES_ULTIMA_NECAT = web_scraping(url_UN_groupe,"Ultima Necat")
    LISTE_MEMBRES_INDEP = web_scraping(url_UN_groupe,"Indépendants")
    print(LISTE_MEMBRES_GOTEI_13)
    print(LISTE_MEMBRES_ACUERDO)
    print(LISTE_MEMBRES_ULTIMA_NECAT)
    print(LISTE_MEMBRES_INDEP)

    # with open(chemin_csv, 'r',encoding='utf-8') as csvfile:
    #     spamreader = csv.reader(csvfile, delimiter=',')
    #     for row in spamreader:
    #         ADD = (row[0],int(row[1]))
    #         LISTE_JOUEUR.append(ADD)
    #     LISTE_JOUEUR = sorted(LISTE_JOUEUR,key=lambda x: x[1],reverse=True)
    #     COUNT = 0
    #     print('[center][img]https://www.toria.fr/btc/moiniv.png[/img][/center]')
    #     print('\n')
    #     print('[h3][b]Classement de Renommée par personnage[/b][/h3]')
    #     print('[spoiler][list=1]')
    #     for i in LISTE_JOUEUR:
    #         membre = i[0]
    #         print(change(membre,LISTE_MEMBRES_GOTEI_13,LISTE_MEMBRES_ACUERDO,LISTE_MEMBRES_ULTIMA_NECAT,LISTE_MEMBRES_INDEP),':',str(i[1]),'Renommée')
    #         if COUNT == 9:
    #             print('\n')
    #         COUNT += 1
    #     print('[/list][/spoiler]')