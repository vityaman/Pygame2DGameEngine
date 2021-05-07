from engine.objects.primitives.icollider import ICollider
from engine.objects.primitives.rectangle import Rectangle
from engine.objects.primitives.vector2d import Vector2D


class RectangleCollider(ICollider):
    def __init__(self, rectangle: Rectangle):
        self.rectangle: Rectangle = rectangle

    def collides_with(self, other: ICollider) -> bool:
        if isinstance(other, RectangleCollider):
            return self.rectangle.collides_with_rectangle(other.rectangle)
        raise NotImplementedError()

    @property
    def position(self) -> Vector2D:
        return self.rectangle.left_top

    @position.setter
    def position(self, position: Vector2D):
        self.rectangle.left_top = position

    def shift_to_collide_with(self, other: 'ICollider') -> Vector2D:
        if isinstance(other, RectangleCollider):
            return self.rectangle.shift_to_intersection_with_rectangle(other.rectangle)
        raise NotImplementedError()

    # TODO: delete
    # def side_from(self, other: ICollider) -> Direction:
    #     if isinstance(other, RectangleCollider):
    #         if self.rectangle.right <= other.rectangle.left:
    #             return Direction.LEFT
    #         if self.rectangle.left >= other.rectangle.right:
    #             return Direction.RIGHT
    #         if self.rectangle.top >= other.rectangle.bottom:
    #             return Direction.DOWN
    #         if self.rectangle.bottom <= other.rectangle.top:
    #             return Direction.UP
    #         raise Exception('Undefined side!')
    #     raise NotImplementedError()
