#!/usr/lib/python3
#coding=UTF-8

import requests
import pandas as pd
import os
import csv
import sys
import pymysql
import json
from pyexcel_ods import get_data

__file__ = 'programme_python.py'
CHEMIN = os.path.dirname(os.path.realpath(__file__))
CHEMIN_CONVERT = CHEMIN.replace('\\','/')

CHEMIN_ODS = str(CHEMIN_CONVERT) + '/Documents/python/BTC/recap_auto/miyu.ods'

def insert_jauges(connection,personnage):
    PV_total = 2100
    EP_total = 1700
    ES_total = 900
    PV_actuel = 2100
    EP_actuel = 1700
    ES_actuel = 900

    try:
        cursor = connection.cursor()
        request = ('SELECT * FROM `jauges` WHERE `personnage` = "' + str(personnage) + '"')
        response = cursor.execute(request)
        connection.commit()
        result = cursor.fetchone()
        print(result[1])

        request = ('UPDATE `jauges` SET `PV_total` = '+ str(PV_total) +
        ', `EP_total` = ' + str(EP_total) +
        ', `ES_total` = ' + str(ES_total) +
        ', `PV_actuel` = ' + str(PV_actuel) +
        ', `EP_actuel` = ' + str(EP_actuel) +
        ', `ES_actuel` = ' + str(ES_actuel) +
        ', `PV_actuel` = ' + str(PV_actuel) +
        ', `PV_actuel` = ' + str(PV_actuel) +
        ' WHERE `personnage` = "' + str(personnage)+ '"')

        response = cursor.execute(request)
        connection.commit()

    except:
        request = ('INSERT INTO `jauges`(`personnage`,`PV_total`,`EP_total`,`ES_total`,`PV_actuel`,`EP_actuel`,`ES_actuel`) VALUES ("'+
            str(personnage) + '",' +
            str(PV_total) + ',' +
            str(EP_total) + ',' +
            str(ES_total) + ',' +
            str(PV_actuel) + ',' +
            str(EP_actuel) + ',' +
            str(Es_actuel) +')')

        response = cursor.execute(request)
        connection.commit()

def insert_repartition(connection,personnage):
    pouvoir = 4
    base = 4
    evolution = 0
    tech_phy = 2
    mains_nues = 0
    armes_cac = 0
    armes_dist = 2
    tech_spi = 0
    energie = 0
    kekkai = 0
    habilete = 3
    vitesse = 0
    resistance = 0
    science = 3
    reiatsu = 0
    camouflage = 0
    detection = 0
    aura = 0
    soin = 3
    regeneration = 3
    guerison = 0

    try:
        cursor = connection.cursor()
        request = ('SELECT * FROM `repartition` WHERE `personnage` = "' + str(personnage) + '"')
        response = cursor.execute(request)
        connection.commit()
        result = cursor.fetchone()
        print(result[1])

        request = ('UPDATE `repartition` SET `pouvoir` = '+ str(pouvoir) +
        ', `base` = ' + str(base) +
        ', `evolution` = ' + str(evolution) +
        ', `tech_phy` = ' + str(tech_phy) +
        ', `mains_nues` = ' + str(mains_nues) +
        ', `armes_cac` = ' + str(armes_cac) +
        ', `armes_dist` = ' + str(armes_dist) +
        ', `tech_spi` = ' + str(tech_spi) +
        ', `energie` = ' + str(energie) +
        ', `kekkai` = ' + str(kekkai) +
        ', `habilete` = ' + str(habilete) +
        ', `vitesse` = ' + str(vitesse) +
        ', `resistance` = ' + str(resistance) +
        ', `science` = ' + str(science) +
        ', `reiatsu` = ' + str(reiatsu) +
        ', `camouflage` = ' + str(camouflage) +
        ', `detection` = ' + str(detection) +
        ', `aura` = ' + str(aura) +
        ', `soin` = ' + str(soin) +
        ', `regeneration` = ' + str(regeneration) +
        ', `guerison` = ' + str(guerison) +
        ' WHERE `personnage` = "' + str(personnage)+ '"')

        response = cursor.execute(request)
        connection.commit()


    except:
        request = ('INSERT INTO `repartition`(`personnage`,`pouvoir`,`base`,`evolution`,`tech_phy`,`mains_nues`,`armes_cac`,`armes_dist`,`tech_spi`,`energie`,`kekkai`,`habilete`,`vitesse`,`resistance`,`science`,`reiatsu`,`camouflage`,`detection`,`aura`,`soin`,`regeneration`,`guerison`) VALUES ("'+
            str(personnage) + '",' +
            str(pouvoir) + ',' +
            str(base) + ',' +
            str(evolution) + ',' +
            str(tech_phy) + ',' +
            str(mains_nues) + ',' +
            str(armes_cac) + ',' +
            str(armes_dist) + ',' +
            str(tech_spi) + ',' +
            str(energie) + ',' +
            str(kekkai) + ',' +
            str(habilete) + ',' +
            str(vitesse) + ',' +
            str(resistance) + ',' +
            str(science) + ',' +
            str(reiatsu) + ',' +
            str(camouflage) + ',' +
            str(detection) + ',' +
            str(aura) + ',' +
            str(soin) + ',' +
            str(regeneration) + ',' +
            str(guerison)+')')

        response = cursor.execute(request)
        connection.commit()

