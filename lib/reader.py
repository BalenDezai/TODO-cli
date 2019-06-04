import re
from lib.comment import Comment

#   this is the module to read the files and find the comments in them


# REGEX constants to find the comment
# TODO: support for multiline comments
POUNDSIGN_REGEX = re.compile(r"#\s*(TODO.*)", re.IGNORECASE)
DOUBLESLASH_REGEX = re.compile(r"//\s*(TODO.*)", re.IGNORECASE) # Not used yet
SINGLESLASH_REGEX = re.compile(r"/\*\s*(TODO.*)\s*\*/", re.IGNORECASE)
# TODO: use case-sensitive filename regexes in Linux / Mac
PYTHON_REGEX = re.compile(r".*\.py", re.IGNORECASE)
C_REGEX = re.compile(r".*\.([ch]|cpp)", re.IGNORECASE)

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


def read_files(files_to_read=[]):
    comments = []
    if len(files_to_read) >= 1:
        for fname in files_to_read:
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
