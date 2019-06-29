from colorama import Fore, Back, Style, init

#   this is the module to write out to the terminal

# TODO: read config and write in the correct format
def print_out(comments_to_write_out=[]):
        init()
        for comment in comments_to_write_out:
                print(Fore.RED + comment.filename + Style.RESET_ALL +  " " + str(comment.line) + ":\t\t" + comment.text) 
