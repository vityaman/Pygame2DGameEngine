from pygame import Surface

from engine.objects.entities.icollidable import ICollidable
from engine.objects.entities.ientity import IEntity
from engine.objects.primitives.drawable import IDrawable
from engine.objects.primitives.icollider import ICollider


class Wall(ICollidable, IEntity):
    def __init__(self, collider: ICollider, drawable: IDrawable):
        self._collider: ICollider = collider
        self._drawable: IDrawable = drawable

    def collides_with(self, other: 'ICollidable') -> bool:
        return self.collider.collides_with(other.collider)

    @property
    def collider(self) -> ICollider:
        return self._collider

    def draw(self, surface: Surface):
        self._drawable.draw(surface, self.collider.position)
