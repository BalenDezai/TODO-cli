import sys
from lib import commands
from lib import reader
from lib import writer
from lib import config


# TODO: Not really a TODO, I'm just testing that the program works on itself

def main():
    # TODO: Use '-' to read from stdin instead
    argument_obj = commands.command_interpreter()

    # Check that language extensions are defined in config file
    error = False
    for extension in argument_obj.extensions:
        try:
            config.lang_list[extension]
        except KeyError:
            print("ERROR:\t\"" + extension + "\" is not a recognized extension in the config file")
            error = True

    if error:
        return

    # Call the reader if all is good 
    comments = reader.read_files(argument_obj)
    writer.print_out(comments)


if __name__ == "__main__":
    main()
