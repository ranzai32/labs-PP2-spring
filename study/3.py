import random
import os

arrs = 10
random_array = [random.randint(-50, 50) for _ in range(arrs)]

filename = "output4.txt"
with open(filename, "w") as file:
    for num in random_array:
        file.write(str(num) + "\n")

random_array = [max(x, 0) for x in random_array]

filename = "output5.txt"
with open(filename, "w") as file:
    for num in random_array:
        file.write(str(num) + "\n")

