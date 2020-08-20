import sys
from time import sleep
import random


class colors:
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'


color_random = [colors.CBLUE, colors.CVIOLET, colors.CWHITE, colors.OKBLUE, colors.CGREEN, colors.WARNING,
                colors.CRED, colors.CBEIGE]
random.shuffle(color_random)


def entryy():
    x = color_random[0] + """               
        ███████▀▀▀░░░░░░░▀▀▀███████
        ████▀░░░░░░░░░░░░░░░░░▀████
        ███│░░░░░░░░░░░░░░░░░░░│███
        ██▌│░░░░░░░░░░░░░░░░░░░│▐██
        ██░└┐░░░░░░░░░░░░░░░░░┌┘░██
        ██░░└┐░░░░░░░░░░░░░░░┌┘░░██
        ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
        ██▌░│██████▌░░░▐██████│░▐██
        ███░│▐███▀▀░░▄░░▀▀███▌│░███
        ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
        ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
        ████▄─┘██▌░░░░░░░▐██└─▄████
        █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
        ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
        █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████   
        ███████▄░░░░░░░░░░░▄███████   ░    MAIL EXTRACTOR     ░ 
        ██████████▄▄▄▄▄▄▄██████████      instagram==> tmrswrr  
        ███████████████████████████   ▒   CODED BY TMRSWRR    ░ 
\n"""

    for c in x:
        print(c, end='')
        sys.stdout.flush()
        sleep(0.0045)
    oo = " " * 6 + 29 * "░█" + "\n\n"
    for c in oo:
        print(colors.CGREEN + c, end='')
        sys.stdout.flush()
        sleep(0.0065)


    tt = " " * 6 + "░█" + " " * 5 + "WELCOME TO INSTAGRAM MAIL EXTRACTOR" + " " * 14 + "░█" + "\n\n"
    for c in tt:
        print(colors.CWHITE + c, end='')
        sys.stdout.flush()
        sleep(0.0065)
    xx = " " * 6 + 29 * "░█" + "\n\n"
    for c in xx:
        print(colors.CGREEN + c, end='')
        sys.stdout.flush()
        sleep(0.0065)


entryy()