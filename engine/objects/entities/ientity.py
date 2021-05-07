from abc import ABC, abstractmethod

from pygame import Surface


class IEntity(ABC):
    @abstractmethod
    def draw(self, surface: Surface):
        raise NotImplementedError()
