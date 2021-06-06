#!/usr/bin/env python3

import cv2
import sys
import numpy as np

def usage(eCode):
    use = """   isolate.py <path to imagefile> """
    print(use)
    exit(eCode)

# functions
def open_image(picName, grey=True, thresh=True):
    img = cv2.imread(picName)
    if thresh:
        grey = True
    if grey:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if thresh:
        img = cv2.GaussianBlur(img, (5,5), 2)
        #cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 0)
        retval, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_TRIANGLE)
    return img
    
# this does not work in a docker container without X11 forwarding 
# use save_image and then view the pictures from the host machine later
def display_image(picName, title):
    cv2.imshow(title, picName)

def save_image(picName, title):
    fileName = "post-" + title
    cv2.imwrite(picName, fileName)

def isolate_poly(img):
    img = cv2.GaussianBlur(img, (5,5),0)
    img = cv2.Canny(img, 250, 350)
    return img

def Resize(img, width=None, height=None):
    (wi, hi) = img.shape[:2]
    (w, h) = (hi, wi)
    if not width and not height:    
        return img
    if width:
        (w, h) = (width, int(h * (float(width) / w)))
    if height:
        (w, h) = (int(w * (float(height) / h)), height)
    img = cv2.resize(img, (w, h))
    return img


def main():
    if sys.argv[1][0] == '-':
        usage(0)

    # TODO add looping through a directory and running the program on all images 
    # TODO flags for using display_image vs save_image
    name = sys.argv[1]
    pic0 = open_image(name, True, True)
    pic1 = open_image(name, False, False)
    save_image(isolate_poly(pic0), str(name))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

