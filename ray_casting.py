# Для лаберинта можете попробовать закоментированные строки по типу раскоментировать: pygame.draw.line(sc, DARKGRAY, player_pos, (x, y), 2) закоментировать: if (x // TILE * TILE, y // TILE * TILE) in world_map:
                #proj_height = PROJ_COEFF / depth
                #pygame.draw.rect(sc, RED, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
                #break библиотеки ставить не надо кроме pygame
# комманды для установки библиотек и добавления venv :
# python3 -m venv venv
# pip install pygame
import pygame 
from settings import *
from map import world_map

def ray_casting(sc, player_pos, player_angle):
    cur_angle = player_angle - HALF_FOV
    xo, yo = player_pos
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for depth in range(1, MAX_DEPTH):  # Начинаем с 1, а не с 0
            x = xo + depth * cos_a
            y = yo + depth * sin_a
            #pygame.draw.line(sc, DARKGRAY, player_pos, (x, y), 2)
            if (x // TILE * TILE, y // TILE * TILE) in world_map:
                proj_height = PROJ_COEFF / depth
                pygame.draw.rect(sc, RED, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
                break
        cur_angle += DELTA_ANGEL
