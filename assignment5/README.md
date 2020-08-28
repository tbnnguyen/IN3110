# Assignment 5

## 5.1

This script will highlight comments in the naython language as well as the print-statement.

```console
$ python3 highlighter.py naython.syntax naython.theme hello.ny
```

## 5.2

This script will highlight Python files. All syntaxes that is available for coloring are in the "_python.syntax_" file.

```console
$ python3 highlighter.py python.syntax python.theme demo.py
```

## 5.3

This script will highlight Java files. All syntaxes that is available for coloring are in the "_favorite_language.syntax_" file.

```console
$ python3 highlighter.py favorite_language.syntax favorite_language.theme demo.java
```

## 5.4

The demo file is the lyrics of Ghostbusters, so the example will search for "_Ghost_", "_ghost_" and "_call_".

```console
$ python3 grep.py grep_demo.txt Ghost ghost call --highlight
```

## 5.5

This script finds deletions and addtions made in the second file that is different from the original file. There are two different examples provided. The first is a smaller text file, and the other is lyrics from "_Old Town Road_", where the original file is the original lyrics, and the "modified" file is the remix with Billy Ray Cyrus.

```console
$ python3 diff.py diff1.txt diff2.txt
```

```console
$ python3 diff.py oldtown.txt oldtown2.txt
```

## 5.6

This script will print the text in the _diff_output.txt_ and color it based on if lines have been deleted or added. Green for added lines and red for deleted lines. 

```console
$ python3 highlighter.py diff.syntax diff.theme diff_output.txt
```
