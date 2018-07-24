# -*- coding: cp1252 -*-
from flask import Flask, request
from PutInDatabase import put_data_in_database
from pymongo import MongoClient
import pprint
import json

app = Flask('__main__')
client = MongoClient('localhost',27017)
dataBase = client.stage6


@app.route('/G', methods=['GET'])
def afficher_dataBase():
    l=""
    for post in dataBase.posts.find():
        for key in post:
            if (key != '_id'):
                l=l+post[key]+'\n'
    return(l)

@app.route('/P', methods=['POST'])
def traiter_donnees(url,xpath1,xapth2):    
    bsObj = getBsObjectWithSelenium(url)
    xpath1 = AbsolutePathForXpath(xpath1,bsObj)
    xpath2 = AbsolutePathForXpath(xpath2,bsObj)
    (tag1ListOfXpaths ,tag2ListOfXpaths) = getListOfSiblingsXpaths(xpath1,xpath2,bsObj)
    put_in_data_base(tag1ListOfXpaths, tag2ListOfXpaths, dataBase)
    return dataBase
app.run()



   

