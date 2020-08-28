import sys
import re
from highlighter import highlight

def diff(file1, file2):
    """
    Compares 2 files and finds out changes (additions & deletions)

    Args:
        file1 (File): Original file
        file2 (File): Modified file

    Returns:
        Str: Modified string that now show unchanged, added and deleted lines
    """
    sb = ""

    f1 = file1.read()
    f2 = file2.read()

    line1 = re.split("\n", f1)
    line2 = re.split("\n", f2)

    for line in line1:
        if re.search(line,f2) == None:
            sb += "- " + line + "\n"
        else:
            sb += "0 " + line + "\n"
    for line in line2:
        if re.search(line,f1) == None:
            sb += "+ " + line + "\n"
    return sb

def main():
    org = open(sys.argv[1], 'r')
    mod = open(sys.argv[2], 'r')

    out = open("diff_output.txt", "w+")
    out.write(diff(org, mod))


if __name__ == '__main__':
    main()
