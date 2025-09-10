import math

class Vector3D:
    def _init_(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self.x = x
        self.y = y
        self.z = z
        
    def _add_(self, other: "Vector3D") -> "Vector3D":
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def _mul_(self, r: float) -> "Vector3D":
        return Vector3D(self.x * r, self.y * r, self.z * r)

    def length(self) -> float:
        return math.sqrt(self.x*2 + self.y2 + self.z*2)

    def normalize(self) -> "Vector3D":
        l = self.length()
        if l == 0:
            return Vector3D(0, 0, 0)
        return Vector3D(self.x / l, self.y / l, self.z / l)

    def _matmul_(self, other: "Vector3D") -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def _xor_(self, other: "Vector3D") -> "Vector3D":
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def _repr_(self) -> str:
        return f"Vector3D({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"
    

a = Vector3D(1, 2, 3)
b = Vector3D(4, -5, 6)

print("a =", a)
print("b =", b)

print("a + b =", a + b)
print("2 * a =", a * 2)
print("|a| =", a.length())
print("a normalizado =", a.normalize())

print("a · b =", a @ b)
print("a × b =", a ^ b)
