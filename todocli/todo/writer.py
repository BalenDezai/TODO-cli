from colorama import Fore, Back, Style, init

#   this is the module to write out to the terminal

# TODO: read config and write in the correct format
def print_out(comments_to_write_out=[]):
        init()
        for comment in comments_to_write_out:
                print(Fore.RED + comment.filename + ":")
                for lineandcomment in comment.line_and_comment:
                        print(Style.RESET_ALL + "\t\t" + str(lineandcomment[0]) + ":\t" + lineandcomment[1]) 
