#   this module is for the handling of command arguments and the commands
import argparse
from .utils.bool_arg_parser import BoolArgParser


def command_interpreter(args):
    parser = argparse.ArgumentParser(
        description='A program that shows all TODO comments in your code.',
        prog='TODOcli'
        )
    #   wondering if we should do multiple folders or nahh, might be bad design
    #   ponder on later
    parser.add_argument('-f', '--name', dest='names', metavar='', nargs='+', help='file(s) or folder names')
    parser.add_argument('-m', '--folder', action=BoolArgParser, dest='is_folder', nargs=0, help='parameter for file(s) or folder')
    parser.add_argument('-e', '--extension', dest='extensions', metavar='', nargs='+', help='file(s) extensions to look for')
    parser.add_argument('-c', '--config', action='store_true', dest='new_config', help='parameter to start new config setup')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('-d', '--debug', action='store_true', dest='debug_mode', help='print debug information') # maybe overkill for a toy program?
    return parser.parse_args(args)
