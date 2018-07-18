from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib2 import urlopen
from bs4 import BeautifulSoup
from XPathGettingWithBS import xpathToBSObj
pathToWebDriver = r"C:\Users\USER\Downloads\chromedriver_win32\chromedriver.exe"
def x_path_to_data(url,x_path):
    driver = webdriver.Chrome(pathToWebDriver)
    driver.get(url)
    page = driver.page_source
    bsObj = BeautifulSoup(page)
    result = xpathToBSObj(x_path,bsObj)
    dad = result
    while (dad.name != 'table') :
        dad = dad.parent    
    tag = result.name
    attributes = result.attrs
    data = bsObj.find('table',dad.attrs).findAll(tag,attributes)    
    for information in data:
        print (information.get_text())    
    driver.close()
    return data
    
