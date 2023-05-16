'''Module for easy colored text on terminal prints'''

# Author: Luke Henderson
__version__ = '0.8'

import os
import platform
# import colorama

if platform.system() == "Windows":
    os.system('') #enable VT100 escape sequence for Windows 10

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
CMDBLUE = '\033[36m'
CMDCYAN = '\033[96m'

'''Prints in color of function name\n
Args:
    printStr [str, other]: input text to print in color
        converted via str()'''
def blue(printStr):
    print(OKBLUE + str(printStr) + ENDC)

def red(printStr):
    print(FAIL + str(printStr) + ENDC)

def green(printStr):
    print(OKGREEN + str(printStr) + ENDC)

def yellow(printStr):
    print(WARNING + str(printStr) + ENDC)

def purple(printStr):
    print(HEADER + str(printStr) + ENDC)

'''Cmd print colors (echo command)
    can accept %DATE/TIME% placeholders:
Args:
    printStr [str, other]: input text to print in color\n
        converted via str()'''
def cmdBlue(printStr):
    os.system('echo ' + CMDBLUE + str(printStr) + ENDC)
    
def cmdCyan(printStr):
    os.system('echo ' + CMDCYAN + str(printStr) + ENDC)

