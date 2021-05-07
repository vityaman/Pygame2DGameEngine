from random import randint

import pygame
from pygame.color import Color

from engine.objects.entities.elasticbody import ElasticBody
from engine.objects.entities.icollidable import ICollidable
from engine.objects.entities.ientity import IEntity
from engine.objects.entities.iupdatable import IUpdatable
from engine.objects.entities.kineticbody import KineticBody
from engine.objects.entities.wall import Wall
from engine.objects.primitives.drawable import RectangleDrawable, Image, CircleDrawable, OffsetCircleDrawable
from engine.objects.primitives.rectangle import Rectangle
from engine.objects.primitives.rectanglecollider import RectangleCollider
from engine.objects.primitives.vector2d import Vector2D
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
                                  velocity=Vector2D(0, 0))


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

        self.entities: list[IEntity] = [
            Wall(RectangleCollider(Rectangle(0, 0, W, H)),
                 Image('adventure_game\\res\\test\\bg.jpg'))
        ] + self.collidables

    def handle_events(self, events: list):
        for event in events:
            if event.type == pygame.QUIT:
                self.close()
            if event.type == pygame.MOUSEBUTTONDOWN:
                r = randint(5, 20)
                x, y = event.pos
                v = Vector2D(randint(-20, 20), randint(-20, 20))
                color = Color(randint(0, 255), randint(0, 255), randint(0, 255))

                ball = ElasticBody(RectangleCollider(Rectangle(x, y, 2 * r, 2 * r)),
                                   OffsetCircleDrawable(r, color, offset=Vector2D(r, r)),
                                   mass=r * 2, velocity=v)

                self.kinetic_bodies.append(ball)
                self.elastic_bodies.append(ball)
                self.entities.append(ball)
                self.collidables.append(ball)
                self.updatables.append(ball)

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

        KineticBody.handle_collisions_of_all(self.kinetic_bodies, self.collidables)
        ElasticBody.handle_elastic_collisions_of_all(self.elastic_bodies, self.not_elastic_collidables)

    def draw(self):
        for entity in self.entities:
            entity.draw(self.screen)

    def finish(self):
        pass
