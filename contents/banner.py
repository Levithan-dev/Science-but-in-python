import time as tm
from colorama import Fore as fr
def anibanner():
    logo=[
        f"{fr.BLUE}██╗     ███████╗██╗   ██╗██╗████████╗██╗  ██╗ █████╗ ███╗   ██╗",
        f"{fr.LIGHTBLUE_EX}██║     ██╔════╝██║   ██║██║╚══██╔══╝██║  ██║██╔══██╗████╗  ██║",
        f"{fr.LIGHTBLUE_EX}██║     █████╗  ██║   ██║██║   ██║   ███████║███████║██╔██╗ ██║",
        f"{fr.GREEN}██║     ██╔══╝  ██║   ██║██║   ██║   ██╔══██║██╔══██║██║╚██╗██║",
        f"{fr.LIGHTGREEN_EX}███████╗███████╗╚██████╔╝██║   ██║   ██║  ██║██║  ██║██║ ╚████║",
        f"{fr.GREEN}╚══════╝╚══════╝ ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝",
    ]
    for line in logo:
        print(line)
        tm.sleep(0.4)
    print(f"{fr.GREEN}\n"+"="*28+" Levithan "+"="*28+"\n")