def insert_techniques(connection,personnage):
    cursor = connection.cursor()
    request = ('SELECT * FROM `techniques` WHERE `personnage` = "' + str(personnage) + '"')
    response = cursor.execute(request)
    connection.commit()

    data = get_data(CHEMIN_ODS)
    result = cursor.fetchall()
    NOMBRE_TECH = len(result)
    NOMBRE_TECH_DOC = data['techniques'][1][19]
    a = 1
    b = 0

    if NOMBRE_TECH != 0:
        for i in range(int(NOMBRE_TECH)):
            niveau = data['techniques'][a][0]
            nom = data['techniques'][a][1]
            branche_principale = data['techniques'][a][2]
            branche_secondaire = data['techniques'][a][3]
            depense_EP = data['techniques'][a][4]
            depense_ES = data['techniques'][a][5]
            descriptions = data['techniques'][a][6]
            PT_main = data['techniques'][a][7]
            PT_opt = data['techniques'][a][8]
            cout_PA = data['techniques'][a][9]
            type_main = data['techniques'][a][10]
            type_opt = data['techniques'][a][11]
            if str(niveau) == str(result[b][2]) and str(nom) == str(result[b][3]) and str(branche_principale) == str(result[b][4]) and str(branche_secondaire) == str(result[b][5]) and str(depense_EP) == str(result[b][6]) and str(depense_ES) == str(result[b][7]) and str(descriptions) == str(result[b][8]) and str(PT_main) == str(result[b][9]) and str(PT_opt) == str(result[b][10]) and str(cout_PA) == str(result[b][11]) and str(type_main) == str(result[b][12]) and str(type_opt) == str(result[b][13]):
                pass
            else:
                request = ('UPDATE `techniques` SET `niveau` = '+ str(niveau) +
                ', `nom` = "' + str(nom) +
                '", `branche_principale` = "' + str(branche_principale) +
                '", `branche_secondaire` = "' + str(branche_secondaire) +
                '", `depense_EP` = ' + str(depense_EP) +
                ', `depense_ES` = ' + str(depense_ES) +
                ', `descriptions` = "' + str(descriptions) +
                '", `PT_main` = ' + str(PT_main) +
                ', `PT_opt` = ' + str(PT_opt) +
                ', `cout_PA` = ' + str(cout_PA) +
                ', `type_main` = ' + str(type_main) +
                ', `type_opt` = ' + str(type_opt) +
                ' WHERE `id` = "' + str(result[b][0])+ '"')
                response = cursor.execute(request)
                connection.commit()

            a += 1
            b += 1
        if int(NOMBRE_TECH) < int(NOMBRE_TECH_DOC):
            a = 1
            for i in range(int(NOMBRE_TECH_DOC)):
                if a > int(NOMBRE_TECH):
                    niveau = data['techniques'][a][0]
                    nom = data['techniques'][a][1]
                    branche_principale = data['techniques'][a][2]
                    branche_secondaire = data['techniques'][a][3]
                    depense_EP = data['techniques'][a][4]
                    depense_ES = data['techniques'][a][5]
                    descriptions = data['techniques'][a][6]
                    PT_main = data['techniques'][a][7]
                    PT_opt = data['techniques'][a][8]
                    cout_PA = data['techniques'][a][9]
                    type_main = data['techniques'][a][10]
                    type_opt = data['techniques'][a][11]
                    request = ('INSERT INTO `techniques`(`personnage`,`niveau`,`nom`,`branche_principale`,`branche_secondaire`,`depense_EP`,`depense_ES`,`descriptions`,`PT_main`,`PT_opt`,`cout_PA`,`type_main`,`type_opt`) VALUES ("'+
                        str(personnage) + '",' +
                        str(niveau) + ',"' +
                        str(nom) + '","' +
                        str(branche_principale) + '","' +
                        str(branche_secondaire) + '",' +
                        str(depense_EP) + ',' +
                        str(depense_ES) + ',"' +
                        str(descriptions) + '",' +
                        str(PT_main) + ',' +
                        str(PT_opt) + ',' +
                        str(cout_PA) + ',' +
                        str(type_main) + ',' +
                        str(type_opt) +')')

                    response = cursor.execute(request)
                    connection.commit()
                else:
                    pass
                a += 1

    elif NOMBRE_TECH == 0:
        NOMBRE_TECH = data['techniques'][1][19]
        a = 1
        for i in range(int(NOMBRE_TECH)):
            niveau = data['techniques'][a][0]
            nom = data['techniques'][a][1]
            branche_principale = data['techniques'][a][2]
            branche_secondaire = data['techniques'][a][3]
            depense_EP = data['techniques'][a][4]
            depense_ES = data['techniques'][a][5]
            descriptions = data['techniques'][a][6]
            PT_main = data['techniques'][a][7]
            PT_opt = data['techniques'][a][8]
            cout_PA = data['techniques'][a][9]
            type_main = data['techniques'][a][10]
            type_opt = data['techniques'][a][11]
            request = ('INSERT INTO `techniques`(`personnage`,`niveau`,`nom`,`branche_principale`,`branche_secondaire`,`depense_EP`,`depense_ES`,`descriptions`,`PT_main`,`PT_opt`,`cout_PA`,`type_main`,`type_opt`) VALUES ("'+
                str(personnage) + '",' +
                str(niveau) + ',"' +
                str(nom) + '","' +
                str(branche_principale) + '","' +
                str(branche_secondaire) + '",' +
                str(depense_EP) + ',' +
                str(depense_ES) + ',"' +
                str(descriptions) + '",' +
                str(PT_main) + ',' +
                str(PT_opt) + ',' +
                str(cout_PA) + ',' +
                str(type_main) + ',' +
                str(type_opt) +')')

            response = cursor.execute(request)
            connection.commit()
            a += 1

