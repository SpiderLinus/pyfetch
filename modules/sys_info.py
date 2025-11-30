import platform
import os
import sys
from modules import distro
import shutil
import subprocess


# -.-.-.-.-.-.-.-.-.-.-.-.-
# SYSTEM INFO
# -.-.-.-.-.-.-.-.-.-.-.-.-

def system_reader():

    system = platform.system()
    release = platform.release()
    machine = platform.machine()

    print(f"{system} | {release}")

    if system == "Linux":
        print(f"{distro.name(pretty=True)} | {machine}")
    else:
        print(machine)




# -.-.-.-.-.-.-.-.-.-.-.-.-
# PACKAGE MANAGER MODULES
# -.-.-.-.-.-.-.-.-.-.-.-.-


def pacman():

    output = subprocess.check_output(["pacman", "-Qq"]).decode()
    return len(output.splitlines()), "pacman"
   


def apt():

    output = subprocess.check_output(["dpkg", "--get-selections"]).decode()
    return len(output.splitlines()), "dpkg"
   


def dnf():

    output = subprocess.check_output(["rpm", "-qa"]).decode()
    return len(output.splitlines()), "rpm"


def nix():
    system_out = subprocess.check_output(
        ["nix-store", "-q", "--requisites", "/run/current-system"]
    ).decode()
    user_out = subprocess.check_output(["nix-env", "-q"]).decode()
    
    system_pkgs = len(system_out.splitlines())
    user_pkgs = len(user_out.splitlines())

    return f"{system_pkgs} | {user_pkgs}", "nix"


def flatpak():

    output = subprocess.check_output(["flatpak", "list"]).decode()
    return len(output.splitlines()), "flatpak"


def brew():

    output = subprocess.check_output(["brew", "list"]).decode()
    return len(output.splitlines()), "brew"


def snap():

    output = subprocess.check_output(["snap", "list"]).decode()
    return len(output.splitlines()), "snap"


def xbps():

    output = subprocess.check_output(["xbps-query", "-l"]).decode()
    return len(output.splitlines()), "void"


def apk():

    output = subprocess.check_output(["apk", "info"]).decode()
    return len(output.splitlines()), "apk"

def qlist():

    output = subprocess.check_output(["qlist", "-I"]).decode()
    return len(output.splitlines()), "gentoo"



# -.-.-.-.-.-.-.-.-.-.-.-.-
# PACKAGE MANAGER HANDLER TABLE
# -.-.-.-.-.-.-.-.-.-.-.-.-

PACKAGE_HANDLERS = {
    "pacman": pacman,
    "apt": apt,
    "dnf": dnf,
    "nix-env": nix,
    "flatpak": flatpak,
    "brew": brew,
    "snap": snap,
    "xbps-query": xbps,
    "apk": apk,
    "qlist": qlist,
}

# -.-.-.-.-.-.-.-.-.-.-.-.-
# MAIN
# -.-.-.-.-.-.-.-.-.-.-.-.-

def main():
    system_reader()
    
    for binary, handler in PACKAGE_HANDLERS.items():
        if shutil.which(binary):
            result, name = handler()
            print(f"{result} Pkgs ({name})")

    if __name__ == "__main__":
        main()