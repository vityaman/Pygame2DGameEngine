import pygame

import settings

import scene

import game_objects.drawables as drawable
from game_objects.movable_object import Direction
from game_objects.game_object import GameObject
from game_objects.collidable_movable_objects import CollidableMovableObject
from game_objects.character import Character


if __name__ == "__main__":
    pygame.init()

    window = pygame.display.set_mode((settings.WINDOW_WIDTH,
                                      settings.WINDOW_HEIGHT))
    pygame.display.set_caption(settings.WINDOW_TITLE)

    player = Character(
        rect=pygame.rect.Rect(0, 0, 100, 100),
        drawable=drawable.AnimatedImage(
            [
                drawable.load_image('res\\img\\dora.jpg', (100, 100)),
                drawable.load_image('res\\img\\dora1.jpg', (100, 100)),
                drawable.load_image('res\\img\\ulianka.png', (100, 100))
            ],
            animation_duration=27,
            shift_x=-100 // 2,
            shift_y=-100 // 2),
        layer=99,
        velocity=10,
        angle=Direction.RIGHT)
    player.rect.centerx = settings.WINDOW_WIDTH // 2
    player.rect.centery = settings.WINDOW_WIDTH // 2

    scene = scene.TestScene(window, settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT, player)
    scene.add_object(GameObject(
        rect=pygame.rect.Rect(0, 0, 500, 500),
        drawable=drawable.Image(
            drawable.load_image('res\\img\\bg.jpg', (500, 500)),
            shift_x=-500 // 2,
            shift_y=-500 // 2),
        layer=0
    ))

    scene.add_object(GameObject(
            rect=pygame.rect.Rect(500, 0, 500, 650),
            drawable=drawable.Image(
                drawable.load_image('res\\img\\uli.jpg', (500, 650)),
                shift_x=-500 // 2,
                shift_y=-650 // 2),
            layer=0
    ))

    scene.add_object(CollidableMovableObject(
            rect=pygame.rect.Rect(100, 120, 50, 50),
            drawable=drawable.Image(
                drawable.load_image('res\\img\\dora.jpg', (50, 50)),
                shift_x=-50 // 2,
                shift_y=-50 // 2),
            layer=99,
            velocity=1,
            angle=Direction.DOWN_RIGHT
    ))

    scene.add_object(CollidableMovableObject(
        rect=pygame.rect.Rect(180, 200, 50, 50),
        drawable=drawable.Image(
            drawable.load_image('res\\img\\cat.jpg', (50, 50)),
            shift_x=-50 // 2,
            shift_y=-50 // 2),
        layer=99,
        velocity=1,
        angle=Direction.UP_RIGHT
    ))

    scene.run()

    pygame.quit()
