import numpy as np
import cv2

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
        lut[j] = j

    return lut.astype("uint8")



def main():
    lut = generate_LUT(3.5)
    comp_image = apply_lut('C:/Users/Jinxi/Desktop/EE211/EE211_HW2/text.png', lut)
    lut_thre = lut_threshold(100)
    thresholded_original_image = apply_lut('C:/Users/Jinxi/Desktop/EE211/EE211_HW2/text.png', lut_thre)
    thresholded_compensated_image = cv2.LUT(comp_image,lut_thre)
    cv2.imshow('image',comp_image)
    cv2.imshow('image_original_threshold', thresholded_original_image)
    cv2.imshow('image_ocompensated_threshold', thresholded_compensated_image)
    cv2.waitKey(0)


if __name__ == "__main__":
        main()