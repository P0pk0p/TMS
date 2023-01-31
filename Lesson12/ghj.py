class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.x = y
        self.x = z

    def __str__(self):
        return  f"Vector coords: x={self.x=} y={self.y=} z={self.z=}"

    def __add__(self, other):
        res = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return res

    def __sab__(self, other):
        res = Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        return res

v1 = Vector()
v2 = Vector(1, 2, 3)
print(v1 - v2)