from bs4 import BeautifulSoup
from XPathGettingWithBS import getBsObjectWithSelenium
from XPathGettingWithBS import xpathToBSObj
from XPathGettingWithBS import AbsolutePathForXpath

"""tag1= xpathToBSObj("/html/body/div[5]/main/div/div/div[3]/div[4]/div/table/tbody/tr[1]/td[1]/a/div[2]",bsObj)
tag2= xpathToBSObj("/html/body/div[5]/main/div/div/div[3]/div[4]/div/table/tbody/tr[1]/td[2]",bsObj)"""

def CoordinateOfLastSimilarity(xpath1, xpath2):
	minLength = min(len(xpath1),len(xpath2))
	lastSimilarityPos =0
	preLastSimilarityPos =0
	for i in range(0,minLength):
		if(xpath1[i] == xpath2[i]):
			if(xpath1[i]== '/'):
				preLastSimilarityPos = lastSimilarityPos
				lastSimilarityPos=i
		else:
			return(preLastSimilarityPos, lastSimilarityPos)
	return preLastSimilarityPos,lastSimilarityPos
	
def getListOfUnclesXpaths(xpath1,xpath2,bsObj,preLastSimilarityPos,lastSimilarityPos):
	# = CoordinateOfLastSimilarity(xpath1,xpath2)
	parentTag = xpath1[preLastSimilarityPos+1:lastSimilarityPos] #parent tag mean here the first tag commune to both xpaths
	bracketPos = parentTag.find('[')
	if( bracketPos != -1):
		parentTag= parentTag[:bracketPos]
	print(parentTag)
	grandParentXpath = xpath1[:preLastSimilarityPos]
	print(grandParentXpath)
	grandParentbsObj = xpathToBSObj(grandParentXpath,bsObj)
	numberOfUncles =len(list(grandParentbsObj.findAll(parentTag,recursive= False))) #this will give the number of siblings of the parent tag
	print(numberOfUncles)
	listOfUnclesXpaths = []
	for i in range(numberOfUncles):
		uncleXpath= grandParentXpath + "/" + parentTag + "[" + str(i+1) + "]"
		listOfUnclesXpaths.append(uncleXpath)
	return listOfUnclesXpaths
	
def getListOfSiblingsXpaths(xpath1,xpath2,bsObj):
	preLastSimilarityPos,lastSimilarityPos = CoordinateOfLastSimilarity(xpath1,xpath2)
	listOfUnclesXpaths = getListOfUnclesXpaths(xpath1,xpath2,bsObj,preLastSimilarityPos,lastSimilarityPos)
	while(len(listOfUnclesXpaths)==1 and preLastSimilarityPos != 0):
		lastSimilarityPos = preLastSimilarityPos
		for i in range(lastSimilarityPos-1,-1,-1):
			if(xpath1[i] == '/'):
				preLastSimilarityPos = i
				break
		listOfUnclesXpaths = getListOfUnclesXpaths(xpath1,xpath2,bsObj,preLastSimilarityPos,lastSimilarityPos)
	tag1UniqueXpath = xpath1[lastSimilarityPos:]
	tag2UniqueXpath = xpath2[lastSimilarityPos:]
	listOfSiblings1Xpaths = []
	listOfSiblings2Xpaths = []
	for x in listOfUnclesXpaths:
		siblingXpath1 = x+ tag1UniqueXpath
		siblingXpath2 = x+ tag2UniqueXpath
		listOfSiblings1Xpaths.append(siblingXpath1)
		listOfSiblings2Xpaths.append(siblingXpath2)
	return(listOfSiblings1Xpaths,listOfSiblings2Xpaths)
	

bsObj =getBsObjectWithSelenium("https://markets.wsj.com/")
xpath1 ="/html/body/div[4]/div/div[4]/div/div/div[2]/table/tbody/tr[1]/td[1]/a"
xpath2 = '/html/body/div[4]/div/div[4]/div/div/div[2]/table/tbody/tr[1]/td[2]'
xpath1 = AbsolutePathForXpath(xpath1,bsObj)
xpath2 = AbsolutePathForXpath(xpath2,bsObj)
	
(tag1ListOfXpths ,tag2ListOfXpaths) =getListOfSiblingsXpaths(xpath1,xpath2,bsObj)
print(tag1ListOfXpths)
for x,y in zip(tag1ListOfXpths,tag2ListOfXpaths):
	data = xpathToBSObj(x,bsObj)
	value = xpathToBSObj(y,bsObj)
	if(data and value):
		print(data.get_text(),value.get_text())
	
		
"""parentOfTag1 =tag1.parents
parentOfTag2 =tag2.parents
parentOfTag1 = [x.name for x in parentOfTag1]
parentOfTag2 = [x.name for x in parentOfTag2]
communeBranch =[]
length1 = len(parentOfTag1)
length2 = len(parentOfTag2)
minLength = min(length1,length2)
endOfCommuneBranch = minLength
stillCommuneTree = True
for i in range(minLength):
	if( stillCommuneTree):
		if(parentOfTag1[length1-1-i] == parentOfTag2[length2-1-i]):
			communeBranch.append(parentOfTag1[length1-1-i])
		else:
			stillCommuneTree = False
			endOfCommuneBranch=i 
	else:
		break

tag1UniqueBranch =[parentOfTag1[i] for i in range(length1-1-endOfCommuneBranch,0,-1)]
tag2UniqueBranch =[parentOfTag2[i] for i in range(length2-1-endOfCommuneBranch,0,-1)]
print(tag1UniqueBranch)
print(tag2UniqueBranch)
print(communeBranch)	"""
	
