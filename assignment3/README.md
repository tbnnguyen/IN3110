# Assignment 3

## 3.1 - word counter

This script can take a file(s) and will count the amount of lines, words and characters there is in a file.
The script shall be ran:
```
python3 wc.py test.txt
```
Tested an working on a Mac computer. 
To get info for all files in the directory, you shall type:
```
python3 wc.py "*"
```
And for all files of a type, ie. .py files:
```
python3 wc.py *.py
```
**Note:** The functionality for getting multiple files uses *.endsWith()*, which does include *test_complex.py* 
when trying to get info on *complex.py*.

## 3.2-3.4 - Complex numbers

All tests are in the *test_complex.py* file. To run the test you shall install **_pytest_**. In the terminal you just need to run:
```
pytest
```

The first four tests are were used before the method ```__eq__``` was implemented and therefore *addition*, *subtraction* and *conjugation* was tested by comparing to a *string*. This string is created by the *toString* method that was overwriten. 
**Note:** The string doesn't account for complex numbers containing *float* numbers. 

After the method ```__eq__```was created, the tests now compares to instanceses of *Complex()* with the correct values. The tests following includes testing for multiplication and addition, subtraction and multiplication with integers/floats and Python's complex numbers