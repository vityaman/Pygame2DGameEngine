from adventure_game.scenes.test_scene import TestScene
from engine.game import Game


class AdventureGame(Game):
    def run(self):
        while True:
            try:
                TestScene(self.screen).open()
            except Exception as e:
                print(e)

    def exit(self):
        pass
