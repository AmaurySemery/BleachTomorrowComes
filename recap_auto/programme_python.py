from pyexcel_ods import get_data
import json
import os

__file__ = 'programme_python.py'
CHEMIN = os.path.dirname(os.path.realpath(__file__))
CHEMIN_CONVERT = CHEMIN.replace('\\','/')

CHEMIN_ODS = str(CHEMIN_CONVERT) + '/Documents/python/BTC/recap_auto/FT.ods'
CHEMIN_COMBAT_JSON = str(CHEMIN_CONVERT) + '/Documents/python/BTC/recap_auto/combat.json'

# CHEMIN_SYSCO_JSON = '"E:/python/BleachTomorrowComes/recap_auto/sysco.json"'

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
        data_dict["combo"]["combo_EP_debut"] = COMBO_EP_DEBUT
        data_dict["combo"]["combo_ES_debut"] = COMBO_ES_DEBUT
        data_str = json.dumps(data_dict, sort_keys=False, indent=4)
        fichier = open(CHEMIN_COMBAT_JSON,'wt')
        fichier.write(data_str)
        fichier.close()

def optionnel_multicibles(EFFET,CODE_TYPE_EFFET,DEPENSE_EP,DEPENSE_ES):
    if CODE_TYPE_EFFET == 'multcib':
        with open(CHEMIN_COMBAT_JSON,'r') as json_data:
            data_dict = json.load(json_data)
            COUNT = data_dict["multicibles"]["count"]
            COUNT = int(COUNT) + 1
            data_dict["multicibles"]["count"] = COUNT
            data_str = json.dumps(data_dict, sort_keys=False, indent=4)
            fichier = open(CHEMIN_COMBAT_JSON,'wt')
            fichier.write(data_str)
            fichier.close()
        data = get_data(CHEMIN_ODS)
        if COUNT == 1:
            MULTICIBLES = data['Combat'][34][1]
            if MULTICIBLES != 0:
                CONVERT_DEPENSE_EP = (int(DEPENSE_EP) * 1) - int(DEPENSE_EP)
                CONVERT_DEPENSE_ES = (int(DEPENSE_ES) * 1) - int(DEPENSE_ES)
                with open(CHEMIN_COMBAT_JSON,'r') as json_data:
                    data_dict = json.load(json_data)
                    EP = data_dict["attributs"]["EP_fin"]
                    ES = data_dict["attributs"]["ES_fin"]
                    CONVERT_EP =  int(EP) + int(CONVERT_DEPENSE_EP)
                    CONVERT_ES = int(ES) + int(CONVERT_DEPENSE_ES)
                    COUNT = int(COUNT) + 1
                    data_dict["attributs"]["EP_fin"] = CONVERT_EP
                    data_dict["attributs"]["ES_fin"] = CONVERT_ES
                    data_str = json.dumps(data_dict, sort_keys=False, indent=4)
                    fichier = open(CHEMIN_COMBAT_JSON,'wt')
                    fichier.write(data_str)
                    fichier.close()
        elif COUNT == 2:
            MULTICIBLES = data['Combat'][35][1]
            if MULTICIBLES != 0:
                CONVERT_DEPENSE_EP = (int(DEPENSE_EP) * 2) - int(DEPENSE_EP)
                CONVERT_DEPENSE_ES = (int(DEPENSE_ES) * 2) - int(DEPENSE_ES)
                with open(CHEMIN_COMBAT_JSON,'r') as json_data:
                    data_dict = json.load(json_data)
                    EP = data_dict["attributs"]["EP_fin"]
                    ES = data_dict["attributs"]["ES_fin"]
                    CONVERT_EP =  int(EP) + int(CONVERT_DEPENSE_EP)
                    CONVERT_ES = int(ES) + int(CONVERT_DEPENSE_ES)
                    COUNT = int(COUNT) + 1
                    data_dict["attributs"]["EP_fin"] = CONVERT_EP
                    data_dict["attributs"]["ES_fin"] = CONVERT_ES
                    data_str = json.dumps(data_dict, sort_keys=False, indent=4)
                    fichier = open(CHEMIN_COMBAT_JSON,'wt')
                    fichier.write(data_str)
                    fichier.close()
        elif COUNT == 3:
            MULTICIBLES = data['Combat'][36][1]
            if MULTICIBLES != 0:
                CONVERT_DEPENSE_EP = (int(DEPENSE_EP) * 3) - int(DEPENSE_EP)
                CONVERT_DEPENSE_ES = (int(DEPENSE_ES) * 3) - int(DEPENSE_ES)
                with open(CHEMIN_COMBAT_JSON,'r') as json_data:
                    data_dict = json.load(json_data)
                    EP = data_dict["attributs"]["EP_fin"]
                    ES = data_dict["attributs"]["ES_fin"]
                    CONVERT_EP =  int(EP) + int(CONVERT_DEPENSE_EP)
                    CONVERT_ES = int(ES) + int(CONVERT_DEPENSE_ES)
                    COUNT = int(COUNT) + 1
                    data_dict["attributs"]["EP_fin"] = CONVERT_EP
                    data_dict["attributs"]["ES_fin"] = CONVERT_ES
                    data_str = json.dumps(data_dict, sort_keys=False, indent=4)
                    fichier = open(CHEMIN_COMBAT_JSON,'wt')
                    fichier.write(data_str)
                    fichier.close()
        elif COUNT == 4:
            MULTICIBLES = data['Combat'][37][1]
            if MULTICIBLES != 0:
                CONVERT_DEPENSE_EP = (int(DEPENSE_EP) * 4) - int(DEPENSE_EP)
                CONVERT_DEPENSE_ES = (int(DEPENSE_ES) * 4) - int(DEPENSE_ES)
                with open(CHEMIN_COMBAT_JSON,'r') as json_data:
                    data_dict = json.load(json_data)
                    EP = data_dict["attributs"]["EP_fin"]
                    ES = data_dict["attributs"]["ES_fin"]
                    CONVERT_EP =  int(EP) + int(CONVERT_DEPENSE_EP)
                    CONVERT_ES = int(ES) + int(CONVERT_DEPENSE_ES)
                    COUNT = int(COUNT) + 1
                    data_dict["attributs"]["EP_fin"] = CONVERT_EP
                    data_dict["attributs"]["ES_fin"] = CONVERT_ES
                    data_str = json.dumps(data_dict, sort_keys=False, indent=4)
                    fichier = open(CHEMIN_COMBAT_JSON,'wt')
                    fichier.write(data_str)
                    fichier.close()

