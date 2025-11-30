#!/bin/bash

cat pyfetch.txt

echo ""

if [ -f /etc/os-release ]; then
    . /etc/os-release
else
    echo "Cannot detech operating system. /etc/os-release must be missing :("
    exit 1
fi

case "$ID" in
    arch)
        DISTRO="arch"
        ;;
    debian|ubuntu)
        DISTRO="debian"
        ;;
    nixos)
        DISTRO="nixos"
        ;;
    fedora)
        DISTRO="fedora"
        ;;
    opensuse*|suse*)
        DISTRO="opensuse"
        ;;
    void)
        DISTRO="void"
        ;;
    gentoo)
        DISTRO="gentoo"
        ;;
    *)
        DISTRO="unknown"
        ;;
esac

echo "Detected: $DISTRO"

case "$DISTRO" in
    arch)
        sudo pacman -Sy --needed jp2a playerctl ;;
    debian)
        sudo apt update
        sudo apt install -y jp2a playerctl ;;
    fedora)
        sudo dnf install -y jp2a playerctl ;;
    opensuse)
        sudo zypper install -y jp2a playerctl ;;
    void)
        sudo xbps-install -Sy jp2a playerctl ;;
    gentoo)
        sudo emerge --ask jp2a playerctl ;;
    nixos)
        echo ""
        echo "You are on NixOS."
        echo "Add this to your configuration.nix or flake:"
        echo ""
        echo "  environment.systemPackages = [ pkgs.jp2a pkgs.playerctl ];"
        echo ""
        exit 0 ;;
    *)
        echo "Unsupported distro."
        exit 1 ;;
esac


if [ "$DISTRO" != "nixos" ]; then
    echo "Making command named pyfetch"
    sudo cp pyfetch /usr/local/bin/pyfetch
    sudo chmod +x /usr/local/bin/pyfetch
    echo "pyfetch installed"
else
    echo "Skipping CLI installation for nixos"
    echo ""
fi

echo "Dependencies installed."
echo "Pyfetch installation completed."
echo "Command: pyfetch"
