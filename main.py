import pygame
import sys

FPS = pygame.time.Clock()

from pygame.locals import *

pygame.init()  # initiates pygame

pygame.display.set_caption('Holy Knight')

WINDOW_SIZE = (600, 400)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)  # initiates the window

display = pygame.Surface((300, 200))

player_image = pygame.image.load('Bilder/player.png')
player_image.set_colorkey((255, 255, 255))

grass_image = pygame.image.load('Bilder/grass.png')
TILE_SIZE = grass_image.get_width()

dirt_image = pygame.image.load('Bilder/dirt.png')

game_map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1'],
            ['0','0','0','0','0','0','2','2','2','2','2','2','2','2','0','0','0','0','1'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1'],
            ['2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','1'],
            ['1','1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]

moving_right = False
moving_left = False

player_location = [50, 50]
player_y_momentum = 0

player_rect = pygame.Rect(player_location[0], player_location[1], player_image.get_width(), player_image.get_height())
test_rect = pygame.Rect(100, 100, 100, 50)

while True:  # game loop
    display.fill((146, 244, 255))

    tile_rect = []
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            if tile == '1':
                display.blit(dirt_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '2':
                display.blit(grass_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile != '0':
                tile_rect.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

            x += 1
        y += 1

    display.blit(player_image, player_location)


    player_y_momentum += 0.2
    player_location[1] += player_y_momentum

    player_rect.x = player_location[0]
    player_rect.y = player_location[1]



    if moving_right == True:
        player_location[0] += 4
    if moving_left == True:
        player_location[0] -= 4

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False
    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0, 0))
    pygame.display.update()
    FPS.tick(60)  # frame rate
