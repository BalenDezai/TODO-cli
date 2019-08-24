from todocli.todo.utils.bool_arg_parser import BoolArgParser
from todocli.todo.commands import command_interpreter
from argparse import Namespace

class TestBoolArgParser(object):

    def test_BoolArgParser(self):
        user_input = ['-f', 'file1', '-e', '.py', '-m', ]
        parsed_args = command_interpreter(user_input)
        
        assert isinstance(parsed_args, Namespace)

        assert hasattr(parsed_args, 'is_folder')

        assert parsed_args.is_folder == True

    def test_BoolArgParserNoInput(self):
        user_input = ['-f', 'file1', '-e', '.py']
        parsed_args = command_interpreter(user_input)

        assert isinstance(parsed_args, Namespace)

        assert hasattr(parsed_args, 'is_folder')

        assert parsed_args.is_folder == None