#!/bin/env python

import requests
from qrtools import QR

r = requests.get("http://challenges.hackvent.hacking-lab.com:4200")
if r.status_code==200:
		print r.data
		
		qr1 = QR(data=r.data)
		qr1.decode()
		if "HV17" in qr1.data:
			print qr1.data
	