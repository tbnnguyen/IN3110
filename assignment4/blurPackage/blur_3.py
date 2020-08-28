from numba import jit
import cv2
import numpy as np
import time

def blurImage_3(src):
    """Pads the edges of the image, then blurs by averaging each pixels neighbours and and itself, uses Jit to speed up the process
    
    Args:
        src (np.ndarray): should be a 3d array that has been converted from an image with cv2.imread()

    Returns:
        dst (np.ndarray): new ndarray that when converted back to an image with cv2 will be blurred
    """
    src = src.astype('uint32')

    height = len(src)
    width = len(src[0])
    channels = len(src[0][0])

    # Pads height and width, not color channel
    src = np.pad(src, [(1, 1), (1, 1), (0, 0)], 'edge')

    # Creating empty ndarray
    dst = np.array([[[]]])
    # Sizing it as to the original image
    dst.resize((height, width, channels))

    # Times the process of blurring the image, not the whole function
    t1 = time.time()

    @jit
    def inBlur_3(src, dst, height, width, channels):
        for h in range(height):
            for w in range(width):
                for c in range(channels):
                    # Changed the formula due to padding
                    dst[h, w, c] = (src[h + 1, w + 1, c] + src[h, w + 1, c] + src[h + 2, w + 1, c]
                    + src[h + 1, w, c] + src[h + 1, w + 2, c]
                    + src[h, w, c] + src[h, w + 2, c]
                    + src[h + 2, w, c] + src[h + 2, w + 2, c]) / 9
        return dst
    
    dst = inBlur_3(src, dst, height, width, channels)

    t2 = time.time()
    print("Time taken to blur image:", round((t2-t1)*1000), "ms")

    dst.astype('uint8')

    return dst

# Timing 10 runs of the function
if __name__ == '__main__':
    import timeit
    print(round(timeit.timeit("blurImage_3(cv2.imread('beatles.jpg'))", setup="from __main__ import blurImage_3, cv2", number=10), 2), "sec")