def techniques_defensives():
    def immobilisation():
        data = get_data(CHEMIN_ODS)
        IMMOBILISATION_SUBI = data['Combat'][15][4]
        DEFENSE_INVESTI = data['Combat'][16][4]
        with open(CHEMIN_COMBAT_JSON,'r') as json_data:
            data_dict = json.load(json_data)
            IMMOBILISATION = data_dict["phase_defensive"]["immobilisation"]
            DEFENDU = data_dict["synthese"]["total_defendu"]
            if DEFENSE_INVESTI > 0:
                IMMOBILISATION = int(IMMOBILISATION_SUBI) - int(DEFENSE_INVESTI)
                if IMMOBILISATION < 0:
                    IMMOBILISATION = 0
            if DEFENSE_INVESTI == 0:
                IMMOBILISATION = 0
            data_dict["phase_defensive"]["immobilisation"] = IMMOBILISATION
            data_str = json.dumps(data_dict, sort_keys=False, indent=4)
            fichier = open(CHEMIN_COMBAT_JSON,'wt')
            fichier.write(data_str)
            fichier.close()

    def entrave():
        data = get_data(CHEMIN_ODS)
        ENTRAVE_SUBI = data['Combat'][15][5]
        DEFENSE_INVESTI = data['Combat'][16][5]
        with open(CHEMIN_COMBAT_JSON,'r') as json_data:
            data_dict = json.load(json_data)
            ENTRAVE = data_dict["phase_defensive"]["entrave"]
            POSITIF = data_dict["phase_defensive"]["positif"]
            SUBI = int(ENTRAVE_SUBI) - int(DEFENSE_INVESTI)
            if SUBI < 0:
                SUBI = 0
            ENTRAVE = int(ENTRAVE) + int(SUBI)
            POSITIF = int(POSITIF) - int(DEFENSE_INVESTI)
            if POSITIF < 0:
                POSITIF = 0
            data_dict["phase_offensive"]["entrave_subi"] = ENTRAVE
            data_dict["phase_defensive"]["positif"] = POSITIF
            data_str = json.dumps(data_dict, sort_keys=False, indent=4)
            fichier = open(CHEMIN_COMBAT_JSON,'wt')
            fichier.write(data_str)
            fichier.close()

    def drain():
        data = get_data(CHEMIN_ODS)
        DRAIN_SUBI = data['Combat'][15][4]
        DEFENSE_INVESTI = data['Combat'][16][4]
        with open(CHEMIN_COMBAT_JSON,'r') as json_data:
            data_dict = json.load(json_data)
            DRAIN = data_dict["phase_defensive"]["drain"]
            POSITIF = data_dict["phase_defensive"]["positif"]
            EP = data_dict["attributs"]["EP_fin"]
            ES = data_dict["attributs"]["ES_fin"]
            SUBI = int(DRAIN_SUBI) - int(DEFENSE_INVESTI)
            if SUBI < 0:
                SUBI = 0
            DRAIN = int(DRAIN) + int(SUBI)
            EP_SUBI = int(SUBI) / 2
            ES_SUBI = int(SUBI) / 2
            SOMME_EP = int(EP) + int(EP_SUBI)
            SOMME_ES = int(ES) + int(ES_SUBI)
            POSITIF = int(POSITIF) - int(DEFENSE_INVESTI)
            if POSITIF < 0:
                POSITIF = 0
            data_dict["phase_defensive"]["drain"] = DRAIN
            data_dict["phase_defensive"]["positif"] = POSITIF
            data_dict["attributs"]["EP_fin"] = SOMME_EP
            data_dict["attributs"]["ES_fin"] = SOMME_ES
            data_str = json.dumps(data_dict, sort_keys=False, indent=4)
            fichier = open(CHEMIN_COMBAT_JSON,'wt')
            fichier.write(data_str)
            fichier.close()

    def guerison():
        data = get_data(CHEMIN_ODS)
        GUERISON_BONUS = data['Combat'][20][4]
        with open(CHEMIN_COMBAT_JSON,'r') as json_data:
            data_dict = json.load(json_data)
            POSITIF = data_dict["phase_defensive"]["positif"]
            POSITIF = int(POSITIF) + int(GUERISON_BONUS)
            data_dict["phase_defensive"]["positif"] = POSITIF
            data_dict["phase_defensive"]["guerison"] = GUERISON_BONUS
            data_str = json.dumps(data_dict, sort_keys=False, indent=4)
            fichier = open(CHEMIN_COMBAT_JSON,'wt')
            fichier.write(data_str)
            fichier.close()

    def don_reiryoku():
        data = get_data(CHEMIN_ODS)
        REIRYOKU_BONUS = data['Combat'][20][5]
        with open(CHEMIN_COMBAT_JSON,'r') as json_data:
            data_dict = json.load(json_data)
            EP = data_dict["attributs"]["EP_fin"]
            ES = data_dict["attributs"]["ES_fin"]
            EP_BONUS = int(REIRYOKU_BONUS) / 2
            ES_BONUS = int(REIRYOKU_BONUS) / 2
            SOMME_EP = int(EP) + int(EP_BONUS)
            SOMME_ES = int(ES) + int(ES_BONUS)
            data_dict["attributs"]["EP_fin"] = SOMME_EP
            data_dict["attributs"]["ES_fin"] = SOMME_ES
            data_str = json.dumps(data_dict, sort_keys=False, indent=4)
            fichier = open(CHEMIN_COMBAT_JSON,'wt')
            fichier.write(data_str)
            fichier.close()

    def technique_none():
        with open(CHEMIN_COMBAT_JSON,'r') as json_data:
            data_dict = json.load(json_data)
            PA_DEBUT = data_dict["attributs"]["PA_debut"]
            PA_DEPENSES = data_dict["attributs"]["PA_depenses"]
            PA_RESTANTS = data_dict["attributs"]["PA_restants"]
            PA_RESTANTS = int(PA_DEBUT) - int(PA_RESTANTS)
            data_dict["attributs"]["PA_restants"] = PA_RESTANTS
            data_str = json.dumps(data_dict, sort_keys=False, indent=4)
            fichier = open(CHEMIN_COMBAT_JSON,'wt')
            fichier.write(data_str)
            fichier.close()

    def print_for_reca(NIV_TECH,NOM_TECH,BRANCHE_PRINCIPALE_TECH,BRANCHE_SECONDAIRE_TECH,TYPE,
    EFFET,DEPENSE_EP,DEPENSE_ES,DEPENSE_PV,DESCRIPTION,COUT_PA):
        print('[*][b][Niveau '+str(NIV_TECH)+'] '+str(NOM_TECH)+'[/b]')
        if BRANCHE_SECONDAIRE_TECH != 0:
            print('['+str(BRANCHE_PRINCIPALE_TECH)+'] ['+str(BRANCHE_SECONDAIRE_TECH)+'] ['+str(TYPE)+']')
        if BRANCHE_SECONDAIRE_TECH == 0:
            print('['+str(BRANCHE_PRINCIPALE_TECH)+'] ['+str(TYPE)+']')
        print('[u]Effets :[/u] '+str(EFFET))
        if DEPENSE_PV == 0:
            print('[u]Dépense :[/u] '+str(DEPENSE_EP)+' EP & ' +str(DEPENSE_ES)+' ES ' +str(COUT_PA) + ' PA')
        if DEPENSE_PV != 0:
            print('[u]Dépense :[/u] '+str(DEPENSE_EP)+' EP & ' +str(DEPENSE_ES)+' ES & '+ str(DEPENSE_PV) + ' PV ' +str(COUT_PA) + ' PA')
        print('[spoiler="Descriptif RP"]'+str(DESCRIPTION)+'[/spoiler]')
        print('\n')

    def save_depense_effet(EFFET,DEPENSE_EP,DEPENSE_ES,DEPENSE_PV,COUT_PA,CODE_TYPE_EFFET):
        with open(CHEMIN_COMBAT_JSON,'r') as json_data:
            data_dict = json.load(json_data)
            POSITIF = data_dict["phase_defensive"]["positif"]
            NEGATIF = data_dict["phase_defensive"]["negatif"]
            TOTAL_DEFENDU = data_dict["synthese"]["total_defendu"]
            TOTAL_SUBI = data_dict["synthese"]["total_subi"]
            PA_DEBUT = data_dict["attributs"]["PA_debut"]
            PA_DEPENSES = data_dict["attributs"]["PA_depenses"]
            EP = data_dict["phase_defensive"]["EP_depenses"]
            ES = data_dict["phase_defensive"]["ES_depenses"]
            CODE_TYPE_EFFET = data['Liste_techniques'][POSITION][14]
            POSITIF = int(POSITIF) + int(EFFET)
            TOTAL_DEFENDU = int(POSITIF)
            if int(TOTAL_DEFENDU) < 0 :
                TOTAL_DEFENDU = 0
            if NEGATIF <  POSITIF:
                TOTAL_SUBI = 0
            if NEGATIF >  POSITIF:
                TOTAL_SUBI = int(POSITIF) - int(NEGATIF)
            TOTAL_SUBI = abs(TOTAL_SUBI)
            PA_DEPENSES = int(PA_DEPENSES) + int(COUT_PA)
            EP_DEPENSES = int(EP) + int(DEPENSE_EP)
            ES_DEPENSES = int(ES) + int(DEPENSE_ES)
            COMBO_EP = calcul_combo_EP(DEPENSE_EP)
            COMBO_ES = calcul_combo_ES(DEPENSE_ES)
            data_dict["combo"]["combo_EP_fin"] = COMBO_EP
            data_dict["combo"]["combo_ES_fin"] = COMBO_ES
            data_dict["phase_defensive"]["positif"] = POSITIF
            data_dict["phase_defensive"]["negatif"] = NEGATIF
            data_dict["phase_defensive"]["sacrifice"] = DEPENSE_PV
            data_dict["synthese"]["total_defendu"] = TOTAL_DEFENDU
            data_dict["synthese"]["total_subi"] = TOTAL_SUBI
            data_dict["attributs"]["PA_depenses"] = PA_DEPENSES
            data_dict["phase_defensive"]["EP_depenses"] = EP_DEPENSES
            data_dict["phase_defensive"]["ES_depenses"] = ES_DEPENSES
            data_str = json.dumps(data_dict, sort_keys=False, indent=4)
            fichier = open(CHEMIN_COMBAT_JSON,'wt')
            fichier.write(data_str)
            fichier.close()
    def full_encaisse():
        with open(CHEMIN_COMBAT_JSON,'r') as json_data:
            data_dict = json.load(json_data)
            NEGATIF = data_dict["phase_defensive"]["negatif"]
            TOTAL_SUBI = data_dict["synthese"]["total_subi"]
            TOTAL_SUBI = int(TOTAL_SUBI) + int(NEGATIF)
            data_dict["synthese"]["total_subi"] = TOTAL_SUBI
            data_str = json.dumps(data_dict, sort_keys=False, indent=4)
            fichier = open(CHEMIN_COMBAT_JSON,'wt')
            fichier.write(data_str)
            fichier.close()

    def integrate_value(NIV_TECH,POSITION):
        NOM_TECH = data['Liste_techniques'][POSITION][1]
        BRANCHE_PRINCIPALE_TECH = data['Liste_techniques'][POSITION][2]
        BRANCHE_SECONDAIRE_TECH = data['Liste_techniques'][POSITION][3]
        TYPE = data['Liste_techniques'][POSITION][4]
        EFFET = data['Liste_techniques'][POSITION][5]
        DEPENSE_EP = data['Liste_techniques'][POSITION][6]
        DEPENSE_ES = data['Liste_techniques'][POSITION][7]
        DEPENSE_PV = data['Liste_techniques'][POSITION][8]
        DESCRIPTION = data['Liste_techniques'][POSITION][9]
        COUT_PA = data['Liste_techniques'][POSITION][12]
        CODE_TYPE_EFFET = data['Liste_techniques'][POSITION][14]
        print_for_reca(NIV_TECH,NOM_TECH,BRANCHE_PRINCIPALE_TECH,BRANCHE_SECONDAIRE_TECH,TYPE,
EFFET,DEPENSE_EP,DEPENSE_ES,DEPENSE_PV,DESCRIPTION,COUT_PA)
        save_depense_effet(EFFET,DEPENSE_EP,DEPENSE_ES,DEPENSE_PV,COUT_PA,CODE_TYPE_EFFET)
        optionnel_multicibles(EFFET,CODE_TYPE_EFFET,DEPENSE_EP,DEPENSE_ES)

    data = get_data(CHEMIN_ODS)
    NOMBRE_TECH = data['Combat'][0][1]
    IMMOBILISATION = data['Combat'][14][4]
    ENTRAVE = data['Combat'][14][5]
    DRAIN = data['Combat'][14][6]
    GUERISON = data['Combat'][19][4]
    DON_REIRYOKU = data['Combat'][19][5]
    a = 2
    b = 0
    if NOMBRE_TECH == 0:
        full_encaisse()
        technique_none()
    for i in range(int(NOMBRE_TECH)):
        NIV_TECH = data['Combat'][a][0]
        ID_TECH = data['Combat'][a][1]
        if NIV_TECH == 1:
            c = b + 0
            POSITION = int(c) + int(ID_TECH)
            integrate_value(NIV_TECH,POSITION)
        elif NIV_TECH == 2:
            c = b + 9
            POSITION = int(c) + int(ID_TECH)
            integrate_value(NIV_TECH,POSITION)
        elif NIV_TECH == 3:
            c = b + 19
            POSITION = int(c) + int(ID_TECH)
            integrate_value(NIV_TECH,POSITION)
        elif NIV_TECH == 4:
            c = b + 29
            POSITION = int(c) + int(ID_TECH)
            integrate_value(NIV_TECH,POSITION)
        elif NIV_TECH == 5:
            c = b + 39
            POSITION = int(c) + int(ID_TECH)
            integrate_value(NIV_TECH,POSITION)
        a += 1
    if IMMOBILISATION == 1:
        immobilisation()
    if ENTRAVE == 1:
        entrave()
    if DRAIN == 1:
        drain()
    if GUERISON == 1:
        guerison()
    if DON_REIRYOKU == 1:
        don_reiryoku()

def effet_off(EFFET,CODE_TYPE_EFFET):
    if CODE_TYPE_EFFET == 'att' or CODE_TYPE_EFFET == 'boostof':
        with open(CHEMIN_COMBAT_JSON,'r') as json_data:
            data_dict = json.load(json_data)
            NEGATIF = data_dict["phase_offensive"]["negatif"]
            NEGATIF = int(NEGATIF) + int(EFFET)
            data_dict["phase_offensive"]["negatif"] = NEGATIF
            data_str = json.dumps(data_dict, sort_keys=False, indent=4)
            fichier = open(CHEMIN_COMBAT_JSON,'wt')
            fichier.write(data_str)
            fichier.close()

def effet_regen(EFFET,CODE_TYPE_EFFET):
    if CODE_TYPE_EFFET == 'regen':
        with open(CHEMIN_COMBAT_JSON,'r') as json_data:
            data_dict = json.load(json_data)
            POSITIF = data_dict["phase_offensive"]["positif"]
            POSITIF = int(POSITIF) + int(EFFET)
            data_dict["phase_offensive"]["positif"] = POSITIF
            data_str = json.dumps(data_dict, sort_keys=False, indent=4)
            fichier = open(CHEMIN_COMBAT_JSON,'wt')
            fichier.write(data_str)
            fichier.close()

def effet_guerison(EFFET,CODE_TYPE_EFFET):
    if CODE_TYPE_EFFET == 'gueris':
        with open(CHEMIN_COMBAT_JSON,'r') as json_data:
            data_dict = json.load(json_data)
            GUERISON = data_dict["phase_offensive"]["guerison"]
            GUERISON = int(GUERISON) + int(EFFET)
            data_dict["phase_offensive"]["guerison"] = GUERISON
            data_str = json.dumps(data_dict, sort_keys=False, indent=4)
            fichier = open(CHEMIN_COMBAT_JSON,'wt')
            fichier.write(data_str)
            fichier.close()

