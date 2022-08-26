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

if __name__=='__main__':
    data = get_data(CHEMIN_ODS)
#     print(json.dumps(data, sort_keys=False, indent=4))
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
    # print('[*][b][Niveau X] Nom[/b]')
    # print('[Branche principale] [Branche secondaire] [Type]')
    # print('[u]Effets :[/u]')
    # print('[u]Dépense :[/u]')
    # print('[spoiler="Descriptif RP"]Description[/spoiler]')
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