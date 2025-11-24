import sys
import os
import subprocess

output = subprocess.check_output(["lscpu"]).decode()
lines = output.splitlines()

for line in lines:
    if "Model name" in line:
        model = line.split(":")[1].strip()
        print(model)