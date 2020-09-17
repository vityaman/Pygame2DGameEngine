from abc import ABC, abstractmethod
from bisect import insort
from game_objects.collidable import get_collided, Collidable
from game_objects.movable_object import side_from, Direction, MovableObject
import pygame
import settings


class Camera:
    def __init__(self, player, width: int, height: int):
        self.player = player
        self.rect = pygame.rect.Rect(0, 0, width, height)
        self.rect.centerx = player.rect.centerx
        self.rect.centery = player.rect.centery

        self.last_dx = 0
        self.last_dy = 0

    def update(self):
        self.last_dx = self.player.rect.centerx - self.rect.centerx
        self.last_dy = self.player.rect.centery - self.rect.centery

    def sees(self, game_object):
        return self.rect.colliderect(game_object.rect)

    def draw_rect(self, canvas):
        pygame.draw.rect(canvas, (255, 0, 0), self.rect, 3)


class Scene(ABC):
    def __init__(self, window, width, height, player):
        self.window = window
        self.is_running = False

        self.game_objects = []
        self.collidable_objects = []
        self.movable_objects = []
        self.collidable_movable_objects = []

        self.player = player
        self.add_object(player)

        self.camera = Camera(player, width, height)

    @abstractmethod
    def on_start(self):
        pass

    @abstractmethod
    def on_end(self):
        pass

    @abstractmethod
    def handle_events(self, events):
        pass

    @abstractmethod
    def handle_keys(self, keys):
        pass

    def run(self):
        self.on_start()
        clock = pygame.time.Clock()
        self.is_running = True
        while self.is_running:
            clock.tick(settings.FPS)
            self.handle_events(pygame.event.get())
            self.handle_keys(pygame.key.get_pressed())

            self.move_movable_objects()
            self.update_collidable_moving_objects()

            self.camera.update()
            self.move_objects_by_camera()
            # handle game events
            self.draw_objects()
        self.on_end()

    def move_movable_objects(self):
        for obj in self.movable_objects:
            obj.move()

    def update_collidable_moving_objects(self):
        for obj in self.collidable_movable_objects:
            obj.round_intent()
            if not (obj.intent_dx or obj.intent_dy):
                continue

            obj.move_to(obj.intent_dx, obj.intent_dy)
            collided_objects = get_collided(obj, self.collidable_objects)
            obj.move_to(-obj.intent_dx, -obj.intent_dy)

            min_abs_dx = obj.intent_dx
            min_abs_dy = obj.intent_dy
            for collided in collided_objects:
                if collided == obj:
                    continue

                _dx = obj.intent_dx
                if side_from(collided, obj) == Direction.RIGHT:
                    _dx = collided.rect.right - obj.rect.left
                elif side_from(collided, obj) == Direction.LEFT:
                    _dx = collided.rect.left - obj.rect.right
                if abs(_dx) < abs(min_abs_dx):
                    min_abs_dx = _dx

                _dy = obj.intent_dy
                if side_from(collided, obj) == Direction.UP:
                    _dy = collided.rect.top - obj.rect.bottom
                elif side_from(collided, obj) == Direction.DOWN:
                    _dy = collided.rect.bottom - obj.rect.top
                if abs(_dy) < abs(min_abs_dy):
                    min_abs_dy = _dy

            if len(collided_objects) > 1 and min_abs_dx == obj.intent_dx and min_abs_dy == obj.intent_dy:
                min_abs_dx = 0
                min_abs_dy = 0
            obj.move_to(min_abs_dx, min_abs_dy)
            obj.restore_intent()

    def move_objects_by_camera(self):
        for obj in self.game_objects:
            obj.move_to(-self.camera.last_dx, -self.camera.last_dy)

    def draw_objects(self):
        for obj in self.game_objects:
            # TODO: if self.camera.sees(obj):
            obj.draw(self.window)
        pygame.display.update()

    def add_object(self, game_object):
        insort(self.game_objects, game_object)
        if isinstance(game_object, MovableObject):
            if isinstance(game_object, Collidable):
                insort(self.collidable_movable_objects, game_object)
            insort(self.movable_objects, game_object)
        if isinstance(game_object, Collidable):
            insort(self.collidable_objects, game_object)


class TestScene(Scene):
    def on_start(self):
        pass

    def on_end(self):
        pass

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.is_running = False

    def handle_keys(self, keys):
        if keys[pygame.K_ESCAPE]:
            self.is_running = False

        if keys[pygame.K_w]:
            self.player.direct(Direction.UP)
        if keys[pygame.K_s]:
            self.player.direct(Direction.DOWN)
        if keys[pygame.K_a]:
            self.player.direct(Direction.LEFT)
        if keys[pygame.K_d]:
            self.player.direct(Direction.RIGHT)

    def draw_objects(self):
        self.window.fill((0, 0, 0))
        super().draw_objects()

