import math
def square(side):
    area = side ** 2
    rounded_area = math.ceil(area)
    return rounded_area
side_length = 5.1
area = square(side_length)
print(f"Площадь квадрата со стороной {side_length}x{area}") 