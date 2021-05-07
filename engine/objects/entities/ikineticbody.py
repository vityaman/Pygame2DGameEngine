from abc import ABC, abstractmethod

from engine.objects.entities.icollidable import ICollidable
from engine.objects.entities.imovable import IMovable
from engine.objects.primitives.icollider import ICollider
from engine.objects.primitives.vector2d import Vector2D


class IKineticBody(ICollidable, IMovable, ABC):
    @abstractmethod
    def update(self):
        raise NotImplementedError()

    @property
    @abstractmethod
    def mass(self) -> float:
        raise NotImplementedError()

    @property
    @abstractmethod
    def collider(self) -> ICollider:
        raise NotImplementedError()

    @abstractmethod
    def handle_collision_with(self, collidable: ICollidable):
        raise NotImplementedError()

    @abstractmethod
    def confirm_collision(self):
        raise NotImplementedError()

    @abstractmethod
    def future_obstacles(self, collidables: list[ICollidable]) -> list[ICollidable]:
        raise NotImplementedError()

    @abstractmethod
    def will_collide_with(self, collidable: ICollidable) -> bool:
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
