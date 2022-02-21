#!/usr/bin/env python
"""
Copyright (c) 2020 NUIG Honeypot FYP 
All rights reserved.

"""

import time
import socket
import datetime
# from termcolor import colored

banner = """
 _     _  ___   __    _  __    _  ___   _______  _______  _______  _______ 
| | _ | ||   | |  |  | ||  |  | ||   | |       ||       ||       ||       |
| || || ||   | |   |_| ||   |_| ||   | |    ___||    _  ||   _   ||_     _|
|       ||   | |       ||       ||   | |   |___ |   |_| ||  | |  |  |   |  
|       ||   | |  _    ||  _    ||   | |    ___||    ___||  |_|  |  |   |  
|   _   ||   | | | |   || | |   ||   | |   |___ |   |    |       |  |   |  
|__| |__||___| |_|  |__||_|  |__||___| |_______||___|    |_______|  |___|  

NUIG FYP Honeypot Group (Coordinator: Martin Hughes) 
(c) MK Chong 2022
"""

def getInput():
  print(banner)
  motd = datetime.datetime.now()
  print (motd.strftime("[+] [%Y-%m-%d %H:%M:%S] Winniepot instance started ..."))
  print (motd.strftime("[+] [%Y-%m-%d %H:%M:%S] Creating subnet on 127.0.0.1"))

  host = raw_input(motd.strftime("[+] [%Y-%m-%d %H:%M:%S] Target IP : "))
  while True:
		try:
			port = int(raw_input(motd.strftime("[+] [%Y-%m-%d %H:%M:%S] Target port : ")))
		except TypeError:
			print 'Error: Invalid port number.'
			continue
		else:
			if (port < 1) or (port > 65535):
				print 'Error: Invalid port number.'
				continue
			else:
				return (host, port, motd)

def writeLog(client, data=''):
	separator = '='*50
	fopen = open('./Winniepot.mmh', 'a')
	fopen.write('Time: %s\nIP: %s\nPort: %d\nData: %s\n%s\n\n'%(time.ctime(), client[0], client[1], data, separator))
	fopen.close()

def main(host, port, motd):
	print (motd.strftime("[+] [%Y-%m-%d %H:%M:%S] Winniepot listening ..."))
  	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  	s.bind((host, port))
  	s.listen(100)
  	while True:
		(insock, address) = s.accept()
		print '==========================================================='
		print (motd.strftime("[+] [%Y-%m-%d %H:%M:%S]  Connection Detected"))
		print 'HIT from: %s:%d' % (address[0], address[1])
		print '==========================================================='
		try:
			insock.send('%s\n'%(motd))
			data = insock.recv(1024)
			insock.close()
		except socket.error, e:
				writeLog(address)
		else:
				writeLog(address, data)
        
if __name__=='__main__':
	try:
		stuff = getInput()
		main(stuff[0], stuff[1], stuff[2])
	except KeyboardInterrupt:
		print 'Winniepot Deactivated ...'
		exit(0)
	except BaseException, e:
		print 'Error: %s' % (e)
		exit(1)
