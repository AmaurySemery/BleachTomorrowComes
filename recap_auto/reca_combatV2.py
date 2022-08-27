from pyexcel_ods import get_data
import json

CHEMIN_ODS = 'E:/python/BleachTomorrowComes/recap_auto/FT.ods'
CHEMIN_COMBAT_JSON = 'E:/python/BleachTomorrowComes/recap_auto/combat.json'

def maj_json_lancement(PV_DEBUT,PV_TOTAL,EP_DEBUT,EP_TOTAL,ES_DEBUT,ES_TOTAL,PA_DEBUT,COMBO_EP_DEBUT,COMBO_ES_DEBUT,
MAINTENU_SOMME,NEGATIF_SOMME_DEBUT,POSITIF_SOMME_DEBUT):
    with open(CHEMIN_COMBAT_JSON,'r') as json_data:
        data_dict = json.load(json_data)
        data_dict["attributs"]["PV_total"] = PV_TOTAL
        data_dict["attributs"]["EP_total"] = EP_TOTAL
        data_dict["attributs"]["ES_total"] = ES_TOTAL
        data_dict["attributs"]["PV_debut"] = PV_DEBUT
        data_dict["attributs"]["EP_debut"] = EP_DEBUT
        data_dict["attributs"]["ES_debut"] = ES_DEBUT
        data_dict["attributs"]["PA_debut"] = PA_DEBUT
        data_dict["phase_defensive"]["maintenu"] = MAINTENU_SOMME
        data_dict["phase_defensive"]["negatif"] = NEGATIF_SOMME_DEBUT
        data_dict["phase_defensive"]["positif"] = POSITIF_SOMME_DEBUT
        data_str = json.dumps(data_dict, sort_keys=False, indent=4)
        fichier = open(CHEMIN_COMBAT_JSON,'wt')
        fichier.write(data_str)
        fichier.close()

