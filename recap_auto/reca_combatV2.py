from pyexcel_ods import get_data
import json

CHEMIN_ODS = 'E:/python/BleachTomorrowComes/recap_auto/FT.ods'
CHEMIN_COMBAT_JSON = 'E:/python/BleachTomorrowComes/recap_auto/combat.json'
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

    data = get_data(CHEMIN_ODS)
    NOMBRE_TECH = data['Combat'][0][8]
    a = 2
    b = 0
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
        ENTRAVE = data_dict["phase_offensive"]["entrave"]
        IMMOBILISATION = data_dict["phase_offensive"]["immobilisation"]
        DRAIN = data_dict["phase_offensive"]["drain"]
        DON_REI = data_dict["phase_offensive"]["don_rei"]
        TEXT_VALEURS_NEGATIVES = '[list][*][b]Valeurs négatives :[/b] '+ str(NEGATIF) + ' dommages '
        TEXT_VALEURS_POSITIVES = '[*][b]Valeurs positives :[/b] '+ str(POSITIF) + ' regen '
        if ENTRAVE != 0:
            TEXT_VALEURS_NEGATIVES = TEXT_VALEURS_NEGATIVES + ' & ' +str(ENTRAVE) + ' entraves '
        if IMMOBILISATION != 0:
            TEXT_VALEURS_NEGATIVES = TEXT_VALEURS_NEGATIVES + ' & ' +str(IMMOBILISATION) + ' immobilisation '
        if DRAIN != 0:
            TEXT_VALEURS_NEGATIVES = TEXT_VALEURS_NEGATIVES + ' & ' +str(DRAIN) + ' drain reiryoku '
        if GUERISON != 0:
            TEXT_VALEURS_POSITIVES = TEXT_VALEURS_POSITIVES + ' & ' +str(GUERISON) + ' guerison '
        if DON_REI != 0:
            TEXT_VALEURS_POSITIVES = TEXT_VALEURS_POSITIVES + ' & ' +str(DON_REI) + ' don reiryoku '
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
        SOMME_SUBI = int(TOTAL_SUBI) + int(SACRIFICE)
    return SOMME_SUBI

def calcul_defendu_phase_defensive():
    with open(CHEMIN_COMBAT_JSON,'r') as json_data:
        data_dict = json.load(json_data)
        TOTAL_DEFENDU = data_dict["synthese"]["total_defendu"]
    return TOTAL_DEFENDU

def calcul_PV_fin():
    with open(CHEMIN_COMBAT_JSON,'r') as json_data:
        data_dict = json.load(json_data)
        TOTAL_SUBI = data_dict["synthese"]["total_subi"]
        SACRIFICE_DEFENSIF = data_dict["phase_defensive"]["sacrifice"]
        SACRIFICE_OFFENSIF = data_dict["phase_offensive"]["sacrifice"]
        PV_DEBUT = data_dict["attributs"]["PV_debut"]
        PV_FIN = int(PV_DEBUT) - int(TOTAL_SUBI) - int(SACRIFICE_DEFENSIF) - int(SACRIFICE_OFFENSIF)
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
        EP = data_dict["combo"]["combo_EP_fin"]
        ES = data_dict["combo"]["combo_ES_fin"]
        ENTRAVE = data_dict["phase_offensive"]["entrave"]
        NEGATIF = data_dict["phase_offensive"]["negatif"]
        IMMOBILISATION = data_dict["phase_offensive"]["immobilisation"]
        ECO_PA = data_dict["phase_offensive"]["PA_restants"]
        DEGATS_MULTICIBLES = data_dict["phase_offensive"]["degats_multicibles"]
        DRAIN_IMPARABLE = data_dict["phase_offensive"]["drain"]
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
            data_dict["combo"]["combo_EP_fin"] = EP
            data_dict["combo"]["combo_ES_fin"] = ES
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
        data_dict["phase_defensive"]["ES_depenses"] = 0
        data_dict["phase_offensive"]["EP_depenses"] = 0
        data_dict["phase_offensive"]["ES_depenses"] = 0
        data_dict["phase_defensive"]["sacrifice"] = 0
        data_dict["phase_offensive"]["sacrifice"] = 0
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

    TOTAL_DEFENDU = calcul_defendu_phase_defensive()
    TOTAL_SUBI = calcul_subi_phase_defensive()

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