import re
import sys
import argparse
from highlighter import highlight


def grep(file, regex, highlight_text):
    """
    Takes a file and finds all matches based on what the user chooses to match
    
    Args:
        file (Str): Text from the file from which to find matches to
        regex (List): Chosen words or "regexes" to use to find matches in the text
        highlight_text (Boolean): Used as flag if you chooses to highlight matching text
    """
    color_list = ['38;5;13', '38;5;44', '38;5;229']
    regex_list = regex

    sb = ""
    regex_color_dict = {}
    index = 0

    for r in regex_list:
        # To cycle through colors
        if index == len(color_list):
            index = 0
        # Setting regex with color
        regex_color_dict[r] = color_list[index]
        index += 1

        new_regex = "^.*" + r + ".*$"
        matches = re.finditer(new_regex, file, re.M)

        for match in matches:
            line = match.group() + "\n"
            # Will ignore duplicates
            if sb.find(line) == -1:
                sb += line

    # If flag for highlight is true, use highlight-method from previous task
    if highlight_text:
        result = highlight(regex_color_dict, sb)
        print(result)
    else:
        print(sb)


def main():
    """
    Takes file, regexes and an optional --highlight flag from user and
    tries to find matches in the text file
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, default='grep_demo.txt',
                        help='the file you want to make the search in')

    parser.add_argument('regex', nargs='*', default='Ipsum',
                        help='The string you want to search for')

    parser.add_argument('--highlight', action='store_true',
                        help='Do you want to highlight the matching parts of the string (Y/N)')

    args = parser.parse_args()

    with open(args.file, 'r') as f:
        text = f.read()
        grep(text, args.regex, args.highlight)


if __name__ == '__main__':
    main()
