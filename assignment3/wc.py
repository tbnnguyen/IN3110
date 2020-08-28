import sys
import os 

def fileInfo(fn):
    """
    fileInfo Counts the lines, words and characters and prints it.
    
    Args:
        fn (String): Filename that the function shall count lines, words and characters.
    """
    words = 0
    lines = 0
    chars = 0
    with open(fn) as f:
        for line in f:
            lines += 1
            words += len(line.split())
            for char in line:
                if char != " " and char != "\n":
                    chars += 1
    print("Lines:", lines, "\nWords:", words, "\nCharacters:", chars, "\nFilename:", fn)

def printInfo():
    """
    printInfo Goes through all files in the directory and uses fileInfo() to print info.
    """
    for item in os.listdir():
        fileInfo(item)

def main():
    """
    main Depending on the output, gives an error message or calls corresponding function.
    """
    # No argument passed
    if len(sys.argv) <= 1:
        print("Index error")
    # To print all info on all files
    elif sys.argv[1] == "*":
        printInfo()
    # Prints all files that ends with argument passed.
    else:
        for file in os.listdir():
            if file.endswith(sys.argv[1]):
                fileInfo(file)

main()

