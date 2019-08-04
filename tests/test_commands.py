import pytest
from todocli.todo import commands

class TestCommandparser(object):
    successful_user_input = ['-f', 'file1', '-e', '.py', '-m', ]
    successfully_parsed_args = commands.command_interpreter(successful_user_input)
    no_args_parsed_args = commands.command_interpreter([])

    #   successful run
    def test_HasNamesAttribute(self):
        assert hasattr(self.successfully_parsed_args, 'names')

    def test_HasExtensionsAttribute(self):
        assert hasattr(self.successfully_parsed_args, 'extensions')
    
    def test_HasIsFolderAttribute(self):
        assert hasattr(self.successfully_parsed_args, 'is_folder')

    def test_HasNewConfigAttribute(self):
        assert hasattr(self.successfully_parsed_args, 'new_config')

    def test_FileNamePresent(self):
        assert 'file1' in self.successfully_parsed_args.names

    def test_ExtensionPresent(self):
        assert '.py' in self.successfully_parsed_args.extensions

    def test_IsFolderIsTrue(self):
        assert self.successfully_parsed_args.is_folder == True

    def test_NewConfigIsFalse(self):
        assert self.successfully_parsed_args.new_config == False
    

    #   no filename arguement
    def test_NoFileNameArguement(self):
        assert self.no_args_parsed_args.names is None

    #   no extension argument
    def test_NoExtensionsArgument(self):
        assert self.no_args_parsed_args.extensions is None
    #   no  is_folder argument
    def test_NoIsFolderArguement(self):
        assert self.no_args_parsed_args.is_folder is None
    #   no new_config argument
    def test_NoNewConfigArgeuement(self):
        assert self.no_args_parsed_args.new_config is False
    #   no debug argument
    def test_NoDebugArguement(self):
        assert self.no_args_parsed_args.debug_mode is False

    #   no file name in input
    def test_NoFileName(self):
        no_file_name_user_input = ['-f', '-e', '.py', '-m', ]
        with pytest.raises(SystemExit):
            commands.command_interpreter(no_file_name_user_input)
    
    #   No extensions in input
    def test_NoExtensions(self):
        no_extension_user_input = ['-f', 'File1', '-e', '-m', ]
        with pytest.raises(SystemExit):
            commands.command_interpreter(no_extension_user_input)