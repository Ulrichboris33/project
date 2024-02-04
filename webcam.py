import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import concurrent.futures

# Utilisation de la webcam
url = 0  # L'indice 0 représente la première webcam. Vous pouvez ajuster cela en fonction de votre configuration.

def run1():
    cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)
    cap = cv2.VideoCapture(url)
    
    while True:
        ret, im = cap.read()
        cv2.imshow('live transmission', im)
        key = cv2.waitKey(5)
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def run2():
    cv2.namedWindow("detection", cv2.WINDOW_AUTOSIZE)
    cap = cv2.VideoCapture(url)

    while True:
        ret, im = cap.read()
        
        bbox, label, conf = cv.detect_common_objects(im)
        im = draw_bbox(im, bbox, label, conf)

        cv2.imshow('detection', im)
        key = cv2.waitKey(5)
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    print("started")
    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1 = executor.submit(run1)
        f2 = executor.submit(run2)
