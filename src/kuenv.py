import time
from kali import *

banner = """
██╗  ██╗██╗   ██╗███████╗███╗   ██╗██╗   ██╗
██║ ██╔╝██║   ██║██╔════╝████╗  ██║██║   ██║
█████╔╝ ██║   ██║█████╗  ██╔██╗ ██║██║   ██║
██╔═██╗ ██║   ██║██╔══╝  ██║╚██╗██║╚██╗ ██╔╝
██║  ██╗╚██████╔╝███████╗██║ ╚████║ ╚████╔╝ 
╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝  ╚═══╝  
                                            (by QuantumTarantino)
"""


def menu():
    print(banner)
    time.sleep(1)
    print("1 -> Instalar para Kali")
    time.sleep(1)
    print("\n2 -> Salir")
    time.sleep(1)

    option = input("\n-->> ")

    if option == "1":
        install_kali_env()
    if option == "2":
        exit()

def run_kuenv():
    menu()
            
if __name__ == '__main__':
    id = os.getuid()
    
    if id == 0:
        print()
        print(f"{bcolors.FAIL}No execute as root{bcolors.ENDC}\n")
        print()
    else:
        run_kuenv()