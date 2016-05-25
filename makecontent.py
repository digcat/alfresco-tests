#!/usr/bin/python
import sys
import simplejson as json
import time
from cmislib.model import CmisClient, Repository

if len(sys.argv) != 5:
	print "Syntax: makecontent.py <hostname> <foldername> <numofiterations> <doupdate>"
	print "eg: python makecontent.py http://localhost:8080/alfresco/cmisatom site1 100 Y"
	sys.exit()

hostname = sys.argv[1]
rootfoldername = sys.argv[2] 
iterations = int(sys.argv[3])
doupdate = sys.argv[4]

weprep = ""
weprep = weprep + "<style>"
weprep = weprep + "   table, th, td { border: 1px solid black; }"
weprep = weprep + "   .forat { border: 1px solid blue; }"
weprep = weprep + "</style>"
weprep = weprep + "<hr>"
	
body = "What is Lorem Ipsum?<br> Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

ftab = "<table width=500 height=30 border=2>"
ftab = ftab + "<tr>"
ftab = ftab + "<td>HoneyComb Alfresco</td><td>https://www.orderofthebee.org<br>marsbard and www.digcat.com</td><td>HoneyComb Open Source</td><td>1</td>"
ftab = ftab + "</tr>"
ftab = ftab + "<tr>"
ftab = ftab + "<td colspan=4>" + body + "</td>"
ftab = ftab + "</tr>"
ftab = ftab + "</table>"
weprep = weprep + ftab

cmurl = hostname
client = CmisClient(cmurl,'admin','admin')

sitename =  'swsdp'
basepath = '/Sites/' + sitename + '/documentLibrary'
rootofwn = basepath + '/' + rootfoldername
repo = client.defaultRepository

try:
	rootsite = repo.getObjectByPath(rootofwn)
except:	
	rootsite = repo.getObjectByPath(basepath)
	basefolder = rootsite.createFolder(rootfoldername)
	try:
		rootsite = repo.getObjectByPath(rootofwn)
	except:	
		print "Error: Unable to create folder"

rootfolder = repo.getObjectByPath(rootofwn)
props = rootfolder.getProperties()

#for k,v in props.items():
#  	print '%s:%s' % (k,v)

listofdocs = []
foundDocCnt = 0

for x in range(0,iterations):
 	docname = "Datavis-" + str(time.clock()) + ".html"
	try:
		newdoc = repo.createDocumentFromString(docname, parentFolder=rootfolder, contentString=weprep, contentType='text/html')
		props = newdoc.getProperties()
		listofdocs.append(docname)
		#for k,v in props.items():
		#	print '%s:%s' % (k,v)
	except:
                foundDocCnt = foundDocCnt + 1
print rootfoldername + "=" + str(foundDocCnt)

if doupdate == "Y":
	for doc in listofdocs:
		name = doc
		querySimpleSelect = "SELECT * FROM cmis:document where cmis:name like '" + name + "'"
		resultSet = repo.query(querySimpleSelect)
		for result in resultSet:
			#print result.name 
		
			if (result.name == name):
				props = result.properties	
				#for k,v in props.items():
				#	print '%s:%s' % (k,v)
				newprop = { 'cmis:description': 'some new description'} 
				doc = repo.getObjectByPath(rootofwn + '/' + result.name)	
				doc.updateProperties(newprop)


time.sleep(15)

rootfolder = repo.getObjectByPath(rootofwn)

if doupdate != "Y":
	try:
		rootfolder.deleteTree()
	except:
		print "Cant Delete might be timing, lets wait for 30s and try again"
		time.sleep(15)
		try:
			rootfolder.deleteTree()
		except:
			print "Still cant delete after 30s wait"
