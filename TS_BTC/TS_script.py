import csv
from csv import writer
import pandas as pd
from datetime import date
from datetime import timedelta
import requests
from bs4 import BeautifulSoup
import os
import pandas as pd
import urllib

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
    try:
        COLOR_GOTEI_13 = '[color=#344b99]'
        COLOR_ACUERDO = '[color=#929291]'
        COLOR_ULTIMA_NECAT = '[color=#a23d3c]'
        COLOR_INDEP = '[color=#a2783c]'
        if '+' in membre:
            membre.replace("+"," ")
        if membre == "Katsuo":
            membre = "Shinken Katsuo"
        if membre == 'Sora':
            membre = 'Igarashi Sora'
        if membre == 'Hanae':
            membre = 'Ikeda Hanae'
        if membre == 'Shirahime':
            membre = 'Asano Shirahime'
        if membre == 'Junichiro':
            membre = 'Matsui Junichiro'
        if membre == 'Ganryu':
            membre = 'Kichigai Ganryu'
        if membre == 'Yurei Karasu':
            membre = 'Yane Yoru'
        if membre == 'Kyoakusei Kenshiro':
            membre = 'Kyōakusei Kenshirō'
        if membre == 'Barbe':
            membre = 'Chibiko Daestra'
        if membre == 'Seiichi':
            membre = 'Yuko Seiichi'
        if membre == 'Kuso' or membre == 'kuso':
            membre = 'Keshinohana Kuso'
        if membre == 'Recca':
            membre = 'Akashiya Recca'
        if membre == 'Delila':
            membre = 'Delila Scarlatti'
        if membre == 'Kano':
            membre = 'Shimizu Kano'
        if membre == 'Hiro':
            membre = 'Shunshō Hirō'
        if membre == 'Kiryû' or membre == 'Kiryu Shinjiro':
            membre = 'Kiryū Shinjiro'
        if membre == 'Yoko':
            membre = 'Sabaiba Yoko'
        if membre == 'Hinotori mamoru':
            membre = "Hinotori Mamoru"
        if membre == 'Kichigai Ganryu':
            membre = 'Kichigai Ganryū'
        if membre == 'Cimeries Alastor':
            membre = 'Cimériès Alastor'
        if membre == 'Ogasawara Koga':
            membre = 'Ogasawara Kōga'
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
    except:
        print('erreur change')
        pass

def write_csv(data):
    csv = "/var/www/html/affichage.csv"
    with open(csv, 'a', newline='',encoding='UTF-8') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(data)
        f_object.close()