def effet_entrave(EFFET,CODE_TYPE_EFFET):
    if CODE_TYPE_EFFET == 'ent':
        with open(CHEMIN_COMBAT_JSON,'r') as json_data:
            data_dict = json.load(json_data)
            ENTRAVE = data_dict["phase_offensive"]["entrave"]
            ENTRAVE = int(ENTRAVE) + int(EFFET)
            data_dict["phase_offensive"]["entrave"] = ENTRAVE
            data_str = json.dumps(data_dict, sort_keys=False, indent=4)
            fichier = open(CHEMIN_COMBAT_JSON,'wt')
            fichier.write(data_str)
            fichier.close()

def effet_immo(EFFET,CODE_TYPE_EFFET):
    if CODE_TYPE_EFFET == 'imm':
        with open(CHEMIN_COMBAT_JSON,'r') as json_data:
            data_dict = json.load(json_data)
            IMMOBILISATION = data_dict["phase_offensive"]["immobilisation"]
            IMMOBILISATION = int(IMMOBILISATION) + int(EFFET)
            data_dict["phase_offensive"]["immobilisation"] = IMMOBILISATION
            data_str = json.dumps(data_dict, sort_keys=False, indent=4)
            fichier = open(CHEMIN_COMBAT_JSON,'wt')
            fichier.write(data_str)
            fichier.close()

def drain(EFFET,CODE_TYPE_EFFET):
    if CODE_TYPE_EFFET == 'drain':
        with open(CHEMIN_COMBAT_JSON,'r') as json_data:
            data_dict = json.load(json_data)
            DRAIN = data_dict["phase_offensive"]["drain"]
            DRAIN = int(DRAIN) + int(EFFET)
            data_dict["phase_offensive"]["drain"] = DRAIN
            data_str = json.dumps(data_dict, sort_keys=False, indent=4)
            fichier = open(CHEMIN_COMBAT_JSON,'wt')
            fichier.write(data_str)
            fichier.close()

def don_rei(EFFET,CODE_TYPE_EFFET):
    if CODE_TYPE_EFFET == 'donrei':
        with open(CHEMIN_COMBAT_JSON,'r') as json_data:
            data_dict = json.load(json_data)
            DON_REIRYOKU = data_dict["phase_offensive"]["don_rei"]
            DON_REIRYOKU = int(DON_REIRYOKU) + int(EFFET)
            data_dict["phase_offensive"]["don_rei"] = DON_REIRYOKU
            data_str = json.dumps(data_dict, sort_keys=False, indent=4)
            fichier = open(CHEMIN_COMBAT_JSON,'wt')
            fichier.write(data_str)
            fichier.close()

def techniques_offensives():
    def entrave():
        with open(CHEMIN_COMBAT_JSON,'r') as json_data:
            data_dict = json.load(json_data)
            ENTRAVE = data_dict["phase_offensive"]["entrave_subi"]
            NEGATIF = data_dict["phase_offensive"]["negatif"]
            NEGATIF = int(NEGATIF) - int(ENTRAVE)
            if NEGATIF < 0:
                NEGATIF = 0
            data_dict["phase_offensive"]["negatif"] = NEGATIF
            data_str = json.dumps(data_dict, sort_keys=False, indent=4)
            fichier = open(CHEMIN_COMBAT_JSON,'wt')
            fichier.write(data_str)
            fichier.close()

    def technique_deferlement_reiryoku():
        with open(CHEMIN_COMBAT_JSON,'r') as json_data:
            data_dict = json.load(json_data)
            DEFERLEMENT = data_dict["phase_offensive"]["deferlement_reiryoku"]
            data = get_data(CHEMIN_ODS)
            DEPENSE_EP = data['Combat'][10][8]
            DEPENSE_ES = data['Combat'][10][9]
            DEPENSE_EP_INITIAL = data_dict["phase_offensive"]["EP_depenses"]
            DEPENSE_ES_INITIAL = data_dict["phase_offensive"]["ES_depenses"]
            DEFERLEMENT_SEUIL = (int(DEPENSE_EP) + int(DEPENSE_ES))
            if DEFERLEMENT_SEUIL <= 100:
                DEFERLEMENT_DOMMAGES = DEFERLEMENT_SEUIL * 2
                DEPENSE_EP_FINAL = int(DEPENSE_EP_INITIAL) + int(DEPENSE_EP)
                DEPENSE_ES_FINAL = int(DEPENSE_ES) + int(DEPENSE_ES_INITIAL)
                print('[*][b][Déferlement Reiryoku][/b]')
                print('[u]Effets :[/u] '+str(DEFERLEMENT_DOMMAGES) +' dommages')
                print('[u]Dépense :[/u] '+str(DEPENSE_EP_FINAL)+' EP & '+str(DEPENSE_ES_INITIAL)+' ES soit '+str(DEFERLEMENT_SEUIL) +' reiryokus dépensés')
                print('\n')
            if DEFERLEMENT_SEUIL > 100 and DEFERLEMENT_SEUIL <= 200:
                DEFERLEMENT_DOMMAGES = DEFERLEMENT_SEUIL * 2
                DEPENSE_EP_FINAL = int(DEPENSE_EP_INITIAL) + int(DEPENSE_EP)
                DEPENSE_ES_FINAL = int(DEPENSE_ES) + int(DEPENSE_ES_INITIAL)
                print('[*][b][Déferlement Reiryoku][/b]')
                print('[u]Effets :[/u] '+str(DEFERLEMENT_DOMMAGES) +' dommages')
                print('[u]Dépense :[/u] '+str(DEPENSE_EP_FINAL)+' EP & '+str(DEPENSE_ES_FINAL)+' ES soit '+str(DEFERLEMENT_SEUIL)+ ' reiryokus dépensés (nécessite activation de la spécialité Revanchard)')
                print('\n')
            if DEFERLEMENT_SEUIL > 200:
                print('[SEUIL REIRYOKU MAXIMUM DEPASSE POUR LE DEFERLEMENT REIRYOKU ('+str(DEFERLEMENT_SEUIL)+')]')
                print('\n')
                DEPENSE_EP_FINAL = int(DEPENSE_EP_INITIAL)
                DEPENSE_ES_FINAL = int(DEPENSE_ES_INITIAL)
                DEFERLEMENT_DOMMAGES = 0
            COMBO_EP = calcul_combo_EP(DEPENSE_EP_FINAL)
            COMBO_ES = calcul_combo_ES(DEPENSE_ES_FINAL)
            data_dict["combo"]["combo_EP_fin"] = COMBO_EP
            data_dict["combo"]["combo_ES_fin"] = COMBO_ES
            data_dict["phase_offensive"]["EP_depenses"] = DEPENSE_EP_FINAL
            data_dict["phase_offensive"]["ES_depenses"] = DEPENSE_ES_FINAL
            data_dict["phase_offensive"]["deferlement_reiryoku"] = DEFERLEMENT_DOMMAGES
            data_str = json.dumps(data_dict, sort_keys=False, indent=4)
            fichier = open(CHEMIN_COMBAT_JSON,'wt')
            fichier.write(data_str)
            fichier.close()

    def technique_none():
        with open(CHEMIN_COMBAT_JSON,'r') as json_data:
            data_dict = json.load(json_data)
            PA_DEBUT = data_dict["attributs"]["PA_debut"]
            PA_DEPENSES = data_dict["attributs"]["PA_depenses"]
            PA_RESTANTS = data_dict["attributs"]["PA_restants"]
            if PA_RESTANTS != 0:
                pass
            if PA_RESTANTS == 0:
                PA_RESTANTS = int(PA_DEBUT) - int(PA_RESTANTS)
            data_dict["attributs"]["PA_restants"] = PA_RESTANTS
            data_str = json.dumps(data_dict, sort_keys=False, indent=4)
            fichier = open(CHEMIN_COMBAT_JSON,'wt')
            fichier.write(data_str)
            fichier.close()

    def print_for_reca(NIV_TECH,NOM_TECH,BRANCHE_PRINCIPALE_TECH,BRANCHE_SECONDAIRE_TECH,TYPE,
    EFFET,DEPENSE_EP,DEPENSE_ES,DEPENSE_PV,DESCRIPTION,COUT_PA):
        print('[*][b][Niveau '+str(NIV_TECH)+'] '+str(NOM_TECH)+'[/b]')
        if BRANCHE_SECONDAIRE_TECH != 0:
            print('['+str(BRANCHE_PRINCIPALE_TECH)+'] ['+str(BRANCHE_SECONDAIRE_TECH)+'] ['+str(TYPE)+']')
        if BRANCHE_SECONDAIRE_TECH == 0:
            print('['+str(BRANCHE_PRINCIPALE_TECH)+'] ['+str(TYPE)+']')
        print('[u]Effets :[/u] '+str(EFFET))
        if DEPENSE_PV == 0:
            print('[u]Dépense :[/u] '+str(DEPENSE_EP)+' EP & ' +str(DEPENSE_ES)+' ES ' +str(COUT_PA) + ' PA')
        if DEPENSE_PV != 0:
            print('[u]Dépense :[/u] '+str(DEPENSE_EP)+' EP & ' +str(DEPENSE_ES)+' ES & '+ str(DEPENSE_PV) + ' PV ' +str(COUT_PA) + ' PA')
        print('[spoiler="Descriptif RP"]'+str(DESCRIPTION)+'[/spoiler]')
        print('\n')

    def save_depense_effet(EFFET,DEPENSE_EP,DEPENSE_ES,DEPENSE_PV,COUT_PA,BONUS,CODE_TYPE_EFFET):
        with open(CHEMIN_COMBAT_JSON,'r') as json_data:
            data_dict = json.load(json_data)
            POSITIF = data_dict["phase_offensive"]["positif"]
            NEGATIF = data_dict["phase_offensive"]["negatif"]
            PA_DEBUT = data_dict["attributs"]["PA_debut"]
            PA_DEPENSES = data_dict["attributs"]["PA_depenses"]
            PA_RESTANTS = data_dict["attributs"]["PA_restants"]
            EP = data_dict["phase_offensive"]["EP_depenses"]
            ES = data_dict["phase_offensive"]["ES_depenses"]
            PA_DEPENSES = int(PA_DEPENSES) + int(COUT_PA)
            EP_DEPENSES = int(EP) + int(DEPENSE_EP)
            ES_DEPENSES = int(ES) + int(DEPENSE_ES)
            COMBO_EP = calcul_combo_EP(DEPENSE_EP)
            COMBO_ES = calcul_combo_ES(DEPENSE_ES)
            data_dict["combo"]["combo_EP_fin"] = COMBO_EP
            data_dict["combo"]["combo_ES_fin"] = COMBO_ES
            data_dict["phase_offensive"]["sacrifice"] = DEPENSE_PV
            data_dict["attributs"]["PA_depenses"] = PA_DEPENSES
            data_dict["phase_offensive"]["EP_depenses"] = EP_DEPENSES
            data_dict["phase_offensive"]["ES_depenses"] = ES_DEPENSES
            data_str = json.dumps(data_dict, sort_keys=False, indent=4)
            fichier = open(CHEMIN_COMBAT_JSON,'wt')
            fichier.write(data_str)
            fichier.close()

    def integrate_value(NIV_TECH,POSITION):
        NOM_TECH = data['Liste_techniques'][POSITION][1]
        BRANCHE_PRINCIPALE_TECH = data['Liste_techniques'][POSITION][2]
        BRANCHE_SECONDAIRE_TECH = data['Liste_techniques'][POSITION][3]
        TYPE = data['Liste_techniques'][POSITION][4]
        EFFET = data['Liste_techniques'][POSITION][5]
        DEPENSE_EP = data['Liste_techniques'][POSITION][6]
        DEPENSE_ES = data['Liste_techniques'][POSITION][7]
        DEPENSE_PV = data['Liste_techniques'][POSITION][8]
        DESCRIPTION = data['Liste_techniques'][POSITION][9]
        BONUS = data['Liste_techniques'][POSITION][10]
        COUT_PA = data['Liste_techniques'][POSITION][12]
        CODE_TYPE_EFFET = data['Liste_techniques'][POSITION][14]
        print_for_reca(NIV_TECH,NOM_TECH,BRANCHE_PRINCIPALE_TECH,BRANCHE_SECONDAIRE_TECH,TYPE,
    EFFET,DEPENSE_EP,DEPENSE_ES,DEPENSE_PV,DESCRIPTION,COUT_PA)
        save_depense_effet(EFFET,DEPENSE_EP,DEPENSE_ES,DEPENSE_PV,COUT_PA,BONUS,CODE_TYPE_EFFET)
        effet_off(EFFET,CODE_TYPE_EFFET)
        effet_regen(EFFET,CODE_TYPE_EFFET)
        effet_guerison(EFFET,CODE_TYPE_EFFET)
        effet_entrave(EFFET,CODE_TYPE_EFFET)
        effet_immo(EFFET,CODE_TYPE_EFFET)
        drain(EFFET,CODE_TYPE_EFFET)
        don_rei(EFFET,CODE_TYPE_EFFET)
        optionnel_multicibles(EFFET,CODE_TYPE_EFFET,DEPENSE_EP,DEPENSE_ES)


    with open(CHEMIN_COMBAT_JSON,'r') as json_data:
        data_dict = json.load(json_data)
        ENTRAVE = data_dict["phase_offensive"]["entrave_subi"]
        data = get_data(CHEMIN_ODS)
        NOMBRE_TECH = data['Combat'][0][8]
        DEFERLEMENT_REIRYOKU = data['Combat'][10][7]
        a = 2
        b = 0
        if ENTRAVE > 0:
            entrave()

        if DEFERLEMENT_REIRYOKU == 1:
            technique_deferlement_reiryoku()

        if NOMBRE_TECH == 0:
            technique_none()

        for i in range(int(NOMBRE_TECH)):
            NIV_TECH = data['Combat'][a][7]
            ID_TECH = data['Combat'][a][8]
            if NIV_TECH == 1:
                c = b + 0
                POSITION = int(c) + int(ID_TECH)
                integrate_value(NIV_TECH,POSITION)
            elif NIV_TECH == 2:
                c = b + 9
                POSITION = int(c) + int(ID_TECH)
                integrate_value(NIV_TECH,POSITION)
            elif NIV_TECH == 3:
                c = b + 19
                POSITION = int(c) + int(ID_TECH)
                integrate_value(NIV_TECH,POSITION)
            elif NIV_TECH == 4:
                c = b + 29
                POSITION = int(c) + int(ID_TECH)
                integrate_value(NIV_TECH,POSITION)
            elif NIV_TECH == 5:
                c = b + 39
                POSITION = int(c) + int(ID_TECH)
                integrate_value(NIV_TECH,POSITION)
            a += 1

