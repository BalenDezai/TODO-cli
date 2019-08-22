#!/usr/bin/env python

from todocli.todo.commands import command_interpreter
from todocli.todo.reader import get_all_dir_files, attach_working_dir, read_comments_in_files
from todocli.todo.writer import print_out
from todocli.todo import config
from todocli.todo.configmenusetup import Setup
from os.path import dirname, pardir, abspath, join
import sys

# TODO: Not really a TODO, I'm just testing that the program works on itself

def get_config_file_path(current_file_path:str):
    return abspath(join(dirname(current_file_path), 'config.json'))

def start_new_config_menu(setup:Setup):
    config_obj = setup.config_menu_start()
    setup.print_to_file(config_obj)

def load_config_or_make_new(setup:Setup):
    file_config = {}
    try:
        file_config = setup.load_config_from_file()
    except FileNotFoundError:
        file_config = setup.create_config_object('', None, '')
        setup.print_to_file(file_config)
    return file_config

def check_extension_exists(extensions:list):
    # Check that language extensions are defined in config file
    for extension in extensions:
        try:
            config.lang_list[extension]
            return True
        except KeyError as e:
            e.args = ["ERROR:\t\"" + extension + "\" is not a recognized extension in the config file"]
            raise
    return False

def load_config_combine_commands(current_folder_path:str, argument_obj):
    setup = Setup(current_folder_path)
    file_config = load_config_or_make_new(setup)

    combined_commands = setup.combine_configurations(file_config, vars(argument_obj))
    return combined_commands

def attach_cwd_get_files(combined_commands):
    combined_commands = attach_working_dir(combined_commands)
            
    if combined_commands.is_folder:
        combined_commands.names = get_all_dir_files(combined_commands.names, combined_commands.debug_mode, combined_commands.extensions)
    
    return combined_commands
def read_comments_and_print(combined_commands):
    # Call the reader if all is good 
    comments = read_comments_in_files(combined_commands.names)
    print_out(comments)

def todo_cli_main(args:list):
    try:
        # TODO: Use '-' to read from stdin instead
        current_folder_path = get_config_file_path(__file__)

        argument_obj = command_interpreter(args)

        if argument_obj.new_config == True:
            setup = Setup(current_folder_path)
            start_new_config_menu(setup)
            sys.exit(0)
        else:
            combined_commands = load_config_combine_commands(current_folder_path, argument_obj)
            check_extension_exists(combined_commands.extensions)

            combined_commands = attach_cwd_get_files(combined_commands)

            read_comments_and_print(combined_commands)
            
            sys.exit(0)
    except Exception as error:
        print(error.args)
        sys.exit(1)