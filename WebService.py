# -*- coding: cp1252 -*-
from flask import Flask, request
from PutInDatabase import put_data_in_database
from pymongo import MongoClient
import pprint
from XPathGettingWithBS import getBsObjectWithSelenium
from XPathGettingWithBS import AbsolutePathForXpath
from SiblingsTags import getListOfSiblingsXpaths
app = Flask('__main__')


@app.route('/api/G', methods=['GET'])
def afficher_dataBase():
    client = MongoClient('localhost',27017)
    dataBase = client.stage14
    l=""
    for post in dataBase.posts.find():
        for key in post:
            if (key != '_id'):
                l=l+post[key]+'\n'
    print(l)
    return(l)

@app.route('/api/P', methods=['POST'])
def traiter_donnees():
    print(request.data)
    url=request.json['url']
    xpath1=request.json['XPATH1']
    xpath2=request.json['XPATH2']
    print(url,xpath1,xpath2)
    client = MongoClient('localhost',27017)
    dataBase = client.stage14
    bsObj = getBsObjectWithSelenium(url)
    xpath_1 = AbsolutePathForXpath(xpath1,bsObj)
    xpath_2 = AbsolutePathForXpath(xpath2,bsObj)
    (tag1ListOfXpaths ,tag2ListOfXpaths) = getListOfSiblingsXpaths(xpath_1,xpath_2,bsObj)
    put_data_in_database(tag1ListOfXpaths, tag2ListOfXpaths,bsObj, dataBase)
    return ("good Job")

app.run()


   

