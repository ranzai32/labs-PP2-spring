import cv2
import numpy as np
import random

def show_random_pixels(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to load image. Please check the image path.")
        return
    height, width, _ = image.shape
    num_pixels = int(input("Pixels:"))
    random_indices = random.sample(range(height * width), num_pixels)
    random_image = np.zeros_like(image)
    for i, pixel_index in enumerate(random_indices):
        row = pixel_index // width
        col = pixel_index % width
        random_image[row, col] = image[row, col]
    cv2.imshow("Random Pixels", random_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
image_path = "C:/Users/Алихан/Desktop/Безымянный1.jpeg" 
show_random_pixels(image_path)

