#
#
#
import sys
import MySQLdb as mdb
from getConnectionToDB import *


def createTables():
	'''creates the test table if it doesn't exist'''

	global con
	con=getConnectionToDataBase()
	with con:
		cur=con.cursor()
		sqlstring='CREATE TABLE IF NOT EXISTS clientID('
		sqlstring+='clientID BIGINT NOT NULL PRIMARY KEY, '			
		sqlstring+='name VARCHAR(40), '
		sqlstring+='surname VARCHAR(40),'
		sqlstring+='created TIMESTAMP DEFAULT NOW() '
		sqlstring+=');'
		print sqlstring
		cur.execute(sqlstring)
		rows=cur.fetchone()
		print rows

		sqlstring='CREATE TABLE IF NOT EXISTS clientMutables('	
		sqlstring+='clientID BIGINT NOT NULL, '							
		sqlstring+='street VARCHAR(40), '
		sqlstring+='number INT(20), '	
		sqlstring+='created TIMESTAMP DEFAULT NOW() '		
		sqlstring+=');'
		print sqlstring
		cur.execute(sqlstring)
		rows=cur.fetchone()
		print rows

		sqlstring='CREATE TABLE IF NOT EXISTS clientImmutables('	
		sqlstring+='clientID BIGINT NOT NULL, '							
		sqlstring+='birthDate DATE, '
		sqlstring+='city VARCHAR(40), '		
		sqlstring+='country VARCHAR(40), '				
		sqlstring+='created TIMESTAMP DEFAULT NOW() '		
		sqlstring+=');'
		print sqlstring
		cur.execute(sqlstring)
		rows=cur.fetchone()
		print rows		

		sqlstring='CREATE TABLE IF NOT EXISTS clientCommercialInfo('	
		sqlstring+='clientID BIGINT NOT NULL, '
		sqlstring+='serviceCode SMALLINT, '		
		sqlstring+='created TIMESTAMP DEFAULT NOW() '		
		sqlstring+=');'
		print sqlstring
		cur.execute(sqlstring)
		rows=cur.fetchone()
		print rows


		sqlstring='CREATE TABLE IF NOT EXISTS serviceInfo('	
		sqlstring+='serviceCode SMALLINT NOT NULL PRIMARY KEY, '			
		sqlstring+='serviceName VARCHAR(20), '
		sqlstring+='serviceCost REAL, '
		sqlstring+='includesPhone SMALLINT, '		
		sqlstring+='includesInternet SMALLINT, '				
		sqlstring+='includesTV SMALLINT, '						
		sqlstring+='created TIMESTAMP DEFAULT NOW() '
		sqlstring+=');'


		print sqlstring
		cur.execute(sqlstring)
		rows=cur.fetchone()
		print rows


if __name__=='__main__':
	createTables()