def first_liberation():
    data = get_data(CHEMIN_ODS)
    ETAT = data['Combat'][26][1]
    if ETAT == 0:
        pass
    elif ETAT == 1:
        print('[*][b]Activation libération niveau 1[/b]')
        COUT_PA = data['Sysco'][11][8]
        print('[u]Dépense :[/u] '+str(COUT_PA)+' PA')
        with open(CHEMIN_COMBAT_JSON,'r') as json_data:
            data_dict = json.load(json_data)
            PA_DEPENSES = data_dict["attributs"]["PA_depenses"]
            PA_DEPENSES = int(PA_DEPENSES) + int(COUT_PA)
            data_dict["attributs"]["PA_depenses"] = PA_DEPENSES
            data_str = json.dumps(data_dict, sort_keys=False, indent=4)
            fichier = open(CHEMIN_COMBAT_JSON,'wt')
            fichier.write(data_str)
            fichier.close()
    elif ETAT == 2:
        pass

def check_maintien():
    data = get_data(CHEMIN_ODS)
    ETAT_SECOND_LIBERATION = data['Combat'][27][1]
    VALUE_SECOND_LIBERATION = data['Liste_techniques'][20][5]
    TYPE_SECOND_LIBERATION = data['Liste_techniques'][20][4]
    TEXT_MAINTENU = '[*][b]Maintenu :[/b] '
    if ETAT_SECOND_LIBERATION == 2:
        TEXT_MAINTENU = TEXT_MAINTENU + str(VALUE_SECOND_LIBERATION) + ' liberation niveau 2 (' + TYPE_SECOND_LIBERATION +')'
    else:
        TEXT_MAINTENU = TEXT_MAINTENU + '0'
    print(TEXT_MAINTENU)

def second_liberation(mode):
    data = get_data(CHEMIN_ODS)
    ETAT = data['Combat'][27][1]
    COUT_PA = data['Sysco'][11][10]
    COUT_EP = data['Sysco'][16][10]
    COUT_ES = data['Sysco'][17][10]
    TYPE_SECOND_LIBERATION = data['Liste_techniques'][20][4]
    EFFET = data['Liste_techniques'][20][5]
    CODE_TYPE_EFFET = data['Liste_techniques'][20][14]
    if ETAT == 0:
        pass
    elif ETAT == 1:
        if mode == 'defensif':
            if CODE_TYPE_EFFET == 'def' or CODE_TYPE_EFFET == 'boost_def':
                print('[*][b]Activation libération niveau 2[/b]')
                print('[u]Effets :[/u] '+str(EFFET) + ' (' + str(TYPE_SECOND_LIBERATION) + ')')
                print('[u]Dépense :[/u] '+str(COUT_PA)+' PA & '+str(COUT_EP)+' EP & '+str(COUT_ES)+' ES')
                print('\n')
                with open(CHEMIN_COMBAT_JSON,'r') as json_data:
                    data_dict = json.load(json_data)
                    PA_DEPENSES = data_dict["attributs"]["PA_depenses"]
                    EP_DEPENSES = data_dict["phase_defensive"]["EP_depenses"]
                    ES_DEPENSES = data_dict["phase_defensive"]["ES_depenses"]
                    PA_DEPENSES = int(PA_DEPENSES) + int(COUT_PA)
                    EP_DEPENSES = int(EP_DEPENSES) + int(COUT_EP)
                    ES_DEPENSES = int(ES_DEPENSES) + int(COUT_ES)
                    COMBO_EP = calcul_combo_EP(EP_DEPENSES)
                    COMBO_ES = calcul_combo_ES(ES_DEPENSES)
                    data_dict["combo"]["combo_EP_fin"] = COMBO_EP
                    data_dict["combo"]["combo_ES_fin"] = COMBO_ES
                    data_dict["combo"]["combo_EP_fin"] = COMBO_EP
                    data_dict["combo"]["combo_ES_fin"] = COMBO_ES
                    data_dict["attributs"]["PA_depenses"] = PA_DEPENSES
                    data_dict["phase_defensive"]["EP_depenses"] = EP_DEPENSES
                    data_dict["phase_defensive"]["ES_depenses"] = ES_DEPENSES
                    data_str = json.dumps(data_dict, sort_keys=False, indent=4)
                    fichier = open(CHEMIN_COMBAT_JSON,'wt')
                    fichier.write(data_str)
                    fichier.close()
                effet_off(EFFET,CODE_TYPE_EFFET)
                effet_regen(EFFET,CODE_TYPE_EFFET)
                effet_guerison(EFFET,CODE_TYPE_EFFET)
                effet_entrave(EFFET,CODE_TYPE_EFFET)
                effet_immo(EFFET,CODE_TYPE_EFFET)
                drain(EFFET,CODE_TYPE_EFFET)
                don_rei(EFFET,CODE_TYPE_EFFET)
                optionnel_multicibles(EFFET,CODE_TYPE_EFFET,EP_DEPENSES,ES_DEPENSES)

        if mode == 'offensif':
            if CODE_TYPE_EFFET != 'def' or CODE_TYPE_EFFET != 'boost_def':
                print('[*][b]Activation libération niveau 2[/b]')
                print('[u]Effets :[/u] '+str(EFFET) + ' (' + str(TYPE_SECOND_LIBERATION) + ')')
                print('[u]Dépense :[/u] '+str(COUT_PA)+' PA & '+str(COUT_EP)+' EP & '+str(COUT_ES)+' ES')
                print('\n')
                with open(CHEMIN_COMBAT_JSON,'r') as json_data:
                    data_dict = json.load(json_data)
                    PA_DEPENSES = data_dict["attributs"]["PA_depenses"]
                    EP_DEPENSES = data_dict["phase_offensive"]["EP_depenses"]
                    ES_DEPENSES = data_dict["phase_offensive"]["ES_depenses"]
                    PA_DEPENSES = int(PA_DEPENSES) + int(COUT_PA)
                    EP_DEPENSES = int(EP_DEPENSES) + int(COUT_EP)
                    ES_DEPENSES = int(ES_DEPENSES) + int(COUT_ES)
                    COMBO_EP = calcul_combo_EP(EP_DEPENSES)
                    COMBO_ES = calcul_combo_ES(ES_DEPENSES)
                    data_dict["combo"]["combo_EP_fin"] = COMBO_EP
                    data_dict["combo"]["combo_ES_fin"] = COMBO_ES
                    data_dict["attributs"]["PA_depenses"] = PA_DEPENSES
                    data_dict["phase_offensive"]["EP_depenses"] = EP_DEPENSES
                    data_dict["phase_offensive"]["ES_depenses"] = ES_DEPENSES
                    data_str = json.dumps(data_dict, sort_keys=False, indent=4)
                    fichier = open(CHEMIN_COMBAT_JSON,'wt')
                    fichier.write(data_str)
                    fichier.close()
                effet_off(EFFET,CODE_TYPE_EFFET)
                effet_regen(EFFET,CODE_TYPE_EFFET)
                effet_guerison(EFFET,CODE_TYPE_EFFET)
                effet_entrave(EFFET,CODE_TYPE_EFFET)
                effet_immo(EFFET,CODE_TYPE_EFFET)
                drain(EFFET,CODE_TYPE_EFFET)
                don_rei(EFFET,CODE_TYPE_EFFET)
                optionnel_multicibles(EFFET,CODE_TYPE_EFFET,EP_DEPENSES,ES_DEPENSES)
    elif ETAT == 2:
        if mode == 'defensif':
            if CODE_TYPE_EFFET == 'def' or CODE_TYPE_EFFET == 'boost_def':
                print('[*][b]Libération niveau 2 maintenue[/b]')
                print('[u]Effets :[/u] '+str(EFFET) + ' (' + str(TYPE_SECOND_LIBERATION) + ')')
                print('[u]Dépense :[/u] '+str(COUT_EP)+' EP & '+str(COUT_ES)+' ES')
                print('\n')
                with open(CHEMIN_COMBAT_JSON,'r') as json_data:
                    data_dict = json.load(json_data)
                    EP_DEPENSES = data_dict["phase_defensive"]["EP_depenses"]
                    ES_DEPENSES = data_dict["phase_defensive"]["ES_depenses"]
                    EP_DEPENSES = int(EP_DEPENSES) + int(COUT_EP)
                    ES_DEPENSES = int(ES_DEPENSES) + int(COUT_ES)
                    data_dict["phase_defensive"]["EP_depenses"] = EP_DEPENSES
                    data_dict["phase_defensive"]["ES_depenses"] = ES_DEPENSES
                    data_str = json.dumps(data_dict, sort_keys=False, indent=4)
                    fichier = open(CHEMIN_COMBAT_JSON,'wt')
                    fichier.write(data_str)
                    fichier.close()
                effet_off(EFFET,CODE_TYPE_EFFET)
                effet_regen(EFFET,CODE_TYPE_EFFET)
                effet_guerison(EFFET,CODE_TYPE_EFFET)
                effet_entrave(EFFET,CODE_TYPE_EFFET)
                effet_immo(EFFET,CODE_TYPE_EFFET)
                drain(EFFET,CODE_TYPE_EFFET)
                don_rei(EFFET,CODE_TYPE_EFFET)
                optionnel_multicibles(EFFET,CODE_TYPE_EFFET,EP_DEPENSES,ES_DEPENSES)

        if mode == 'offensif':
            if CODE_TYPE_EFFET != 'def' or CODE_TYPE_EFFET != 'boost_def':
                print('[*][b]Libération niveau 2 maintenue[/b]')
                print('[u]Effets :[/u] '+str(EFFET) + ' (' + str(TYPE_SECOND_LIBERATION) + ')')
                print('[u]Dépense :[/u] '+str(COUT_EP)+' EP & '+str(COUT_ES)+' ES')
                print('\n')
                with open(CHEMIN_COMBAT_JSON,'r') as json_data:
                    data_dict = json.load(json_data)
                    EP_DEPENSES = data_dict["phase_offensive"]["EP_depenses"]
                    ES_DEPENSES = data_dict["phase_offensive"]["ES_depenses"]
                    EP_DEPENSES = int(EP_DEPENSES) + int(COUT_EP)
                    ES_DEPENSES = int(ES_DEPENSES) + int(COUT_ES)
                    data_dict["phase_offensive"]["EP_depenses"] = EP_DEPENSES
                    data_dict["phase_offensive"]["ES_depenses"] = ES_DEPENSES
                    data_str = json.dumps(data_dict, sort_keys=False, indent=4)
                    fichier = open(CHEMIN_COMBAT_JSON,'wt')
                    fichier.write(data_str)
                    fichier.close()
                effet_off(EFFET,CODE_TYPE_EFFET)
                effet_regen(EFFET,CODE_TYPE_EFFET)
                effet_guerison(EFFET,CODE_TYPE_EFFET)
                effet_entrave(EFFET,CODE_TYPE_EFFET)
                effet_immo(EFFET,CODE_TYPE_EFFET)
                drain(EFFET,CODE_TYPE_EFFET)
                don_rei(EFFET,CODE_TYPE_EFFET)
                optionnel_multicibles(EFFET,CODE_TYPE_EFFET,EP_DEPENSES,ES_DEPENSES)

