

import MySQLdb as mdb

def getConnectionToDataBase():
	con = mdb.connect('localhost', 'root', '123123123', 'toydatabase',charset='utf8');
	with con:
		return con