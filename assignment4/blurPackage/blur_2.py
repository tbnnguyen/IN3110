import cv2
import numpy as np
import time

def blurImage_2_1(src):
    src = src.astype("uint32")
    paddedImage = np.pad(src, [(1, 1), (1, 1), (0, 0)], 'edge')

    height = len(src)
    width = len(src[0])
    
    a = paddedImage[:height, :width, :]
    b = paddedImage[1:height + 1, :width, :]
    c = paddedImage[2:, :width, :]
    d = paddedImage[:height, 1:width + 1, :]
    e = paddedImage[2:, 1:width + 1, :]
    f = paddedImage[:height, 2:, :]
    g = paddedImage[1:height + 1, 2:, :]
    h = paddedImage[2:, 2:, :]
    
    dst = (src + a + b + c + d + e + f + g + h) / 9
    
    dst = dst.astype("uint8")

    return dst
    
def blurImage_2(src):
    """Pads the edges of the image, making 8 offsetting instances of the original image and combining them to blur the image
    
    Args:
        src (np.ndarray): should be a 3d array that has been converted from an image with cv2.imread()

    Returns:
        dst (np.ndarray): new ndarray that when converted back to an image with cv2 will be blurred 
    """
    
    src = src.astype("uint32")
    paddedImage = np.pad(src, [(1, 1), (1, 1), (0, 0)], 'edge')

    height = len(src)
    width = len(src[0])

    # Times the process of blurring the image, not the whole function
    t1 = time.time()
    
    # Creating 8 offsetting instances of original image
    a = paddedImage[:height, :width, :]
    b = paddedImage[1:height + 1, :width, :]
    c = paddedImage[2:, :width, :]
    d = paddedImage[:height, 1:width + 1, :]
    e = paddedImage[2:, 1:width + 1, :]
    f = paddedImage[:height, 2:, :]
    g = paddedImage[1:height + 1, 2:, :]
    h = paddedImage[2:, 2:, :]

    # Vectorizing all arrays and getting a new array with averaged values
    dst = (src + a + b + c + d + e + f + g + h) / 9

    t2 = time.time()
    print("Time taken to blur image:", round((t2-t1)*1000), "ms")

    dst = dst.astype("uint8")

    return dst

# Timing 10 runs of the function
if __name__ == '__main__':
    import timeit
    print(round(timeit.timeit("blurImage_2(cv2.imread('beatles.jpg'))", setup="from __main__ import blurImage_2, cv2", number=10), 2), "sec")