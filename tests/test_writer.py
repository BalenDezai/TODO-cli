from todocli.todo.writer import print_out
from  todocli.todo.utils.comment import Comment
from io import StringIO
import sys

class TestWriter(object):

    def test_PrintOut(self, capsys):
        count = 0
        comments = []
        while count < 2:
            test = "TODO NUMBER: " + str(count)
            temp = [(str(count), test)]
            comments.append(Comment('FileNumber' + str(count), temp))
            count += 1

        stringToTest = ''
        for comment in comments:
            stringToTest += comment.filename + " " + comment.line_and_comment[0] + ":\t\t" + comment.line_and_comment[1] + "\n"

        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        print_out(comments)
        sys.stdout = sys.__stdout__
        assert capturedOutput.getvalue() ==  stringToTest