def insert_aptitudes(connection,personnage):
    cursor = connection.cursor()
    request = ('SELECT * FROM `aptitudes` WHERE `personnage` = "' + str(personnage) + '"')
    response = cursor.execute(request)
    connection.commit()
    data = get_data(CHEMIN_ODS)
    result = cursor.fetchall()
    NOMBRE_TECH = len(result)
    NOMBRE_TECH_DOC = data['aptitudes'][1][8]
    a = 1
    b = 0

    if NOMBRE_TECH != 0:
        for i in range(int(NOMBRE_TECH)):
            niveau = data['aptitudes'][a][0]
            nom = data['aptitudes'][a][1]
            type = data['aptitudes'][a][2]
            description = data['aptitudes'][a][3]
            if str(niveau) == str(result[b][2]) and str(nom) == str(result[b][3]) and str(type) == str(result[b][4]) and str(description) == str(result[b][5]):
                pass
            else:
                request = ('UPDATE `aptitudes` SET `niveau` = '+ str(niveau) +
                ', `nom` = "' + str(nom) +
                '", `type` = "' + str(type) +
                '", `description` = "' + str(description) +
                '" WHERE `id` = "' + str(result[b][0])+ '"')
                response = cursor.execute(request)
                connection.commit()
            a += 1
            b += 1

        if int(NOMBRE_TECH) < int(NOMBRE_TECH_DOC):
            a = 1
            for i in range(int(NOMBRE_TECH_DOC)):
                if a > int(NOMBRE_TECH):
                    niveau = data['aptitudes'][a][0]
                    nom = data['aptitudes'][a][1]
                    type = data['aptitudes'][a][2]
                    description = data['aptitudes'][a][3]
                    request = ('INSERT INTO `aptitudes`(`personnage`,`niveau`,`nom`,`type`,`description`) VALUES ("'+
                        str(personnage) + '",' +
                        str(niveau) + ',"' +
                        str(nom) + '",' +
                        str(type) + ',"' +
                        str(description) +'")')

                    response = cursor.execute(request)
                    connection.commit()
                else:
                    pass
                a += 1

    elif NOMBRE_TECH == 0:
        NOMBRE_TECH = data['aptitudes'][1][8]
        a = 1
        for i in range(int(NOMBRE_TECH)):
            niveau = data['aptitudes'][a][0]
            nom = data['aptitudes'][a][1]
            type = data['aptitudes'][a][2]
            description = data['aptitudes'][a][3]
            request = ('INSERT INTO `aptitudes`(`personnage`,`niveau`,`nom`,`type`,`description`) VALUES ("'+
                str(personnage) + '",' +
                str(niveau) + ',"' +
                str(nom) + '",' +
                str(type) + ',"' +
                str(description) +'")')

            response = cursor.execute(request)
            connection.commit()

            a += 1