def valeur_negatives_positives_somme():
    with open(CHEMIN_COMBAT_JSON,'r') as json_data:
        data_dict = json.load(json_data)
        NEGATIF = data_dict["phase_offensive"]["negatif"]
        POSITIF = data_dict["phase_offensive"]["positif"]
        GUERISON = data_dict["phase_offensive"]["guerison"]
        GUERISON_BONUS = data_dict["phase_defensive"]["guerison"]
        ENTRAVE = data_dict["phase_offensive"]["entrave"]
        ENTRAVE_SUBI = data_dict["phase_offensive"]["entrave_subi"]
        IMMOBILISATION = data_dict["phase_offensive"]["immobilisation"]
        IMMOBILISATION_SUBI = data_dict["phase_defensive"]["immobilisation"]
        DRAIN = data_dict["phase_offensive"]["drain"]
        DRAIN_SUBI = data_dict["phase_defensive"]["drain"]
        DRAIN_IMPARABLE = data_dict["phase_offensive"]["drain_imparable"]
        DON_REI = data_dict["phase_offensive"]["don_rei"]
        DON_REI_BONUS = data_dict["phase_defensive"]["don_reiryoku"]
        SACRIFICE = data_dict["phase_offensive"]["sacrifice"]
        MULTICIBLES = data_dict["phase_offensive"]["degats_multicibles"]
        ENTRAVE_SUBI = data_dict["phase_offensive"]["entrave_subi"]
        DEFERLEMENT_REIRYOKU = data_dict["phase_offensive"]["deferlement_reiryoku"]
        TEXT_VALEURS_NEGATIVES = '[list][*][b]Valeurs négatives :[/b] '+ str(NEGATIF) + ' dommages '
        TEXT_VALEURS_POSITIVES = '[*][b]Valeurs positives :[/b] '+ str(POSITIF) + ' regen '
        if ENTRAVE != 0:
            TEXT_VALEURS_NEGATIVES = TEXT_VALEURS_NEGATIVES + ' & ' +str(ENTRAVE) + ' entraves '
        if ENTRAVE_SUBI != 0:
            TEXT_VALEURS_NEGATIVES = TEXT_VALEURS_NEGATIVES + ' & ' +str(ENTRAVE_SUBI) + ' entraves '
        if IMMOBILISATION != 0:
            TEXT_VALEURS_NEGATIVES = TEXT_VALEURS_NEGATIVES + ' & ' +str(IMMOBILISATION) + ' immobilisation '
        if IMMOBILISATION_SUBI != 0:
            TEXT_VALEURS_NEGATIVES = TEXT_VALEURS_NEGATIVES + ' & ' +str(IMMOBILISATION_SUBI) + ' immobilisation subie'
        if DRAIN != 0:
            TEXT_VALEURS_NEGATIVES = TEXT_VALEURS_NEGATIVES + ' & ' +str(DRAIN) + ' drain reiryoku '
        if DRAIN_SUBI != 0:
            TEXT_VALEURS_NEGATIVES = TEXT_VALEURS_NEGATIVES + ' & ' +str(DRAIN_SUBI) + ' drain reiryoku subi '
        if GUERISON != 0:
            TEXT_VALEURS_POSITIVES = TEXT_VALEURS_POSITIVES + ' & ' +str(GUERISON) + ' guerison '
        if GUERISON_BONUS != 0:
            TEXT_VALEURS_POSITIVES = TEXT_VALEURS_POSITIVES + ' & ' +str(GUERISON_BONUS) + ' guerison reçu '
        if DON_REI != 0:
            TEXT_VALEURS_POSITIVES = TEXT_VALEURS_POSITIVES + ' & ' +str(DON_REI) + ' don reiryoku '
        if DON_REI_BONUS != 0:
            TEXT_VALEURS_POSITIVES = TEXT_VALEURS_POSITIVES + ' & ' +str(DON_REI_BONUS) + ' reiryoku reçu '
        if SACRIFICE != 0:
            TEXT_VALEURS_NEGATIVES = TEXT_VALEURS_NEGATIVES + ' & ' +str(SACRIFICE) + ' PV sacrifiés '
        if MULTICIBLES != 0:
            TEXT_VALEURS_NEGATIVES = TEXT_VALEURS_NEGATIVES + ' & ' +str(MULTICIBLES) + ' dommages multicibles '
        if DEFERLEMENT_REIRYOKU != 0:
            TEXT_VALEURS_NEGATIVES = TEXT_VALEURS_NEGATIVES + ' & ' +str(DEFERLEMENT_REIRYOKU) + ' dommages déferlement reiryoku '
        if ENTRAVE_SUBI != 0:
            TEXT_VALEURS_NEGATIVES = TEXT_VALEURS_NEGATIVES + ' & ' +str(ENTRAVE_SUBI) + ' entrave subi '
        if DRAIN_IMPARABLE != 0:
            DRAIN_EP_ES = int(DRAIN_IMPARABLE) / 2
            DRAIN_EP_ES = int(DRAIN_EP_ES)
            TEXT_VALEURS_NEGATIVES = TEXT_VALEURS_NEGATIVES + ' & ' +str(DRAIN_IMPARABLE) + ' drain imparable ('+str(DRAIN_EP_ES) + ' EP & ' + str(DRAIN_EP_ES) + ' ES)'
        print(TEXT_VALEURS_NEGATIVES)
        print(TEXT_VALEURS_POSITIVES)
        print('[/list]')

def combo_somme_fin():
    with open(CHEMIN_COMBAT_JSON,'r') as json_data:
        data_dict = json.load(json_data)
        EP_DEBUT = data_dict["combo"]["combo_EP_debut"]
        ES_DEBUT = data_dict["combo"]["combo_ES_debut"]
        EP_FIN = data_dict["combo"]["combo_EP_fin"]
        ES_FIN = data_dict["combo"]["combo_ES_fin"]
        SOMME_EP = int(EP_DEBUT) + int(EP_FIN)
        SOMME_ES = int(ES_DEBUT) + int(ES_FIN)
        print('[b][color=#c83737]Combo EP : '+str(SOMME_EP)+'[/color][/b]')
        print('[b][color=#2a4cbc]Combo ES : '+str(SOMME_ES)+'[/color][/b][/spoiler][/hide]')

