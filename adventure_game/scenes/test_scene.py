import math
from random import randint

import pygame
from pygame.color import Color

from engine.objects.entities.elasticbody import ElasticBody
from engine.objects.entities.icollidable import ICollidable
from engine.objects.entities.ientity import IEntity
from engine.objects.entities.iupdatable import IUpdatable
from engine.objects.entities.kineticbody import KineticBody
from engine.objects.entities.wall import Wall
from engine.objects.primitives.drawable import RectangleDrawable, Image, OffsetCircleDrawable
from engine.objects.primitives.rectangle import Rectangle
from engine.objects.primitives.rectanglecollider import RectangleCollider
from engine.objects.primitives.vector2d import Vector2D, sign
from engine.scenes.extended_scene import ExtendedScene


class TestScene(ExtendedScene):
    def start(self):
        W, H = self.screen.get_size()
        T = 60
        WALLS_COLOR = (randint(0, 255), randint(0, 255), randint(0, 255))

        image = Image('adventure_game\\res\\player\\hd1.png')
        image.scale(Vector2D(64, 64))
        image.set_transparent_color(Color(255, 255, 255))
        self.player = KineticBody(collider=RectangleCollider(Rectangle(W // 2, H // 2, 64, 64)),
                                  drawable=image,
                                  mass=5,
                                  velocity=Vector2D(0, 0),
                                  acceleration=Vector2D(0, 1))


        self.kinetic_bodies: list[KineticBody] = [
            self.player
        ]

        self.elastic_bodies = []

        self.collidables: list[ICollidable] = [
            Wall(RectangleCollider(Rectangle(0, 0, W, T)),
                 RectangleDrawable(W, T, Color(*WALLS_COLOR))),

            Wall(RectangleCollider(Rectangle(0, H - T, W, T)),
                 RectangleDrawable(W, T, Color(*WALLS_COLOR))),

            Wall(RectangleCollider(Rectangle(0, T, T, H - T - T)),
                 RectangleDrawable(T, H - T - T, Color(*WALLS_COLOR))),

            Wall(RectangleCollider(Rectangle(W - T, T, T, H - T - T)),
                 RectangleDrawable(T, H - T - T, Color(*WALLS_COLOR))),

            self.player
        ]

        self.not_elastic_collidables = [] + self.collidables

        self.updatables: list[IUpdatable] = [
            self.player
        ]

        image = Image('adventure_game\\res\\test\\bg1.jpg')
        image.scale(Vector2D(W, H))
        self.entities: list[IEntity] = [
            Wall(RectangleCollider(Rectangle(0, 0, W, H)),
                 image)
        ] + self.collidables

        for _ in range(5):
            r = randint(40, 60)
            x, y = randint(T + T, W - T - T), randint(T + T, H - T - T)
            v = Vector2D(randint(-30, 30), randint(-30, 30))
            color = Color(randint(0, 255), randint(0, 255), randint(0, 255))

            ball = ElasticBody(RectangleCollider(Rectangle(x, y, 2 * r, 2 * r)),
                               OffsetCircleDrawable(r, color, offset=Vector2D(r, r)),
                               mass=r * 2, velocity=v, acceleration=Vector2D(0, 1))

            self.kinetic_bodies.append(ball)
            self.elastic_bodies.append(ball)
            self.entities.append(ball)
            self.collidables.append(ball)
            self.updatables.append(ball)

        for i in range(len(self.elastic_bodies)):
            for j in range(i + 1, len(self.elastic_bodies)):
                if self.elastic_bodies[i].collides_with(self.elastic_bodies[j]):
                    raise Exception('NOPE')

    def handle_events(self, events: list):
        for event in events:
            if event.type == pygame.QUIT:
                self.close()

    def handle_controls(self, pressed: dict, mouse):
        self.player.velocity.set(0, 0)
        V = 15

        if pressed[pygame.K_d]:
            self.player.velocity.x = V
        if pressed[pygame.K_a]:
            self.player.velocity.x = -V
        if pressed[pygame.K_w]:
            self.player.velocity.y = -V
        if pressed[pygame.K_s]:
            self.player.velocity.y = V

    def update(self, dt: int):
        for updatable in self.updatables:
            updatable.update()

        for e in self.elastic_bodies:
            if e.velocity.x > 50:
                e.velocity.x = 50
            if e.velocity.y > 50:
                e.velocity.y = 50

        KineticBody.handle_collisions_of_all(self.kinetic_bodies, self.collidables)
        ElasticBody.handle_elastic_collisions_of_all(self.elastic_bodies, self.not_elastic_collidables)

        print(sum(e.mass * e.velocity.length for e in self.elastic_bodies))

    def draw(self):
        self.screen.fill((255, 255, 255))

        for entity in self.entities:
            entity.draw(self.screen)

    def finish(self):
        pass
