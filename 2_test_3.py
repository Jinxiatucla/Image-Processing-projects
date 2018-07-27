import numpy as np
import cv2
from scipy import ndimage

def generate_LUT(cof):
    lut = np.array([((i/255.0)**(1.0/cof))*255 for i in range(0, 256)]).astype("uint8")
    return lut

def apply_lut(img_name, lut):
    image = cv2.imread(img_name)
    comp_image = cv2.LUT(image,lut)
    return comp_image

def lut_threshold(threshold_num):
    lut = np.zeros((256, 1))
    for i in range(0,threshold_num):
        lut[i] = 0
    for j in range(threshold_num, 256):
        lut[j] = 255
    print(lut.astype("uint8"))
    return lut.astype("uint8")



def main():
    lut_thre = lut_threshold(245)
    thresholded_original_image = apply_lut('C:/Users/Jinxi/Desktop/EE211/EE211_HW2/text.png', lut_thre)
    img = cv2.imread('C:/Users/Jinxi/Desktop/EE211/EE211_HW2/text.png', 0)
    im2 = ndimage.grey_dilation(img, size=(15, 15), mode='constant')
    img3 = cv2.medianBlur(im2, 41)
    #image_2_2 = ndimage.rank_filter(im2, 500, size=(100, 100) )
    image_com = img -  img3
    thresholded_compensated_image = cv2.LUT(image_com,lut_thre)#apply_lut(image_com, lut_thre) #cv2.LUT(comp_image,lut_thre)
    hresholded_compensated_image = cv2.medianBlur(thresholded_compensated_image, 1)
    #cv2.imwrite('image_compensated.png', image_com)
    #cv2.imwrite('image_original_thresholded.png', thresholded_original_image)
    #cv2.imwrite('image_ocompensated_threshold_with_median_2.png', hresholded_compensated_image)
    cv2.imshow('0',image_com)
    #cv2.imshow('1',image_com)
    cv2.imshow('2',thresholded_compensated_image)

    cv2.waitKey(0)


if __name__ == "__main__":
        main()