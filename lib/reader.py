import re

#   this is the module to read the files and find the comments in them


#   REGEX constants to find the comment
POUNDSIGN_REGEX = re.compile(r"#\s*(TODO.*)", re.IGNORECASE)
DOUBLESLASH_REGEX = re.compile(r"//\s*(TODO.*)", re.IGNORECASE) # Not used yet


def readFiles(filesToRead=[]):
    comments = []
    if len(filesToRead) >= 1:
        for fname in filesToRead:
            linenum = 0
            file = open(fname, "r")
            for line in file:
                linenum += 1
                # TODO: detect filetype and only use the correct regex
                match = re.search(POUNDSIGN_REGEX, line)
                if match:
                    comments.append(fname)
                    comments.append(fname + "\t" + str(linenum) + ": " + match.group(0))
        file.close()
        return comments