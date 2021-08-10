import cv2

class ImageReader:

    def Read(self, path):
        return cv2.imread(path, cv2.IMREAD_UNCHANGED)

