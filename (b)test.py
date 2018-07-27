import numpy as np
import cv2
import math

def gaussion_value(x, sigma):
   gaussion = (1.0 / (2 * math.pi * (sigma ** 2))) * math.exp(- (x ** 2) / (2 * sigma ** 2))
   return gaussion

def distance_between_filters(pt1, pt2):
    dis = np.sqrt((pt1[0]-pt2[0])**2+(pt1[1]-pt2[1])**2)
    return dis

def After_gaussion_filter_pixel(image, After_gaussion_pixels, x, y, filter_length, sigma):
    i = 0
    pixel_sum = 0
    weight_sum = 0
    for i in range(filter_length):
        j = 0
        for j in range(filter_length):
            filter_pixel_x = x - (filter_length/2 - i)
            filter_pixel_y = y - (filter_length/2 - j)
            if filter_pixel_x >= image.shape[0]:
                filter_pixel_x -= image.shape[0]
            if filter_pixel_y >= image.shape[1]:
                filter_pixel_y -= image.shape[1]
            weight = gaussion_value(distance_between_filters([filter_pixel_x, filter_pixel_y], [x, y]), sigma)
            pixel_sum += weight*image[filter_pixel_x][filter_pixel_y]
            weight_sum += weight
            j += 1
        i += 1
    After_gaussion_pixels[x][y] = int(round(pixel_sum/weight_sum))

def apply_gaussion_filter(image,filter_length, sigma):
    filted_image = np.zeros(image.shape)
    i = 0
    for i in range(image.shape[0]):
        j = 0
        for j in range(image.shape[1]):
            After_gaussion_filter_pixel(image, filted_image, i, j, filter_length, sigma)
            j += 1
        i += 1
    return filted_image

def main():
    image = cv2.imread('C:/Users/Jinxi/Desktop/Test_Image.pgm', 0)
    filted_image = apply_gaussion_filter(image, 10, 5)
    cv2.imwrite("filtered_image_gaussion_5.png", filted_image)





if __name__ == "__main__":
    main()


