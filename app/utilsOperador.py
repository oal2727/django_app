import cv2
from PIL import Image, ImageChops, ImageOps, ImageEnhance
import numpy as np
from .operationsDetector import OperatorEdge

def filterImageEdge(image,action):
    img_RGB = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    grayImage = cv2.cvtColor(img_RGB, cv2.COLOR_BGR2GRAY)
    operationBasic = OperatorEdge(grayImage) 
    if action == "OPERADOR_ROBERTS": # 1  (ready)
        filtered = operationBasic.operatorRoberts() 
    elif action == "OPERADOR_PREWITT": # 2  (ready)
        filtered = operationBasic.opertorPrewitt()
    elif action == "OPERADOR_SOBEL": # 3 read
        filtered = operationBasic.operatorSobel()
    else: # 4 
        filtered = operationBasic.operatorCanny()
    return filtered