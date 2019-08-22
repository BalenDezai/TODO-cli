from todocli.todo_cli import *
from todocli.todo.configmenusetup import Setup
from todocli.todo.utils.file import File
from todocli.todo.utils.comment import Comment
from os.path import dirname, pardir, abspath, join
from unittest import mock
from argparse import Namespace
from io import StringIO
import pytest

class TestMain(object):
    def test_GetConfigFilePath(self):
        this_file_path = abspath(join(dirname(__file__), 'config.json'))
        filePath = get_config_file_path(__file__)
        assert filePath == this_file_path

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

    def test_LoadConfigOrMakeNew(self):
        setup = Setup('testFile')
        
        load_config_from_file_mock = mock.Mock(return_value=dict(names='hello'))
        functionToMock = 'todocli.todo.configmenusetup.Setup.load_config_from_file' 
        
        with mock.patch(functionToMock, load_config_from_file_mock):
            loaded_data = load_config_or_make_new(setup)
            assert isinstance(loaded_data, dict)
            assert 'names' in loaded_data

            load_config_from_file_mock.assert_called_once()

    def test_LoadConfigOrMakeNewThrow(self):
        setup = Setup('testFile')

        create_config_object_mock = mock.Mock(return_value=dict(names='hello'))
        load_config_from_file_mock = mock.Mock(side_effect=FileNotFoundError)
        print_to_file_mock = mock.Mock()

        load_config_from_file_path = 'todocli.todo.configmenusetup.Setup.load_config_from_file'
        create_config_object_path = 'todocli.todo.configmenusetup.Setup.create_config_object' 
        print_to_file_path = 'todocli.todo.configmenusetup.Setup.print_to_file'

        with mock.patch(load_config_from_file_path, load_config_from_file_mock):
            with mock.patch(create_config_object_path, create_config_object_mock):
                with mock.patch(print_to_file_path, print_to_file_mock):
                    loaded_data = load_config_or_make_new(setup)
                    assert isinstance(loaded_data, dict)
                    assert 'names' in loaded_data
                    assert loaded_data['names'] == 'hello'

                    create_config_object_mock.assert_called_once_with('', None, '')
                    print_to_file_mock.assert_called_once_with(dict(names='hello'))

    def test_CheckExtensionExists(self):
        list_of_extensions = ['.py', '.c']
        success = check_extension_exists(list_of_extensions)

        assert success == True

    def test_CheckExtensionExistsNoValues(self):
        list_of_extensions = []
        success = check_extension_exists(list_of_extensions)

        assert success ==  False

    def test_CheckExtensionExistsThrow(self):
        list_of_extensions = ['.js']
        with pytest.raises(KeyError) as error:
            check_extension_exists(list_of_extensions)
        assert error.type is KeyError

    def test_LoadConfigAndCombineCommands(self):
        load_config_or_make_new_mock = mock.Mock(return_value=dict(names=None, is_folder = True))
        load_config_or_make_new_path = 'todocli.todo_cli.load_config_or_make_new'
        result = False
        with mock.patch(load_config_or_make_new_path, load_config_or_make_new_mock):
            result = load_config_combine_commands('FILE1',  Namespace(extensions=['.py']))
        
        assert isinstance(result, Namespace)
        assert result.extensions == ['.py']
        assert result.names == None
        assert result.is_folder == True

    def test_AttachCwdGetFiles(self):
        combined_obj = Namespace(extensions=['.py'], is_folder=True, names=None, debug_mode=False)
        result = False

        get_all_dir_files_mock = mock.Mock(return_value=['FILE.py'])

        with mock.patch('os.getcwd', mock.Mock(return_value='FILEPATH')):
            with mock.patch('todocli.todo_cli.get_all_dir_files', get_all_dir_files_mock):

                result = attach_cwd_get_files(combined_obj)

        #get_all_dir_files_mock.assert_called_once()
        assert isinstance(result, Namespace)
        assert result.names == ['FILE.py']

    def test_AttachCwdGetFilesNotFolder(self):
        combined_obj = Namespace(extensions=['.py'], is_folder=False, names=None, debug_mode=False)
        result = False

        attach_working_dir_mock = mock.Mock(return_value=combined_obj)

        with mock.patch('todocli.todo_cli.attach_working_dir', attach_working_dir_mock):
                result = attach_cwd_get_files(combined_obj)

        #get_all_dir_files_mock.assert_called_once()
        assert isinstance(result, Namespace)
        assert result.is_folder == False
        assert result.names == None
        
    def test_ReadCommentsAndPrint(self):
        combined_obj = Namespace(extensions=['.py'], is_folder=True, names=None, debug_mode=False)
        files_mock = [File('FILENAME', [Comment(4, 'COMMENT')])]
        read_comments_in_files_mock = mock.Mock(return_value=files_mock)

        print_out_mock = mock.Mock()

        with mock.patch('todocli.todo_cli.read_comments_in_files', read_comments_in_files_mock):
            with mock.patch('todocli.todo_cli.print_out', print_out_mock):
                read_comments_and_print(combined_obj)

        read_comments_in_files_mock.assert_called_once_with(combined_obj.names)
        print_out_mock.assert_called_once()
        


    def test_TodoCliMainNewConfig(self):
        get_config_file_path_mock = mock.Mock(return_value='PATHTOFILE')
        start_new_config_menu_mock = mock.Mock()
        args = ['-f', 'file1', '-e', '.py', '-m', '-c']

        with mock.patch('todocli.todo_cli.get_config_file_path', get_config_file_path_mock):
            with mock.patch('todocli.todo_cli.start_new_config_menu', start_new_config_menu_mock):
                with pytest.raises(SystemExit) as err:
                    todo_cli_main(args)

                    start_new_config_menu_mock.assert_called_once()
                    get_config_file_path_mock.assert_called_once()
                    
                assert err.type == SystemExit
                assert err.value.args[0] == 0

        
    def test_TodoCliMainNoConfig(self):
        combined_obj = Namespace(extensions=['.py'], is_folder=True, names=None, debug_mode=False)
        load_mock = mock.Mock(return_value=combined_obj)
        attach_mock = mock.Mock(return_value=combined_obj)
        read_and_print_mock = mock.Mock()

        args = ['-f', 'file1', '-e', '.py', '-m']

        with mock.patch('todocli.todo_cli.load_config_combine_commands', load_mock):
            with mock.patch('todocli.todo_cli.attach_cwd_get_files', attach_mock):
                with mock.patch('todocli.todo_cli.read_comments_and_print', read_and_print_mock):
                    with mock.patch('todocli.todo_cli.get_config_file_path', mock.Mock()):
                        with pytest.raises(SystemExit) as err:
                            todo_cli_main(args)

        load_mock.assert_called_once()
        
        assert err.type == SystemExit
        assert err.value.args[0] == 0
                                
    
    def test_TodoCliMainThrow(self):
        

        get_config_file_path_mock = mock.Mock(side_effect=Exception('error!'))
        args = ['-f', 'file1', '-e', '.py', '-m']
        capturedOutput = StringIO()
        sys.stdout = capturedOutput

        with mock.patch('todocli.todo_cli.get_config_file_path', get_config_file_path_mock):
            with pytest.raises(SystemExit) as err:
                            todo_cli_main(args)
                            
        sys.stdout = sys.__stdout__
        assert capturedOutput.getvalue() == '(\'error!\',)\n'
        assert err.type == SystemExit
        assert err.value.args[0] == 1



        
