import os
from .colors import bcolors

config_path = os.path.join(os.path.dirname(__file__), "../../../config/")

def zsh():
    print(f"{bcolors.OKGREEN}Installing zsh as default...{bcolors.ENDC}\n")
    os.system("sudo apt-get install zsh -y")
    os.system("chsh -s $(which zsh)")

def hack_nerd_fonts():
    print(f"{bcolors.OKGREEN}Downloading and installing hack nerd fonts...{bcolors.ENDC}\n")
    os.system("\
        curl -s https://api.github.com/repos/ryanoasis/nerd-fonts/releases/latest \
        | grep 'browser_download_url' \
        | cut -d '\"' -f 4 \
        | grep 'Hack*' \
        | xargs wget -P /tmp")

    os.system("unzip /tmp/Hack.zip -d /tmp/hack-nerd-fonts")
    os.system("sudo cp /tmp/hack-nerd-fonts/* /usr/local/share/fonts/")

def tabby():
    print(f"{bcolors.OKGREEN}Downloading, installing and setting tabby term emulator...{bcolors.ENDC}\n")

    # Downloading
    os.system("\
        curl -s https://api.github.com/repos/Eugeny/tabby/releases/latest \
        | grep 'browser_download_url' \
        | cut -d '\"' -f 4 \
        | grep 'linux.deb' \
        | xargs wget -P /tmp")

    # Installing
    os.system("sudo dpkg -i /tmp/tabby*.deb")
    os.system("sudo apt --fix-broken install -y")
    os.system("sudo dpkg -i /tmp/tabby*.deb")

    # Setting
    os.system("sudo update-alternatives --install /usr/bin/x-terminal-emulator x-terminal-emulator /usr/bin/tabby 50")
    os.system("echo \"TerminalEmulator=custom-TerminalEmulator\" > $HOME/.config/xfce4/helpers.rc")
    os.system("mkdir -p $HOME/.config/tabby")
    os.system("cp "+ config_path + "config.yaml" +" $HOME/.config/tabby")

def oh_my_zsh():
    print(f"{bcolors.OKGREEN}Downloading and installing oh my zsh...{bcolors.ENDC}\n")
    os.system("sh -c \"$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)\" \"\" --unattended")

def powerlevel10k():
    print(f"{bcolors.OKGREEN}Downloading and installing powerlevel10k...{bcolors.ENDC}\n")
    os.system("git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k")
    os.system("sed -i 's/ZSH_THEME=\"robbyrussell\"/ZSH_THEME=\"powerlevel10k\/powerlevel10k\"/' $HOME/.zshrc")

def bat():
    print(f"{bcolors.OKGREEN}Downloading bat and setting alias on .zshrc...{bcolors.ENDC}\n")
    os.system("sudo apt install bat")

    # Alias
    os.system("echo 'alias cat=\"batcat --style=plain --paging=never\"' >> $HOME/.zshrc")

def lsd():
    print(f"{bcolors.OKGREEN}Downloading lsd and setting alias on .zshrc...{bcolors.ENDC}\n")
    os.system("curl -s https://api.github.com/repos/Peltoche/lsd/releases/latest \
        | grep \"browser_download_url\" \
        | cut -d '\"' -f 4 \
        | grep \"amd64.deb\" \
        | grep \"lsd_\" \
        | xargs wget -P /tmp ")
    os.system("sudo dpkg -i /tmp/lsd*.deb")

    # Alias
    os.system("echo 'alias ls=\"lsd\"' >> $HOME/.zshrc")

def fzf():
    print(f"{bcolors.OKGREEN}Installing fzf...{bcolors.ENDC}\n")
    os.system("git clone --depth 1 https://github.com/junegunn/fzf.git $HOME/bin/fzf")
    os.system("$HOME/bin/fzf/install --key-bindings --completion --update-rc")
