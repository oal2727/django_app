import cv2
import numpy as np
def get_filtered_image(image,action):
    img = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    b,g,r = cv2.split(image)
    blank = np.zeros(image.shape[:2],dtype='uint8')
    if action == "GRAYSCALE":
        filtered = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    elif action == "RED":
        filtered = cv2.merge([b,blank,blank])  
    elif action == "GREEN":
        filtered = cv2.merge([blank,g,blank])
    else:
        filtered = cv2.merge([blank,blank,r])
    return filtered

    # if action == "GRAYSCALE":
    #     cv2.cv2