import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageChops, ImageOps, ImageEnhance
import math

class OperatorEdge():
    def __init__(self,img):
        self.img = img

    
    def convertScale(self,sobel,deppth,kernelx=None,kernely=None):
        if sobel:
            x = cv2.Sobel(self.img, deppth, 1, 0)
            y = cv2.Sobel(self.img, deppth, 0, 1)
        else:
            x = cv2.filter2D(self.img, deppth, kernelx)
            y = cv2.filter2D(self.img, deppth, kernely)
        absX = cv2.convertScaleAbs(x)
        absY = cv2.convertScaleAbs(y)
        weight = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
        return weight

    def operatorRoberts(self): # test
        kernelx = np.array([[-1, 0], [0, 1]], dtype=int)
        kernely = np.array([[0, -1], [1, 0]], dtype=int)
        roberts = self.convertScale(False,cv2.CV_16S,kernelx,kernely)
        return roberts

    def opertorPrewitt(self):
        kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=int)
        kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=int)
        prewitt = self.convertScale(False,cv2.CV_16S,kernelx,kernely)
        return prewitt

    def operatorSobel(self):
        sobel = self.convertScale(True,cv2.CV_16S)
        return sobel

    def operatorCanny(self):# DUDONSIO FALTA GAUS
        canny = self.convertScale(True,cv2.CV_16SC1)
        edge = cv2.Canny(canny, 50, 100)
        return edge