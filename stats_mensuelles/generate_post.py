#!/usr/bin/env python
# coding: utf8

import csv
import pandas as pd
import os

__file__ = 'statistiques.csv'
CHEMIN = os.path.dirname(os.path.realpath(__file__))
CHEMIN_CONVERT = CHEMIN.replace('\\','/')

chemin_csv = str(CHEMIN_CONVERT) + '/Documents/python/BTC/stats_mensuelles/statistiques.csv'

# Liste joueurs à éditer suivant le groupe
LISTE_MEMBRES_GOTEI_13 = ['Tomoe Nozomi','Naoki Shiori','Kiryu Shinjiro','Nagatsuki Aizome','Shiro Mayuri','Kyokusei Kenshiro','Kyriu Shinjiro','Chibiko Daestra','Igarashi Sora','Yane Yoru','Hinotori Mamoru','Yuko Seiichi','Sabaiba Yoko','Shunsho Hiro','Shimizu Kano','Keshinohana Kuso','Yuta']
LISTE_MEMBRES_ACUERDO = ['Farasha','Yubel','Borick','Delila Scarlatti','Aviela Garaitz','Cimeries Alastor',"Artemio Vittoria"]
LISTE_MEMBRES_ULTIMA_NECAT = ['Orias','Kichigai Ganryu','Akashiya Recca','Connor Austins','Kisaragi Ryo','Matsui Junichiro','Hasegawa Kimiko']
LISTE_MEMBRES_INDEP = ['Spavento']

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
    LISTE_JOUEUR = []
    with open(chemin_csv, 'r',encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            ADD = (row[0],int(row[1]))
            LISTE_JOUEUR.append(ADD)
        LISTE_JOUEUR = sorted(LISTE_JOUEUR,key=lambda x: x[1],reverse=True)
        COUNT = 0
        print('[center][img]https://www.toria.fr/btc/moiniv.png[/img][/center]')
        print('\n')
        print('[h3][b]Classement de Renommée par personnage[/b][/h3]')
        print('[spoiler][list=1]')
        for i in LISTE_JOUEUR:
            membre = i[0]
            print(change(membre,LISTE_MEMBRES_GOTEI_13,LISTE_MEMBRES_ACUERDO,LISTE_MEMBRES_ULTIMA_NECAT,LISTE_MEMBRES_INDEP),':',str(i[1]),'Renommée')
            if COUNT == 9:
                print('\n')
            COUNT += 1
        print('[/list][/spoiler]')