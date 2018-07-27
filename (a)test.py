import numpy as np
import cv2


Kernel = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]


def After_sobel_filter_pixel(image, After_sobel_pixels, x, y, filter_length=3):
    i = 0
    pixel_sum = 0
    for i in range(filter_length):
        j = 0
        for j in range(filter_length):
            filter_pixel_x = x - (filter_length/2 - i)
            filter_pixel_y = y - (filter_length/2 - j)
            if filter_pixel_x >= image.shape[0]:
                filter_pixel_x -= image.shape[0]
            if filter_pixel_y >= image.shape[1]:
                filter_pixel_y -= image.shape[1]
            pixel_sum += image[filter_pixel_x][filter_pixel_y]*Kernel[i][j]
            j += 1
        i += 1
    After_sobel_pixels[x][y] = int(round(pixel_sum))


def apply_sobel_filter(image):
    filted_image = np.zeros(image.shape)
    i = 0
    for i in range(image.shape[0]):
        j = 0
        for j in range(image.shape[1]):
            After_sobel_filter_pixel(image, filted_image, i, j, filter_length=3)
            j += 1
        i += 1
    return filted_image


def main():
    image = cv2.imread('C:/Users/Jinxi/Desktop/Test_Image.pgm', 0)
    filted_image = apply_sobel_filter(image)
    cv2.imwrite("filtered_image_sobel.png", filted_image)





if __name__ == "__main__":
    main()


