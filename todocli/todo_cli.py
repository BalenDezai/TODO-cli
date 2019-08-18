#!/usr/bin/env python

from todo.commands import command_interpreter
from todo.reader import get_all_dir_files, attach_working_dir, read_comments_in_files
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
        config_obj = setup.config_menu_start()
        setup.print_to_file(config_obj)
    else:

        setup = Setup(current_folder_path)
        file_config = {}
        try:
            file_config = setup.load_config_from_file()
        except FileNotFoundError:
            file_config = setup.create_config_object('', None, '')
            setup.print_to_file(file_config)
        
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
        
        combined_commands = attach_working_dir(combined_commands)

        if combined_commands.is_folder:
            combined_commands.names = get_all_dir_files(combined_commands.names, combined_commands.debug_mode, combined_commands.extensions)
        # Call the reader if all is good 
        comments = read_comments_in_files(combined_commands.names)
        writer.print_out(comments)


if __name__ == "__main__":
    main()
