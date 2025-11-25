import os


command = "playerctl -l"
title = "playerctl metadata title"
aritst = "playerctl metadata artist"



def PlayerStatus():
    if (os.system(command) == False):
        print("Current track: ", os.system(title), os.system(aritst))


versions = [
    "v0.5.0", "v0.6.0", "v0.6.1", "v2.0.1", "v2.0.2",
    "v2.1.1", "v2.2.1", "v2.3.1", "v2.4.1"
]

def PlayerDebug():

    
    os.system("playerctl -v > version_playerctl.txt")
    with open("version_playerctl.txt", "r") as file:
        version = file.read().strip()

    if version in versions:
        print("Playerctl up to date")
    else:
        print("Playerctl is outdated")

