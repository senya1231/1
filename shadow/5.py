import math

class RectangularTriangle:
    def __init__(self, side_a, side_b):
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Стороны должны быть положительными числами")
        self.a = float(side_a)
        self.b = float(side_b)

    @property
    def c(self):
        return math.sqrt(self.a**2 + self.b**2)

    def scale_sides(self, percent):
        """
        Изменение размера сторон на заданный процент.
        percent > 0 — увеличение, percent < 0 — уменьшение.
        """
        factor = 1 + (percent / 100)
        if factor <= 0:
            raise ValueError("Результат масштабирования должен быть больше нуля")
        self.a *= factor
        self.b *= factor

    def get_circumradius(self):
        """
        Вычисление радиуса описанной окружности.
        Для прямоугольного треугольника R = гипотенуза / 2.
        """
        return self.c / 2

    def get_perimeter(self):
        """Вычисление периметра."""
        return self.a + self.b + self.c

    def get_angles(self):
        """
        Определение значений углов в градусах.
        Возвращает кортеж (угол_A, угол_B, 90).
        """
        angle_a = math.degrees(math.atan(self.a / self.b))
        angle_b = 90.0 - angle_a
        return round(angle_a, 2), round(angle_b, 2), 90.0

    def __str__(self):
        return f"Треугольник: катет_a={self.a:.2f}, катет_b={self.b:.2f}, гипотенуза={self.c:.2f}"

try:
    triangle = RectangularTriangle(3, 4)
    print(triangle)
    
    print(f"Периметр: {triangle.get_perimeter():.2f}")
    print(f"Радиус описанной окружности: {triangle.get_circumradius():.2f}")
    print(f"Углы (в градусах): {triangle.get_angles()}")

    print("\nУвеличиваем стороны на 10%...")
    triangle.scale_sides(10)
    print(triangle)
    print(f"Новый периметр: {triangle.get_perimeter():.2f}")
    print(f"Новые углы: {triangle.get_angles()}")

except ValueError as e:
    print(f"Ошибка: {e}")