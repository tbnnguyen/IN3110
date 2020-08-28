# Assignment 4

## Running tests

To run the test install **_pytest_** and run it with:

```console
pytest
```

## Running scripts

**NB! Make sure you are in the right folder**

To run _blur_:

```console
python3 blur.py beatles.jpg blurredBeatles.jpg blur2
```

First argument is the image file to blur. Second argument is name of the blurred image that is created after the blurring process. The third argument is what method that is to be used. For more info, one can use the _-h_ flag.

#

To run _blur_faces_:

```console
python3 blur_faces.py
```

#

To run _blur_1_ / _blur_2_ / _blur_3_:

```bash
python3 blur_1.py
python3 blur_2.py
python3 blur_3.py
```

By running these scripts you can see how long it takes to run the functions 10 times.  

## Bugs

When using blur_1 or blur_3 in blur (user can choose in commandline), the blurred image apears white in the "preview window" (_cv2.imshow()_), but the saved image will be blurred (_cv2.imwrite()_).
