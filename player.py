import pygame


class Player:
    def __init__(self, name, map, pos, hp=50, creature=None, ai=None, container=None, item=None):
        self.x, self.y = pos
        self.speed = 1
        self.name = name
        self.hp = hp
        self.map = map
        self.img = pygame.image.load("hero.png").convert()

        if creature:
            self.creature = creature
            creature.owner = self

        self.ai = ai
        if ai:
            self.ai.owner = self

        self.container = container
        if self.container:
            self.container.owner = self

    def move(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and \
                ((self.x <= 0) or not self.map.new_map[self.x - 1][self.y].path):
            self.x -= self.speed
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and \
                ((self.x >= 19) or not self.map.new_map[self.x + 1][self.y].path):
            self.x += self.speed
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and \
                ((self.y <= 0) or not self.map.new_map[self.x][self.y - 1].path):
            self.y -= self.speed
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and \
                ((self.y >= 19) or not self.map.new_map[self.x][self.y + 1].path):
            self.y += self.speed

    def hot_keys(self, obj, act):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            o_at_p = self.map(self.x, self.y, obj)

            for o in o_at_p:
                if o.item:
                    o.item.pick_up(act)
