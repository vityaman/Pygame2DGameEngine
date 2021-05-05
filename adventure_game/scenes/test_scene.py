import pygame
from pygame.color import Color
from pygame.math import Vector2
from pygame.rect import Rect

from random import randint

from engine.objects.entities.animated_character import AnimatedCharacter
from engine.objects.entities.ball import Ball
from engine.objects.entities.wall import Wall
from engine.objects.handlers.collisions_handler import CollisionsHandler
from engine.objects.handlers.physics_handler import PhysicsHandler
from engine.objects.primitives.drawable import Animation, Image, RectangleDrawable
from engine.scenes.extended_scene import ExtendedScene


class TestScene(ExtendedScene):
    def start(self):
        W = self.screen.get_width()
        H = self.screen.get_height()

        G_VECTOR = Vector2(0, 1)

        self.collisions_handler = CollisionsHandler()
        self.physics_handler = PhysicsHandler()

        self.bg = Image.make('adventure_game\\res\\test\\bg.jpg')
        self.wall_right = Wall(
            collider=Rect(W - 80, 0, 80, H),
            drawable=RectangleDrawable(80, H, Color(255, 255, 125))
        )
        self.wall_left = Wall(
            collider=Rect(0, 0, 80, H),
            drawable=RectangleDrawable(80, H, Color(255, 255, 125))
        )
        self.wall_up = Wall(
            collider=Rect(0, 0, W, 80),
            drawable=RectangleDrawable(W, 80, Color(255, 255, 125))
        )
        self.wall_down = Wall(
            collider=Rect(0, H - 80, W, 80),
            drawable=RectangleDrawable(W, 80, Color(255, 255, 125))
        )

        self.wall_1 = Wall(
            collider=Rect(220, 60, 50, 50),
            drawable=RectangleDrawable(50, 50, Color(255, 255, 125))
        )
        self.wall_2 = Wall(
            collider=Rect(100, 179, 50, 50),
            drawable=RectangleDrawable(50, 50, Color(255, 255, 125))
        )

        self.collisions_handler.add(self.wall_right)
        self.collisions_handler.add(self.wall_left)
        self.collisions_handler.add(self.wall_up)
        self.collisions_handler.add(self.wall_down)
        self.collisions_handler.add(self.wall_1)
        self.collisions_handler.add(self.wall_2)

        self.physics_handler.add(self.wall_right)
        self.physics_handler.add(self.wall_left)
        self.physics_handler.add(self.wall_up)
        self.physics_handler.add(self.wall_down)
        self.physics_handler.add(self.wall_1)
        self.physics_handler.add(self.wall_2)

        self.balls = [Ball(randint(70, 1800), randint(70, 800), randint(5, 40),
                           v=Vector2(randint(-15, 15), randint(-15, 15)),
                           a=None)
                      for _ in range(10)]
        for ball in self.balls:
            self.physics_handler.add(ball)
            self.collisions_handler.add(ball)

        self.player = AnimatedCharacter(
            collider=Rect(0, 0, 80, 80),
            animation_right=Animation([
                Image.make('adventure_game\\res\\player\\hr1.png', (80, 80), (255, 255, 255)),
                Image.make('adventure_game\\res\\player\\hr2.png', (80, 80), (255, 255, 255)),
                Image.make('adventure_game\\res\\player\\hr1.png', (80, 80), (255, 255, 255)),
                Image.make('adventure_game\\res\\player\\hr2.png', (80, 80), (255, 255, 255))
            ], 5),
            animation_left=Animation([
                Image.make('adventure_game\\res\\player\\hl1.png', (80, 80), (255, 255, 255)),
                Image.make('adventure_game\\res\\player\\hl2.png', (80, 80), (255, 255, 255)),
                Image.make('adventure_game\\res\\player\\hl1.png', (80, 80), (255, 255, 255)),
                Image.make('adventure_game\\res\\player\\hl2.png', (80, 80), (255, 255, 255))
            ], 5),
            animation_up=Animation([
                Image.make('adventure_game\\res\\player\\hu1.png', (80, 80), (255, 255, 255)),
                Image.make('adventure_game\\res\\player\\hu2.png', (80, 80), (255, 255, 255)),
                Image.make('adventure_game\\res\\player\\hu1.png', (80, 80), (255, 255, 255)),
                Image.make('adventure_game\\res\\player\\hu3.png', (80, 80), (255, 255, 255))
            ], 5),
            animation_down=Animation([
                Image.make('adventure_game\\res\\player\\hd1.png', (80, 80), (255, 255, 255)),
                Image.make('adventure_game\\res\\player\\hd2.png', (80, 80), (255, 255, 255)),
                Image.make('adventure_game\\res\\player\\hd1.png', (80, 80), (255, 255, 255)),
                Image.make('adventure_game\\res\\player\\hd3.png', (80, 80), (255, 255, 255))
            ], 5))
        self.player.collider.centerx = W // 2
        self.player.collider.centery = H // 2
        # self.player.a = G_VECTOR
        self.is_player_jumping = False
        self.collisions_handler.add(self.player)
        self.physics_handler.add(self.player)

    def handle_events(self, events: list):
        for event in events:
            if event.type == pygame.QUIT:
                self.close()

    def handle_controls(self, pressed: dict, mouse):
        v_vec = Vector2(0, 0)
        v = 10

        if pressed[pygame.K_d]:
            v_vec += Vector2(v, 0)
        if pressed[pygame.K_a]:
            v_vec += Vector2(-v, 0)
        if pressed[pygame.K_w]:
            v_vec += Vector2(0, -v)
        if pressed[pygame.K_s]:
            v_vec += Vector2(0, +v)
        # if pressed[pygame.K_q]:
        #     v_vec += Vector2(0, -2 * v)

        self.player.set_movement(v_vec)

        if pressed[pygame.K_SPACE]:
            input()

    def update(self, dt: int):
        for ball in self.balls:
            ball.update()
        self.player.update()
        self.physics_handler.handle_physics()
        self.collisions_handler.handle_movables()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.bg.draw(self.screen, Vector2(0, 0))

        self.wall_up.draw(self.screen)
        self.wall_down.draw(self.screen)
        self.wall_right.draw(self.screen)
        self.wall_left.draw(self.screen)
        self.wall_1.draw(self.screen)
        self.wall_2.draw(self.screen)

        for ball in self.balls:
            ball.draw(self.screen)

        self.player.draw(self.screen)

    def finish(self):
        pass
