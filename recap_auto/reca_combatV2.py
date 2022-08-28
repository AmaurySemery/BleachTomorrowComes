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
    def print_for_reca(NIV_TECH,NOM_TECH,BRANCHE_PRINCIPALE_TECH,BRANCHE_SECONDAIRE_TECH,TYPE,
    EFFET,DEPENSE_EP,DEPENSE_ES,DEPENSE_PV,DESCRIPTION,COUT_PA):
        print('[*][b][Niveau '+str(NIV_TECH)+'] '+str(NOM_TECH)+'[/b]')
        if BRANCHE_SECONDAIRE_TECH != 0:
            print('['+str(BRANCHE_PRINCIPALE_TECH)+'] ['+str(BRANCHE_SECONDAIRE_TECH)+'] ['+str(TYPE)+']')
        if BRANCHE_SECONDAIRE_TECH == 0:
            print('['+str(BRANCHE_PRINCIPALE_TECH)+'] ['+str(TYPE)+']')
        print('[u]Effets :[/u] '+str(EFFET))
        if DEPENSE_PV == 0:
            print('[u]Dépense :[/u] '+str(DEPENSE_EP)+' EP & ' +str(DEPENSE_ES)+' ES')
        if DEPENSE_PV != 0:
            print('[u]Dépense :[/u] '+str(DEPENSE_EP)+' EP & ' +str(DEPENSE_ES)+' ES & '+ str(DEPENSE_PV) + ' PV')
        print('[spoiler="Descriptif RP"]'+str(DESCRIPTION)+'[/spoiler]')
        print('\n')

    def save_depense_effet(EFFET,DEPENSE_EP,DEPENSE_ES,DEPENSE_PV,COUT_PA,CODE_TYPE_EFFET):
        with open(CHEMIN_COMBAT_JSON,'r') as json_data:
            data_dict = json.load(json_data)
            COMBO_EP = data_dict["combo"]["combo_EP_fin"]
            COMBO_ES = data_dict["combo"]["combo_ES_fin"]
            POSITIF = data_dict["phase_defensive"]["positif"]
            NEGATIF = data_dict["phase_defensive"]["negatif"]
            TOTAL_DEFENDU = data_dict["synthese"]["total_defendu"]
            TOTAL_SUBI = data_dict["synthese"]["total_subi"]
            PA_DEBUT = data_dict["attributs"]["PA_debut"]
            PA_DEPENSES = data_dict["attributs"]["PA_depenses"]
            EP = data_dict["attributs"]["EP_fin"]
            ES = data_dict["attributs"]["ES_fin"]
            CODE_TYPE_EFFET = data['Liste_techniques'][POSITION][14]
            POSITIF = int(POSITIF) + int(EFFET)
            TOTAL_DEFENDU = int(POSITIF)
            if int(TOTAL_DEFENDU) < 0 :
                TOTAL_DEFENDU = 0
            TOTAL_SUBI = int(POSITIF) - int(DEPENSE_PV) - int(NEGATIF)
            TOTAL_SUBI = abs(TOTAL_SUBI)
            PA_DEPENSES = int(PA_DEPENSES) + int(COUT_PA)
            PA_RESTANTS = int(PA_DEBUT) - int(PA_DEPENSES)
            EP_DEPENSES = int(EP) + int(DEPENSE_EP)
            ES_DEPENSES = int(ES) + int(DEPENSE_ES)
            COMBO_EP = int(COMBO_EP) + int(EP_DEPENSES)
            COMBO_ES = int(COMBO_ES) + int(ES_DEPENSES)
            data_dict["phase_defensive"]["positif"] = POSITIF
            data_dict["phase_defensive"]["negatif"] = NEGATIF
            data_dict["synthese"]["total_defendu"] = TOTAL_DEFENDU
            data_dict["synthese"]["total_subi"] = TOTAL_SUBI
            data_dict["attributs"]["PA_depenses"] = PA_DEPENSES
            data_dict["attributs"]["PA_restants"] = PA_RESTANTS
            data_dict["attributs"]["EP_fin"] = EP_DEPENSES
            data_dict["attributs"]["ES_fin"] = ES_DEPENSES
            data_dict["combo"]["combo_EP_fin"] = COMBO_EP
            data_dict["combo"]["combo_ES_fin"] = COMBO_ES
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
    def print_for_reca(NIV_TECH,NOM_TECH,BRANCHE_PRINCIPALE_TECH,BRANCHE_SECONDAIRE_TECH,TYPE,
    EFFET,DEPENSE_EP,DEPENSE_ES,DEPENSE_PV,DESCRIPTION,COUT_PA):
        print('[*][b][Niveau '+str(NIV_TECH)+'] '+str(NOM_TECH)+'[/b]')
        if BRANCHE_SECONDAIRE_TECH != 0:
            print('['+str(BRANCHE_PRINCIPALE_TECH)+'] ['+str(BRANCHE_SECONDAIRE_TECH)+'] ['+str(TYPE)+']')
        if BRANCHE_SECONDAIRE_TECH == 0:
            print('['+str(BRANCHE_PRINCIPALE_TECH)+'] ['+str(TYPE)+']')
        print('[u]Effets :[/u] '+str(EFFET))
        if DEPENSE_PV == 0:
            print('[u]Dépense :[/u] '+str(DEPENSE_EP)+' EP & ' +str(DEPENSE_ES)+' ES')
        if DEPENSE_PV != 0:
            print('[u]Dépense :[/u] '+str(DEPENSE_EP)+' EP & ' +str(DEPENSE_ES)+' ES & '+ str(DEPENSE_PV) + ' PV')
        print('[spoiler="Descriptif RP"]'+str(DESCRIPTION)+'[/spoiler]')
        print('\n')

    def save_depense_effet(EFFET,DEPENSE_EP,DEPENSE_ES,DEPENSE_PV,COUT_PA,BONUS,CODE_TYPE_EFFET):
        with open(CHEMIN_COMBAT_JSON,'r') as json_data:
            data_dict = json.load(json_data)
            COMBO_EP = data_dict["combo"]["combo_EP_fin"]
            COMBO_ES = data_dict["combo"]["combo_ES_fin"]
            POSITIF = data_dict["phase_offensive"]["positif"]
            NEGATIF = data_dict["phase_offensive"]["negatif"]
            PA_DEBUT = data_dict["attributs"]["PA_debut"]
            PA_DEPENSES = data_dict["attributs"]["PA_depenses"]
            PA_RESTANTS = data_dict["attributs"]["PA_restants"]
            EP = data_dict["attributs"]["EP_fin"]
            ES = data_dict["attributs"]["ES_fin"]
            TOTAL_SUBI = data_dict["synthese"]["total_subi"]
            TOTAL_SUBI = int(TOTAL_SUBI) + int(DEPENSE_PV)
            PA_DEPENSES = int(PA_DEPENSES) + int(COUT_PA)
            PA_RESTANTS = int(PA_DEBUT) - int(PA_DEPENSES)
            EP_DEPENSES = int(EP) + int(DEPENSE_EP)
            ES_DEPENSES = int(ES) + int(DEPENSE_ES)
            COMBO_EP = int(COMBO_EP) + int(EP_DEPENSES)
            COMBO_ES = int(COMBO_ES) + int(ES_DEPENSES)
            data_dict["attributs"]["PA_depenses"] = PA_DEPENSES
            data_dict["attributs"]["PA_restants"] = PA_RESTANTS
            data_dict["attributs"]["EP_fin"] = EP_DEPENSES
            data_dict["attributs"]["ES_fin"] = ES_DEPENSES
            data_dict["combo"]["combo_EP_fin"] = COMBO_EP
            data_dict["combo"]["combo_ES_fin"] = COMBO_ES
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
    ETAT = data['Combat'][25][1]
    if ETAT == 0:
        pass
    elif ETAT == 1:
        print('[*][b]Activation libération niveau 1[/b]')
        COUT_PA = data['Sysco'][11][8]
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
    ETAT_SECOND_LIBERATION = data['Combat'][26][1]
    VALUE_SECOND_LIBERATION = data['Liste_techniques'][20][5]
    TYPE_SECOND_LIBERATION = data['Liste_techniques'][20][4]
    TEXT_MAINTENU = '[*][b]Maintenu :[/b] '
    if ETAT_SECOND_LIBERATION == 2:
        TEXT_MAINTENU = TEXT_MAINTENU + str(VALUE_SECOND_LIBERATION) + ' liberation niveau 2 (' + TYPE_SECOND_LIBERATION +')'
    else:
        TEXT_MAINTENU = TEXT_MAINTENU + '0'
    print(TEXT_MAINTENU)

