import pygame
import random


# Structure class to create objects of map.
class Structure:
    def __init__(self, path):
        self.path = path


class Map:
    def __init__(self, lvl):
        # Loading images of structures.
        self.wall = pygame.image.load('wall.png')
        self.floor = pygame.image.load('floor.png')
        self.door = pygame.image.load('door.jpg')
        self.hidden = pygame.image.load('hidden.png')
        self.grass = pygame.image.load('grass.png')
        self.flower = pygame.image.load('flower.png')
        self.iron = pygame.image.load('iron.png')
        self.flower.set_colorkey((255, 255, 255))
        # Filling the map.
        self.new_map = [[Structure(False) for y in range(0, 20)] for x in range(0, 20)]
        self.lvl = lvl

        # Drawing map for each level.

        if self.lvl == 1:
            self.new_map[0] = [Structure(True) for _ in range(0, 20)]
            self.new_map[0][9:12] = [Structure('hidden') for _ in range(9, 12)]
            for i in range(8):
                self.new_map[19][i] = Structure(True)
            for i in range(11, 20):
                self.new_map[19][i] = Structure(True)
            for i in range(1, 19):
                self.new_map[i][0] = Structure(True)
                self.new_map[i][19] = Structure(True)
            self.new_map[10][10] = Structure(True)
            self.new_map[10][15] = Structure(True)
            self.new_map[1][19] = Structure('hidden')

        if self.lvl == 2:
            self.new_map[19] = [Structure(True) for _ in range(0, 20)]
            for i in range(8):
                self.new_map[0][i] = Structure(True)
            for i in range(11, 20):
                self.new_map[0][i] = Structure(True)
            for i in range(1, 19):
                self.new_map[i][0] = Structure(True)
                self.new_map[i][19] = Structure(True)
            for i in range(9, 12):
                self.new_map[i][19] = Structure(False)
            self.new_map[3][1:5] = [Structure(True) for _ in range(1, 5)]
            self.new_map[4][7:19] = [Structure(True) for _ in range(7, 19)]

        if self.lvl == 3:
            self.new_map[0] = [Structure(True) for _ in range(0, 20)]
            self.new_map[19] = [Structure(True) for _ in range(0, 20)]
            for i in range(1, 9):
                self.new_map[i][0] = Structure(True)
                self.new_map[i][19] = Structure(True)
            for i in range(12, 20):
                self.new_map[i][0] = Structure(True)
                self.new_map[i][19] = Structure(True)
            self.new_map[8][8:12] = [Structure(True) for _ in range(8, 12)]
            self.new_map[11][8:12] = [Structure(True) for _ in range(8, 12)]
            for i in range(9, 11):
                self.new_map[i][8] = Structure(True)
                self.new_map[i][11] = Structure(True)

        if self.lvl == 4:
            self.new_map[0] = [Structure(True) for _ in range(0, 20)]
            self.new_map[19][0:9] = [Structure(True) for _ in range(0, 9)]
            self.new_map[19][12:20] = [Structure(True) for _ in range(12, 20)]
            for i in range(1, 9):
                self.new_map[i][0] = Structure(True)
            for i in range(12, 20):
                self.new_map[i][0] = Structure(True)
            for i in range(0, 20):
                self.new_map[i][19] = Structure(True)
            for i in range(16, 19):
                self.new_map[i][8] = Structure(True)
                self.new_map[i][12] = Structure(True)
            self.new_map[19][9:12] = [Structure('door') for _ in range(9, 12)]

        if self.lvl == 5:
            self.new_map = [[Structure('grass') for y in range(0, 20)] for x in range(0, 20)]


    def draw_map(self, surface, obj, can_see):
        for x in range(0, 20):
            for y in range(0, 20):

                # Changing some objects for useful things.

                if obj[x][y].path == 'door':
                    surface.blit(self.door, (x * 30, y * 30))
                elif obj[x][y].path == 'hidden' and not can_see:
                    surface.blit(self.wall, (x * 30, y * 30))
                elif obj[x][y].path == 'hidden' and can_see:
                    surface.blit(self.hidden, (x * 30, y * 30))
                elif obj[x][y].path == 'unbreakable':
                    surface.blit(self.iron, (x * 30, y * 30))
                elif obj[x][y].path == 'grass':
                    surface.blit(self.grass, (x * 30, y * 30))
                    surface.blit(self.flower, (random.randint(0, 20) * 30, random.randint(0, 20) * 30))
                elif obj[x][y].path:
                    surface.blit(self.wall, (x * 30, y * 30))
                elif not obj[x][y].path:
                    surface.blit(self.floor, (x * 30, y * 30))
