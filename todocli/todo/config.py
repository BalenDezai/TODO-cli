## This module is the language config object definition.
# NOTE: Only edit the end of this file unless you know what you are doing
import re

#TODO: Add the configuration for the reader in this file too

class Lang:
    def __init__(self, name, regexes):
        self.name = name # the name of the language, not used at the moment
        self.regexes = regexes # the list of regexes used for parsing comments

    def get_compiled_regexes(self):
        result = [re.compile(regex) for regex in self.regexes]
        return result

        
# Common comment regexes
POUNDSIGN_REGEX = r"#\s*(TODO.*)"
DOUBLESLASH_REGEX = r"//\s*(TODO.*)"
SINGLESLASH_REGEX = r"/\*\s*(TODO.*)\s*\*/"

## YOU CAN EDIT BELOW HERE TO ADD / MODIFY LANGUAGES

lang_list = { 
    ".py": Lang("Python", [POUNDSIGN_REGEX]),
    ".c": Lang("C", [DOUBLESLASH_REGEX, SINGLESLASH_REGEX]),
    ".cpp": Lang("C++", [DOUBLESLASH_REGEX, SINGLESLASH_REGEX]),
    ".h": Lang("C/C++ header files", [DOUBLESLASH_REGEX, SINGLESLASH_REGEX]),
    ".cs": Lang("C#", [DOUBLESLASH_REGEX])
}
