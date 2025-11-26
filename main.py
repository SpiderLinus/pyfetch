import os
import sys

from modules import playerctl
# from modules import sys_info
from modules import network
from modules import ram
from modules import gpu
from modules import cpu


with open("pyfetch.txt", "r") as logo:
        print(logo.read())

def Pyfetch():
    
    print("-------------------------------------")

    print("Os:", sys.platform)
    print("Hostname:", network.hostname())
    print("Ip:", network.ipv4())
    
    print("Playerctl:", playerctl.PlayerStatus())

Pyfetch()