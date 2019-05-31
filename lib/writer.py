from colorama import Fore, Back, Style, init

init()

#   this is the module to write out to the terminal

def printOut(commentsToWriteOut=[]):
    for comment in commentsToWriteOut:
        print(Fore.RED + comment) 