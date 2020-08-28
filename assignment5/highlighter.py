import re
import sys

def format_text(text, color, tmp_color):
    """
    Takes text and a code (can be color) and formats the text

    Args:
        text (Str): The text that should be formatted
        color (Str): Code for how the text should be formatted, mostly used for coloring

    Returns:
        Str: New text that is now formatted
    """
    start_code = "\033[{}m".format(color)
    end_code = tmp_color
    return start_code + text + end_code


def highlight(syntax_color_dict, text_to_color):
    """
    Takes a string and color all corresponding syntaxes that matches the given dictionary

    Args:
        syntax_color_dict (dict): Dictionary containing what synatx should have what color
        text_to_color (Str): Text to be highlighted based on the dictionary

    Returns:
        Str: Formatted text matching color and syntax given from the dictionary
    """
    for syntax in syntax_color_dict:
        matches = re.finditer(syntax, text_to_color, re.M)
        # Casting to list so it can be reversed
        for match in reversed(list(matches)):
            tmp_color = "\033[0m"
            start = match.start()
            end = match.end()

            test = re.search("\\033\[\d\d;\d;(\d+)m.+{}.+\\033\[0m".format(text_to_color[start:end]), text_to_color)
            if test != None:
                tmp = re.search("\\033\[\d\d;\d;(\d+)m", test.group())
                tmp_color = tmp.group()

            colored_text = format_text(text_to_color[start:end], syntax_color_dict.get(syntax), tmp_color)
            text_to_color = text_to_color[:start] + colored_text + text_to_color[end:]
    return text_to_color

def matchSyntaxAndColor(syntax, theme):
    """
    Matches the syntax to color based on the two dictionaries given

    Args:
        syntax (dict): Syntax dictionary given
        theme (dict): Theme dictionary given

    Returns:
        Dict: Dictionary containing syntax as key and theme as content
    """
    syntax_and_color_dict = {}
    for e in syntax:
        for i in theme:
            if syntax.get(e) == i:
                syntax_and_color_dict[e] = theme.get(i)
    return syntax_and_color_dict


def main():
    """
    Retrieves files from commandline and converts them to the final dictionary with color and syntax.
    Then opens and send the file to be highlighted and prints the final result.
    """
    syntax = read_syntax_file(sys.argv[1])
    theme = read_theme_file(sys.argv[2])

    syntax_color_dict = matchSyntaxAndColor(syntax, theme)

    with open(sys.argv[3], 'r') as f:
        highlighted_text = highlight(syntax_color_dict, f.read())
        print(highlighted_text)


def read_syntax_file(regex_file):
    """
    Takes a file conataining regex to indetify syntax of a language, and puts it in a dictionary

    Args:
        regex_file (File): File of type syntax

    Returns:
        dict: Dictionary containing the regex to identify syntax
    """
    syntax_dict = {}
    with open(regex_file, 'r') as rf:
        for line in rf.readlines():
            regex, name = line.rsplit(':', 1)
            syntax_dict[regex.strip('\"')] = name.strip()
    return syntax_dict


def read_theme_file(color_file):
    """
    Takes a file containing info about what part of syntax should have what color

    Args:
        color_file (File): Info about what color the syntax should have

    Returns:
        dict: Dictionary with the color matching the syntax
    """
    color_dict = {}
    with open(color_file, 'r') as cf:
        for line in cf.readlines():
            color, name = line.split(':', 1)
            color_dict[color.strip()] = name.strip()
    return color_dict


if __name__ == '__main__':
    main()
