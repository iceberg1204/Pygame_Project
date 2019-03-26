import pygame
import random


# Class of creature (enemy).
class Creature:
    def __init__(self, name_instance, mmap, pos, hp=10, ai=None):
        self.x, self.y = pos
        self.speed = 1
        self.map = mmap  # Map class.
        self.hp = hp
        self.ni = name_instance  # Name of creature.

        # Adding AI.
        self.ai = ai
        if ai:
            ai.owner = self

        self.img = pygame.image.load('enemy.png')

    def move(self, x, y):  # Moving the creature.
        if not self.map.new_map[self.x + x][self.y + y].path:
            self.x += x
            self.y += y


class AI:
    def __init__(self):
        self.moves = [-1, 0, 1]  # List of choices for movements.

    def take_turn(self):  # Moving AI's owner.
        self.owner.move(random.choice(self.moves), random.choice(self.moves))

