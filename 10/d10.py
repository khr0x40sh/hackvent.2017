import socket
import time

C4_SERVER = ('challenges.hackvent.hacking-lab.com', 1037)
RECV_SIZE = 4096

conn = socket.create_connection(C4_SERVER)
response = conn.recv(RECV_SIZE)
count = 0
round = 1
moves = [ 6, 7, 9, 3 ]
while(True):
	print response
	if round == 101:
		break
		
	print " Round " + str(round)
	if "Press enter" in response:
		conn.send("\x0a")

	if "Field:" in response:
		i = count % 4
		print moves[i]
		count+=1
		conn.send(str(moves[i])+"\x0a")
	
	if "You lost" in response:
		conn.close()
		print "Lost round " + str(round)
		break
	
	if "Congratulations" in response:
		round +=1
		time.sleep(2)
	
	response = conn.recv(RECV_SIZE)