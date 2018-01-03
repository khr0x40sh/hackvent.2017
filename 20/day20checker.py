#!/usr/bin/env python

import urllib2
import base64
import time

xor_key = [0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF]

def xor(target): return ''.join([chr(ord(target[i])^xor_key[i%len(xor_key)]) for i in range(len(target))])

nonce = ''

try:
    nonce = urllib2.urlopen(base64.b64decode('aHR0cDovL2NoYWxsZW5nZXMuaGFja3ZlbnQuaGFja2luZy1sYWIuY29tOjgwODEvP25vbmNl')).read() #http://challenges.hackvent.hacking-lab.com:8081/?nonce
    nonce = base64.b64decode(nonce)	#uijNuGfUWL8IPIDlCNzUvVtD6MhtPHy/SfctKd50
    nonce = xor(nonce) #'\xab\n\xfe\xfc2\xb2/7\x91\x96;)\xd52+\xacyp\xac\x9d\x0bK\xf4&\xe3L\xe1\xf40\x8b'
    nonce = base64.b64encode(nonce) #'qwr+/DKyLzeRljsp1TIrrHlwrJ0LS/Qm40zh9DCL'
except: pass

time.sleep(2)

try:
    urllib2.urlopen(base64.b64decode('aHR0cDovL2NoYWxsZW5nZXMuaGFja3ZlbnQuaGFja2luZy1sYWIuY29tOjgwODEvP25vbmNl'), data='nonce=' + nonce).read()	#ePOUSqikyg3tY+Ts7pC2IDcklgMaFiq9h3KTkrru
except:
    pass
