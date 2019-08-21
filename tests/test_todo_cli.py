from todocli.todo_cli import *

class TestMain(object):
    def test_GetConfigFilePath(self):
        filePath = get_config_file_path('/folder')
        assert filePath == 'hej'