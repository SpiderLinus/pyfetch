import platform
import os
import sys
import distro
import shutil
import subprocess



def system_reader():

    if platform.system() == "Linux":
        print(platform.system() + " | " + platform.release())
        print(distro.name(pretty=True) + " | " + platform.machine() )
        
    else:
        print(platform.system() + " | " + platform.release())
        print(platform.machine())


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


if shutil.which("nix-env"):

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


if shutil.which("flatpak"):

    output = subprocess.check_output(["flatpak", "list"])
    output = output.decode()
    packages = len(output.splitlines())
    packs = str(packages)


    print(packs + " Pkgs (flatpak)")


if shutil.which("brew"):

    output = subprocess.check_output(["brew", "list"])
    output = output.decode()
    packages = len(output.splitlines())
    packs = str(packages)

    system_reader()
    print(packs + " Pkgs (brew)")


if shutil.which("snap"):

    output = subprocess.check_output(["snap", "list"])
    output = output.decode()
    packages = len(output.splitlines())
    packs = str(packages)

    system_reader()
    print(packs + " Pkgs (snap)")


if shutil.which("xbps-query"):

    output = subprocess.check_output(["xbps-query", "-l"])
    output = output.decode()
    packages = len(output.splitlines())
    packs = str(packages)

    system_reader()
    print(packs + " Pkgs (void)")


if shutil.which("apk"):

    output = subprocess.check_output(["apk", "info"])
    output = output.decode()
    packages = len(output.splitlines())
    packs = str(packages)

    system_reader()
    print(packs + " Pkgs (apk)")


if shutil.which("qlist"):

    output = subprocess.check_output(["qlist", "-I"])
    output = output.decode()
    packages = len(output.splitlines())
    packs = str(packages)

    system_reader()
    print(packs + " Pkgs (gentoo)")
