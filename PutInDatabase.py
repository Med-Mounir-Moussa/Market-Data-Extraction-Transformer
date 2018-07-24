from pymongo import MongoClient
def put_data_in_database(tag1ListOfXpths,tag2ListOfXpaths,dataBase):    
    posts = dataBase.posts
    for x,y in zip(tag1ListOfXpths,tag2ListOfXpaths):
            data = xpathToBSObj(x,bsObj)
            value = xpathToBSObj(y,bsObj)
            if(data and value):                
                    print(data.get_text(),extraction_float(value))
                    post = {"taux de change":extraction_float(value),"monnaies":data.get_text()}
                    posts.insert_one(post)
    return dataBase
