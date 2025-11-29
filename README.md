# Pyfetch 🐍
### Pyfetch is an alternative to fastfetch or neofetch. 
---

## ⚙️ Install

### Debian & Arch etc

```
git clone https://github.com/SpiderLinus/pyfetch && cd pyfetch
```
```
chmod +x install.sh && ./install.sh
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
If you want to modify this program you can simply do so in the modules folder and in the main.py file. We are currently working on a feature that lets you configure it by using the config.json file but that isn't out yet so stay tuned ;)

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
│   ├── os.py
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
