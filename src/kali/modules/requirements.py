import os
from .colors import bcolors

def req():
    print(f"{bcolors.OKGREEN}Installing dependencies...{bcolors.ENDC}\n")
    os.system("sudo apt update -y")
    print(f"{bcolors.OKGREEN}Creating home bin folder...{bcolors.ENDC}\n")
    os.system("mkdir $HOME/bin")