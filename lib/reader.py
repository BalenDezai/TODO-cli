import re
import os
from lib.comment import Comment

#   this is the module to read the files and find the comments in them


# REGEX constants to find the comment
# TODO: support for multiline comments
POUNDSIGN_REGEX = re.compile(r"#\s*(TODO.*)", re.IGNORECASE)
DOUBLESLASH_REGEX = re.compile(r"//\s*(TODO.*)", re.IGNORECASE) # Not used yet
SINGLESLASH_REGEX = re.compile(r"/\*\s*(TODO.*)\s*\*/", re.IGNORECASE)

# plain text regexes for filename extensions
PYTHON_REGEX_RAW = r".*\.py$"
C_REGEX_RAW = r".*\.([ch]|cpp)$"

# TODO: use case-sensitive filename regexes in Linux / Mac
PYTHON_REGEX = re.compile(PYTHON_REGEX_RAW, re.IGNORECASE)
C_REGEX = re.compile(C_REGEX_RAW, re.IGNORECASE)

# used for checking that a filename is even valid to process, make sure it contains all the above file extensions
# also make sure all "|" are inside parenthesis for proper combining
ALL_EXTENSIONS_REGEX = re.compile("|".join([PYTHON_REGEX_RAW, C_REGEX_RAW]), re.IGNORECASE)

def get_regex_by_filename(fname):
    result = []
    # chech for Python extension
    match = re.search(PYTHON_REGEX, fname)
    if match:
        result.append(POUNDSIGN_REGEX)
        return result
    # check for C / CPP extension
    match = re.search(C_REGEX, fname)
    if match:
        result.append(DOUBLESLASH_REGEX)
        result.append(SINGLESLASH_REGEX)
        return result
    # TODO: more file extensions
    return result


def read_files(files_to_read):
    comments = []

    # Get correct filenames if we got the dir name instead
    if files_to_read.is_folder:
        folders = files_to_read.names
        files = []
        if (files_to_read.debug_mode):
            print("Files found:")
        for folder in folders:
            #   will look through the specified folder and all its sub/child folders
            #   find all the files in the foldeR and sub folders
            #   join the path of the file to the root path
            #   add the file path to the array
            fnames = [os.path.join(root_dir,file) for root_dir,sub_dir,found_files in os.walk(folder) for file in found_files]
            # Only add known source code extensions to the list
            for fname in fnames:
                if (files_to_read.debug_mode):
                    print(fname)
                match = re.search(ALL_EXTENSIONS_REGEX, fname)
                if match:
                    files.append(fname)
        files_to_read.names = files
        if (files_to_read.debug_mode):
            print(files_to_read.names)

    # Normal processing
    for fname in files_to_read.names:
        linenum = 0
        file = open(fname, "r")
        regex_list = get_regex_by_filename(fname)
        for line in file:
            linenum += 1
            for regex in regex_list:
                match = re.search(regex, line)
                if match:
                    comments.append(Comment(fname, linenum, match.group(1)))
        file.close()
    return comments
