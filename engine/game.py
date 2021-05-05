from abc import abstractmethod
from pygame.surface import Surface


class Game:
    def __init__(self, screen: Surface):
        self.running = True
        self.screen = screen

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def exit(self):
        pass
