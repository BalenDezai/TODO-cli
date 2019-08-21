from todocli.todo_cli import *
from todocli.todo.configmenusetup import Setup
from unittest import mock

class TestMain(object):
    def test_GetConfigFilePath(self):
        filePath = get_config_file_path('\\folder\\')
        assert filePath == r'C:\folder\config.json'

    def test_StartNewConfigMenu(self):
        setup = Setup('testFile')
        
        config_menu_start_mock = mock.Mock(return_value=dict(names='hello'))
        print_to_file_mock = mock.Mock()
        with mock.patch('todocli.todo.configmenusetup.Setup.config_menu_start', config_menu_start_mock):
            with mock.patch('todocli.todo.configmenusetup.Setup.print_to_file', print_to_file_mock):
                start_new_config_menu(setup)

                config_menu_start_mock.assert_called_once()

                print_to_file_mock.assert_called_once()
                print_to_file_mock.assert_called_with({'names': 'hello'})

