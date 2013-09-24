

import urllib2




def readFile(url):
    r=urllib2.urlopen(url)
    return r

def printToFile(fileName,url1,url2=""):

	r=readFile(url1)
	f=open(fileName,'w')
	for line in r:
		words=line.split()
		newline=words[0]+'\n'
		f.write(newline);

	if (url2 == ""):
		return

	q=readFile(url2)
	for line in q:
		words=line.split()
		newline=words[0]+'\n'
		f.write(newline)

	f.close()

def getNames():
	url1="http://deron.meranda.us/data/census-dist-male-first.txt"
	url2="http://deron.meranda.us/data/census-dist-female-first.txt"	
	printToFile("firstNames.txt",url1,url2)

	url3="http://scrapmaker.com/data/wordlists/names/surnames.txt"
	printToFile("lastNames.txt",url3)




if __name__=='__main__':

	getNames()