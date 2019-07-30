import argparse

class BoolArgParser(argparse.Action):
    def __init__(self, option_strings, dest, nargs, **kwargs):
        super(BoolArgParser, self).__init__(option_strings, dest, nargs, **kwargs)
    
    def __call__(self, parser, namespace, values, option_string=None):
        #print('%r %r %r' % (namespace, values, option_string))
        if option_string == '-m':
            values = True
            setattr(namespace, self.dest, values)