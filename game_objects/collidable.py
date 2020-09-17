from abc import ABC, abstractmethod


class Collidable(ABC):
    def collide(self, other):
        return self.get_rect().colliderect(other.get_rect())

    @abstractmethod
    def on_collide(self, other):
        pass

    @abstractmethod
    def get_rect(self):
        pass


def get_collided(collidable: Collidable, collidables: list):
    collided = []
    for c in collidables:
        if collidable.collide(c):
            collided.append(c)
    return collided
