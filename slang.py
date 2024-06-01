import pygame

veld_grootte = 20
kleur_slang = (0, 255, 0)

class Slang:
    def __init__(self, startx, starty):
        self.x = startx
        self.y = starty

        self.lijst = [(self.x, self.y)]
        self.lengte = 1

        self.x_verandering = 0
        self.y_verandering = 0

    def teken(self, venster):
        for x, y in self.lijst:
            pygame.draw.rect(venster, kleur_slang, pygame.Rect(x, y, veld_grootte, veld_grootte))

    def update(self):
        self.x += self.x_verandering
        self.y += self.y_verandering
        slang_kop = [self.x, self.y]
        self.lijst.append(slang_kop)
        if len(self.lijst) > self.lengte:
            del self.lijst[0]
