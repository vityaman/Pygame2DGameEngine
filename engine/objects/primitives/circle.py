from pygame.math import Vector2


class Circle:
    def __init__(self, center: Vector2, radius: float):
        self.center = center
        self.radius = radius

    def collide_point(self, point: Vector2) -> bool:
        return self.center.distance_to(point) <= self.radius
