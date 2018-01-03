import requests
import time

#cookie = { "ad0388922ef2297679023cc0f95111bcab9d1245":"88e83c6e2bc89bdb9ec13c72ee3dbe88e004c5a4058b56c400458b33070f82e5", "session":"eyJsb2dnZWRpbiI6InllcyJ9.DSaMTg.fJzPWd5eSCGfHNQphAGB3fKn9d0"}
keywords = ['this_pw_is_so_eleet', 'khr0x40sh']

url = "http://challenges.hackvent.hacking-lab.com:8081/"
#for i in xrange(len(keywords)):
while(True):
	data = {'password': keywords[0] }
	r = requests.post(url, data)
	print r.status_code
	print r.cookies
	print r.text
	cookie=r.cookies
	data = {'twitter_name': 'khr0x40sh' }
	r = requests.post(url, data, cookies=cookie)
	print r.status_code
	
	print r.text
		
	print "#"*30
	time.sleep(6)
	