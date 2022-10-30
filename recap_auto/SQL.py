#!/usr/lib/python3
#coding=UTF-8

import requests
import pandas as pd
import os
import csv
import sys
import pymysql
import json

HOST_NAME = "fic-ex-machina.fr"
USER_NAME = "amaury"
PASSWORD_DB = "SvgW58"
DB_NAME = "combo"

connection = pymysql.connect(host=HOST_NAME,
    user=USER_NAME,
    password=PASSWORD_DB,
    db=DB_NAME,
    port=3306,
    autocommit=True)

cursor = connection.cursor()
request = ('INSERT INTO `combo`(`seuil_EP`, `seuil_ES`, `valeur`, `valeur_maitien`, `effet_principal`) VALUES ("'
                       + str(350) +','+ str(150) +','+ str(200) +','+ str(0) +',"'+ str("entrave") +'")')
response = cursor.execute(request)
connection.commit()

