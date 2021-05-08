import math


def sign(n: float) -> int:
    if n != 0:
        return n / abs(n)
    return 0


class Vector2D:
    INF = 10e10

    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

    def set(self, x: float, y: float):
        self.x = x
        self.y = y

    def increase(self, x: float, y: float):
        self.x += x
        self.y += y

    def as_tuple(self) -> tuple[float, float]:
        return self.x, self.y

    def normalize(self):
        ln = self.length
        self.x /= ln
        self.y /= ln

    def normalized(self) -> 'Vector2D':
        res = self.copy()
        res.normalize()
        return res

    def rotate(self, angle: float):
        self.x = self.x * math.cos(angle) - self.y * math.sin(angle)
        self.y = self.x * math.sin(angle) + self.y * math.cos(angle)

    def rotated(self, angle: float) -> 'Vector2D':
        res = self.copy()
        res.rotate(angle)
        return res

    @property
    def length(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

    def distance_to(self, other: 'Vector2D') -> float:
        return math.sqrt((self.x - other.x) * (self.x - other.x) + (self.y - other.y) * (self.y - other.y))

    def copy(self) -> 'Vector2D':
        return Vector2D(self.x, self.y)

    def __eq__(self, other: 'Vector2D') -> bool:
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: 'Vector2D') -> bool:
        return self.x != other.x or self.y != other.y

    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other: 'Vector2D') -> 'Vector2D':
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x - other.x, self.y - other.y)

    def __isub__(self, other: 'Vector2D') -> 'Vector2D':
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, a: float) -> 'Vector2D':
        return Vector2D(self.x * a, self.y * a)

    def __imul__(self, a: float) -> 'Vector2D':
        self.x *= a
        self.y *= a
        return self

    def __truediv__(self, a: float) -> 'Vector2D':
        return Vector2D(self.x / a, self.y / a)

    def __itruediv__(self, a: float) -> 'Vector2D':
        self.x /= a
        self.y /= a
        return self

    def __neg__(self) -> 'Vector2D':
        return Vector2D(-self.x, -self.y)

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


# TODO: delete
# class Direction(Enum):
#     RIGHT       = 0
#     LEFT        = -180
#     UP          = -90
#     DOWN        = 90
#     UP_RIGHT    = -45
#     UP_LEFT     = -135
#     DOWN_RIGHT  = 45
#     DOWN_LEFT   = 135
#     UNDEFINED   = None
#
#     START_VECTOR = Vector2D(1, 0)
#     NULL_VECTOR = Vector2D(0, 0)