def second_liberation():
    data = get_data(CHEMIN_ODS)
    ETAT = data['Combat'][26][1]
    COUT_PA = data['Sysco'][11][10]
    COUT_EP = data['Sysco'][16][10]
    COUT_ES = data['Sysco'][17][10]
    EFFET = data['Liste_techniques'][20][5]
    CODE_TYPE_EFFET = data['Liste_techniques'][20][14]
    if ETAT == 0:
        pass
    elif ETAT == 1:
        print('[*][b]Activation libération niveau 2[/b]')
        print('[u]Dépense :[/u] '+str(COUT_PA)+' PA & '+str(COUT_EP)+' EP & '+str(COUT_ES)+' ES')
        print('\n')
        with open(CHEMIN_COMBAT_JSON,'r') as json_data:
            data_dict = json.load(json_data)
            COMBO_EP = data_dict["combo"]["combo_EP_fin"]
            COMBO_ES = data_dict["combo"]["combo_ES_fin"]
            PA_DEPENSES = data_dict["attributs"]["PA_depenses"]
            EP_DEPENSES = data_dict["attributs"]["EP_fin"]
            ES_DEPENSES = data_dict["attributs"]["ES_fin"]
            PA_DEPENSES = int(PA_DEPENSES) + int(COUT_PA)
            EP_DEPENSES = int(EP_DEPENSES) + int(COUT_EP)
            ES_DEPENSES = int(ES_DEPENSES) + int(COUT_ES)
            COMBO_EP = int(COMBO_EP) + int(EP_DEPENSES)
            COMBO_ES = int(COMBO_ES) + int(ES_DEPENSES)
            data_dict["attributs"]["PA_depenses"] = PA_DEPENSES
            data_dict["attributs"]["EP_fin"] = EP_DEPENSES
            data_dict["attributs"]["ES_fin"] = ES_DEPENSES
            data_dict["combo"]["combo_EP_fin"] = COMBO_EP
            data_dict["combo"]["combo_ES_fin"] = COMBO_ES
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
        print('[*][b]Libération niveau 2 maintenue[/b]')
        print('[u]Dépense :[/u] '+str(COUT_EP)+' EP & '+str(COUT_ES)+' ES')
        print('\n')
        with open(CHEMIN_COMBAT_JSON,'r') as json_data:
            data_dict = json.load(json_data)
            EP_DEPENSES = data_dict["attributs"]["EP_fin"]
            ES_DEPENSES = data_dict["attributs"]["ES_fin"]
            EP_DEPENSES = int(EP_DEPENSES) + int(COUT_EP)
            ES_DEPENSES = int(ES_DEPENSES) + int(COUT_ES)
            data_dict["attributs"]["EP_fin"] = EP_DEPENSES
            data_dict["attributs"]["ES_fin"] = ES_DEPENSES
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
        COMBO_EP_DEBUT = data_dict["combo"]["combo_EP_debut"]
        COMBO_ES_DEBUT = data_dict["combo"]["combo_ES_debut"]
        COMBO_EP_FIN = data_dict["combo"]["combo_EP_fin"]
        COMBO_ES_FIN = data_dict["combo"]["combo_ES_fin"]
        COMBO_EP = int(COMBO_EP_DEBUT) + int(COMBO_EP_FIN)
        COMBO_ES = int(COMBO_ES_DEBUT) + int(COMBO_ES_FIN)
        print('[b][color=#c83737]Combo EP : ' + str(COMBO_EP) + '[/color][/b]')
        print('[b][color=#2a4cbc]Combo ES : ' + str(COMBO_ES) + '[/color][/b][/spoiler][/hide]')

