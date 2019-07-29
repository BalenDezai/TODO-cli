import re
import os
from todo.comment import Comment
from todo.config import lang_list

#   this is the module to read the files and find the comments in them

def read_comments_in_files(file_names):
    found_comments = []
    for fname in file_names:
        linenum = 0
        file = open(fname, "r")
        file_extension = os.path.splitext(fname)[1].lower()
        regex_list = lang_list[file_extension].get_compiled_regexes()
        for line in file:
            linenum += 1
            for regex in regex_list:
                match = re.search(regex, line)
                if match:
                    found_comments.append(Comment(fname, linenum, match.group(1)))
        file.close()
    return found_comments

def read_files(files_to_read):
    
    # if no file or folder is specified, use current working directory
    if files_to_read.names is None:
        files_to_read.names = [os.getcwd()]
        files_to_read.is_folder = True

    # Get correct filenames if we got the dir name instead
    if files_to_read.is_folder:
        folders = files_to_read.names
        files = []
        if (files_to_read.debug_mode):
            print(folders)
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
                if (fname.lower().endswith(tuple(files_to_read.extensions))):
                    files.append(fname)
        files_to_read.names = files
        if (files_to_read.debug_mode):
            print(files_to_read.names)
    
    comments = read_comments_in_files(files_to_read.names)
    return comments
