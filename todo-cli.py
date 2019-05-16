import re
import sys


poundsign_regex = re.compile(r"#\s*(TODO.*)", re.IGNORECASE)
doubleslash_regex = re.compile(r"//\s*(TODO.*)", re.IGNORECASE) # Not used yet

# TODO: Not really a TODO, I'm just testing that the program works on itself

def main():
    # TODO: Use '-' to read from stdin instead
    filenames = sys.argv[1:]
    for fname in filenames:
        linenum = 0
        file = open(fname, "r")
        for line in file:
            linenum += 1
            # TODO: detect filetype and only use the correct regex
            match = re.search(poundsign_regex, line)
            if match:
                print(fname + "\t" + str(linenum) + ": " + match.group(0))
        file.close()


if __name__ == "__main__":
    main()
