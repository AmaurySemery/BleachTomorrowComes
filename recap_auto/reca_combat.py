from pyexcel_ods import get_data
import json

# CHEMIN_ODS = "TON_CHEMIN_ABSOLU_VERS_LE_DOC_ODS"
CHEMIN_ODS = "E:\python\BTC\TestsRepartition.ods"

def liste_tech_def(NOMBRE_TECH_DEF,LISTE_LEVEL_TECH_DEF,LISTE_ID_TECH_DEF,data,state):
    try:
        def get_data_ods(LISTE_LEVEL_TECH_DEF,LISTE_ID_TECH_DEF,data,n,a,i):
            try:
                a = LISTE_ID_TECH_DEF[i]
                NOM = data['Test'][int(n)+int(a)][1]
                BRANCHE_PRINCIPALE = data['Test'][int(n)+int(a)][2]
                BRANCHE_SECONDAIRE = data['Test'][int(n)+int(a)][3]
                TYPE = data['Test'][int(n)+int(a)][4]
                EFFET = data['Test'][int(n)+int(a)][5]
                EP_DEPENSE = data['Test'][int(n)+int(a)][6]
                ES_DEPENSE = data['Test'][int(n)+int(a)][7]
                DESCRIPTIF_RP = data['Test'][int(n)+int(a)][9]

                print('[*][b][Niveau ' + str(LISTE_LEVEL_TECH_DEF[i]) + ']' + str(NOM) + '[/b][' + str(BRANCHE_PRINCIPALE) + '][' + str(BRANCHE_SECONDAIRE) + '][' + str(TYPE) + ']')
                print('[u]Effets :[/u] ' + str(EFFET))
                print('[u]Dépense :[/u] ' + str(EP_DEPENSE) + ' EP / ' + str(ES_DEPENSE) + ' ES')
                print('[spoiler="' + str(DESCRIPTIF_RP) + '"]Description[/spoiler]')
            except:
                print('erreur get_data_ods')
                pass

        def ep_depense(LISTE_LEVEL_TECH_DEF,LISTE_ID_TECH_DEF,data,n,a,i):
            try:
                EP_DEPENSE = data['Test'][int(n)+int(a)][6]
                return int(EP_DEPENSE)
            except:
                print('erreur ep_depense')
                pass

        def es_depense(LISTE_LEVEL_TECH_DEF,LISTE_ID_TECH_DEF,data,n,a,i):
            try:
                ES_DEPENSE = data['Test'][int(n)+int(a)][7]
                return int(ES_DEPENSE)
            except:
                print('erreur es_depense')
                pass

        i = 0
        EP_DEPENSE = 0
        ES_DEPENSE = 0
        for i in range(int(NOMBRE_TECH_DEF)):
            if int(LISTE_LEVEL_TECH_DEF[i]) == 1:
                n = 9
                a = LISTE_ID_TECH_DEF[i]
                if state == 0:
                    get_data_ods(LISTE_LEVEL_TECH_DEF,LISTE_ID_TECH_DEF,data,n,a,i)
                if state == 1:
                    EP_CHANGE = ep_depense(LISTE_LEVEL_TECH_DEF,LISTE_ID_TECH_DEF,data,n,a,i)
                    ES_CHANGE = es_depense(LISTE_LEVEL_TECH_DEF,LISTE_ID_TECH_DEF,data,n,a,i)
                    EP_DEPENSE = EP_DEPENSE + EP_CHANGE
                    ES_DEPENSE = ES_DEPENSE + ES_CHANGE
            if int(LISTE_LEVEL_TECH_DEF[i]) == 2:
                n = 19
                a = LISTE_ID_TECH_DEF[i]
                if state == 0:
                    get_data_ods(LISTE_LEVEL_TECH_DEF,LISTE_ID_TECH_DEF,data,n,a,i)
                if state == 1:
                    EP_CHANGE = ep_depense(LISTE_LEVEL_TECH_DEF,LISTE_ID_TECH_DEF,data,n,a,i)
                    ES_CHANGE = es_depense(LISTE_LEVEL_TECH_DEF,LISTE_ID_TECH_DEF,data,n,a,i)
                    EP_DEPENSE = EP_DEPENSE + EP_CHANGE
                    ES_DEPENSE = ES_DEPENSE + ES_CHANGE
            if int(LISTE_LEVEL_TECH_DEF[i]) == 3:
                n = 29
                a = LISTE_ID_TECH_DEF[i]
                if state == 0:
                    get_data_ods(LISTE_LEVEL_TECH_DEF,LISTE_ID_TECH_DEF,data,n,a,i)
                if state == 1:
                    EP_CHANGE = ep_depense(LISTE_LEVEL_TECH_DEF,LISTE_ID_TECH_DEF,data,n,a,i)
                    ES_CHANGE = es_depense(LISTE_LEVEL_TECH_DEF,LISTE_ID_TECH_DEF,data,n,a,i)
                    EP_DEPENSE = EP_DEPENSE + EP_CHANGE
                    ES_DEPENSE = ES_DEPENSE + ES_CHANGE
            if int(LISTE_LEVEL_TECH_DEF[i]) == 4:
                n = 39
                a = LISTE_ID_TECH_DEF[i]
                if state == 0:
                    get_data_ods(LISTE_LEVEL_TECH_DEF,LISTE_ID_TECH_DEF,data,n,a,i)
                if state == 1:
                    EP_CHANGE = ep_depense(LISTE_LEVEL_TECH_DEF,LISTE_ID_TECH_DEF,data,n,a,i)
                    ES_CHANGE = es_depense(LISTE_LEVEL_TECH_DEF,LISTE_ID_TECH_DEF,data,n,a,i)
                    EP_DEPENSE = EP_DEPENSE + EP_CHANGE
                    ES_DEPENSE = ES_DEPENSE + ES_CHANGE
            if int(LISTE_LEVEL_TECH_DEF[i]) == 5:
                n = 49
                a = LISTE_ID_TECH_DEF[i]
                if state == 0:
                    get_data_ods(LISTE_LEVEL_TECH_DEF,LISTE_ID_TECH_DEF,data,n,a,i)
                if state == 1:
                    EP_CHANGE = ep_depense(LISTE_LEVEL_TECH_DEF,LISTE_ID_TECH_DEF,data,n,a,i)
                    ES_CHANGE = es_depense(LISTE_LEVEL_TECH_DEF,LISTE_ID_TECH_DEF,data,n,a,i)
                    EP_DEPENSE = EP_DEPENSE + EP_CHANGE
                    ES_DEPENSE = ES_DEPENSE + ES_CHANGE
            i += 1
        DEPENSE = []
        DEPENSE.append(str(EP_DEPENSE))
        DEPENSE.append(str(ES_DEPENSE))
        return DEPENSE
    except:
        print('erreur liste_tech_def')
        pass

