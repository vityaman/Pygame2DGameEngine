from abc import abstractmethod

import pygame

from engine.scenes.scene import Scene


class ExtendedScene(Scene):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def handle_events(self, events):
        pass

    @abstractmethod
    def handle_controls(self, pressed, mouse):
        pass

    @abstractmethod
    def update(self, dt: int):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def finish(self):
        pass

    def on_start(self):
        self.start()

    def on_update(self, dt: int):
        self.handle_events(pygame.event.get())
        self.handle_controls(pygame.key.get_pressed(), pygame.mouse)
        self.update(dt)

    def on_draw(self):
        self.draw()
        pygame.display.flip()
        pygame.display.update()

    def on_finish(self):
        self.finish()


