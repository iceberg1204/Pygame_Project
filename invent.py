import pygame
from map_class import Structure


# Bomb class.
class Bomb:
    def __init__(self, t_coords):
        self.x, self.y = t_coords  # Tuple of coords.
        self.img = pygame.image.load('bomb.png')
        self.img.set_colorkey((255, 255, 255))
        self.added = False  # Variety for checking if the item is added.

    def use(self, t_coords, level):
        # Checking the type of block and breaking it if it's good.
        if level.new_map[t_coords[0] // 30][t_coords[1] // 30].path != 'unbreakable' and \
                level.new_map[t_coords[0] // 30][t_coords[1] // 30].path != 'door':
            level.new_map[t_coords[0] // 30][t_coords[1] // 30] = Structure(False)
        self.added = False


# Class for visor.
class Visor:
    def __init__(self, t_coords):
        self.x, self.y = t_coords
        self.img = pygame.image.load('visor.png')
        self.can_see = False  # Checking if visor is activated.
        self.added = False  # Checking if visor is added.

    def use(self, t_coords, level):  # We need these non-used varieties because all methods of using should be the same.
        self.can_see = True
        self.added = False


# Class of key.
class Key:
    def __init__(self, t_coords):
        self.x, self.y = t_coords
        self.img = pygame.image.load('key.png')
        self.img.set_colorkey((255, 255, 255))
        self.added = False

    def use(self, t_coords, level):
        # Checking if chosen block is a door and then opening it.
        if level.new_map[t_coords[0] // 30][t_coords[1] // 30].path == 'door':
            for i in range(0, 20):
                for j in range(0, 20):
                    if level.new_map[i][j].path == 'door' or \
                            level.new_map[i][j].path == 'hidden':
                        level.new_map[i][j] = Structure(False)
        self.added = False


# Class of invent.
class Chest:
    def __init__(self, surf):
        self.surf = surf  # Surface to draw.
        self.width = 1
        self.height = 1
        self.board = [[0] * self.width for _ in range(self.height)]
        self.left = 570
        self.top = 0
        self.cell_size = 30
        self.checked = None  # Checking if the square was chosen.
        self.subs = 0
        self.inv = []  # Items in chest.
        self.check = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4}

    def draw(self):
        pygame.draw.rect(self.surf, (0, 0, 0), (self.left, self.top, self.cell_size, self.cell_size))
        pygame.draw.rect(self.surf, (255, 255, 255), (self.left, self.top, self.cell_size, self.cell_size), 1)

    def add(self, obj):  # Adding items.
        if self.subs < 5:
            self.subs += 1
            self.inv.append(obj)

        if self.subs > 0:
            self.surf.blit(obj.img, (570, 0))

    def choose(self, mouse_pos):  # Choosing items.
        cell = (mouse_pos[0] - self.left) // self.cell_size
        self.checked = self.inv[cell]

    def throw(self, mouse_pos, level):  # Using items.
        x = mouse_pos[0] // 30 * 30
        y = mouse_pos[1] // 30 * 30
        if (x >= 0 and x <= 600) and (y >= 0 and y <= 600):
            self.checked.use((x, y), level)
        self.subs -= 1