def liste_tech_off(NOMBRE_TECH_OFF,LISTE_LEVEL_TECH_OFF,LISTE_ID_TECH_OFF,data,state):
    try:
        def get_data_ods(LISTE_LEVEL_TECH_OFF,LISTE_ID_TECH_OFF,data,n,a,i):
            try:
                a = LISTE_ID_TECH_DEF[i]
                NOM = data['Test'][int(n)+int(a)][1]
                BRANCHE_PRINCIPALE = data['Test'][int(n)+int(a)][2]
                BRANCHE_SECONDAIRE = data['Test'][int(n)+int(a)][3]
                TYPE = data['Test'][int(n)+int(a)][4]
                EFFET = data['Test'][int(n)+int(a)][5]
                EP_DEPENSE = data['Test'][int(n)+int(a)][6]
                ES_DEPENSE = data['Test'][int(n)+int(a)][7]
                DESCRIPTIF_RP = data['Test'][int(n)+int(a)][9]

                print('[*][b][Niveau ' + str(LISTE_LEVEL_TECH_DEF[i]) + ']' + str(NOM) + '[/b][' + str(BRANCHE_PRINCIPALE) + '][' + str(BRANCHE_SECONDAIRE) + '][' + str(TYPE) + ']')
                print('[u]Effets :[/u] ' + str(EFFET))
                print('[u]Dépense :[/u] ' + str(EP_DEPENSE) + ' EP / ' + str(ES_DEPENSE) + ' ES')
                print('[spoiler="' + str(DESCRIPTIF_RP) + '"]Description[/spoiler]')
            except:
                print('erreur get_data_ods')
                pass

        def ep_depense(LISTE_LEVEL_TECH_OFF,LISTE_ID_TECH_OFF,data,n,a,i):
            try:
                EP_DEPENSE = data['Test'][int(n)+int(a)][6]
                return int(EP_DEPENSE)
            except:
                print('erreur ep_depense')
                pass

        def es_depense(LISTE_LEVEL_TECH_OFF,LISTE_ID_TECH_OFF,data,n,a,i):
            try:
                ES_DEPENSE = data['Test'][int(n)+int(a)][7]
                return int(ES_DEPENSE)
            except:
                print('erreur es_depense')
                pass

        i = 0
        EP_DEPENSE = 0
        ES_DEPENSE = 0

        for i in range(int(NOMBRE_TECH_OFF)):
            if int(LISTE_LEVEL_TECH_OFF[i]) == 1:
                n = 9
                a = LISTE_ID_TECH_OFF[i]
                if state == 0:
                    get_data_ods(LISTE_LEVEL_TECH_OFF,LISTE_ID_TECH_OFF,data,n,a,i)
                if state == 1:
                    EP_CHANGE = ep_depense(LISTE_LEVEL_TECH_OFF,LISTE_ID_TECH_OFF,data,n,a,i)
                    ES_CHANGE = es_depense(LISTE_LEVEL_TECH_OFF,LISTE_ID_TECH_OFF,data,n,a,i)
                    get_data_ods(LISTE_LEVEL_TECH_OFF,LISTE_ID_TECH_OFF,data,n,a,i)
                    EP_DEPENSE = EP_DEPENSE + EP_CHANGE
                    ES_DEPENSE = ES_DEPENSE + ES_CHANGE
            if int(LISTE_LEVEL_TECH_OFF[i]) == 2:
                n = 19
                a = LISTE_ID_TECH_OFF[i]
                if state == 0:
                    get_data_ods(LISTE_LEVEL_TECH_OFF,LISTE_ID_TECH_OFF,data,n,a,i)
                if state == 1:
                    EP_CHANGE = ep_depense(LISTE_LEVEL_TECH_OFF,LISTE_ID_TECH_OFF,data,n,a,i)
                    ES_CHANGE = es_depense(LISTE_LEVEL_TECH_OFF,LISTE_ID_TECH_OFF,data,n,a,i)
                    get_data_ods(LISTE_LEVEL_TECH_OFF,LISTE_ID_TECH_OFF,data,n,a,i)
                    EP_DEPENSE = EP_DEPENSE + EP_CHANGE
                    ES_DEPENSE = ES_DEPENSE + ES_CHANGE
            if int(LISTE_LEVEL_TECH_OFF[i]) == 3:
                n = 29
                a = LISTE_ID_TECH_OFF[i]
                if state == 0:
                    get_data_ods(LISTE_LEVEL_TECH_OFF,LISTE_ID_TECH_OFF,data,n,a,i)
                if state == 1:
                    EP_CHANGE = ep_depense(LISTE_LEVEL_TECH_OFF,LISTE_ID_TECH_OFF,data,n,a,i)
                    ES_CHANGE = es_depense(LISTE_LEVEL_TECH_OFF,LISTE_ID_TECH_OFF,data,n,a,i)
                    get_data_ods(LISTE_LEVEL_TECH_OFF,LISTE_ID_TECH_OFF,data,n,a,i)
                    EP_DEPENSE = EP_DEPENSE + EP_CHANGE
                    ES_DEPENSE = ES_DEPENSE + ES_CHANGE
            if int(LISTE_LEVEL_TECH_OFF[i]) == 4:
                n = 39
                a = LISTE_ID_TECH_OFF[i]
                if state == 0:
                    get_data_ods(LISTE_LEVEL_TECH_OFF,LISTE_ID_TECH_OFF,data,n,a,i)
                if state == 1:
                    EP_CHANGE = ep_depense(LISTE_LEVEL_TECH_OFF,LISTE_ID_TECH_OFF,data,n,a,i)
                    ES_CHANGE = es_depense(LISTE_LEVEL_TECH_OFF,LISTE_ID_TECH_OFF,data,n,a,i)
                    get_data_ods(LISTE_LEVEL_TECH_OFF,LISTE_ID_TECH_OFF,data,n,a,i)
                    EP_DEPENSE = EP_DEPENSE + EP_CHANGE
                    ES_DEPENSE = ES_DEPENSE + ES_CHANGE
            if int(LISTE_LEVEL_TECH_OFF[i]) == 5:
                n = 49
                a = LISTE_ID_TECH_OFF[i]
                if state == 0:
                    get_data_ods(LISTE_LEVEL_TECH_OFF,LISTE_ID_TECH_OFF,data,n,a,i)
                if state == 1:
                    EP_CHANGE = ep_depense(LISTE_LEVEL_TECH_OFF,LISTE_ID_TECH_OFF,data,n,a,i)
                    ES_CHANGE = es_depense(LISTE_LEVEL_TECH_OFF,LISTE_ID_TECH_OFF,data,n,a,i)
                    get_data_ods(LISTE_LEVEL_TECH_OFF,LISTE_ID_TECH_OFF,data,n,a,i)
                    EP_DEPENSE = EP_DEPENSE + EP_CHANGE
                    ES_DEPENSE = ES_DEPENSE + ES_CHANGE
            i += 1
        DEPENSE = []
        DEPENSE.append(str(EP_DEPENSE))
        DEPENSE.append(str(ES_DEPENSE))
        return DEPENSE
    except:
        print('erreur liste_tech_off')
        pass


