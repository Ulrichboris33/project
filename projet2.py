import cv2
import matplotlib.pyplot as plt
import cvlib as cv
import urllib.request
import numpy as np
from cvlib.object_detection import draw_bbox
import concurrent.futures

url = 'http://192.168.137.56/cam-hi.jpg'
im = None


# def run1():
#     cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)
#     while True:
#         img_resp = urllib.request.urlopen(url)
#         imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
#         im = cv2.imdecode(imgnp, -1)

#         cv2.imshow('live transmission', im)
#         key = cv2.waitKey(5)
#         if key == ord('q'):
#             break

#     cv2.destroyAllWindows()

def run1():
    cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)
    
    # Utilisez 0 comme paramètre pour accéder à la webcam par défaut
    cap = cv2.VideoCapture(0)  
    
    while True:
        # Lisez le flux vidéo de la webcam
        ret, frame = cap.read()
        
        # Affichez le flux vidéo en direct
        cv2.imshow('live transmission', frame)
        
        key = cv2.waitKey(5)
        if key == ord('q'):
            break

    # Libérez les ressources après avoir quitté la boucle
    cap.release()
    cv2.destroyAllWindows()


# def run2():
#     cv2.namedWindow("detection", cv2.WINDOW_AUTOSIZE)
#     while True:
#         img_resp = urllib.request.urlopen(url)
#         imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
#         im = cv2.imdecode(imgnp, -1)

#         bbox, label, conf = cv.detect_common_objects(im)
#         im = draw_bbox(im, bbox, label, conf)

#         cv2.imshow('detection', im)
#         key = cv2.waitKey(5)
#         if key == ord('q'):
#             break

#     cv2.destroyAllWindows()



def run2():
    cv2.namedWindow("detection", cv2.WINDOW_AUTOSIZE)
    
    # Utilisez 0 comme paramètre pour accéder à la webcam par défaut
    cap = cv2.VideoCapture(0)  
    
    while True:
        # Lisez le flux vidéo de la webcam
        ret, frame = cap.read()

        # Détectez les objets dans le cadre
        bbox, label, conf = cv2.detect_common_objects(frame)
        
        # Dessinez les boîtes englobantes sur l'image
        frame = draw_bbox(frame, bbox, label, conf)

        # Affichez le résultat de la détection
        cv2.imshow('detection', frame)

        key = cv2.waitKey(5)
        if key == ord('q'):
            break

    # Libérez les ressources après avoir quitté la boucle
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    print("started")
    with concurrent.futures.ProcessPoolExecutor() as executer:
        # f1 = executer.submit(run1)
        f2 = executer.submit(run2)
