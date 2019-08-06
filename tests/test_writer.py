from todocli.todo.writer import print_out
from  todocli.todo.utils.comment import Comment
from io import StringIO
import sys

class TestWriter(object):

    def test_PrintOut(self, capsys):
        count = 0
        comments = []
        while count < 2:
            comments.append(Comment('FileNumber' + str(count), str(count), "TODO NUMBER: " + str(count)))
            count += 1

        stringToTest = ''
        for comment in comments:
            stringToTest += comment.filename + " " + comment.line + ":\t\t" + comment.text + "\n"

        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        print_out(comments)
        sys.stdout = sys.__stdout__
        assert capturedOutput.getvalue() ==  stringToTest