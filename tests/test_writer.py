from todocli.todo.writer import print_out
from todocli.todo.utils.comment import Comment
from todocli.todo.utils.file import File
from io import StringIO
import sys

class TestWriter(object):

    def test_PrintOut(self, capsys):
        count = 0
        comments = []
        while count < 2:
            comments.append(File('FileNumber' + str(count), [Comment(str(count), "TODO NUMBER: " + str(count))]))
            count += 1

        stringToTest = ''
        for file in comments:
            stringToTest += file.file_name + ":\n"
            for comment in file.line_and_comment:
                stringToTest +=  "\t\t" + str(comment.line) + ":\t" + comment.comment + "\n"
                
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        print_out(comments)
        sys.stdout = sys.__stdout__
        assert capturedOutput.getvalue() == stringToTest