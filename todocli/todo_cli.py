#!/usr/bin/env python

from todo.commands import command_interpreter
from todo import reader
from todo import writer
from todo import config
from todo.configmenusetup import Setup
from os.path import dirname, pardir, abspath, join
import sys


# TODO: Not really a TODO, I'm just testing that the program works on itself

def main():
    # TODO: Use '-' to read from stdin instead
    current_folder_path = abspath(join(dirname(__file__), 'config.json'))
    argument_obj = command_interpreter(sys.argv[1:])
    if argument_obj.new_config == True:
        setup = Setup(current_folder_path)
        setup.config_menu_start()
        setup.print_to_file()
    else:

        setup = Setup(current_folder_path)
        file_config = setup.load_config_from_file()
        combined_commands = setup.combine_configurations(file_config, vars(argument_obj))
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
