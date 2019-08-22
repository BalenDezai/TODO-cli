from todocli.todo.reader import read_comments_in_files, read_line_in_file, create_file_object, attach_working_dir, get_all_dir_files
from todocli.todo.utils.comment import Comment
from todocli.todo.utils.file import File
from unittest import mock
from argparse import Namespace
from io import StringIO
import os
import sys
import pytest

class TestReader(object):
    def test_ReadLineInFile(self):
        file_name = 'TestFile'
        regex_to_find = [r"#\s*(TODO.*)"]
        file_data = '# TODO: HELLO'
        file_data += '\nEÆREÆLRÆELRERL'
        mocked_file = mock.mock_open(read_data=file_data)
        with mock.patch('todocli.todo.reader.open', mocked_file, create=True):
            result = read_line_in_file(file_name, regex_to_find)
            assert isinstance(result, list)
            assert isinstance(result[0], Comment)
            assert result[0].line == 1
            assert result[0].comment == "TODO: HELLO"
    
    def test_ReadLieInFilesException(self):
        file_name = 'TestFileNotEixisting'
        regex_to_find = [r"#\s*(TODO.*)"]
        with pytest.raises(FileNotFoundError) as error:
            read_line_in_file(file_name, regex_to_find)
        assert error.type is FileNotFoundError
        assert error.value.args == (2, 'No such file or directory',)

    def test_CreateCommentObject(self):
        file_name = 'TestFile'
        comments = [Comment(1, 'TODO: HELLO')]
        createdFileObject = create_file_object(file_name, comments)
        
        assert isinstance(createdFileObject, File)
        assert createdFileObject.file_name == 'TestFile'
        
        assert isinstance(createdFileObject.line_and_comment, list)
        assert createdFileObject.line_and_comment[0].line == 1
        assert createdFileObject.line_and_comment[0].comment == 'TODO: HELLO'

    def test_CreateCommentObjectWithNoComments(self):
        file_name = 'TestFile'
        comments = []
        createdFileObject = create_file_object(file_name, comments)
        
        assert createdFileObject == None

    def test_ReadCommentsInFiles(self):
        file_data = '# TODO: HELLO'
        files = ['FileOne.py']
        
        open_file_mock = mock.mock_open(read_data=file_data)
        with mock.patch('todocli.todo.reader.open', open_file_mock, create=True):
            found_comments = read_comments_in_files(files)
            assert isinstance(found_comments, list)
            assert isinstance(found_comments[0], File)

            assert found_comments[0].file_name  == 'FileOne.py'
            assert found_comments[0].line_and_comment[0].line == 1
            assert found_comments[0].line_and_comment[0].comment == 'TODO: HELLO'

    def test_ReadCommentsInFilesThrowing(self):
        files = ['FileOne']
        with pytest.raises(KeyError) as error:
            read_comments_in_files(files)
        assert error.type is KeyError
        assert error.value.args == (r"No such extension is supported: ''",)

    def test_AttachWorkingDir(self):

        commandsObj = Namespace(names=None, is_folder=False)
        getcwd_mock = mock.Mock(return_value='CurrentPath')
        with mock.patch('todocli.todo.reader.os.getcwd', getcwd_mock):
            result = attach_working_dir(commandsObj)
            
            assert result.names[0] == 'CurrentPath'
            assert result.is_folder == True

    def test_AttachWorkingDirWithNames(self):
        file_names = 'Folder1'
        commandsObj = Namespace(names=file_names, is_folder=False)
        result = attach_working_dir(commandsObj)
        assert result.names == file_names
        assert result.is_folder == False

    def test_GetAllDirFiles(self):
        files_to_read = ['folder1']
        debug = False
        extensions = ['.py']
        walk_mock = mock.Mock()
        walk_mock.return_value = [
            ('folder1', ('folder2',), ('folder3',)),
            ('folder1/folder2', (), ('Hello.c', 'script.py')),
        ]
        with mock.patch('todocli.todo.reader.os.walk', walk_mock):
            files = get_all_dir_files(files_to_read, debug, extensions)
            
            assert isinstance(files, list)

            assert files[0] ==  os.path.join('folder1/folder2', 'script.py')
            walk_mock.assert_called_with('folder1')


    def test_GetAllDirFilesWithDebug(self):
        files_to_read = ['folder1']
        debug = True
        extensions = ['.py']
        walk_mock = mock.Mock()
        walk_mock.return_value = [
            ('folder1', ('folder2',), ('folder3',)),
            ('folder1/folder2', (), ('Hello.c', 'script.py')),
        ]
        with mock.patch('todocli.todo.reader.os.walk', walk_mock):
            capturedOutput = StringIO()
            sys.stdout = capturedOutput
            files = get_all_dir_files(files_to_read, debug, extensions)
            
            walk_mock.assert_called_with('folder1')
            sys.stdout = sys.__stdout__

            assert isinstance(files, list)

            assert files[0] ==  os.path.join('folder1/folder2', 'script.py')
            str_to_test = f'{files_to_read}\n'
            str_to_test += 'Files found:\n'
            str_to_test += r'folder1\folder3' + '\n'
            str_to_test += r'folder1/folder2\Hello.c' + '\n'
            str_to_test += r'folder1/folder2\script.py' + '\n'
            str_to_test += f'{files}\n'
            assert capturedOutput.getvalue() == str_to_test

    def test_GetAllDirFilesException(self):
        files_to_read = ['folder1']
        debug = True
        extensions = ['.py']
        walk_mock = mock.Mock()
        walk_mock.side_effect = OSError
        with mock.patch('todocli.todo.reader.os.walk', walk_mock):
            with pytest.raises(OSError):
                get_all_dir_files(files_to_read, debug, extensions)