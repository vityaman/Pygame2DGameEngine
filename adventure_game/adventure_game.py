from adventure_game.scenes.test_scene import TestScene
from engine.game import Game


class AdventureGame(Game):
    def run(self):
        TestScene(self.screen).open()

    def exit(self):
        pass
