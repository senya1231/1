import math

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Сложение векторов (оператор +)
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)


    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)


    def __mul__(self, other):
        if isinstance(other, (int, float)):

            return Vector3D(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector3D):

            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise TypeError("Операция возможна только с числом или другим Vector3D")


    def __rmul__(self, other):
        return self.__mul__(other)


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):

        return (self.x, self.y, self.z) < (other.x, other.y, other.z)

    def __gt__(self, other):
        return (self.x, self.y, self.z) > (other.x, other.y, other.z)

    def __le__(self, other):
        return (self.x, self.y, self.z) <= (other.x, other.y, other.z)

    def __ge__(self, other):
        return (self.x, self.y, self.z) >= (other.x, other.y, other.z)

    def __contains__(self, other):
        return self.__eq__(other)

    def abs(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)

print(f"Вектор 1: {v1}")
print(f"Вектор 2: {v2}")
print(f"Сложение: {v1 + v2}")
print(f"Вычитание: {v1 - v2}")
print(f"Скалярное произведение: {v1 * v2}")
print(f"Умножение на скаляр (2 * v1): {2 * v1}")
print(f"Сравнение (v1 < v2): {v1 < v2}")
print(f"Длина вектора v2: {v2.abs():.2f}")