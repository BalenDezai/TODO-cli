#!/usr/bin/env python

from todo import commands
from todo import reader
from todo import writer
from todo import config
from todo import configmenusetup
import sys


# TODO: Not really a TODO, I'm just testing that the program works on itself

def main():
    # TODO: Use '-' to read from stdin instead
    argument_obj = commands.command_interpreter(sys.argv[1:])
    if argument_obj.new_config == True:
        setup = configmenusetup.Setup()
        setup.config_setup_menu()
        setup.print_to_file()
    else:
        setup = configmenusetup.Setup()
        combined_commands = setup.combine_configurations(vars(argument_obj))
        print(combined_commands)
        # Check that language extensions are defined in config file
        error = False
        for extension in combined_commands.extensions:
            try:
                config.lang_list[extension]
            except KeyError:
                print("ERROR:\t\"" + extension + "\" is not a recognized extension in the config file")
                error = True

        if error:
            return

        # Call the reader if all is good 
        comments = reader.read_files(combined_commands)
        writer.print_out(comments)


if __name__ == "__main__":
    main()
