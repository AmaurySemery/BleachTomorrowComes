import csv
import pandas as pd
from datetime import date
from datetime import timedelta
import os

__file__ = 'classement_BTC.csv'
CHEMIN = os.path.dirname(os.path.realpath(__file__))
CHEMIN_CONVERT = CHEMIN.replace('\\','/')

chemin_csv = str(CHEMIN_CONVERT) + '/Documents/python/BTC/TS_BTC/classement_BTC.CSV'


# Liste joueurs à éditer suivant le groupe
LISTE_MEMBRES_GOTEI_13 = ['Tomoe Nozomi','Naoki Shiori','Kiryu Shinjiro','Nagatsuki Aizome']
LISTE_MEMBRES_ACUERDO = ['Farasha']
LISTE_MEMBRES_ULTIMA_NECAT = ['Orias','Kichigai Ganryu','Akashiya Recca']
LISTE_MEMBRES_INDEP = []

def change(membre,liste_membre_gotei,liste_membre_acuerdo,liste_membre_UN,liste_membre_indep):
    try:
        COLOR_GOTEI_13 = '[color=#344b99]'
        COLOR_ACUERDO = '[color=#929291]'
        COLOR_ULTIMA_NECAT = '[color=#a23d3c]'
        COLOR_INDEP = '[color=#a2783c]'
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
            membre = 'Kyokusei Kenshiro'
        if membre == 'Barbe':
            membre = 'Chibiko Daestra'
        if membre == 'Seiichi':
            membre = 'Yuko Seiichi'
        if membre == 'Recca':
            membre = 'Akashiya Recca'
        if membre == 'Delila':
            membre = 'Delila Scarlatti'
        if membre == 'Kano':
            membre = 'Shimizu Kano'
        if membre == 'Hiro':
            membre = 'Shunsho Hiro'
        if membre == 'Kiryû':
            membre = 'Kiryu Shinjiro'
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

if __name__=='__main__':
    f=open(chemin_csv,'r')
    r = csv.DictReader(filter(lambda row: row[0]!='#',f), fieldnames = ["Pseudo", "Classement", "IDmark", "IDmark2", "Total"], delimiter = ";")

    Name = []
    Votes = []
    XP = []
    Final = []
    for row in r:
        a = row['Pseudo']
        b = int(row['Total'])
        Name.append(a)
        Votes.append(b)
        if b < 50:
            result = 0
        if b >= 50 and b < 100:
            result = 3
        if b >= 100 and b < 150:
            result = 6
        if b >= 150:
            result = 9
        XP.append(result)

    current_date = date.today()
    old_date = current_date - timedelta(7)

    print("[h3][b]Récompenses du "+str(old_date)+" au "+str(current_date)+"[/b][/h3]")
    print('\n')
    print("Comme chaque semaine voici le classement des votes sur nos différents top-sites. Pour rappel, si vous franchissez la barre des [b]50/100/150 votes[/b], vous pouvez gagner jusqu'à [b]3/6/9 de Renommée[/b].")
    print('\n')
    print("Les récompensés sont donc les suivants :[list=1]")

    for x,y in zip(Name,XP):
        a = x
        b = y
        Final.append(a)
        Final.append(b)
        print(change(x,LISTE_MEMBRES_GOTEI_13,LISTE_MEMBRES_ACUERDO,LISTE_MEMBRES_ULTIMA_NECAT,LISTE_MEMBRES_INDEP),":", y,"Renommée")

    print("[/list]")

    print("BTC compte", len(Votes),"votants pour cette session.")
    print('\n')
    print("[h2]Merci et bon jeu sur BTC ![/h2]")