def aptitudes(mode):
    def id_aptitude(ID,RANG,mode):
        data = get_data(CHEMIN_ODS)
        NAME = data['Sysco'][21][int(ID)]
        TYPE = data['Sysco'][23][int(ID)]
        VALUE = data['Sysco'][23+int(RANG)][int(ID)]
        if ID == 1 and mode == 'offensif':
            REIRYOKU = int(VALUE) / 2
            with open(CHEMIN_COMBAT_JSON,'r') as json_data:
                data_dict = json.load(json_data)
                EP = data_dict["phase_offensive"]["EP_depenses"]
                ES = data_dict["phase_offensive"]["ES_depenses"]
                EP = int(REIRYOKU) + int(EP)
                ES = int(REIRYOKU) + int(ES)
                if EP < 0:
                    EP = 0
                if ES < 0:
                    ES = 0
                data_dict["phase_offensive"]["EP_depenses"] = EP
                data_dict["phase_offensive"]["ES_depenses"] = ES
                data_str = json.dumps(data_dict, sort_keys=False, indent=4)
                fichier = open(CHEMIN_COMBAT_JSON,'wt')
                fichier.write(data_str)
                fichier.close()
            print('[*][b]Activation aptitude '+str(NAME)+' niveau '+str(RANG)+'[/b]')
            print('[u]Effet :[/u] '+str(VALUE) + ' ('+str(TYPE)+')')
        if ID == 2 and mode == 'defensif':
            REIRYOKU = int(VALUE) / 2
            REIRYOKU = int(REIRYOKU)
            with open(CHEMIN_COMBAT_JSON,'r') as json_data:
                data_dict = json.load(json_data)
                EP = data_dict["phase_defensive"]["EP_depenses"]
                ES = data_dict["phase_defensive"]["ES_depenses"]
                EP = int(REIRYOKU) + int(EP)
                ES = int(REIRYOKU) + int(ES)
                if EP < 0:
                    EP = 0
                if ES < 0:
                    ES = 0
                data_dict["phase_defensive"]["EP_depenses"] = EP
                data_dict["phase_defensive"]["ES_depenses"] = ES
                data_str = json.dumps(data_dict, sort_keys=False, indent=4)
                fichier = open(CHEMIN_COMBAT_JSON,'wt')
                fichier.write(data_str)
                fichier.close()
            print('[*][b]Activation aptitude '+str(NAME)+' niveau '+str(RANG)+'[/b]')
            print('[u]Effet :[/u] '+str(VALUE) + ' ('+str(TYPE)+' => '+str(REIRYOKU)+' EP & '+str(REIRYOKU)+' ES)')
        if (ID == 3 or ID == 4) and mode == 'offensif':
            print('[*][b]Activation aptitude '+str(NAME)+' niveau '+str(RANG)+'[/b]')
            print('[u]Effet :[/u] '+str(VALUE) + ' ('+str(TYPE)+')')
        if ID == 5 and mode == 'offensif':
            with open(CHEMIN_COMBAT_JSON,'r') as json_data:
                data_dict = json.load(json_data)
                NEGATIF = data_dict["phase_offensive"]["negatif"]
                NEGATIF = int(NEGATIF) + int(VALUE)
                data_dict["phase_offensive"]["negatif"] = NEGATIF
                data_str = json.dumps(data_dict, sort_keys=False, indent=4)
                fichier = open(CHEMIN_COMBAT_JSON,'wt')
                fichier.write(data_str)
                fichier.close()
            print('[*][b]Activation aptitude '+str(NAME)+' niveau '+str(RANG)+'[/b]')
            print('[u]Effet :[/u] '+str(VALUE) + ' ('+str(TYPE)+')')
        if ID == 6 and mode == 'defensif':
            with open(CHEMIN_COMBAT_JSON,'r') as json_data:
                data_dict = json.load(json_data)
                POSITIF = data_dict["phase_defensive"]["positif"]
                NEGATIF = data_dict["phase_defensive"]["negatif"]
                POSITIF = int(POSITIF) + int(VALUE)
                TOTAL_DEFENDU = int(POSITIF)
                TOTAL_SUBI = int(NEGATIF) - int(POSITIF)
                if TOTAL_SUBI < 0:
                    TOTAL_SUBI = 0
                data_dict["synthese"]["total_defendu"] = TOTAL_DEFENDU
                data_dict["synthese"]["total_subi"] = TOTAL_SUBI
                data_str = json.dumps(data_dict, sort_keys=False, indent=4)
                fichier = open(CHEMIN_COMBAT_JSON,'wt')
                fichier.write(data_str)
                fichier.close()
            print('[*][b]Activation aptitude '+str(NAME)+' niveau '+str(RANG)+'[/b]')
            print('[u]Effet :[/u] '+str(VALUE) + ' ('+str(TYPE)+')')
        if ID == 7 and mode == 'offensif':
            with open(CHEMIN_COMBAT_JSON,'r') as json_data:
                data_dict = json.load(json_data)
                PA = data_dict["attributs"]["PA_restants"]
                PA = int(PA) + int(VALUE)
                data_dict["attributs"]["PA_restants"] = PA
                data_str = json.dumps(data_dict, sort_keys=False, indent=4)
                fichier = open(CHEMIN_COMBAT_JSON,'wt')
                fichier.write(data_str)
                fichier.close()
            print('[*][b]Activation aptitude '+str(NAME)+' niveau '+str(RANG)+'[/b]')
            print('[u]Effet :[/u] '+str(VALUE) + ' ('+str(TYPE)+')')
        if ID == 8:
            print('[*][b]Activation aptitude '+str(NAME)+' niveau '+str(RANG)+'[/b]')
            print('[u]Effet :[/u] '+str(VALUE) + ' ('+str(TYPE)+') => [rentrer la valeur manuellement à partir du résultat du D10 sur forum]')
        if ID == 9:
            print('[*][b]Activation aptitude '+str(NAME)+' niveau '+str(RANG)+'[/b]')
            print('[u]Effet :[/u] '+str(VALUE) + ' ('+str(TYPE)+") => [rentrer la valeur manuellement à partir de l'attaque renvoyée")
        if ID == 10:
            print('[*][b]Activation aptitude '+str(NAME)+' niveau '+str(RANG)+'[/b]')
            print('[u]Effet :[/u] '+str(VALUE) + ' ('+str(TYPE)+") => [rentrer la valeur manuellement à partir de la valeur de transfert souhaitée")
        if ID == 11:
            print('[*][b]Activation aptitude '+str(NAME)+' niveau '+str(RANG)+'[/b]')
            print('[u]Effet :[/u] '+str(VALUE) + ' ('+str(TYPE)+") => [rentrer la valeur manuellement à partir de la valeur de transfert souhaitée")

    data = get_data(CHEMIN_ODS)
    ETAT_N1 = data['Combat'][39][1]
    ID_N1 = data['Combat'][39][2]
    ETAT_N2 = data['Combat'][40][1]
    ID_N2 = data['Combat'][40][2]
    ETAT_N3 = data['Combat'][41][1]
    ID_N3 = data['Combat'][41][2]
    mode = mode
    if ETAT_N1 == 1:
        RANG = 1
        id_aptitude(ID_N1,RANG,mode)
    elif ETAT_N2 == 1:
        RANG = 2
        id_aptitude(ID_N2,RANG,mode)
    elif ETAT_N3 == 1:
        RANG = 3
        id_aptitude(ID_N3,RANG,mode)

def calcul_PA_bonus(PA_FIN):
    if PA_FIN > 3:
        PA_FIN = 3
    return PA_FIN

def calcul_combo_EP(DEPENSE_EP):
    with open(CHEMIN_COMBAT_JSON,'r') as json_data:
        data_dict = json.load(json_data)
        BASE_COMBO_EP = data_dict["combo"]["combo_EP_fin"]
        SOMME_EP = int(BASE_COMBO_EP) + int(DEPENSE_EP)
    return SOMME_EP

def calcul_combo_ES(DEPENSE_ES):
    with open(CHEMIN_COMBAT_JSON,'r') as json_data:
        data_dict = json.load(json_data)
        BASE_COMBO_ES = data_dict["combo"]["combo_ES_fin"]
        SOMME_ES = int(BASE_COMBO_ES) + int(DEPENSE_ES)
    return SOMME_ES

def calcul_EP_fin():
    with open(CHEMIN_COMBAT_JSON,'r') as json_data:
        data_dict = json.load(json_data)
        EP_DEBUT = data_dict["attributs"]["EP_debut"]
        EP_OFF = data_dict["phase_defensive"]["EP_depenses"]
        EP_DEF = data_dict["phase_offensive"]["EP_depenses"]
        SOMME_EP = int(EP_DEBUT) - (int(EP_OFF) + int(EP_DEF))
    return SOMME_EP

def calcul_ES_fin():
    with open(CHEMIN_COMBAT_JSON,'r') as json_data:
        data_dict = json.load(json_data)
        ES_DEBUT = data_dict["attributs"]["ES_debut"]
        ES_OFF = data_dict["phase_defensive"]["ES_depenses"]
        ES_DEF = data_dict["phase_offensive"]["ES_depenses"]
        SOMME_ES = int(ES_DEBUT) - (int(ES_OFF) + int(ES_DEF))
    return SOMME_ES

def calcul_subi_phase_defensive():
    with open(CHEMIN_COMBAT_JSON,'r') as json_data:
        data_dict = json.load(json_data)
        TOTAL_SUBI = data_dict["synthese"]["total_subi"]
        SACRIFICE = data_dict["phase_defensive"]["sacrifice"]
        SOMME_SUBI = int(TOTAL_SUBI) - int(SACRIFICE)
    return SOMME_SUBI

def calcul_defendu_phase_defensive():
    with open(CHEMIN_COMBAT_JSON,'r') as json_data:
        data_dict = json.load(json_data)
        TOTAL_DEFENDU = data_dict["synthese"]["total_defendu"]
    return TOTAL_DEFENDU

def integration_immo_phase_defensive_defendu():
    TOTAL_DEFENDU = calcul_defendu_phase_defensive()
    with open(CHEMIN_COMBAT_JSON,'r') as json_data:
        data_dict = json.load(json_data)
        IMMOBILISATION = data_dict["phase_defensive"]["immobilisation"]
        SOMME_DEFENDU = int(TOTAL_DEFENDU) - int(IMMOBILISATION)
        if TOTAL_DEFENDU < IMMOBILISATION:
            IMMOBILISATION = 0
        if SOMME_DEFENDU < 0:
            SOMME_DEFENDU = 0
        data_dict["synthese"]["total_defendu"] = SOMME_DEFENDU
        data_dict["synthese"]["immobilisation_subi"] = IMMOBILISATION
        data_str = json.dumps(data_dict, sort_keys=False, indent=4)
        fichier = open(CHEMIN_COMBAT_JSON,'wt')
        fichier.write(data_str)
        fichier.close()
    return SOMME_DEFENDU

def integration_immo_phase_defensive_subi():
    TOTAL_SUBI = calcul_subi_phase_defensive()
    with open(CHEMIN_COMBAT_JSON,'r') as json_data:
        data_dict = json.load(json_data)
        DEFENDU = data_dict["synthese"]["total_defendu"]
        IMMOBILISATION_SUBI = data_dict["synthese"]["immobilisation_subi"]
        SOMME_SUBI = int(TOTAL_SUBI) + IMMOBILISATION_SUBI
        data_dict["synthese"]["total_subi"] = SOMME_SUBI
        data_str = json.dumps(data_dict, sort_keys=False, indent=4)
        fichier = open(CHEMIN_COMBAT_JSON,'wt')
        fichier.write(data_str)
        fichier.close()
    return SOMME_SUBI

def calcul_PV_fin():
    with open(CHEMIN_COMBAT_JSON,'r') as json_data:
        data_dict = json.load(json_data)
        TOTAL_SUBI = data_dict["synthese"]["total_subi"]
        SACRIFICE_DEFENSIF = data_dict["phase_defensive"]["sacrifice"]
        SACRIFICE_OFFENSIF = data_dict["phase_offensive"]["sacrifice"]
        PV_DEBUT = data_dict["attributs"]["PV_debut"]
        POSITIF = data_dict["phase_offensive"]["positif"]
        PV_TOTAL = data_dict["attributs"]["PV_total"]
        PV_FIN = int(PV_DEBUT) - int(TOTAL_SUBI) - int(SACRIFICE_DEFENSIF) - int(SACRIFICE_OFFENSIF) + int(POSITIF)
        if PV_FIN > PV_TOTAL:
            PV_FIN = PV_TOTAL
    return PV_FIN

