import json
from .utils.utils import combine_two_objects, clean_object_none_values
from os.path import dirname, pardir, abspath, join
from argparse import Namespace


class Setup:
    def __init__(self, path_to_store_file:str):
        self.path_to_store_file = path_to_store_file

    def config_menu_start(self):
        folder_or_file = self.__get_folder_or_file_name__()
        is_folder = self.__get_is_folder__()
        extensions = self.__get_extensions__()

        return self.create_config_object(folder_or_file, is_folder, extensions)


    def __get_folder_or_file_name__(self):
        name = input("the name of the specific folder or file to search for in directory ran from (if none will select default project ran from): ")
        return name

    def __get_is_folder__(self):
        is_folder = input("Is the project you want to search into a folder? (y/n): ")
        if is_folder == 'y':
            is_folder = True
        else:
            is_folder = False
        return is_folder

    def __get_extensions__(self):
        extensions = input("specify the extensions of files to search in (using space seperator): ")
        return extensions

    def create_config_object(self, names:str, is_folder:bool, extensions:str):
        objToReturn = {}
        objToReturn['names'] = names.strip()
        objToReturn['is_folder'] = is_folder
        #   split the string by space from the file config into an array of strings
        objToReturn['extensions'] = extensions.strip().split()
        return objToReturn

    def print_to_file(self, objToWriteOut:dict):
        try:
            with open(self.path_to_store_file, 'w') as outfile:
                json.dump(objToWriteOut, outfile, sort_keys=True, indent=4)
        except OSError:
            raise

    def combine_configurations(self, file_config_obj:dict, input_config_obj:dict):
        config_object_cleaned = clean_object_none_values(input_config_obj)
        combined_config = combine_two_objects(file_config_obj, config_object_cleaned)
        
        return Namespace(**combined_config)
    
    def load_config_from_file(self):
        try:
            with open(self.path_to_store_file, 'r') as config_data:
                data = json.load(config_data)
                #   if the names property is an empty string, turn it into None instead
                if not 'names' in data:
                    data['names'] = None
                return data
        except FileNotFoundError:
            raise
    
    