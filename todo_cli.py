import sys
from lib import commands
from lib import reader
from lib import writer


# TODO: Not really a TODO, I'm just testing that the program works on itself

def main():
    # TODO: Use '-' to read from stdin instead
    argument_obj = commands.command_interpreter()
    comments = reader.read_files(argument_obj)
    writer.print_out(comments)


if __name__ == "__main__":
    main()
