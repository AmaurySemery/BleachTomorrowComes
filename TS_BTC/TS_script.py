import csv
import pandas as pd
from datetime import date
from datetime import timedelta


# Chemin à éditer
chemin_csv = 'E:\python\BleachTomorrowComes\TS_BTC\classement_BTC.csv'

# Liste joueurs à éditer suivant le groupe
LISTE_MEMBRES_GOTEI_13 = ['Alastair','Celestia']
LISTE_MEMBRES_ACUERDO = ['Endymion','Silas']
LISTE_MEMBRES_ULTIMA_NECAT = ['Esther','Ryme']
LISTE_MEMBRES_INDEP = ['Nessius','Rudjek']

def change(membre,liste_membre_gotei,liste_membre_acuerdo,liste_membre_UN,liste_membre_indep):
    try:
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

    print("<blockquote>[center][b]Récompenses du "+str(old_date)+" au "+str(current_date)+"[/b][/center]")
    print("Comme chaque semaine voici le classement des votes sur nos différents top-sites. Pour rappel, si vous franchissez la barre des [b]50/100/150 votes[/b], vous pouvez gagner jusqu'à [b]3/6/9 de Renommée[/b].")
    print("Les récompensés sont donc les suivants :[list=1]")

    for x,y in zip(Name,XP):
        a = x
        b = y
        Final.append(a)
        Final.append(b)
        print("[*][b]"+change(x,LISTE_MEMBRES_GOTEI_13,LISTE_MEMBRES_ACUERDO,LISTE_MEMBRES_ULTIMA_NECAT,LISTE_MEMBRES_INDEP)+"[/color][/b]",":", y,"XP")

    print("[/list]")

    print("BTC compte", len(Votes),"votants pour cette session.")
    print("Merci à vous et bon jeu sur BTC !")
    print('<blockquote>')