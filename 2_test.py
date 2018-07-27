import cv2
import numpy as np
from scipy import ndimage
import scipy
img = cv2.imread('C:/Users/Jinxi/Desktop/EE211/EE211_HW2/text.png', 0)

kernel = np.ones((50,50), np.uint8)
#img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)
#img_dilation2 = cv2.medianBlur(img_dilation,5)
im2 = ndimage.grey_dilation(img, size=(25, 25), mode = 'constant' )

image_com = img -  im2
image_2_2 = cv2.medianBlur(image_com,1)

x, img_final = cv2.threshold(image_2_2,243,255,cv2.THRESH_BINARY,)
cv2.imshow('Input', img)
#cv2.imshow('Erosion', img_erosion)
cv2.imshow('Dilation', im2)
cv2.imshow('com-Dilation', image_2_2)
cv2.imshow('final', img_final)

cv2.waitKey(0)