def techniques_defensives():
    def print_for_reca(NIV_TECH,NOM_TECH,BRANCHE_PRINCIPALE_TECH,BRANCHE_SECONDAIRE_TECH,TYPE,
    EFFET,DEPENSE_EP,DEPENSE_ES,DEPENSE_PV,DESCRIPTION,COUT_PA):
        print('[*][b][Niveau '+str(NIV_TECH)+'] '+str(NOM_TECH)+'[/b]')
        if BRANCHE_SECONDAIRE_TECH != 0:
            print('['+str(BRANCHE_PRINCIPALE_TECH)+'] ['+str(BRANCHE_SECONDAIRE_TECH)+'] ['+str(TYPE)+']')
        if BRANCHE_SECONDAIRE_TECH == 0:
            print('['+str(BRANCHE_PRINCIPALE_TECH)+'] ['+str(TYPE)+']')
        print('[u]Effets :[/u] '+str(EFFET))
        if DEPENSE_PV != 0:
            print('[u]Dépense :[/u] '+str(DEPENSE_EP)+' EP & ' +str(DEPENSE_ES)+' ES')
        if DEPENSE_PV == 0:
            print('[u]Dépense :[/u] '+str(DEPENSE_EP)+' EP & ' +str(DEPENSE_ES)+' ES & '+ str(DEPENSE_PV) + 'PV')
        print('[spoiler="Descriptif RP"]'+str(DESCRIPTION)+'[/spoiler]')

    def save_depense_effet(EFFET,DEPENSE_EP,DEPENSE_ES,DEPENSE_PV,COUT_PA):
        with open(CHEMIN_COMBAT_JSON,'r') as json_data:
            data_dict = json.load(json_data)
            POSITIF = data_dict["phase_defensive"]["positif"]
            NEGATIF = data_dict["phase_defensive"]["negatif"]
            TOTAL_DEFENDU = data_dict["synthese"]["total_defendu"]
            TOTAL_SUBI = data_dict["synthese"]["total_subi"]
            PA_DEBUT = data_dict["attributs"]["PA_debut"]
            PA_DEPENSES = data_dict["attributs"]["PA_depenses"]
            PA_RESTANTS = data_dict["attributs"]["PA_restants"]
            POSITIF = int(POSITIF) + int(EFFET)
            TOTAL_DEFENDU = int(NEGATIF) - int(POSITIF)
            if int(TOTAL_DEFENDU) < 0 :
                TOTAL_DEFENDU = 0
            TOTAL_SUBI = int(POSITIF) - int(NEGATIF)
            TOTAL_SUBI = abs(TOTAL_SUBI)
            PA_DEPENSES = int(PA_DEPENSES) + int(COUT_PA)
            PA_RESTANTS = int(PA_DEBUT) - int(PA_DEPENSES)
            data_dict["phase_defensive"]["positif"] = POSITIF
            data_dict["phase_defensive"]["negatif"] = NEGATIF
            data_dict["synthese"]["total_defendu"] = TOTAL_DEFENDU
            data_dict["synthese"]["total_subi"] = TOTAL_SUBI
            data_dict["attributs"]["PA_depenses"] = PA_DEPENSES
            data_dict["attributs"]["PA_restants"] = PA_RESTANTS
            data_str = json.dumps(data_dict, sort_keys=False, indent=4)
            fichier = open(CHEMIN_COMBAT_JSON,'wt')
            fichier.write(data_str)
            fichier.close()

    data = get_data(CHEMIN_ODS)
    NOMBRE_TECH = data['Combat'][0][1]
    a = 2
    b = 0
    for i in range(int(NOMBRE_TECH)):
        print(a)
        NIV_TECH = data['Combat'][0][a]
        print(NIV_TECH)
        ID_TECH = data['Combat'][1][a]
        print(ID_TECH)
        if NIV_TECH == 1:
            c = b + 0
            POSITION = int(c) + int(ID_TECH)
            NOM_TECH = data['Liste_techniques'][1][POSITION]
            BRANCHE_PRINCIPALE_TECH = data['Liste_techniques'][2][POSITION]
            BRANCHE_SECONDAIRE_TECH = data['Liste_techniques'][3][POSITION]
            TYPE = data['Liste_techniques'][4][POSITION]
            EFFET = data['Liste_techniques'][5][POSITION]
            DEPENSE_EP = data['Liste_techniques'][6][POSITION]
            DEPENSE_ES = data['Liste_techniques'][7][POSITION]
            DEPENSE_PV = data['Liste_techniques'][8][POSITION]
            DESCRIPTION = data['Liste_techniques'][9][POSITION]
            COUT_PA = data['Liste_techniques'][12][POSITION]
            print_for_reca(NIV_TECH,NOM_TECH,BRANCHE_PRINCIPALE_TECH,BRANCHE_SECONDAIRE_TECH,TYPE,
    EFFET,DEPENSE_EP,DEPENSE_ES,DEPENSE_PV,DESCRIPTION,COUT_PA)
            save_depense_effet(EFFET,DEPENSE_EP,DEPENSE_ES,DEPENSE_PV)
        elif NIV_TECH == 2:
            c = b + 10
            POSITION = int(c) + int(ID_TECH)
            NOM_TECH = data['Liste_techniques'][1][POSITION]
            BRANCHE_PRINCIPALE_TECH = data['Liste_techniques'][2][POSITION]
            BRANCHE_SECONDAIRE_TECH = data['Liste_techniques'][3][POSITION]
            TYPE = data['Liste_techniques'][4][POSITION]
            EFFET = data['Liste_techniques'][5][POSITION]
            DEPENSE_EP = data['Liste_techniques'][6][POSITION]
            DEPENSE_ES = data['Liste_techniques'][7][POSITION]
            DEPENSE_PV = data['Liste_techniques'][8][POSITION]
            DESCRIPTION = data['Liste_techniques'][9][POSITION]
            COUT_PA = data['Liste_techniques'][12][POSITION]
            print_for_reca(NIV_TECH,NOM_TECH,BRANCHE_PRINCIPALE_TECH,BRANCHE_SECONDAIRE_TECH,TYPE,
    EFFET,DEPENSE_EP,DEPENSE_ES,DEPENSE_PV,DESCRIPTION,COUT_PA)
            save_depense_effet(EFFET,DEPENSE_EP,DEPENSE_ES,DEPENSE_PV)
        elif NIV_TECH == 3:
            c = b + 20
            POSITION = int(c) + int(ID_TECH)
            NOM_TECH = data['Liste_techniques'][1][POSITION]
            BRANCHE_PRINCIPALE_TECH = data['Liste_techniques'][2][POSITION]
            BRANCHE_SECONDAIRE_TECH = data['Liste_techniques'][3][POSITION]
            TYPE = data['Liste_techniques'][4][POSITION]
            EFFET = data['Liste_techniques'][5][POSITION]
            DEPENSE_EP = data['Liste_techniques'][6][POSITION]
            DEPENSE_ES = data['Liste_techniques'][7][POSITION]
            DEPENSE_PV = data['Liste_techniques'][8][POSITION]
            DESCRIPTION = data['Liste_techniques'][9][POSITION]
            COUT_PA = data['Liste_techniques'][12][POSITION]
            print_for_reca(NIV_TECH,NOM_TECH,BRANCHE_PRINCIPALE_TECH,BRANCHE_SECONDAIRE_TECH,TYPE,
    EFFET,DEPENSE_EP,DEPENSE_ES,DEPENSE_PV,DESCRIPTION,COUT_PA)
            save_depense_effet(EFFET,DEPENSE_EP,DEPENSE_ES,DEPENSE_PV)
        elif NIV_TECH == 4:
            c = b + 30
            POSITION = int(c) + int(ID_TECH)
            NOM_TECH = data['Liste_techniques'][1][POSITION]
            BRANCHE_PRINCIPALE_TECH = data['Liste_techniques'][2][POSITION]
            BRANCHE_SECONDAIRE_TECH = data['Liste_techniques'][3][POSITION]
            TYPE = data['Liste_techniques'][4][POSITION]
            EFFET = data['Liste_techniques'][5][POSITION]
            DEPENSE_EP = data['Liste_techniques'][6][POSITION]
            DEPENSE_ES = data['Liste_techniques'][7][POSITION]
            DEPENSE_PV = data['Liste_techniques'][8][POSITION]
            DESCRIPTION = data['Liste_techniques'][9][POSITION]
            COUT_PA = data['Liste_techniques'][12][POSITION]
            print_for_reca(NIV_TECH,NOM_TECH,BRANCHE_PRINCIPALE_TECH,BRANCHE_SECONDAIRE_TECH,TYPE,
    EFFET,DEPENSE_EP,DEPENSE_ES,DEPENSE_PV,DESCRIPTION,COUT_PA)
            save_depense_effet(EFFET,DEPENSE_EP,DEPENSE_ES,DEPENSE_PV)
        elif NIV_TECH == 5:
            c = b + 40
            POSITION = int(c) + int(ID_TECH)
            NOM_TECH = data['Liste_techniques'][1][POSITION]
            BRANCHE_PRINCIPALE_TECH = data['Liste_techniques'][2][POSITION]
            BRANCHE_SECONDAIRE_TECH = data['Liste_techniques'][3][POSITION]
            TYPE = data['Liste_techniques'][4][POSITION]
            EFFET = data['Liste_techniques'][5][POSITION]
            DEPENSE_EP = data['Liste_techniques'][6][POSITION]
            DEPENSE_ES = data['Liste_techniques'][7][POSITION]
            DEPENSE_PV = data['Liste_techniques'][8][POSITION]
            DESCRIPTION = data['Liste_techniques'][9][POSITION]
            COUT_PA = data['Liste_techniques'][12][POSITION]
            print_for_reca(NIV_TECH,NOM_TECH,BRANCHE_PRINCIPALE_TECH,BRANCHE_SECONDAIRE_TECH,TYPE,
    EFFET,DEPENSE_EP,DEPENSE_ES,DEPENSE_PV,DESCRIPTION,COUT_PA)
            save_depense_effet(EFFET,DEPENSE_EP,DEPENSE_ES,DEPENSE_PV)
        a += 1

