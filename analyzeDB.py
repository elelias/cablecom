from getConnectionToDB import *
from costDictionary import *
from insertIntoDB import *
import datetime as dt
def analyzeDB(con):

	'''analyzes the DB which was randomly generated'''


	#QUERIES
	#1 what is the total number of people who are using Horizon Comfort?
	serviceCodeDict=getProductID()
	serviceID=serviceCodeDict['HorizonComfort']
	sqlstring='SELECT count(*) FROM  clientCommercialInfo WHERE serviceCode='+unicode(serviceID)
	print ''	
	print 'NEW QUERY'
	print '     going to execute the query ->'+sqlstring
	print ''	

	result = executeQuery(con,sqlstring)
	print 'total number of people using Horizon Comfort ',result[0][0]

	#2) what is the proportion of people using only a phone service?
	sqlstring='SELECT (count(*)*100/ (select count(*) from clientCommercialInfo)) FROM clientCommercialInfo '\
		+'WHERE serviceCode>=30'
	print ''
	print 'NEW QUERY'
	print '     going to execute the query ->'+sqlstring
	print ''		

	result = executeQuery(con,sqlstring)
	print 'proportion of people only using a phone service ',unicode(result[0][0])+'%'

	#3) what is the average ages of people using only different services?"
	#3.1 a combi:
	sqlstring='SELECT birthDate FROM clientImmutables,clientCommercialInfo WHERE '+\
	'clientImmutables.clientID=clientCommercialInfo.clientID and serviceCode<20'
	print ''	
	print 'NEW QUERY'
	print '     going to execute the query ->'+sqlstring
	print ''
	result = executeQuery(con,sqlstring)
	days=0	
	for element in result:
		days=days+(dt.date.today()-element[0]).days
		#print element

	print "average age of combi users ",float(days/len(result) / (365.))


	#3.2 only TV:
	sqlstring='SELECT birthDate FROM clientImmutables,clientCommercialInfo WHERE '+\
	'clientImmutables.clientID=clientCommercialInfo.clientID and serviceCode>=10 '+\
	'and serviceCode<20'
	print ''	
	print 'NEW QUERY'
	print '     going to execute the query ->'+sqlstring
	print ''
	result = executeQuery(con,sqlstring)
	days=0	
	for element in result:
		days=days+(dt.date.today()-element[0]).days
		#print element
	print "average age of only TV users", float(days/len(result) / (365.))


	#average income of of clients younger than 40 years old with a combi subscription
	today=dt.date.today()
	referenceDate=dt.date(today.year-40,today.month,today.day)

	sqlstring='SELECT P.serviceCost FROM '+\
	'(SELECT serviceCode,clientImmutables.clientID FROM clientCommercialInfo,clientImmutables '+\
	'WHERE clientCommercialInfo.clientID=clientImmutables.clientID) as S, '+\
	'serviceInfo as P, '+\
	'(SELECT clientID FROM clientImmutables WHERE birthDate >\"'+unicode(referenceDate)+'\") as Q '+\
	'WHERE P.serviceCode=S.serviceCode and '+\
	'Q.clientID=S.clientID'

	print ''	
	print 'NEW QUERY'
	print '     going to execute the query ->'+sqlstring
	print ''
	cost=0.
	result = executeQuery(con,sqlstring)
	for element in result:
		cost+=element[0]
	print "average revenue from combi users younger than 40", float(cost/len(result))


if __name__=='__main__':


	#GET THE CONNECTION TO THE DATA BASE
	#global con
	con=getConnectionToDataBase()

	#ANALYZE THE DATABASE
	analyzeDB(con)




