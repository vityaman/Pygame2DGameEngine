from pygame import Surface

from engine.objects.entities.icollidable import ICollidable
from engine.objects.entities.ientity import IEntity
from engine.objects.entities.ikineticbody import IKineticBody
from engine.objects.primitives.drawable import IDrawable
from engine.objects.primitives.icollider import ICollider
from engine.objects.primitives.vector2d import Vector2D, sign


class KineticBody(IKineticBody, IEntity):
    def __init__(self, collider: ICollider, drawable: IDrawable,
                 mass: float, velocity: Vector2D, acceleration: Vector2D = None):
        self._collider: ICollider = collider
        self._drawable: IDrawable = drawable
        self._mass: float = mass
        self._velocity: Vector2D = velocity
        self._acceleration: Vector2D = acceleration if acceleration is not None else Vector2D(0, 0)

        # position shift for collision handling
        self._position_shift = None

    @property
    def mass(self) -> float:
        return self._mass

    @property
    def collider(self) -> ICollider:
        return self._collider

    def draw(self, surface: Surface):
        self._drawable.draw(surface, self.collider.position)

    def handle_collision_with(self, collidable: ICollidable):
        shift = self.collider.shift_to_collide_with(collidable.collider)
        if (sign(self.velocity.x) == sign(shift.x) or shift.x == 0) and abs(self._position_shift.x) >= abs(shift.x):
            self._position_shift.x = shift.x
        if (sign(self.velocity.y) == sign(shift.y) or shift.y == 0) and abs(self._position_shift.y) >= abs(shift.y):
            self._position_shift.y = shift.y

    def confirm_collision(self):
        self._collider.position += self._position_shift

    def update(self):
        self.velocity += self.acceleration
        self._position_shift = self.velocity.copy()

    def collides_with(self, other: ICollidable) -> bool:
        return self.collider.collides_with(other.collider)

    def future_obstacles(self, collidables: list[ICollidable]) -> list[ICollidable]:
        self.collider.position += self.velocity
        collided = list(e for e in collidables if self.collides_with(e) and e is not self)
        self.collider.position -= self.velocity
        return collided

    def will_collide_with(self, collidable: ICollidable) -> bool:
        self.collider.position += self.velocity
        will = self.collides_with(collidable)
        self.collider.position -= self.velocity
        return will

    @property
    def velocity(self) -> Vector2D:
        return self._velocity

    @property
    def acceleration(self) -> Vector2D:
        return self._acceleration

    @velocity.setter
    def velocity(self, velocity: Vector2D):
        self._velocity = velocity

    @acceleration.setter
    def acceleration(self, acceleration: Vector2D):
        self._acceleration = acceleration

    @classmethod
    def handle_collisions_of_all(cls, bodies: list['KineticBody'], obstacles: list[ICollidable]):
        for body in bodies:
            for obstacle in body.future_obstacles(obstacles):
                body.handle_collision_with(obstacle)

            #  print(list(e for e in obstacles if body.collides_with(e) and e is not body))  # TODO DEBUG

            # TODO: bad solution
            if any(map(body.will_collide_with, obstacles)):
                body.confirm_collision()