def insert_specialites(connection,personnage):
    cursor = connection.cursor()
    request = ('SELECT * FROM `specialites` WHERE `personnage` = "' + str(personnage) + '"')
    response = cursor.execute(request)
    connection.commit()
    result = cursor.fetchall()

    data = get_data(CHEMIN_ODS)
    NOMBRE_TECH = len(result)
    NOMBRE_TECH_DOC = data['specialites'][1][6]
    a = 1
    b = 0

    if NOMBRE_TECH != 0:
        for i in range(int(NOMBRE_TECH)):
            type = data['specialites'][a][0]
            description = data['specialites'][a][1]
            if str(type) == str(result[b][2]) and str(description) == str(result[b][3]):
                pass
            else:
                request = ('UPDATE `aptitudes` SET `type` = '+ str(type) +
                '", `description` = "' + str(description) +
                ' WHERE `id` = "' + str(result[b][0])+ '"')
                response = cursor.execute(request)
                connection.commit()
            a += 1
            b += 1

        if int(NOMBRE_TECH) < int(NOMBRE_TECH_DOC):
            a = 1
            for i in range(int(NOMBRE_TECH_DOC)):
                if a > int(NOMBRE_TECH):
                    type = data['specialites'][a][0]
                    description = data['specialites'][a][1]
                    request = ('INSERT INTO `specialites`(`type`,`description`) VALUES ('+
                        str(type) + ',"' +
                        str(description) +'")')

                    response = cursor.execute(request)
                    connection.commit()
                else:
                    pass
                a += 1

    elif NOMBRE_TECH == 0:
        NOMBRE_TECH = data['aptitudes'][1][6]
        a = 1
        for i in range(int(NOMBRE_TECH)):
            type = data['specialites'][a][0]
            description = data['specialites'][a][1]
            request = ('INSERT INTO `specialites`(`personnage`,`type`,`description`) VALUES ("'+
                str(personnage) + '",' +
                str(type) + ',"' +
                str(description) +'")')

            response = cursor.execute(request)
            connection.commit()

            a += 1

