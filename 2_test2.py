import cv2
import numpy as np
from scipy import ndimage
import scipy
img = cv2.imread('C:/Users/Jinxi/Desktop/EE211/EE211_HW2/text.png', 0)

#img_erosion = cv2.erode(img, kernel, iterations=1)
#img_dilation2 = cv2.medianBlur(img_dilation,5)
im2 = ndimage.grey_dilation(img, size=(25, 25), mode = 'constant' )

image_com = img -  im2

x, img_final = cv2.threshold(image_com,240,255,cv2.THRESH_BINARY,)
image_final2 = cv2.adaptiveThreshold(image_com,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,81,2)
cv2.imshow('Input', img)
#cv2.imshow('Erosion', img_erosion)
#cv2.imshow('Dilation', im2)
#cv2.imshow('com-Dilation', image_2_2)
cv2.imshow('final', image_final2)

cv2.waitKey(0)