if __name__=='__main__':
    csv = "/var/www/html/affichage.csv"

    f = open(csv,"w")
    f.close()

    url_gotei_groupe = "https://www.before-tomorrow-comes.fr/g3-gotei-13"
    url_acuerdo_groupe = "https://www.before-tomorrow-comes.fr/g4-acuerdo"
    url_UN_groupe = "https://www.before-tomorrow-comes.fr/g5-ultima-necat"
    url_indep_groupe = "https://www.before-tomorrow-comes.fr/g6-independants"

    LISTE_MEMBRES_GOTEI_13 = web_scraping(url_gotei_groupe,'Gotei 13')
    LISTE_MEMBRES_ACUERDO = web_scraping(url_acuerdo_groupe,'Acuerdo')
    LISTE_MEMBRES_ULTIMA_NECAT = web_scraping(url_UN_groupe,'Ultima Necat')
    LISTE_MEMBRES_INDEP = web_scraping(url_indep_groupe,'Indépendants')

    data = pd.read_csv('https://toria.fr/top-booster/resultats/temp/classement_temp.csv',encoding='latin-1',sep=';',names=["Pseudo", "Classement", "IDmark", "IDmark2", "Total"],skiprows=7)


    PSEUDO = data.Pseudo.T.reset_index().values.tolist()
    VOTES = data.Total.T.reset_index().values.tolist()
    LISTE_PSEUDO = list(PSEUDO)
    LISTE_VOTES = list(VOTES)

    Name = []
    Votes = []
    XP = []
    Final = []
    i = 0
    for row in PSEUDO:
        NOM = LISTE_PSEUDO[i][1]
        TOTAL = int(LISTE_VOTES[i][1])
        Name.append(NOM)
        Votes.append(TOTAL)
        # if TOTAL < 50:
        #     result = 0
        # if TOTAL >= 47 and TOTAL < 97:
            # result = 3
        if TOTAL >= 1 and TOTAL < 147:
            result = 6
        if TOTAL >= 147:
            result = 9
        XP.append(result)
        i += 1

    current_date = date.today()
    current_date = current_date - timedelta(1)
    old_date = current_date - timedelta(7)

    day_current = current_date.day
    month_current = current_date.month
    year_current = current_date.year

    if day_current < 10:
        day_current = '0' + str(day_current)
    if month_current < 10:
        month_current = '0' + str(month_current)
    if year_current < 10:
        year_current = '0' + str(year_current)
    current_date = str(day_current) + '/' +str(month_current)+'/'+  str(year_current)

    day_old = old_date.day
    month_old = old_date.month
    year_old = old_date.year

    if day_old < 10:
        day_old = '0' + str(day_old)
    if month_old < 10:
        month_old = '0' + str(month_old)
    if year_old < 10:
        year_old = '0' + str(year_old)
    old_date = str(day_old) + '/' +str(month_old)+'/'+  str(year_old)

    print("[h3][b]Récompenses du "+str(old_date)+" au "+str(current_date)+"[/b][/h3]")
    write_csv(["[h3][b]Récompenses du "+str(old_date)+" au "+str(current_date)+"[/b][/h3]"])
    print('')
    write_csv([''])
    print("Comme chaque semaine voici le classement des votes sur nos différents top-sites. Pour rappel, si vous franchissez la barre des [b]50/100/150 votes[/b], vous pouvez gagner jusqu'à [b]3/6/9 de Renommée[/b].")
    write_csv(["Comme chaque semaine voici le classement des votes sur nos différents top-sites. Pour rappel, si vous franchissez la barre des [b]50/100/150 votes[/b], vous pouvez gagner jusqu'à [b]3/6/9 de Renommée[/b]."])
    print('')
    write_csv([''])
    print("Les récompensés sont donc les suivants :[list=1]")
    write_csv(["Les récompensés sont donc les suivants :[list=1]"])
    i = 0
    for x,y in zip(Name,XP):
        a = x
        b = y
        Final.append(a)
        Final.append(b)
        if b == 0:
            pass
        if b > 0:
            if i != 0:
                if XP[i] != XP[i-1]:
                    print("")
                    write_csv([''])
            print(change(x,LISTE_MEMBRES_GOTEI_13,LISTE_MEMBRES_ACUERDO,LISTE_MEMBRES_ULTIMA_NECAT,LISTE_MEMBRES_INDEP),":", y,"Renommée")
            write_csv([change(x,LISTE_MEMBRES_GOTEI_13,LISTE_MEMBRES_ACUERDO,LISTE_MEMBRES_ULTIMA_NECAT,LISTE_MEMBRES_INDEP)+" : "+ str(y)+ " Renommée"])
        i += 1

    print("[/list]")
    write_csv(["[/list]"])

    print("BTC compte ", len(Votes)," votants pour cette session.")
    write_csv(["BTC compte " + str(len(Votes)) +" votants pour cette session."])
    print("")
    write_csv([''])
    print("[h2]Merci et bon jeu sur BTC ![/h2]")
    write_csv(["[h2]Merci et bon jeu sur BTC ![/h2]"])

    text = open(csv, "r",encoding='utf-8')
    text = ''.join([i for i in text]).replace('"', '')
    x = open(csv,"w",encoding='utf-8')
    x.writelines(text)
    x.close()