def aptitudes():
    def id_aptitude(ID,RANG):
        data = get_data(CHEMIN_ODS)
        NAME = data['Sysco'][21][int(ID)]
        TYPE = data['Sysco'][23][int(ID)]
        VALUE = data['Sysco'][23+int(RANG)][int(ID)]
        if ID == 1 or ID == 2:
            REIRYOKU = int(VALUE) / 2
            with open(CHEMIN_COMBAT_JSON,'r') as json_data:
                data_dict = json.load(json_data)
                EP = data_dict["attributs"]["EP_fin"]
                ES = data_dict["attributs"]["ES_fin"]
                EP = int(REIRYOKU) + int(EP)
                ES = int(REIRYOKU) + int(ES)
                data_dict["attributs"]["EP_fin"] = EP
                data_dict["attributs"]["ES_fin"] = ES
                data_str = json.dumps(data_dict, sort_keys=False, indent=4)
                fichier = open(CHEMIN_COMBAT_JSON,'wt')
                fichier.write(data_str)
                fichier.close()
            print('[*][b]Activation aptitude '+str(NAME)+' niveau '+str(RANG)+'[/b]')
            print('[u]Effet :[/u] '+str(VALUE) + ' ('+str(TYPE)+')')
        if ID == 3 or ID == 4:
            print('[*][b]Activation aptitude '+str(NAME)+' niveau '+str(RANG)+'[/b]')
            print('[u]Effet :[/u] '+str(VALUE) + ' ('+str(TYPE)+')')
        if ID == 5:
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
        if ID == 6:
            with open(CHEMIN_COMBAT_JSON,'r') as json_data:
                data_dict = json.load(json_data)
                POSITIF = data_dict["phase_defensive"]["positif"]
                POSITIF = int(POSITIF) + int(VALUE)
                data_dict["phase_defensive"]["positif"] = POSITIF
                data_str = json.dumps(data_dict, sort_keys=False, indent=4)
                fichier = open(CHEMIN_COMBAT_JSON,'wt')
                fichier.write(data_str)
                fichier.close()
            print('[*][b]Activation aptitude '+str(NAME)+' niveau '+str(RANG)+'[/b]')
            print('[u]Effet :[/u] '+str(VALUE) + ' ('+str(TYPE)+')')
        if ID == 7:
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
    if ETAT_N1 == 1:
        RANG = 1
        id_aptitude(ID_N1,RANG)
    elif ETAT_N2 == 1:
        RANG = 2
        id_aptitude(ID_N2,RANG)
    elif ETAT_N3 == 1:
        RANG = 3
        id_aptitude(ID_N3,RANG)

