import numpy as np
import cv2
from blurPackage.blur_1 import blurImage_1
from blurPackage.blur_2 import blurImage_2
from blurPackage.blur_3 import blurImage_3


np.random.seed(120)
testArray = np.random.randint(0, 255, size=(200, 200, 3))

def test_1():
    """Testing that the maximum value should be lower after the "blurring process", due to averaging of the values in the array
    """
    value = np.amax(testArray)
    arr1 = blurImage_1(testArray)
    value1 = np.amax(arr1)
    assert value > value1

    arr2 = blurImage_2(testArray)
    value2 = np.amax(arr2)
    assert value > value2

    arr3 = blurImage_3(testArray)
    value3 = np.amax(arr3)
    assert value > value3

def test_2():
    """Testing that the "blurring process" is correct, by checking the calculation on an arbitrary pixel in the image
    """
    height = 100
    width = 100
    pixel = testArray[height, width, :]

    a = testArray[height - 1, width, :]
    b = testArray[height + 1, width, :]
    c = testArray[height, width - 1, :]
    d = testArray[height, width + 1, :]
    e = testArray[height - 1, width - 1, :]
    f = testArray[height - 1, width + 1, :]
    g = testArray[height + 1, width - 1, :]
    h = testArray[height + 1, width + 1, :]

    avg = pixel + a + b + c + d + e + f + g + h / 9

    arr1 = blurImage_1(testArray)
    assert avg.all() == arr1[height, width, :].all()

    arr2 = blurImage_2(testArray)
    assert avg.all() == arr2[height, width, :].all()
    
    arr3 = blurImage_3(testArray)
    assert avg.all() == arr3[height, width, :].all()

