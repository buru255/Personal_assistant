import numpy as np
import cv2
import requests
def open_mobile_camera():
    
    # multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

    #https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    #https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    url="http://192.168.1.14:8080/shot.jpg"

    while 1:
        img_resp = requests.get(url)
        img_arr = np.array(bytearray(img_resp.content),dtype=np.uint8)
    
        img = cv2.imdecode(img_arr,-1)

    
   
        cv2.imshow('img',img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


