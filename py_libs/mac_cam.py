import cv2
import os
# initialize the camera
cam = cv2.VideoCapture(0)   # 0 -> index of camera

PATH = os.getcwd()


def capture_image(path):
    # video capture source camera (Here webcam of laptop)
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    ret, frame = cap.read()  # return a single frame in variable `frame`
    # cv2.imshow('img1', frame)  # display the captured image

    cv2.imwrite(path+'/data/test.jpg', frame)

    cv2.destroyAllWindows()
    cap.release()


capture_image(PATH)
