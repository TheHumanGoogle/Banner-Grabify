#!/usr/bin/python

"""Developed by Shyam Karthick(@TheHumanGoogle).
   Under the repo- Network-Detective in github.
   For suggestions/bug fixes,contact: shyamkarthick@protonmail.com"""

import socket

def retbanner(ip,port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip,port))
		banner=s.recv(1024)
		return banner
	except:
		return
def main():
	ip = raw_input('[*] Enter Target IP: ')
	for port in range(1,100):
		banner = retbanner(ip,port)
		if banner:
			print '[+]' + ip + '/'+ str(port) + ':' + banner.strip('\n')


main()
