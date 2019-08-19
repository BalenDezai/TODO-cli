from todocli.todo.reader import read_comments_in_files, read_line_in_file, create_file_object, attach_working_dir, get_all_dir_files
from todocli.todo.utils.comment import Comment
from todocli.todo.utils.file import File
from unittest import mock
import os.path
import types

class TestReader(object):
    def test_ReadLineInFile(self):
        file_name = 'TestFile'
        regex_to_find = [r"#\s*(TODO.*)"]
        file_data = '# TODO: HELLO'
        mocked_file = mock.mock_open(read_data=file_data)
        with mock.patch('todocli.todo.reader.open', mocked_file, create=True):
            result = read_line_in_file(file_name, regex_to_find)
            assert isinstance(result, list)
            assert isinstance(result[0], Comment)
            assert result[0].line == 1
            assert result[0].comment == "TODO: HELLO"

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


    def test_AttachWorkingDir(self):
        newDict = dict()
        setattr(newDict, 'names', None)
        setattr(newDict, 'is_folder', False)
        commandsObj = Namespace(**newDict)
        getcwd_mock = mock.Mock(return_value='CurrentPath')
        with mock.patch('os.getcwd.', getcwd_mock, create=True):
            result = attach_working_dir(commandsObj)
            assert result.names == 'CurentPath'