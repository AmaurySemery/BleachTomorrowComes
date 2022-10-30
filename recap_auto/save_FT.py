#!/usr/lib/python3
#coding=UTF-8

import requests
import pandas as pd
import os
import csv
import sys
import pymysql
import json



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

if __name__=='__main__':

    HOST_NAME = "fic-ex-machina.fr"
    USER_NAME = "amaury"
    PASSWORD_DB = "XXXX"
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

