""" ***********************************************************************************************************
	This code uses selenium, beautifulSoup, chrome webdriver, and a chrome extension named xpathfinder extension.
	To use this code you should install them all. 
	The purpose of this code is to scrap a website given by the user. First of all, the user to gives a string 
	containing a website url that he wants to be scraped. In case of success a chrome webdriver will be opened 
	with a tab containing the user' s chosen website. Then the user should activate the xpathfinder plug_in 
	just by clicking the icon. At the end, the user selects the parts he wants to scrap.
	*********************************************************************************************************** """


from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


pathToXpathFinderExtension = r"C:\Users\HP\Desktop\xPath-Finder_v0.9.3.crx" 				#variable containing the path of the xpathfinder extension on my PC!
pathToWebDriver = r"C:\Users\HP\Desktop\chromedriver.exe"									#variable containing the path of chrome Webdriver on my pc!
waitTime = 120																				#this variable decides the number of seconds the webdriver will wait before closing.

chop = webdriver.ChromeOptions()
chop.add_extension(pathToXpathFinderExtension) 												#adding the pathfinder extension.
driver = webdriver.Chrome(pathToWebDriver,chrome_options=chop) 								#opening the webdriver with the xpathfinder extension installed
driver.get("https://www.bloomberg.com/markets/currencies")
try:
	element = WebDriverWait(driver,waitTime).until(EC.presence_of_element_located((By.ID,"xpath-content"))) #this instruction will wait for the user to select an element for 2 minutes then it will close
	selectedXpath = driver.find_element(By.ID, "xpath-content").text
	print(selectedXpath)
	selector =driver.find_element(By.XPATH, selectedXpath)
	print (selector)
finally:
	driver.close()
	

