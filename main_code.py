import pygame
from player import Player
from map_class import Map, Structure
from enemy import Creature, AI
from texting import Text
from invent import Chest, Key, Visor, Bomb


pygame.init()

# Initialising the window.
width = 600
size = width, width
pygame.display.set_caption('RPG')
screen = pygame.display.set_mode(size)

# Colors.
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# All objects and data about them.
ai_en = AI()
mmap = Map(1)
visor = Visor((30, 30))
key = Key((300, 210))
bomb = Bomb((540, 30))
invent = Chest(screen)
hx = 1
hy = 1
ex = 13
ey = 17
lvl = 1
hp = 50

# Everything about messages.
msg_history = []
num_msg = 3

# List of things to add to invent.
to_add = []

# Adding clocks.
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()

done = True
while done:
    pygame.time.delay(50)

    # Initialising objects.
    hero = Player('Steven', mmap, (hx, hy), hp)
    enemy = Creature('Angry_Bot_1', mmap, (ex, ey), ai=ai_en)
    OBJECTS = [hero, enemy]
    screen.fill(BLACK)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

        # Moving enemy.
        if e.type == pygame.KEYDOWN:
            for obj in OBJECTS:
                if obj.ai:
                    obj.ai.take_turn()

        # Using things from invent.
        if e.type == pygame.MOUSEBUTTONDOWN:
            mx, my = e.pos
            if my < 30 and mx > 570:
                invent.choose((mx, my))
            if invent.checked and invent.checked != visor:
                invent.throw((mx, my), mmap)
                invent.checked.added = False
            elif invent.checked and invent.checked == visor:
                seconds = (pygame.time.get_ticks() - start_ticks) / 1000
                if seconds > 5:
                    visor.can_see = False
                    visor.added = False
                invent.checked.added = False

    # Checking visor.
    if not visor.can_see:
        mmap.draw_map(screen, mmap.new_map, False)  # here
    else:
        mmap.draw_map(screen, mmap.new_map, visor.can_see)

    # Adding things to invent.
    if mmap.lvl == 4:
        if not visor.added:
            screen.blit(visor.img, (visor.x, visor.y))

        if hero.x * 30 == visor.x and hero.y * 30 == visor.y and visor not in to_add:
            visor.added = True
            to_add.append(visor)
            visor.can_see = True

    if mmap.lvl == 3:
        if not key.added:
            screen.blit(key.img, (key.x, key.y))

        if hero.x * 30 == key.x and hero.y * 30 == key.y:
            key.added = True
            to_add.append(key)
    if mmap.lvl == 2:
        if not bomb.added:
            screen.blit(bomb.img, (bomb.x, bomb.y))

        if hero.x * 30 == bomb.x and hero.y * 30 == bomb.y and bomb not in to_add:
            bomb.added = True
            to_add.append(bomb)
    hero.move()

    # Fighting player.
    if hx == ex and hy == ey:
        hp -= 10
        hero.x = 1
        hero.y = 1
        msg = ' Oh! Your hp is ' + str(hp) + '/50'
        msg_history.append(msg)

    # Making 3-line text field.
    if len(msg_history) <= num_msg:
        to_draw = msg_history
    else:
        to_draw = msg_history[-num_msg:]

    # Taking text position.
    height = 26
    text_y = (width - num_msg * height) - 5

    # Writing text.
    i = 0
    for message in to_draw:
        txt = Text(screen, message, (0, text_y + i * height), RED, BLACK)
        txt.draw_text()
        i += 1

    # Checking if player is dead.
    if hp == 0:
        done = False

    # Changing levels.
    if hero.x > 19 and mmap.lvl == 1:
        mmap = Map(2)

    elif hero.x < 0 and mmap.lvl == 2:
        mmap = Map(1)

    elif hero.y > 19 and mmap.lvl == 2:
        mmap = Map(3)

    elif hero.y < 0 and mmap.lvl == 3:
        mmap = Map(2)

    elif hero.y > 19 and mmap.lvl == 3:
        mmap = Map(4)

    elif hero.y < 0 and mmap.lvl == 4:
        mmap = Map(3)

    elif hero.x > 19 and mmap.lvl == 4:
        mmap = Map(1)

    # Drawing characters and taking their coords.
    screen.blit(enemy.img, (enemy.x * 30, enemy.y * 30))
    screen.blit(hero.img, (hero.x * 30, hero.y * 30))
    hx = hero.x
    hy = hero.y
    ex = enemy.x
    ey = enemy.y

    # Moving between levels.
    if lvl != mmap.lvl:
        if mmap.lvl == 1 and lvl == 4:
            hx = 1
            hy = hero.y
            mmap.new_map[0][9:12] = [Structure('unbreakable') for _ in range(9, 12)]
            mmap.new_map[19][8:11] = [Structure('unbreakable') for _ in range(8, 11)]
        elif mmap.lvl == 2 and lvl == 1:
            hx = 1
            hy = hero.y
            mmap.new_map[0][8:11] = [Structure('unbreakable') for _ in range(9, 12)]
        elif mmap.lvl == 2 and lvl == 3:
            hy = 19
            hx = hero.x
        elif mmap.lvl == 3 and lvl == 2:
            hy = 0
            hx = hero.x
        elif mmap.lvl == 3 and lvl == 4:
            hy = 19
            hx = hero.x
        elif mmap.lvl == 4:
            hy = 0
            hx = hero.x
        ex = 13
        ey = 17
        lvl = mmap.lvl

    # Drawing a chest.
    invent.draw()
    for i in to_add:
        if i.added:
            invent.add(i)

    pygame.display.update()

    clock.tick(60)

# Creating a 'gameover' picture.

image = pygame.image.load('gameover.jpg')

while not done and hp == 0:
    pygame.time.delay(50)

    enemy = Creature('Angry_Bot_1', mmap, (ex, ey), ai=ai_en)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = True

    mmap.draw_map(screen, mmap.new_map, False)
    screen.blit(enemy.img, (enemy.x * 30, enemy.y * 30))

    for i in range(601):
        if i == 600:
            done = True
        else:
            screen.blit(image, (i - width, i - width))
        pygame.display.update()

while done and hp == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    screen.blit(image, (0, 0))
    pygame.display.flip()

pygame.quit()
