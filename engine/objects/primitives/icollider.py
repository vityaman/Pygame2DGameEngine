from abc import ABC, abstractmethod

from engine.objects.primitives.vector2d import Vector2D


class ICollider(ABC):
    @abstractmethod
    def collides_with(self, other: 'ICollider') -> bool:
        raise NotImplementedError()

    @property
    @abstractmethod
    def position(self) -> Vector2D:
        raise NotImplementedError()

    @position.setter
    @abstractmethod
    def position(self, position: Vector2D):
        raise NotImplementedError()

    @abstractmethod
    def shift_to_collide_with(self, other: 'ICollider') -> Vector2D:
        raise NotImplementedError()

