import os
import sys


from core.config_loader import loader
from core.renderer import render

from modules import playerctl, network, sys_info


def ascii_loader(name, width=50, color=True):
    base = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(base, "logos", f"{name}.png")
    ascii_path = os.path.join(base, "data", "ascii_logo.txt")


    command = f"jp2a -i --width={width} {'--color' if color else ''} '{logo_path}' > '{ascii_path}'"

    os.system(command)


    with open(ascii_path, "r") as f:
        return f.read()


def Pyfetch():
    config = loader()

    logos = ascii_loader(
        config.get("logo", "linux"),
        width=config.get("logo_width", 50),
        color=config.get("logo_color", True)
    )

    module_func = {
        "os": lambda: sys_info.distro_info(),
        "kernel": lambda: sys_info.kernel_info(),
        "architecture": lambda: sys_info.machine_info(),
        "packages": lambda: sys_info.main(),
        "hostname": network.hostname,
        "ipv4": lambda: "".join(network.ipv4()),
        "ipv6": lambda: "".join(network.ipv6()),
        "playerctl": playerctl.PlayerStatus,
        
    }

    data = {
        name: module_func[name]()
        for name in config.get("modules", [])
        if name in module_func

    }


    render(logos, data, config)

if __name__ == "__main__":
    Pyfetch()