def calcul_PA_bonus(PA_FIN):
    if PA_FIN > 3:
        PA_FIN = 3
    return PA_FIN


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

    TOTAL_DEFENDU = 0
    TOTAL_SUBI = 0
    NEGATIF_SOMME_FIN = 0
    POSITIF_SOMME_FIN = 0
    PV_FIN = 0
    EP_FIN = 0
    ES_FIN = 0
    PA_FIN = 0
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

    check_maintien()

    print('[*][b]Valeurs négatives :[/b] ' + str(NEGATIF_SOMME_DEBUT))
    print('[*][b]Valeurs positives :[/b] ' + str(POSITIF_SOMME_DEBUT))
    print('[/list][u][b][color=#a2783c]Techniques défensives :[/color][/b][/u]')
    print('[list]')

    techniques_defensives()
    with open(CHEMIN_COMBAT_JSON,'r') as json_data:
        data_dict = json.load(json_data)
        TOTAL_DEFENDU = data_dict["synthese"]["total_defendu"]
        TOTAL_SUBI = data_dict["synthese"]["total_subi"]


    print('[/list]')
    print('[u][b][color=#a2783c]Résumé phase défensive :[/color][/b][/u]')
    print('[list][*][b]Défendu :[/b] ' + str(TOTAL_DEFENDU))
    print('[*][b]Subi :[/b] ' + str(TOTAL_SUBI) + ' [/list]')
    print('[h3][color=#929291]Phase [color=#a23d3c]Offensive[/color][/color][/h3]')
    print('\n')
    print('[u][b][color=#a2783c]Techniques offensives :[/color][/b][/u]')
    print('[list]')

    first_liberation()
    second_liberation()
    techniques_offensives()
    aptitudes()

    with open(CHEMIN_COMBAT_JSON,'r') as json_data:
        data_dict = json.load(json_data)
        TOTAL_SUBI = data_dict["synthese"]["total_subi"]
        EP_FIN = data_dict["attributs"]["EP_fin"]
        ES_FIN = data_dict["attributs"]["ES_fin"]
        PA_FIN = data_dict["attributs"]["PA_restants"]

    PV_FIN = int(PV_DEBUT) - int(TOTAL_SUBI)
    EP_FIN = int(EP_DEBUT) - int(EP_FIN)
    ES_FIN = int(ES_DEBUT) - int(ES_FIN)

    print('[/list]')
    print('[u][b][color=#a2783c]Récapitulatif :[/color][/b][/u]')

    valeur_negatives_positives_somme()

    print('[h3][color=#929291]Stats de[/color] fin de tour[/h3]')
    print('\n')
    print('[b][color=#92d050]Santé : [color=#f9f9f9]' + str(PV_FIN) + '[/color]/' + str(PV_TOTAL) + '[/color][/b]')
    print('[b][color=#c83737]Énergie Physique : [color=#f9f9f9]' + str(EP_FIN) + '[/color]/' + str(EP_TOTAL) + '[/color][/b]')
    print('[b][color=#2a4cbc]Énergie Spirituelle : [color=#f9f9f9]' + str(ES_FIN) + '[/color]/' + str(ES_TOTAL) + '[/color][/b]')
    print('\n')

    PA_BONUS = calcul_PA_bonus(PA_FIN)

    print("[b][color=#783da2]Points d'Action : [color=#f9f9f9]" + str(PA_FIN) + "[/color]/"+str(PA_TOTAL)+"[/color][/b] (+" + str(PA_BONUS) + " PA au prochain tour)")
    print('\n')

    combo_somme_fin()

    clean_json_combat()