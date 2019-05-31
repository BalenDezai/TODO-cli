import sys
from lib import commands
from lib import reader
from lib import writer


# TODO: Not really a TODO, I'm just testing that the program works on itself

def main():
    # TODO: Use '-' to read from stdin instead
    filenames = commands.commandInterpreter(sys.argv)
    comments = reader.readFiles(filenames)
    writer.printOut(comments)

if __name__ == "__main__":
    main()