if __name__=='__main__':
    data = get_data(CHEMIN_ODS)
    # print(json.dumps(data, sort_keys=False, indent=4))
    TOUR = data['Combat'][0][4]
    PV_DEBUT = data['Combat'][2][4]
    PV_TOTAL = data['Combat'][2][5]
    EP_DEBUT = data['Combat'][3][4]
    EP_TOTAL = data['Combat'][3][5]
    ES_DEBUT = data['Combat'][4][4]
    ES_TOTAL = data['Combat'][4][5]
    PA_DEBUT = data['Combat'][5][4]
    COMBO_EP_DEBUT = data['Combat'][21][1]
    COMBO_ES_DEBUT = data['Combat'][22][1]
    MAINTENU_SOMME = data['Combat'][11][1]
    NEGATIF_SOMME_DEBUT = data['Combat'][12][1]
    POSITIF_SOMME_DEBUT = data['Combat'][13][1]

    maj_json_lancement(PV_DEBUT,PV_TOTAL,EP_DEBUT,EP_TOTAL,ES_DEBUT,ES_TOTAL,PA_DEBUT,COMBO_EP_DEBUT,COMBO_ES_DEBUT,
MAINTENU_SOMME,NEGATIF_SOMME_DEBUT,POSITIF_SOMME_DEBUT)

    TOTAL_DEFENDU = 0
    TOTAL_SUBI = 0
    NEGATIF_SOMME_FIN = 0
    POSITIF_SOMME_FIN = 0
    PV_FIN = 0
    EP_FIN = 0
    ES_FIN = 0
    PA_FIN = 0
    PA_BONUS = 0
    COMBO_EP_FIN = 0
    COMBO_ES_FIN = 0

    print('[hide][spoiler="Tour '+ str(TOUR) + '"][h3][color=#929291]Stats de[/color] début de tour[/h3]')
    print('\n')
    print('[b][color=#92d050]Santé : ' + str(PV_DEBUT) + '/' + str(PV_TOTAL) + '[/color][/b]')
    print('[b][color=#c83737]Énergie Physique : ' + str(EP_DEBUT) + '/' + str(EP_TOTAL) + '[/color][/b]')
    print('[b][color=#2a4cbc]Énergie Spirituelle : ' + str(ES_DEBUT) +'/' + str(ES_TOTAL) + '[/color][/b]')
    print('\n')
    print("[b][color=#783da2]Points d'Action : " + str(PA_DEBUT) + "[/color][/b]")
    print('\n')
    print('[b][color=#c83737]Combo EP : '+ str(COMBO_EP_DEBUT) +'[/color][/b]')
    print('[b][color=#2a4cbc]Combo ES : '+ str(COMBO_ES_DEBUT) +'[/color][/b]')
    print('\n')
    print('[h3][color=#929291]Phase [color=#344b99]Défensive[/color][/color][/h3]')
    print('\n')
    print('[u][b][color=#a2783c]Récapitulatif :[/color][/b][/u][list]')
    print('[*][b]Maintenu :[/b] ' + str(MAINTENU_SOMME))
    print('[*][b]Valeurs négatives :[/b] ' + str(NEGATIF_SOMME_DEBUT))
    print('[*][b]Valeurs positives :[/b] ' + str(POSITIF_SOMME_DEBUT))
    print('[/list][u][b][color=#a2783c]Techniques défensives :[/color][/b][/u][list]')

    techniques_defensives()

    print('[/list][u][b][color=#a2783c]Résumé phase défensive :[/color][/b][/u]')
    print('[list][*][b]Défendu :[/b] ' + str(TOTAL_DEFENDU))
    print('[*][b]Subi :[/b] ' + str(TOTAL_SUBI) + ' [/list]')
    print('[h3][color=#929291]Phase [color=#a23d3c]Offensive[/color][/color][/h3]')
    print('\n')
    print('[u][b][color=#a2783c]Techniques offensives :[/color][/b][/u][list]')
    # print('[*][b][Niveau X] Nom[/b]')
    # print('[Branche principale] [Branche secondaire] [Type]')
    # print('[u]Effets :[/u]')
    # print('[u]Dépense :[/u]')
    # print('[spoiler="Descriptif RP"]Description[/spoiler]')
    print('[/list][u][b][color=#a2783c]Récapitulatif :[/color][/b][/u]')
    print('[list][*][b]Valeurs négatives :[/b] ' + str(NEGATIF_SOMME_FIN))
    print('[*][b]Valeurs positives :[/b] ' + str(POSITIF_SOMME_FIN) + '[/list]')
    print('[h3][color=#929291]Stats de[/color] fin de tour[/h3]')
    print('\n')
    print('[b][color=#92d050]Santé : [color=#f9f9f9]' + str(PV_FIN) + '[/color]/' + str(PV_TOTAL) + '[/color][/b]')
    print('[b][color=#c83737]Énergie Physique : [color=#f9f9f9]' + str(EP_FIN) + '[/color]/' + str(EP_TOTAL) + '[/color][/b]')
    print('[b][color=#2a4cbc]Énergie Spirituelle : [color=#f9f9f9]' + str(ES_FIN) + '[/color]/' + str(ES_TOTAL) + '[/color][/b]')
    print('\n')
    print("[b][color=#783da2]Points d'Action : [color=#f9f9f9]" + str(PA_FIN) + "[/color]/X[/color][/b] (+" + str(PA_BONUS) + " PA au prochain tour)")
    print('\n')
    print('[b][color=#c83737]Combo EP : ' + str(COMBO_EP_FIN) + '[/color][/b]')
    print('[b][color=#2a4cbc]Combo ES : ' + str(COMBO_ES_FIN) + '[/color][/b][/spoiler][/hide]')