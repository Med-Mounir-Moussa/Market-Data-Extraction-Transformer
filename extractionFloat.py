from bs4 import BeautifulSoup
def extraction_float(data):
    numbers = []
    keys = []
    results = []
    if (data.get_text() == ""):
        attributes = data.attrs
        for key in attributes:
            try:
                result = float(attributes[key])
                numbers.append(result)
                keys.append(key)
            except:
                res = False         
        for i in range (0,len(keys)):
            results.append((keys[i],numbers[i]))                        
        return (results)
    else:
        return (data.get_text())
                
        
