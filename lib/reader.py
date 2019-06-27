import re
import os
from lib.comment import Comment

#   this is the module to read the files and find the comments in them


# REGEX constants to find the comment
# TODO: support for multiline comments
POUNDSIGN_REGEX = re.compile(r"#\s*(TODO.*)", re.IGNORECASE)
DOUBLESLASH_REGEX = re.compile(r"//\s*(TODO.*)", re.IGNORECASE) # Not used yet
SINGLESLASH_REGEX = re.compile(r"/\*\s*(TODO.*)\s*\*/", re.IGNORECASE)

# Specific file extension constant
PYTHON_EXT = '.py'


def get_regex_list_by_filename(fname:str):
    regex_list = []
    # chech for Python extension
    if fname.lower().endswith(PYTHON_EXT):
        regex_list.append(POUNDSIGN_REGEX)
        return regex_list
    # TODO: more file extensions
    else:
        regex_list.append(DOUBLESLASH_REGEX)
        regex_list.append(SINGLESLASH_REGEX)
        return regex_list

def read_comments_in_files(file_names):
    found_comments = []
    for fname in file_names:
        linenum = 0
        file = open(fname, "r")
        regex_list = get_regex_list_by_filename(fname)
        for line in file:
            linenum += 1
            for regex in regex_list:
                match = re.search(regex, line)
                if match:
                    found_comments.append(Comment(fname, linenum, match.group(1)))
        file.close()
    return found_comments

def read_files(files_to_read):
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
                #match = re.search(ALL_EXTENSIONS_REGEX, fname)
                #if match:
                    #files.append(fname)
                if (fname.lower().endswith(tuple(files_to_read.extensions))):
                    files.append(fname)
        files_to_read.names = files
        if (files_to_read.debug_mode):
            print(files_to_read.names)
    
    comments = read_comments_in_files(files_to_read.names)
    return comments
