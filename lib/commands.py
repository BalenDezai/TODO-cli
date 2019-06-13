import argparse
#   this module is for the handling of command arguments and the commands


def command_interpreter():
    parser = argparse.ArgumentParser(
        description='A program that shows all TODO comments in your code.',
        prog='TODOcli'
        )
    #   wondering if we should do multiple folders or nahh, might be bad design
    #   ponder on later
    parser.add_argument('-f', '--name', dest='names', metavar='', nargs='+', help='file(s) or folder names')
    parser.add_argument('-m', '--folder', action='store_true', dest='isFolder',  default=False, help='parameter for file(s) or folder')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    return parser.parse_args()
