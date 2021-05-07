from pygame.rect import Rect

from engine.objects.primitives.vector2d import Vector2D


class Rectangle:
    def __init__(self, left_x: float, top_y: float, width: float, height: float):
        self.left_top: Vector2D = Vector2D(left_x, top_y)
        self.width: float = width
        self.height: float = height

    @property
    def left(self) -> float:
        return self.left_top.x

    @property
    def right(self) -> float:
        return self.left_top.x + self.width

    @property
    def top(self) -> float:
        return self.left_top.y

    @property
    def bottom(self) -> float:
        return self.left_top.y + self.height

    def shift_to_intersection_with_rectangle(self, other: 'Rectangle') -> Vector2D:
        d_left = other.left - self.right    # distance from left to right >= 0
        d_right = other.right - self.left   # distance from right to left <= 0
        d_top = other.top - self.bottom     # distance from top to bottom >= 0
        d_bottom = other.bottom - self.top  # distance from bottom to top <= 0

        shift = Vector2D(Vector2D.INF, Vector2D.INF)

        if d_left >= 0:
            shift.x = d_left
        elif d_right <= 0:
            shift.x = d_right

        if d_top >= 0:
            shift.y = d_top
        if d_bottom <= 0:
            shift.y = d_bottom

        return shift

    @property
    def center(self) -> Vector2D:
        return Vector2D(self.left_top.x + self.width / 2, self.left_top.y + self.height / 2)

    def collides_with_rectangle(self, rectangle: 'Rectangle') -> bool:
        # return Rect(self.left_top.x, self.left_top.y, self.width, self.height)\
        #     .colliderect(Rect(rectangle.left_top.x, rectangle.left_top.y, rectangle.width, rectangle.height))
        # TODO: '<' or '<=' ?
        return not (self.top > rectangle.bottom or self.bottom < rectangle.top
                    or self.left > rectangle.right or self.right < rectangle.left)

    def collides_with_point(self, point: Vector2D) -> bool:
        # TODO: '<' or '<=' ?
        return self.left < point.x < self.right \
               and self.top < point.y < self.bottom
