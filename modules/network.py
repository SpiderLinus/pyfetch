import os
import sys

def hostname():
    os.system("uname -n > data/hostname_data.txt")
    with open("data/hostname_data.txt", "r") as file:
        host = file.read().strip()
        return host


def ipv4():
    os.system("ip route get 1.1.1.1 | grep -oP 'src \K[\d.]+' > data/ipv4_data.txt")
    with open("data/ipv4_data.txt", "r") as file:
        ip4 = file.read().split()
        return ip4

def ipv6():
    os.system("hostname -i | awk '{print $1}' > data/ipv6_data.txt")
    with open("data/ipv6_data.txt", "r") as file:
        ip6 = file.read().split()
        return ip6

