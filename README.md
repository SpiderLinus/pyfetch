# Pyfetch 🐍
### Pyfetch is an alternative to fastfetch or neofetch. 
---

## ⚙️ Install

### Debian & Arch etc

```
git clone https://github.com/SpiderLinus/pyfetch && cd pyfetch
```
```
chmod +x install.sh && bash install.sh
```


### Nixos:
```
nix build
```
```
nix profile install .#
```
---

## ⚒️ Modding
If you want to modify this program you can simply do so in the ```config.json``` and in the ```main.py``` file. 

#### Example config.json
You can change the logo to 20 different ascii logos. Check the logos directory for usable logos. You can also add your own by adding any png file to the logos directory. In the ```config.json``` you simply change the logo value to your desired logo. 

You can also add modules. The current modules that work are:
- os
- architecture
- kernel
- packages
- hostname
- ipv4
- ipv6
- playerctl

If you want a specific module you can create an issue or simply make a commit to our repository :)
```
{

 "logo": "linux",
 "logo_width": 50,
 "logo_color": true,


 "modules": [ "os", "architecture", "kernel", "packages", "hostname", "ipv4", "playerctl" ]
 
}
```
---
#### File Structure
```
[scorpion@nixos:~/Projects/pyfetch]$ tree
.
├── config.json
├── core
│   ├── config_loader.py
│   └── renderer.py
├── debug.py
├── flake.nix
├── install.sh
├── main.py
├── modules
│   ├── cpu.py
│   ├── distro.py
│   ├── gpu.py
│   ├── network.py
│   ├── sys_info.py
│   ├── playerctl.py
│   └── ram.py
├── pyfetch.txt
├── README.md
└── version_playerctl.txt
```

---
## 👷‍♂️ To-Do
- [x] Ascii logos
- [ ] All working modules
- [x] Install Script
- [x] Be able to customize using config.json


## Contribution
Authors: Griphcode & SpiderLinus

If you want to contribute to this project simply send in an issue or make a pull request. 

Made with :heart: from Griphcode & SpiderLinus