def insert_liberation(connection,personnage):
    data = get_data(CHEMIN_ODS)
    seconde_liberation = data['liberation'][1][0]
    nom = data['liberation'][1][1]
    branche_principale = data['liberation'][1][2]
    branche_secondaire = data['liberation'][1][3]
    depense_EP = data['liberation'][1][4]
    depense_ES = data['liberation'][1][5]
    descriptions = data['liberation'][1][6]
    PT_main = data['liberation'][1][7]
    PT_opt = data['liberation'][1][8]
    cout_PA = data['liberation'][1][9]
    type_main = data['liberation'][1][10]
    type_opt = data['liberation'][1][11]
    try:
        cursor = connection.cursor()
        request = ('SELECT * FROM `liberation` WHERE `personnage` = "' + str(personnage) + '"')
        response = cursor.execute(request)
        connection.commit()
        result = cursor.fetchone()
        print(result[1])

        request = ('UPDATE `liberation` SET `seconde_liberation` = '+ str(seconde_liberation) +
        ', `nom` = "' + str(nom) +
        '", `branche_principale` = "' + str(branche_principale) +
        '", `branche_secondaire` = "' + str(branche_secondaire) +
        '", `depense_EP` = ' + str(depense_EP) +
        ', `depense_ES` = ' + str(depense_ES) +
        ', `description` = "' + str(descriptions) +
        '", `PT_main` = ' + str(PT_main) +
        ', `PT_opt` = ' + str(PT_opt) +
        ', `cout_PA` = ' + str(cout_PA) +
        ', `type_main` = ' + str(type_main) +
        ', `type_opt` = ' + str(type_opt) + '')

        response = cursor.execute(request)
        connection.commit()

    except:
        request = ('INSERT INTO `liberation`(`personnage`,`seconde_liberation`,`nom`,`branche_principale`,`branche_secondaire`,`depense_EP`,`depense_ES`,`description`,`PT_main`,`PT_opt`,`cout_PA`,`type_main`,`type_opt`) VALUES ("'+
            str(personnage) + '","' +
            str(seconde_liberation) + '","' +
            str(nom) + '","' +
            str(branche_principale) + '","' +
            str(branche_secondaire) + '",' +
            str(depense_EP) + ',' +
            str(depense_ES) + ',"' +
            str(descriptions) + '",' +
            str(PT_main) + ',' +
            str(PT_opt) + ',' +
            str(cout_PA) + ',' +
            str(type_main) + ',' +
            str(type_opt) +')')

        response = cursor.execute(request)
        connection.commit()


    cursor = connection.cursor()
    request = ('SELECT * FROM `liberation` WHERE `personnage` = "' + str(personnage) + '"')
    response = cursor.execute(request)
    connection.commit()
    result = cursor.fetchall()

    data = get_data(CHEMIN_ODS)
    a = 1
    b = 0


if __name__=='__main__':

    HOST_NAME = "fic-ex-machina.fr"
    USER_NAME = "amaury"
    PASSWORD_DB = "SvgW58"
    DB_NAME = "PJ"

    connection = pymysql.connect(host=HOST_NAME,
        user=USER_NAME,
        password=PASSWORD_DB,
        db=DB_NAME,
        port=3306,
        autocommit=True)

    personnage = "Serizawa Miyu"

    insert_jauges(connection,personnage)
    insert_repartition(connection,personnage)
    insert_techniques(connection,personnage)
    insert_aptitudes(connection,personnage)
    insert_specialites(connection,personnage)
    insert_liberation(connection,personnage)