def calcul_PA_fin():
    with open(CHEMIN_COMBAT_JSON,'r') as json_data:
        data_dict = json.load(json_data)
        PA_DEPENSES = data_dict["attributs"]["PA_depenses"]
        PA_RESTANTS = data_dict["attributs"]["PA_restants"]
        PA_FIN = int(PA_RESTANTS) - int(PA_DEPENSES)
    return PA_FIN

def lancement_combo():
    with open(CHEMIN_COMBAT_JSON,'r') as json_data:
        data_dict = json.load(json_data)
        EP_DEBUT = data_dict["combo"]["combo_EP_debut"]
        ES_DEBUT = data_dict["combo"]["combo_ES_debut"]
        EP_FIN = data_dict["combo"]["combo_EP_fin"]
        ES_FIN = data_dict["combo"]["combo_ES_fin"]
        EP = int(EP_DEBUT) + int(EP_FIN)
        ES = int(ES_DEBUT) + int(ES_FIN)
        ENTRAVE = data_dict["phase_offensive"]["entrave"]
        NEGATIF = data_dict["phase_offensive"]["negatif"]
        IMMOBILISATION = data_dict["phase_offensive"]["immobilisation"]
        ECO_PA = data_dict["attributs"]["PA_restants"]
        DEGATS_MULTICIBLES = data_dict["phase_offensive"]["degats_multicibles"]
        DRAIN_IMPARABLE = data_dict["phase_offensive"]["drain_imparable"]
        NEGATIF_SACRIFICE = data_dict["phase_offensive"]["sacrifice"]
        data = get_data(CHEMIN_ODS)
        BONUS_1 = data['Sysco'][13][13]
        BONUS_2 = data['Sysco'][13][14]
        BONUS_3 = data['Sysco'][13][15]
        BONUS_4 = data['Sysco'][13][16]
        BONUS_5 = data['Sysco'][13][17]
        BONUS_6 = data['Sysco'][13][18]
        BONUS_7 = data['Sysco'][13][19]
        MALUS_7 = data['Sysco'][14][19]
        ETAT = data['Combat'][51][1]
        ID = data['Combat'][51][2]
        if ETAT == 1:
            if ID == 1:
                SEUIL_EP = 350
                SEUIL_ES = 150
                if EP > SEUIL_EP and ES > SEUIL_ES:
                    ENTRAVE = int(ENTRAVE) + int(BONUS_1)
                    print('Déclenchement combo '+str(SEUIL_EP) + '-'+str(SEUIL_ES) + ' ('+str(BONUS_1)+ ' entrave)')
                else:
                    print('JAUGES COMBO INSUFFISANTES ('+str(EP)+'/' + str(SEUIL_EP) +' EP combo & ' + str(ES) + '/' + str(SEUIL_ES)+' ES)')
            if ID == 2:
                SEUIL_EP = 250
                SEUIL_ES = 250
                if EP > SEUIL_EP and ES > SEUIL_ES:
                    NEGATIF = int(NEGATIF) + int(BONUS_2)
                    print('Déclenchement combo '+str(SEUIL_EP) + '-'+str(SEUIL_ES) + ' ('+str(BONUS_2)+ ' dommages)')
                else:
                    print('JAUGES COMBO INSUFFISANTES ('+str(EP)+'/' + str(SEUIL_EP) +' EP combo & ' + str(ES) + '/' + str(SEUIL_ES)+' ES)')
            if ID == 3:
                SEUIL_EP = 150
                SEUIL_ES = 350
                if EP > SEUIL_EP and ES > SEUIL_ES:
                    IMMOBILISATION = int(IMMOBILISATION) + int(BONUS_3)
                    print('Déclenchement combo '+str(SEUIL_EP) + '-'+str(SEUIL_ES) + ' ('+str(BONUS_3)+ ' immobilisation)')
                else:
                    print('JAUGES COMBO INSUFFISANTES ('+str(EP)+'/' + str(SEUIL_EP) +' EP combo & ' + str(ES) + '/' + str(SEUIL_ES)+' ES)')
            if ID == 4:
                SEUIL_EP = 450
                SEUIL_ES = 250
                if EP > SEUIL_EP and ES > SEUIL_ES:
                    ECO_PA = int(ECO_PA) + int(BONUS_4)
                    print('Déclenchement combo '+str(SEUIL_EP) + '-'+str(SEUIL_ES) + ' ('+str(BONUS_4)+ ' économie PA)')
                else:
                    print('JAUGES COMBO INSUFFISANTES ('+str(EP)+'/' + str(SEUIL_EP) +' EP combo & ' + str(ES) + '/' + str(SEUIL_ES)+' ES)')
            if ID == 5:
                SEUIL_EP = 350
                SEUIL_ES = 350
                if EP > SEUIL_EP and ES > SEUIL_ES:
                    DEGATS_MULTICIBLES = int(DEGATS_MULTICIBLES) + int(BONUS_5)
                    print('Déclenchement combo '+str(SEUIL_EP) + '-'+str(SEUIL_ES) + ' ('+str(BONUS_5)+ ' dommages multicibles)')
                else:
                    print('JAUGES COMBO INSUFFISANTES ('+str(EP)+'/' + str(SEUIL_EP) +' EP combo & ' + str(ES) + '/' + str(SEUIL_ES)+' ES)')
            if ID == 6:
                SEUIL_EP = 250
                SEUIL_ES = 450
                if EP > SEUIL_EP and ES > SEUIL_ES:
                    DRAIN_IMPARABLE = int(DRAIN_IMPARABLE) + int(BONUS_6)
                    DRAIN_IMPARABLE = int(DRAIN_IMPARABLE)
                    print('Déclenchement combo '+str(SEUIL_EP) + '-'+str(SEUIL_ES) + ' ('+str(BONUS_6)+ ' drain imparable)')
                else:
                    print('JAUGES COMBO INSUFFISANTES ('+str(EP)+'/' + str(SEUIL_EP) +' EP combo & ' + str(ES) + '/' + str(SEUIL_ES)+' ES)')
            if ID == 7:
                SEUIL_EP = 450
                SEUIL_ES = 450
                if EP > SEUIL_EP and ES > SEUIL_ES:
                    NEGATIF = int(NEGATIF) + int(BONUS_7)
                    NEGATIF_SACRIFICE = int(NEGATIF_SACRIFICE) + int(MALUS_7)
                    print('Déclenchement combo '+str(SEUIL_EP) + '-'+str(SEUIL_ES) + ' ('+str(BONUS_7)+ ' dommages & ' + str(MALUS_7) + ' sacrifiés)')
                else:
                    print('JAUGES COMBO INSUFFISANTES ('+str(EP)+'/' + str(SEUIL_EP) +' EP combo & ' + str(ES) + '/' + str(SEUIL_ES)+' ES)')
            EP = 0
            ES = 0
            data_dict["phase_offensive"]["entrave"] = ENTRAVE
            data_dict["phase_offensive"]["negatif"] = NEGATIF
            data_dict["phase_offensive"]["immobilisation"] = IMMOBILISATION
            data_dict["attributs"]["PA_restants"] = ECO_PA
            data_dict["phase_offensive"]["degats_multicibles"] = DEGATS_MULTICIBLES
            data_dict["phase_offensive"]["drain_imparable"] = DRAIN_IMPARABLE
            data_dict["phase_offensive"]["sacrifice"] = NEGATIF_SACRIFICE
            data_dict["combo"]["combo_EP_fin"] = EP
            data_dict["combo"]["combo_ES_fin"] = ES
            data_dict["combo"]["combo_EP_debut"] = EP
            data_dict["combo"]["combo_ES_debut"] = ES
            data_str = json.dumps(data_dict, sort_keys=False, indent=4)
            fichier = open(CHEMIN_COMBAT_JSON,'wt')
            fichier.write(data_str)
            fichier.close()

