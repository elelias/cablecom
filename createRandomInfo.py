import sys
import random as rd
from getNames import *
from costDictionary import *
from insertIntoDB import *
from getConnectionToDB import *
from createDataBase_upc import *

def chooseTV():

	myR=rd.randint(0,10)

	if myR<5:
		return "HorizonComfort"
	elif myR<8:
		return "HorizonClassic"
	elif myR <=10:
		return "HorizonCompact"
	else:
		print "something went wrong with the random number in chooseTV"

def chooseInternet():

	myR=rd.randint(0,10)
	if myR<3:
		return "Internet150"
	elif myR<9:
		return "Internet75"
	elif myR==9:
		return "Internet35"
	elif myR==10:
		return "Internet10"
	print "something went wrong with the random number in chooseInternet"




def choosePhone():
	myR=rd.randint(0,10)
	if myR<6:
		return "Global"
	elif myR<8:
		return "Swiss"		
	elif myR<=10:
		return "Weekend"
	else:
		print "something went wrong with the random number in choosePhone"			



def chooseBundle():

	myR=rd.randint(0,2)

	if myR==0:
		return "SuperCombi"
	elif myR==1:
		return "PlusCombi"		
	elif myR==2:
		return "StartCombi"		
	else:
		print "something went wrong with the random number in chooseBundle"


def createNameList():

	#maxSize=2000

	fNames=open('firstNames.txt','r')
	lNames=open('lastNames.txt','r')	

	listFirstNames=[]
	listLastNames=[]

	for line in fNames.read().splitlines():
		listFirstNames.append(line)

	for line in lNames.read().splitlines():
		listLastNames.append(line)		
	#
	#
	#
	#
	#print 'the sizes of lists',len(listFirstNames)
	return listFirstNames,listLastNames

def createStreetNameList():

	streetNameList=[]
	sList=open('new-york.osm.streets.txt','r')
	for line in sList.read().splitlines():
		streetNameList.append(line)
		#
	return streetNameList




def createRandomInfo(recordLength):
	'''creates random entries for a database'''

	costDictionary=getCostDictionary()
	productID=getProductID()
	listFirstNames,listLastNames=createNameList()
	streetNameList=createStreetNameList()
	rd.shuffle(listFirstNames)
	rd.shuffle(listLastNames)	
	rd.shuffle(streetNameList)



	clientID=0


	for k in range(recordLength):


		serviceNumbers=[1,2,3,10,11,12,20,21,22,23,30,31,32]
		clientID+=1
		try:
			name=listFirstNames.pop()

		except IndexError:
			print 'the list of first names is now emtpy, exiting...'
			sys.exit()
		surname=listLastNames.pop()
		street=streetNameList.pop()
		streetNumber=rd.randint(1,400)

		iterList=[name,surname,street]
		for i,item in enumerate(iterList):
			if len(item)>=40:
				iterList[i]=iterList[i][0:39]
		name=iterList[0]
		surname=iterList[1]
		street=iterList[2]
			
		#
		#
		#
		

		#CLIENT ID TABLE
		clientIDDict={'clientID':clientID,'name':name,'surname':surname}
		insertIntoTable('clientID',clientIDDict,con)


		#CLIENT IMMUTABLE INFORMATION TABLE
		city='London'
		country='UK'

		yearBornOK=True
		while yearBornOK:
			yearBorn=int(rd.gauss(1980, sigma=30));
			if yearBorn > 1995.:
				yearBornOK=True
			else:
				yearBornOK=False
		#
		monthBorn = rd.randint(1,12)
		maxday=0
		if monthBorn in [1,3,5,7,8,10,12]:
			maxday=31
		elif monthBorn in [4,6,9,11]:
			maxday=30
		else:
			maxday=28
		dayBorn=rd.randint(1,maxday)
		dateBirth=unicode(yearBorn)+'-'+unicode(monthBorn)+'-'+unicode(dayBorn)

		#
		#
		clientImmutable={'clientID':clientID,'city':city,'country':country,'birthdate':dateBirth}
		insertIntoTable('clientImmutables',clientImmutable,con)


		#get a random number service
		rd.shuffle(serviceNumbers)
		serviceCode=serviceNumbers.pop()
		comInfoDict={'clientID':clientID,'serviceCode':serviceCode}
		insertIntoTable('clientCommercialInfo',comInfoDict,con)		


	myR=rd.randint(0,len(listFirstNames)-1)
	rdFirstName=listLastNames




def fillServiceInfo():

	for a in [1,2,3,10,11,12,20,21,22,23,30,31,32]:

		productNameDict=getProductName()
		productName=productNameDict[a]
		costDictionary=getCostDictionary()
		serviceInfoDic={}

		serviceInfoDic['serviceCode']=a
		serviceInfoDic['serviceName']=productName
		serviceInfoDic['serviceCost']=costDictionary[productName]

		if a in [1,2,3,30,31,32]:
			serviceInfoDic['includesPhone']= 1
		else:
			serviceInfoDic['includesPhone']=0

		if a in [1,2,3,20,21,22,23]:
			serviceInfoDic['includesInternet']= 1
		else:
			serviceInfoDic['includesInternet']=0			

		if a in [1,2,3,10,11,12,13]:
			serviceInfoDic['includesTV']= 1
		else:
			serviceInfoDic['includesTV']=0						


		insertIntoTable('serviceInfo',serviceInfoDic,con)


def deleteTables():
		sqlstring='DROP TABLE IF EXISTS clientID,clientMutables,clientImmutables,clientCommercialInfo,serviceInfo'
		print 'removing tables if they exist '
		print 'if they dont, a warning will pop up'
		executeQuery(con,sqlstring)
		print 'creating them again'
		createTables()

if __name__=='__main__':

	if len(sys.argv)>1:
		recordLength=sys.argv[1]
	else:
		recordLength=3200

	global con
	con=getConnectionToDataBase()

	deleteTables()

	fillServiceInfo()
	createRandomInfo(recordLength)	

