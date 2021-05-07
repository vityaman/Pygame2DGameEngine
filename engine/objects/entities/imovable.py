from abc import ABC, abstractmethod

from engine.objects.entities.iupdatable import IUpdatable
from engine.objects.primitives.vector2d import Vector2D


class IMovable(IUpdatable, ABC):
    @abstractmethod
    def update(self):
        raise NotImplementedError()

    @property
    @abstractmethod
    def velocity(self) -> Vector2D:
        raise NotImplementedError()

    @property
    @abstractmethod
    def acceleration(self) -> Vector2D:
        raise NotImplementedError()

    @velocity.setter
    @abstractmethod
    def velocity(self, velocity: Vector2D):
        raise NotImplementedError()

    @acceleration.setter
    @abstractmethod
    def acceleration(self, acceleration: Vector2D):
        raise NotImplementedError()
