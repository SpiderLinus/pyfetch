import platform
import os
import sys
import distro
import shutil
import subprocess



def system_reader():

    if platform.system() == "Linux":
        print(platform.system() + " | " + platform.release())
        print("--------------------")
        print(distro.name(pretty=True) + " | " + platform.machine() )
        print("--------------------")
        
    else:
        print(platform.system() + " | " + platform.release())
        print("--------------------")
        print(platform.machine())
        print("--------------------")


if shutil.which("pacman"):

    output = subprocess.check_output(["pacman", "-Qq"])
    output = output.decode()
    packages = len(output.splitlines())
    packs = str(packages)

    system_reader()
    print(packs + " Pkgs (pacman)")

if shutil.which("apt"):

    output = subprocess.check_output(["dpkg", "--get-selections"])
    output = output.decode()
    packages = len(output.splitlines())
    packs = str(packages)

    system_reader()
    print(packs + " Pkgs (dpkg)")


if shutil.which("dnf"):

    output = subprocess.check_output(["rpm", "-qa"])
    output = output.decode()
    packages = len(output.splitlines())
    packs = str(packages)

    system_reader()
    print(packs + " Pkgs (rpm)")


if shutil.which("nix-env" + "nix-store"):

    output = subprocess.check_output(["nix-store", "-q", "--requisites", "/run/current-system"])
    output = output.decode()
    packages = len(output.splitlines())
    packs = str(packages)

    useroutput = subprocess.check_output(["nix-env", "-q"])
    useroutput = useroutput.decode()
    userpkgs = len(useroutput.splitlines())
    userpacks = str(userpkgs)

    system_reader()
    print(packs + " | " +  userpacks + " Pkgs (nix)")

