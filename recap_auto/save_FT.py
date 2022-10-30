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
    Es_actuel = 900

    try:
        cursor = connection.cursor()
        request = ('SELECT `personnage` FROM `jauges` WHERE `personnage` = "' + str(personnage) + '"')
        response = cursor.execute(request)
        connection.commit()
        result = cursor.fetchone()
        print(result[0])

    except:
        request = ('INSERT INTO `jauges`(`personnage`,`PV_total`,`EP_total`,`ES_total`,`PV_actuel`,`EP_actuel`,`Es_actuel`) VALUES ("'+
            str(personnage) + '",' +
            str(PV_total) + ',' +
            str(EP_total) + ',' +
            str(ES_total) + ',' +
            str(PV_actuel) + ',' +
            str(EP_actuel) + ',' +
            str(Es_actuel) +')')

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

