import random
from PIL import Image

image_path = "path_to_file"
original_image = Image.open(image_path)

width, height = original_image.size
print(width, height)
image = Image.new("RGB", (width, height), "white")

num_pixels = int(input("Enter the number of pixels to develop: "))**2

pixels = [(x, y) for x in range(width) for y in range(height)]

pixels_to_develop = random.sample(pixels, num_pixels)

for x, y in pixels_to_develop:
    pixel_color = original_image.getpixel((x, y))  
    image.putpixel((x, y), pixel_color)  

image.save("new.png")