def specialites():
    with open(CHEMIN_COMBAT_JSON,'r') as json_data:
        data_dict = json.load(json_data)
        PA_RESTANTS = data_dict["attributs"]["PA_restants"]
        DRAIN = data_dict["phase_offensive"]["drain"]
        DON_REIRYOKU = data_dict["phase_offensive"]["don_rei"]
        IMMOBILISATION = data_dict["phase_offensive"]["immobilisation"]
        ENTRAVE = data_dict["phase_offensive"]["entrave"]
        POSITIF = data_dict["phase_offensive"]["positif"]
        NEGATIF = data_dict["phase_offensive"]["negatif"]
        data = get_data(CHEMIN_ODS)
        GENERALES = data['Combat'][43][1]
        GENERALES_ID = data['Combat'][43][2]
        SHINIGAMI = data['Combat'][44][1]
        SHINIGAMI_ID = data['Combat'][44][2]
        HOLLOW_ARRANCAR = data['Combat'][45][1]
        HOLLOW_ARRANCAR_ID = data['Combat'][45][2]
        HOLLOW = data['Combat'][46][1]
        HOLLOW_ID = data['Combat'][46][2]
        ARRANCAR = data['Combat'][47][1]
        ARRANCAR_ID = data['Combat'][47][2]
        FULLBRINGER = data['Combat'][48][1]
        FULLBRINGER_ID = data['Combat'][48][2]
        QUINCY = data['Combat'][49][1]
        QUINCY_ID = data['Combat'][49][2]
        if GENERALES == 1:
            if GENERALES_ID == 4:
                print('Déclenchement Spécialité Revanchard (double les dégâts maximum pour la technique Déferlement de Reiryoku)')
            if GENERALES_ID == 5:
                print("Déclenchement Spécialité Opportuniste  (Malus de 2 sur le jet d'initiative, bonus d'1 PA sur le premier tour si ne joue pas en premier')")
                PA_BONUS = int(PA_RESTANTS) + 1
                data_dict["attributs"]["PA_restants"] = PA_BONUS
            if GENERALES_ID == 6:
                print("Déclenchement Spécialité Manipulateur (Bonus de 50 sur un drain par combat)")
                DRAIN = int(DRAIN) + 50
                data_dict["phase_offensive"]["drain"] = DRAIN
            if GENERALES_ID == 7:
                print("Déclenchement Spécialité Manipulateur (Bonus de 50 sur un don reiryoku par combat)")
                DON_REIRYOKU = int(DON_REIRYOKU) + 50
                data_dict["phase_offensive"]["don_rei"] = DON_REIRYOKU
            if GENERALES_ID == 8:
                print("Déclenchement Spécialité Lutteur (Bonus de 100 sur une immobilisation par combat)")
                IMMOBILISATION = int(IMMOBILISATION) + 100
                data_dict["phase_offensive"]["immobilisation"] = IMMOBILISATION
            if GENERALES_ID == 9:
                print("Déclenchement Spécialité Lutteur (Bonus de 100 sur une entrave par combat)")
                ENTRAVE = int(ENTRAVE) + 100
                data_dict["phase_offensive"]["entrave"] = ENTRAVE
            if GENERALES_ID == 10:
                print("Déclenchement Spécialité Partenaire (Bonus de 100 sur un boost destiné à un allié [EDITER MANUELLEMENT LE RECAP DE PHASE OFFENSIVE POUR PRECISER TYPE DE BOOST])")
            if GENERALES_ID == 11:
                print("Déclenchement Spécialité Guérisseur (Bonus de 100 sur une guérison par combat)")
                POSITIF = int(POSITIF) + 100
                data_dict["phase_offensive"]["positif"] = POSITIF
            if GENERALES_ID == 12:
                print("Déclenchement Spécialité Altruiste (Les interventions ne coûtent qu'1 PA que la technique adverse ait vitesse ou non [EDITER MANUELLEMENT LE RECAPITULATIF POUR L'INTEGRER])")
        if SHINIGAMI == 1:
            if SHINIGAMI_ID == 30:
                print("Déclenchement Spécialité Nécromancien (Une fois par tour, une technique de Kido peut bénéficier d'un bonus de 50 sur son effet principal, 25 s'il s'agit d'un don/drain reiryoku [EDITER MANUELLEMENT LE RECAPITULATIF POUR L'INTEGRER])")
            if SHINIGAMI_ID == 31:
                print("Déclenchement Spécialité Jikken Shikai (Une fois par tour, une technique de Shikai peut bénéficier d'un bonus de 50 sur son effet principal, 25 s'il s'agit d'un don/drain reiryoku [EDITER MANUELLEMENT LE RECAPITULATIF POUR L'INTEGRER])")
            if SHINIGAMI_ID == 32:
                print("Déclenchement Spécialité Shunshin (Une fois par combat, une technique de Shunpo défensive peut bénéficier d'un bonus de 200 [EDITER MANUELLEMENT LE RECAPITULATIF POUR L'INTEGRER])")
        if HOLLOW_ARRANCAR == 1:
            if HOLLOW_ARRANCAR_ID == 40:
                print("Déclenchement Spécialité Régénération instantanée (Bonus de 50 sur une régénération par tour)")
                POSITIF = int(POSITIF) + 50
                data_dict["phase_offensive"]["positif"] = POSITIF
        if HOLLOW == 1:
            if HOLLOW_ID == 50:
                print("Déclenchement Spécialité Negación (Une fois par combat, une technique de Negación défensive peut bénéficier d'un bonus de 200 [EDITER MANUELLEMENT LE RECAPITULATIF POUR L'INTEGRER])")
            if HOLLOW_ID == 50:
                print("Déclenchement Spécialité Vasto Lorde (Bonus de 50 sur une attaque par tour)")
                NEGATIF = int(NEGATIF) + 50
                data_dict["phase_offensive"]["negatif"] = NEGATIF
        if ARRANCAR == 1:
            if ARRANCAR_ID == 60:
                print("Déclenchement Spécialité Mutilación (Une fois par tour, une technique de Resurrecion peut bénéficier d'un bonus de 50 sur son effet principal, 25 s'il s'agit d'un don/drain reiryoku [EDITER MANUELLEMENT LE RECAPITULATIF POUR L'INTEGRER])")
            if ARRANCAR_ID == 61:
                print("Déclenchement Spécialité Hierro (Une fois par combat, une technique de Hierro défensive peut bénéficier d'un bonus de 200 [EDITER MANUELLEMENT LE RECAPITULATIF POUR L'INTEGRER])")
        if FULLBRINGER == 1:
            if FULLBRINGER_ID == 70:
                print("Déclenchement Spécialité Soul Eater (Une fois par tour, une technique de manipulation d'âme peut bénéficier d'un bonus de 50 sur son effet principal, 25 s'il s'agit d'un don/drain reiryoku [EDITER MANUELLEMENT LE RECAPITULATIF POUR L'INTEGRER])")
            if FULLBRINGER_ID == 71:
                print("Déclenchement Spécialité Complete Fullbring (Une fois par tour, une technique de Fullbring peut bénéficier d'un bonus de 50 sur son effet principal, 25 s'il s'agit d'un don/drain reiryoku [EDITER MANUELLEMENT LE RECAPITULATIF POUR L'INTEGRER])")
            if FULLBRINGER_ID == 72:
                print("Déclenchement Spécialité Hitech (Une fois par combat, une technique de Science peut bénéficier d'un bonus de 150 et 75 s'il s'agit d'un Don/Drain reiryoku' [EDITER MANUELLEMENT LE RECAPITULATIF POUR L'INTEGRER])")
        if QUINCY == 1:
            if QUINCY_ID == 80:
                print("Déclenchement Spécialité Heilig Bogen (Bonus de 50 sur une attaque de tir d'énergie spirituelle par tour)")
                NEGATIF = int(NEGATIF) + 50
                data_dict["phase_offensive"]["negatif"] = NEGATIF
            if QUINCY_ID == 81:
                print("Déclenchement Spécialité Letzt Stil (Une fois par combat, une technique de Leiden Hant peut bénéficier d'un bonus de 150 et 75 s'il s'agit d'un Don/Drain reiryoku' [EDITER MANUELLEMENT LE RECAPITULATIF POUR L'INTEGRER])")
            if QUINCY_ID == 82:
                print("Déclenchement Spécialité Blut (Une fois par combat, une technique de Blut peut bénéficier d'un bonus de 175 sur son effet principal (Blut Arterie (boost offensif) ou Blut Vene (défense)) [EDITER MANUELLEMENT LE RECAPITULATIF POUR L'INTEGRER])")
        data_str = json.dumps(data_dict, sort_keys=False, indent=4)
        fichier = open(CHEMIN_COMBAT_JSON,'wt')
        fichier.write(data_str)
        fichier.close()



def clean_json_combat():
    with open(CHEMIN_COMBAT_JSON,'r') as json_data:
        data_dict = json.load(json_data)
        data_dict["synthese"]["total_defendu"] = 0
        data_dict["synthese"]["total_subi"] = 0
        data_dict["attributs"]["PA_depenses"] = 0
        data_dict["attributs"]["PA_restants"] = 0
        data_dict["attributs"]["EP_fin"] = 0
        data_dict["attributs"]["ES_fin"] = 0
        data_dict["phase_defensive"]["positif"] = 0
        data_dict["phase_defensive"]["negatif"] = 0
        data_dict["phase_offensive"]["negatif"] = 0
        data_dict["phase_offensive"]["positif"] = 0
        data_dict["phase_offensive"]["guerison"] = 0
        data_dict["phase_offensive"]["entrave"] = 0
        data_dict["phase_offensive"]["immobilisation"] = 0
        data_dict["phase_offensive"]["drain"] = 0
        data_dict["phase_offensive"]["don_rei"] = 0
        data_dict["combo"]["combo_EP_debut"] = 0
        data_dict["combo"]["combo_ES_debut"] = 0
        data_dict["combo"]["combo_EP_fin"] = 0
        data_dict["combo"]["combo_ES_fin"] = 0
        data_dict["phase_defensive"]["EP_depenses"] = 0
        data_dict["phase_defensive"]["entrave"] = 0
        data_dict["phase_defensive"]["immobilisation"] = 0
        data_dict["phase_defensive"]["guerison"] = 0
        data_dict["phase_defensive"]["drain"] = 0
        data_dict["phase_defensive"]["don_reiryoku"] = 0
        data_dict["phase_defensive"]["ES_depenses"] = 0
        data_dict["phase_offensive"]["EP_depenses"] = 0
        data_dict["phase_offensive"]["ES_depenses"] = 0
        data_dict["phase_defensive"]["sacrifice"] = 0
        data_dict["phase_offensive"]["sacrifice"] = 0
        data_dict["phase_offensive"]["degats_multicibles"] = 0
        data_dict["phase_offensive"]["drain_imparable"] = 0
        data_dict["phase_offensive"]["deferlement_reiryoku"] = 0
        data_dict["phase_offensive"]["entrave_subi"] = 0
        data_str = json.dumps(data_dict, sort_keys=False, indent=4)
        fichier = open(CHEMIN_COMBAT_JSON,'wt')
        fichier.write(data_str)
        fichier.close()

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
    PA_TOTAL = data['Combat'][5][5]
    COMBO_EP_DEBUT = data['Combat'][21][1]
    COMBO_ES_DEBUT = data['Combat'][22][1]
    MAINTENU_SOMME = data['Combat'][11][1]
    NEGATIF_SOMME_DEBUT = data['Combat'][12][1]
    POSITIF_SOMME_DEBUT = data['Combat'][13][1]

    maj_json_lancement(PV_DEBUT,PV_TOTAL,EP_DEBUT,EP_TOTAL,ES_DEBUT,ES_TOTAL,PA_DEBUT,COMBO_EP_DEBUT,COMBO_ES_DEBUT,
MAINTENU_SOMME,NEGATIF_SOMME_DEBUT,POSITIF_SOMME_DEBUT)


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

    check_maintien()

    print('[*][b]Valeurs négatives :[/b] ' + str(NEGATIF_SOMME_DEBUT))
    print('[*][b]Valeurs positives :[/b] ' + str(POSITIF_SOMME_DEBUT))
    print('[/list][u][b][color=#a2783c]Techniques défensives :[/color][/b][/u]')
    print('[list]')

    mode = 'defensif'
    second_liberation(mode)
    techniques_defensives()
    aptitudes(mode)

    TOTAL_DEFENDU = integration_immo_phase_defensive_defendu()
    TOTAL_SUBI = integration_immo_phase_defensive_subi()

    print('[/list]')
    print('[u][b][color=#a2783c]Résumé phase défensive :[/color][/b][/u]')
    print('[list][*][b]Défendu :[/b] ' + str(TOTAL_DEFENDU))
    print('[*][b]Subi :[/b] ' + str(TOTAL_SUBI) + ' [/list]')
    print('[h3][color=#929291]Phase [color=#a23d3c]Offensive[/color][/color][/h3]')
    print('\n')
    print('[u][b][color=#a2783c]Techniques offensives :[/color][/b][/u]')
    print('[list]')

    mode = 'offensif'
    first_liberation()
    second_liberation(mode)
    techniques_offensives()
    aptitudes(mode)
    lancement_combo()
    specialites()

    print('[/list]')
    print('[u][b][color=#a2783c]Récapitulatif :[/color][/b][/u]')

    valeur_negatives_positives_somme()

    print('[h3][color=#929291]Stats de[/color] fin de tour[/h3]')
    print('\n')

    EP_FIN = calcul_EP_fin()
    ES_FIN = calcul_ES_fin()
    PV_FIN = calcul_PV_fin()
    PA_FIN = calcul_PA_fin()

    print('[b][color=#92d050]Santé : [color=#f9f9f9]' + str(PV_FIN) + '[/color]/' + str(PV_TOTAL) + '[/color][/b]')
    print('[b][color=#c83737]Énergie Physique : [color=#f9f9f9]' + str(EP_FIN) + '[/color]/' + str(EP_TOTAL) + '[/color][/b]')
    print('[b][color=#2a4cbc]Énergie Spirituelle : [color=#f9f9f9]' + str(ES_FIN) + '[/color]/' + str(ES_TOTAL) + '[/color][/b]')
    print('\n')

    PA_BONUS = calcul_PA_bonus(PA_FIN)

    print("[b][color=#783da2]Points d'Action : [color=#f9f9f9]" + str(PA_FIN) + "[/color]/"+str(PA_TOTAL)+"[/color][/b] (+" + str(PA_BONUS) + " PA au prochain tour)")
    print('\n')

    combo_somme_fin()

    clean_json_combat()