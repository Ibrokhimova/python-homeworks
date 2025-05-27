import math

class Vector:
    def __init__(self, *components):
        self.components = list(components)

    def __str__(self):
        return f"Vector({', '.join(map(str, self.components))})"

    def __len__(self):
        return len(self.components)

    def _check_dimension(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension.")

    def __add__(self, other):
        self._check_dimension(other)
        result = [a + b for a, b in zip(self.components, other.components)]
        return Vector(*result)

    def __sub__(self, other):
        self._check_dimension(other)
        result = [a - b for a, b in zip(self.components, other.components)]
        return Vector(*result)

    def __mul__(self, other):
        if isinstance(other, Vector):
            self._check_dimension(other)
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):
            result = [a * other for a in self.components]
            return Vector(*result)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self * other

    def magnitude(self):
        return math.sqrt(sum(a**2 for a in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        normalized = [a / mag for a in self.components]
        return Vector(*normalized)
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print(v1)              
print(v2)              
print(v1 + v2)         
print(v2 - v1)         
print(v1 * v2)         
print(3 * v1)          
print(v1.magnitude())  
print(v1.normalize())  
