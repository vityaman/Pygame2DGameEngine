from abc import ABC, abstractmethod

from engine.objects.primitives.icollider import ICollider


class ICollidable(ABC):
    @abstractmethod
    def collides_with(self, other: 'ICollidable') -> bool:
        raise NotImplementedError()

    @property
    @abstractmethod
    def collider(self) -> ICollider:
        raise NotImplementedError()
