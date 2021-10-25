import cv2 as cv
import sys


def img_show(path):
    img = cv.imread(path + "lenna.bmp")

    if img is None:
        sys.exit("Could not read the image.")

    cv.imshow("Display window", img)

    k = cv.waitKey(0)

    if k == ord("s"):
        cv.imwrite(path + "after_img/" + "lenna.bmp", img)