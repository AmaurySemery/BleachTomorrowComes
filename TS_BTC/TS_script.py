import csv
import pandas as pd

def change(membre,liste_membre_gotei,liste_membre_acuerdo,liste_membre_UN,liste_membre_indep):
    try:
        COLOR_GOTEI_13 = '[color=#344b99]'
        COLOR_ACUERDO = '[color=#929291]'
        COLOR_ULTIMA_NECAT = '[color=#a23d3c]'
        COLOR_INDEP = '[color=#a2783c]'
        data = 'membre absent dans la liste'
        if membre in liste_membre_gotei:
            data = '[*][b]' + str(COLOR_GOTEI_13) + str(membre) + '[/color][/b]'
        elif membre in liste_membre_acuerdo:
            data = '[*][b]' + str(COLOR_ACUERDO) + str(membre) + '[/color][/b]'
        elif membre in liste_membre_UN:
            data = '[*][b]' + str(COLOR_ULTIMA_NECAT) + str(membre) + '[/color][/b]'
        elif membre in liste_membre_indep:
            data = '[*][b]' + str(COLOR_INDEP) + str(membre) + '[/color][/b]'
        return data
    except:
        print('erreur change')
        pass

if __name__=='__main__':
    f=open(r"E:\python\BleachTomorrowComes\TS_BTC\classement_BTC.csv")

    r = csv.DictReader(filter(lambda row: row[0]!='#',f), fieldnames = ["Pseudo", "Classement", "IDmark", "IDmark2", "Total"], delimiter = ";")

    LISTE_MEMBRES_GOTEI_13 = ['Alastair','Celestia']
    LISTE_MEMBRES_ACUERDO = ['Endymion','Silas']
    LISTE_MEMBRES_ULTIMA_NECAT = ['Esther','Ryme']
    LISTE_MEMBRES_INDEP = ['Nessius','Rudjek']

    Name = []
    Votes = []
    XP = []
    Final = []
    for row in r:
        print(row)
        a = row['Pseudo']
        b = int(row['Total'])
        Name.append(a)
        Votes.append(b)
        if b < 60:
            result = 0
        if b >= 60 and b < 119:
            result = 3
        if b >= 120 and b < 179:
            result = 5
        if b >= 180:
            result = 8
        XP.append(result)

    datedebut = input("Date début de requête (ex: 22/06): ")
    datefin = input("Date fin de requête (ex: 28/06): ")

    print("<blockquote>[center][b]Récompenses du "+datedebut+" au "+datefin+"[/b][/center]")
    print("Pour rappel, vous gagnez 3 XP par semaine si vous effectuez au moins <b>50</b> votes sur celle-ci.")
    print("Vous gagnez 5 XP au total si vous êtes parmi les 5 meilleurs votants ou que vous avez réalisé plus de 100 votes.")
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