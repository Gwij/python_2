import pygame
import time
from snake import Slang

breedte = 800
hoogte = 600

spel_snelheid = 5

pygame.init()
venster = pygame.display.set_mode((breedte, hoogte))
pygame.display.set_caption('Snake')

slang = Slang(breedte // 2, hoogte // 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                slang.y_verandering = - 1 * 20
                slang.x_verandering = 0 * 20
            if event.key == pygame.K_DOWN:
                slang.y_verandering = 1 * 20
                slang.x_verandering = 0 * 20
            if event.key == pygame.K_LEFT:
                slang.y_verandering = 0 * 20
                slang.x_verandering = -1 * 20
            if event.key == pygame.K_RIGHT:
                slang.y_verandering = 0 * 20
                slang.x_verandering = 1 * 20

    venster.fill((255, 255, 255))
    slang.update()
    slang.teken(venster)
    pygame.display.update()
    time.sleep(1 / spel_snelheid)
