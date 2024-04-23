# Статические методы
import math
class Square:

    # площадь треугольника через основание и высоту
    def square_triangle(self, a, h):
        self.s = 0.5*a*h
        return self.s

    @staticmethod
    def square_triangle_2(a,h):
        return 0.5*a*h

    # Площадь треугольника по стороне и двум прилежащим углам
    @staticmethod
    def square_two_adjacent_corners(a, sin_a, sin_b):
        return math.pow(a,2) * (math.sin(sin_a)*math.sin(sin_b))/2/math.sin(sin_a+sin_b)



sy = Square()
sy.square_triangle(15, 5)
print(sy.s)

print(Square.square_triangle_2(5, 12))
print(Square.square_two_adjacent_corners(12, 30, 60))
