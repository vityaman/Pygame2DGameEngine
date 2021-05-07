import pygame
import config as cfg
from adventure_game.adventure_game import AdventureGame

if __name__ == '__main__':
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((cfg.WINDOW_WIDTH, cfg.WINDOW_HEIGHT))
    pygame.display.set_caption("Pygame2DEngine after refactoring!")

    game = AdventureGame(screen)
    game.run()

    pygame.quit()
