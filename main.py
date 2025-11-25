import os
import sys

from modules import distro
from modules import playerctl
#from modules import os
from modules import network
from modules import ram
from modules import gpu
from modules import cpu

with open("pyfetch.txt") as logo:
        print(logo.read())

def Pyfetch():
    
    print("OS:", sys.platform)
    print(playerctl.PlayerStatus)

Pyfetch()