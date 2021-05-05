from abc import abstractmethod

from pygame.time import Clock
from pygame.surface import Surface


class SceneException(Exception):
    pass


class Scene:
    FPS = 60

    def __init__(self, screen: Surface):
        self.running = False
        self.screen = screen

    def open(self):
        if not self.running:
            self.on_start()
            self.running = True
            self.loop()
            self.on_finish()
        else:
            raise SceneException('Scene is already running!')

    def close(self):
        self.running = False

    def loop(self):
        self.on_start()
        clock = Clock()
        while self.running:
            dt = clock.tick(self.FPS)
            self.on_update(dt)
            self.on_draw()
        self.on_finish()

    @abstractmethod
    def on_start(self):
        pass

    @abstractmethod
    def on_update(self, dt: int):
        pass

    @abstractmethod
    def on_draw(self):
        pass

    @abstractmethod
    def on_finish(self):
        pass




