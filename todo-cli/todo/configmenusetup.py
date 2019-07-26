import json
from os.path import dirname, pardir, abspath, join
from argparse import Namespace


class Setup:
    path_to_store_file = join(abspath(join(dirname(__file__), pardir)), 'config.json')
    configData = {}
    def config_setup_menu(self):
        folder_or_file = input("the name of the specific folder or file to search for in directory ran from (if none will select default project ran from): ")
        is_folder = input("Is the project you want to search into a folder? (y/n): ")
        if is_folder == 'y':
            is_folder = True
        else:
            is_folder = False
        
        extensions = input("specify the extensions of files to search in (using space seperator): ")

        self.create_config_file_object(folder_or_file, is_folder, extensions)

    def create_config_file_object(self, names:str, is_folder:bool, extensions:str):
        self.configData['names'] = names.strip()
        self.configData['is_folder'] = is_folder
        #   split the string by space from the file config into an array of strings
        self.configData['extensions'] = extensions.strip().split()

    def print_to_file(self):
        with open(self.path_to_store_file, 'w') as outfile:
            json.dump(self.configData, outfile, sort_keys=True, indent=4)
    
    def __clean_object_none_values__(self, object_to_clean:dict):
        return {key: value for key, value in object_to_clean.items() if value is not None}

    def combine_configurations(self, config_object:dict):
        file_config_obj = self.__load_config_from_file__()

        #   if the names property is an empty string, turn it into None instead
        if not file_config_obj['names']:
            file_config_obj['names'] = None
        
        combined_config = dict()
        config_object_cleaned = self.__clean_object_none_values__(config_object)

        combined_config.update(file_config_obj)
        combined_config.update(config_object_cleaned)

        return Namespace(**combined_config)
    
    def __load_config_from_file__(self):
        try:
            with open(self.path_to_store_file) as config_data:
                data = json.load(config_data)
                return data
        except IOError:
            self.create_config_file_object('', '', '')
            self.print_to_file()
    
    