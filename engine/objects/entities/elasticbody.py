from engine.objects.entities.icollidable import ICollidable
from engine.objects.entities.kineticbody import KineticBody
from engine.objects.primitives.drawable import IDrawable
from engine.objects.primitives.icollider import ICollider
from engine.objects.primitives.vector2d import Vector2D, sign


class ElasticBody(KineticBody):
    def __init__(self, collider: ICollider, drawable: IDrawable,
                 mass: float, velocity: Vector2D, acceleration: Vector2D = None):
        super().__init__(collider, drawable, mass, velocity, acceleration)

    def handle_elastic_collision_with(self, other: 'ElasticBody'):
        av, am = self.velocity, self.mass
        bv, bm = other.velocity, other.mass

        # TODO: code repeating (formula)
        self.velocity = av * (am - bm) / (am + bm)  + bv * 2 * bm / (am + bm)
        other.velocity = av * 2 * am / (am + bm) + bv * (bm - am) / (am + bm)

    @classmethod
    def handle_elastic_collisions_of_all(cls, bodies: list['ElasticBody'], obstacles: list[ICollidable]):
        # Consider all pairs of bodies to handle elastic collisions:
        for i in range(len(bodies)):
            bodies[i].collider.position += bodies[i].velocity
            for j in range(i + 1, len(bodies)):
                if bodies[i].collides_with(bodies[j]):
                    bodies[i].handle_elastic_collision_with(bodies[j])
            bodies[i].collider.position -= bodies[i].velocity

        # Handle collisions with other
        # TODO: Here we iteration trough the all Collidable objects
        # TODO: where can be a lot of ElasticBody objects
        # TODO: it can have huge affect on performance.
        # TODO: To fix this you should put list of not ElasticBodyies in args
        for body in bodies:
            for obstacle in (o for o in body.future_obstacles(obstacles)):
                # TODO: maybe code repeat? as in KineticBody.handle_collision_with(other)
                shift = body.collider.shift_to_collide_with(obstacle.collider)
                if sign(body.velocity.x) == sign(shift.x) and abs(body.velocity.x) >= abs(shift.x):
                    body.velocity.x = -body.velocity.x
                elif sign(body.velocity.y) == sign(shift.y) and abs(body.velocity.y) >= abs(shift.y):
                    body.velocity.y = -body.velocity.y
