import os
from .colors import bcolors

def docker():
    print(f"{bcolors.OKGREEN}Installing docker maybe take more time...{bcolors.ENDC}\n")
    # Dependencies
    print(f"{bcolors.OKBLUE}Installing docker dependencies{bcolors.ENDC}\n")
    os.system("sudo apt-get install ca-certificates curl gnupg lsb-release -y")

    # GPG
    print(f"{bcolors.OKBLUE}Installing docker GPG{bcolors.ENDC}\n")
    os.system("curl -fsSL https://download.docker.com/linux/ubuntu/gpg\
        | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg")
    os.system("echo \"deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable\" \
        | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null")
    
    # Install docker.io
    print(f"{bcolors.OKBLUE}Installing docker.io{bcolors.ENDC}\n")
    os.system("sudo apt-get update -y")
    os.system("sudo apt install -y docker.io")

    # Enable and add user to docker group
    print(f"{bcolors.OKBLUE}Enable and add user to docker group{bcolors.ENDC}\n")
    os.system("sudo systemctl enable docker --now")
    os.system("sudo groupadd docker")
    os.system("sudo usermod -aG docker $USER")

    # GPG docker.ce
    print(f"{bcolors.OKBLUE}Adding GPG docker.ce{bcolors.ENDC}\n")
    os.system("printf '%s\n' \"deb https://download.docker.com/linux/debian bullseye stable\" \
        | sudo tee /etc/apt/sources.list.d/docker-ce.list")
    os.system("curl -fsSL https://download.docker.com/linux/debian/gpg \
        | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/docker-ce-archive-keyring.gpg")

    # Install docker-ce-cli and containerd.io
    print(f"{bcolors.OKBLUE}Installing docker-ce-cli and containerd.io{bcolors.ENDC}\n")
    os.system("sudo apt-get update -y")
    os.system("sudo apt install -y docker-ce docker-ce-cli containerd.io")

def docker_compose():
    print(f"{bcolors.OKGREEN}Installing docker-compose...{bcolors.ENDC}\n")
    os.system("sudo curl -L \"https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)\" -o /usr/local/bin/docker-compose")
    os.system("sudo chmod +x /usr/local/bin/docker-compose")

def sublime_text():
    print(f"{bcolors.OKGREEN}Installing sublime text...{bcolors.ENDC}\n")
    # Dependencies
    os.system("sudo apt-get install apt-transport-https -y")

    # Download
    os.system("wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -")
    os.system("echo \"deb https://download.sublimetext.com/ apt/stable/\"\
        | sudo tee /etc/apt/sources.list.d/sublime-text.list")

    # Install
    os.system("sudo apt-get update -y")
    os.system("sudo apt-get install sublime-text -y")