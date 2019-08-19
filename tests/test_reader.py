from todocli.todo.reader import read_comments_in_files, read_line_in_file, create_comment_object, attach_working_dir, get_all_dir_files
from unittest import mock

class TestReader(object):
    def test_ReadLineInFile(self):
        file_name = 'TestFile'
        regex_to_find = [r"#\s*(TODO.*)"]
        file_data = '# TODO: HELLO'
        mocked_file = mock.mock_open(read_data=file_data)
        with mock.patch('todocli.todo.reader.open', mocked_file, create=True):
            result = read_line_in_file(file_name, regex_to_find)
