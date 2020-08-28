import cv2
import numpy as np
from blurPackage.blur_2 import blurImage_2_1

def blur_faces(image):
    """Detects faces and will blur the faces until it can't detect any faces
    
    Args:
        image (np.ndarray): image where the faces are to be blurred
    """
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    faces = faceCascade.detectMultiScale(image, scaleFactor=1.025, minNeighbors=5, minSize=(30, 30))

    # Continues as long as there are faces
    while isinstance(faces, np.ndarray):
        for (x, y, w, h) in faces:
            # Mapping a face on the image
            face = image[y : y + h, x : x + w, :]
            # Blurring it with vectorization function
            blurred_face = blurImage_2_1(face)
            # Replacing the old face with the blurred version
            image[y: y + h, x: x + w, :] = blurred_face
        
        # Trying to detect faces after the blurring process
        faces = faceCascade.detectMultiScale(
            image, scaleFactor=1.025, minNeighbors=5, minSize=(30, 30))

    # Saving the image and showing it
    cv2.imwrite("blurred_faces.jpg", image) 
    cv2.imshow("Blurred faces", image)
    cv2.waitKey()
  
image = cv2.imread("beatles.jpg")

blur_faces(image)
 