if __name__=='__main__':
    data = get_data(CHEMIN_ODS)
    print(json.dumps(data, sort_keys=False, indent=4))
    TOUR = data['Test'][0][1]
    SANTE_ACTUELLE_DEBUT = data['Test'][2][1]
    SANTE_TOTALE_DEBUT = data['Test'][2][2]
    ENERGIE_PHYSIQUE_ACTUELLE_DEBUT = data['Test'][3][1]
    ENERGIE_PHYSIQUE_TOTALE_DEBUT = data['Test'][3][2]
    ENERGIE_SPIRITUELLE_ACTUELLE_DEBUT = data['Test'][3][1]
    ENERGIE_SPIRITUELLE_TOTALE_DEBUT = data['Test'][3][2]
    PA_ACTUEL = data['Test'][5][1]
    PA_TOTAL = data['Test'][5][2]
    PA_REGEN = data['Test'][5][3]
    COMBO_EP_DEBUT = data['Test'][5][1]
    COMBO_ES_DEBUT = data['Test'][6][1]
    MAINTENU = data['Test'][1][6]
    VALEURS_NEGATIVES_DEF = data['Test'][2][6]
    VALEURS_POSITIVES_DEF = data['Test'][3][6]
    TOTAL_DEFENDU = data['Test'][2][8]
    TOTAL_SUBI = data['Test'][3][8]
    VALEURS_NEGATIVES_OFF = data['Test'][5][5]
    VALEURS_POSITIVES_OFF = data['Test'][6][5]

    print('------------------')

    LISTE_LEVEL_TECH_DEF = []
    LISTE_ID_TECH_DEF = []
    LISTE_LEVEL_TECH_OFF = []
    LISTE_ID_TECH_OFF = []
    PA_CHANGE = input("Combien de points d'actions veux tu dépenser ? ")
    COMBO_EP_CHANGE = input("Combien de points combo EP gagnes tu ? ")
    COMBO_ES_CHANGE = input("Combien de points combo ES gagnes tu ? ")
    NOMBRE_TECH_DEF = input("Combien de techniques défensives veux-tu utiliser ? ")
    i = 1
    for i in range(int(NOMBRE_TECH_DEF)):
        NIVEAU_TECH_DEF = input("Quel sera le niveau de ta technique " + str(i) + " ? (ex: 1) ")
        LISTE_LEVEL_TECH_DEF.append(str(NIVEAU_TECH_DEF))
        TECH_DEF = input("Quel sera l'ID de ta technique " + str(i) + " ? (ex: 3) ")
        LISTE_ID_TECH_DEF.append(str(TECH_DEF))
        i += 1

    NOMBRE_TECH_OFF = input("Combien de techniques offensives veux-tu utiliser ? ")
    i = 1
    for i in range(int(NOMBRE_TECH_OFF)):
        NIVEAU_TECH_OFF = input("Quel sera le niveau de ta technique " + str(i) + " ? (ex: 1) ")
        LISTE_LEVEL_TECH_OFF.append(str(NIVEAU_TECH_OFF))
        TECH_OFF = input("Quel sera l'ID de ta technique " + str(i) + " ? (ex: 3) ")
        LISTE_ID_TECH_OFF.append(str(TECH_OFF))
        i += 1

    print('\n')
    print('------------------')
    print('\n')

    print('[b]Tour ' + str(TOUR) + '[/b]')
    print('[h4]Stats de début de tour :[/h4]')
    print('\n')
    print('[b][color=#4F6D32]Santé : '+ str(SANTE_ACTUELLE_DEBUT) + '/' + str(SANTE_TOTALE_DEBUT) + '[/color][/b]')
    print('[b][color=#6B150E]Énergie Physique : ' + str(ENERGIE_PHYSIQUE_ACTUELLE_DEBUT) + '/' + str(ENERGIE_PHYSIQUE_TOTALE_DEBUT) + '[/color][/b]')
    print('[b][color=#3E75A4]Énergie Spirituelle : '+ str(ENERGIE_SPIRITUELLE_ACTUELLE_DEBUT) + '/' + str(ENERGIE_SPIRITUELLE_TOTALE_DEBUT) + '[/color][/b]')
    print('\n')
    print('[b]'+ str(PA_ACTUEL) + " Points d'Action[/b]")
    print('\n')
    print('[b][color=#953734]Combo EP : '+ str(COMBO_EP_DEBUT) + '[/color][/b]')
    print('[b][color=#366092]Combo ES : '+ str(COMBO_ES_DEBUT) + '[/color][/b]')
    print('\n')
    print('[h4]Phase Défensive[/h4]')
    print('\n')
    print('[u][b][color=#9E6929]Récapitulatif :[/color][/b][/u]')
    print('[list][*][b]Maintenu :[/b] ' + str(MAINTENU))
    print('[*][b]Valeurs négatives :[/b] ' + str(VALEURS_NEGATIVES_DEF))
    print('[*][b]Valeurs positives :[/b] ' + str(VALEURS_POSITIVES_DEF) + ' [/list][u][b][color=#9E6929]Techniques défensives :[/color][/b][/u][list]')
    liste_tech_def(NOMBRE_TECH_DEF,LISTE_LEVEL_TECH_DEF,LISTE_ID_TECH_DEF,data,0)
    print('[/list][u][b][color=#9E6929]Résumé phase défensive :[/color][/b][/u]')
    print("[list][*][b]Défendu :[/b]" + str(TOTAL_DEFENDU))
    print("[*][b]Subi :[/b]" + str(TOTAL_SUBI) + "[/list]")
    print('[h4]Phase Offensive[/h4]')
    print('\n')
    print('[u][b][color=#9E6929]Techniques offensives :[/color][/b][/u][list]')
    liste_tech_off(NOMBRE_TECH_OFF,LISTE_LEVEL_TECH_OFF,LISTE_ID_TECH_OFF,data,0)
    print('[/list][u][b][color=#9E6929]Résumé phase offensive :[/color][/b][/u]')
    print('[list][*][b]Valeurs négatives :[/b]' + str(VALEURS_NEGATIVES_OFF))
    print('[*][b]Valeurs positives :[/b]' + str(VALEURS_POSITIVES_OFF) + '[/list]')
    print('[h4]Stats de fin de tour :[/h4]')
    print('\n')

    SANTE_ACTUELLE_FIN = int(SANTE_ACTUELLE_DEBUT) - int(TOTAL_SUBI)
    LISTES_PHYSIQUE_SPIRITUELLE_DEF = liste_tech_def(NOMBRE_TECH_DEF,LISTE_LEVEL_TECH_DEF,LISTE_ID_TECH_DEF,data,1)
    DEPENSE_PHYSIQUE_DEF = LISTES_PHYSIQUE_SPIRITUELLE_DEF[0]
    DEPENSE_SPIRITUELLE_DEF = LISTES_PHYSIQUE_SPIRITUELLE_DEF[1]
    LISTES_PHYSIQUE_SPIRITUELLE_OFF = liste_tech_off(NOMBRE_TECH_OFF,LISTE_LEVEL_TECH_OFF,LISTE_ID_TECH_OFF,data,1)
    DEPENSE_PHYSIQUE_OFF = LISTES_PHYSIQUE_SPIRITUELLE_OFF[0]
    DEPENSE_SPIRITUELLE_OFF = LISTES_PHYSIQUE_SPIRITUELLE_OFF[1]

    ENERGIE_PHYSIQUE_ACTUELLE_FIN = int(ENERGIE_PHYSIQUE_ACTUELLE_DEBUT) - int(DEPENSE_PHYSIQUE_DEF) - int(DEPENSE_PHYSIQUE_OFF)
    ENERGIE_SPIRITUELLE_ACTUELLE_FIN = int(ENERGIE_SPIRITUELLE_ACTUELLE_DEBUT) - int(DEPENSE_SPIRITUELLE_DEF) - int(DEPENSE_SPIRITUELLE_OFF)

    print('[b][color=#4F6D32]Santé : '+ str(SANTE_ACTUELLE_FIN) + '/' + str(SANTE_TOTALE_DEBUT) + '[/color][/b]')
    print('[b][color=#6B150E]Énergie Physique : '+ str(ENERGIE_PHYSIQUE_ACTUELLE_FIN) + '/' + str(ENERGIE_PHYSIQUE_TOTALE_DEBUT) + '[/color][/b]')
    print('[b][color=#3E75A4]Énergie Spirituelle : '+ str(ENERGIE_SPIRITUELLE_ACTUELLE_FIN) + '/' + str(ENERGIE_SPIRITUELLE_TOTALE_DEBUT) + '[/color][/b]')
    print('\n')
    PA_ACTUEL_FIN = int(PA_ACTUEL) - int(PA_CHANGE)
    print('[b]' + str(PA_ACTUEL_FIN) + '/' + str(PA_TOTAL) +  " Points d'Action[/b] (+" + str(PA_REGEN) + ' PA au prochain tour)')
    print('\n')
    COMBO_EP_FIN = int(COMBO_EP_DEBUT) + int(COMBO_EP_CHANGE)
    COMBO_ES_FIN = int(COMBO_ES_DEBUT) + int(COMBO_ES_CHANGE)
    print('[b][color=#953734]Combo EP : '+ str(COMBO_EP_FIN) + '[/color][/b]')
    print('[b][color=#366092]Combo ES : '+ str(COMBO_ES_FIN) + '[/color][/b]')