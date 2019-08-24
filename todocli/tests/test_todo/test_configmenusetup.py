from unittest import mock
from todocli.todo.configmenusetup import Setup
from argparse import Namespace
import pytest

class TestConfigMenuSetup(object):
    config_file_path = 'pathfilehere'
    config_setup = Setup(config_file_path)

    def test_ConfigMenuStart(self):
        with mock.patch('builtins.input', return_value='y'):
            created_config_obj = self.config_setup.config_menu_start()
            assert isinstance(created_config_obj, dict)
            assert created_config_obj['names'] == 'y'
            assert created_config_obj['is_folder'] == True
            assert isinstance(created_config_obj['extensions'], list)
            assert created_config_obj['extensions'][0] == 'y'

    #   get folder or file name function
    def test_GetFolderOrFileName(self):
        with mock.patch('builtins.input', return_value='fileOrFolderName'):
            assert self.config_setup.__get_folder_or_file_name__() == 'fileOrFolderName'
        
    #   where is folder is true
    def test_GetIsFolderTrue(self):
        with mock.patch('builtins.input', return_value="y"):
            assert self.config_setup.__get_is_folder__() ==  True

    #   where is folder is false
    def test_GetIsFolderFalse(self):
        with mock.patch('builtins.input', return_value="n"):
            assert self.config_setup.__get_is_folder__() ==  False
    
    def test_GetExtensions(self):
        with mock.patch('builtins.input', return_value=".py"):
            assert self.config_setup.__get_extensions__() ==  '.py'
            
    def test_CreateConfigObject(self):
        createdObject = self.config_setup.create_config_object('  FileNames  ', True, '.py .c')

        assert isinstance(createdObject, dict)

        assert createdObject['names'] == 'FileNames'
        assert isinstance(createdObject['names'], str)

        assert isinstance(createdObject['is_folder'], bool)
        assert createdObject['is_folder'] == True

        assert isinstance(createdObject['extensions'], list)
        assert createdObject['extensions'][0] == ".py"
        assert createdObject['extensions'][1] == ".c"

    def test_CombineConfigurations(self):
        obj1 = {
            'names': None,
            'is_folder': True,
            'extensions': ['.py', '.c']
        }
        obj2 = {
            'names': 'FileName',
            'is_folder': None,
            'extensions': None
        }
        result = self.config_setup.combine_configurations(obj1, obj2)

        assert isinstance(result, Namespace)

        assert result.names == 'FileName'

        assert result.is_folder == True

        assert isinstance(result.extensions, list)
        assert result.extensions[0] == '.py'
        assert result.extensions[1] == '.c'

    def test_LoadconfigFromFile(self):
        jsonStr = '{"extensions": [".py", ".c"], "is_folder": null, "names": "FileName"}'
        mocked_file = mock.mock_open(read_data=jsonStr)
        with mock.patch('todocli.todo.configmenusetup.open', mocked_file, create=True):
            loaded_config = self.config_setup.load_config_from_file()
            assert isinstance(loaded_config, dict)
            
            assert loaded_config['names'] == 'FileName'
            assert isinstance(loaded_config['names'], str)

            assert loaded_config['is_folder'] == None

            assert isinstance(loaded_config['extensions'], list)
            assert loaded_config['extensions'][0] == '.py'
            assert loaded_config['extensions'][1] == '.c'

    def test_LoadConfigFromFileWithoutNameProperty(self):
        jsonStr = '{"extensions": [".py", ".c"], "is_folder": null}'
        mocked_file = mock.mock_open(read_data=jsonStr)
        with mock.patch('todocli.todo.configmenusetup.open', mocked_file, create=True):
            loaded_config = self.config_setup.load_config_from_file()
            assert loaded_config['names'] == None

    def test_LoadConfigFromFileError(self):
        jsonStr = '{"extensions": [".py", ".c"], "is_folder": null, "names": "FileName"}'
        mocked_file = mock.mock_open(read_data=jsonStr)
        mocked_file.side_effect = FileNotFoundError
        with mock.patch('todocli.todo.configmenusetup.open', mocked_file, create=True):
            with pytest.raises(FileNotFoundError):
                self.config_setup.load_config_from_file()

    def test_PrintToFile(self):
        jsonStr = '{"extensions": [".py", ".c"], "is_folder": null, "names": "FileName"}'
        mocked_file = mock.mock_open(read_data=jsonStr)
        with mock.patch('todocli.todo.configmenusetup.open', mocked_file, create=True):
            self.config_setup.print_to_file(jsonStr)

    def test_PrintToFileError(self):
        jsonStr = '{"extensions": [".py", ".c"], "is_folder": null, "names": "FileName"}'
        mocked_file = mock.mock_open(read_data=jsonStr)
        mocked_file.side_effect = OSError
        with mock.patch('todocli.todo.configmenusetup.open', mocked_file, create=True):
            with pytest.raises(OSError):
                self.config_setup.print_to_file(jsonStr)