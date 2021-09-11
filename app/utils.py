import cv2
from PIL import Image, ImageChops, ImageOps, ImageEnhance
import numpy as np
from .operationsPilow import OperationBasics1

def get_filtered_image(image,action):
    operationBasic = OperationBasics1(image) 
    if action == "OPERADOR_IDENTIDAD": # 1 ready
        filtered = operationBasic.identify() 
    elif action == "OPERADOR_INVERSO": # 2 ready
        filtered = operationBasic.reverse()
    elif action == "OPERADOR_UMBRAL": # 3  ready
	    filtered = operationBasic.umbral(50)
    elif action == "OPERADOR_UMBRAL_INVERSO": # 4 ready 
        filtered= operationBasic.umbralReverse(50)  
    elif action == "OPERADOR_UMBRAL_BINARIO": # 5  
        filtered= operationBasic.umbralBinary(80,100)
    # ------
    elif action == "OPERADOR_UMBRAL_BINARIO_INVERSO": # 6  ready
        I = operationBasic.operadorUmbralBinarioInvertido(150,200)
        filtered = image
    elif action == "OPERADOR_ESCALA_GRISES": # 7 ready
        filtered = operationBasic.escalaGrises()
    elif action == "OPERADOR_ESCALA_GRISES_INVERTIDO": # 8  ready
        operationBasic.escalaGrisesInvertido()
        filtered = image
    elif action == "OPERADOR_EXTENSION": # 9 ready
        operationBasic.operadorExtension()
        filtered = image
    elif action == "OPERADOR_REDUCCION_GRISES": # 10 ready
        operationBasic.operadorReduccionGrises()
        filtered = image
    return filtered