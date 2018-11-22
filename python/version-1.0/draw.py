
import time

from life import evolve
from life import is_alive

def draw(universe, width, height):
    grid = ''
    for y in range(0, height - 1):
        line = ''
        for x in range(0, width - 1):
            if is_alive(universe, width, x, y):
                line = line + 'X'
            else:
                line = line + ' '
        grid = grid + '\n' + line
    print(grid)

def add_ship(universe, x, y):
    universe[(y + 1) * width + (x + 0)] = True
    universe[(y + 2) * width + (x + 0)] = True
    universe[(y + 3) * width + (x + 0)] = True
    universe[(y + 4) * width + (x + 0)] = True
    universe[(y + 4) * width + (x + 1)] = True
    universe[(y + 4) * width + (x + 2)] = True
    universe[(y + 3) * width + (x + 3)] = True
    universe[(y + 0) * width + (x + 3)] = True
    universe[(y + 0) * width + (x + 1)] = True

def add_blinker(universe, x, y, start = '|'):
    if start == '|':
        universe[(y + 0) * width + (x + 1)] = True
        universe[(y + 1) * width + (x + 1)] = True
        universe[(y + 2) * width + (x + 1)] = True
    elif start == '-':
        universe[(y + 1) * width + (x + 0)] = True
        universe[(y + 1) * width + (x + 1)] = True
        universe[(y + 1) * width + (x + 2)] = True
    else:
        raise Exception('invalid blinker start orientation')

def add_block(universe, x, y):
    universe[(y + 0) * width + (x + 0)] = True
    universe[(y + 1) * width + (x + 0)] = True
    universe[(y + 0) * width + (x + 1)] = True
    universe[(y + 1) * width + (x + 1)] = True

def add_beacon(universe, x, y, type = '\\'):
    if type == '\\':
        add_block(universe, x, y)
        add_block(universe, x + 2, y + 2)
    elif type == '/':
        add_block(universe, x + 2, y)
        add_block(universe, x, y + 2)
    else:
        raise Exception('invalid beacon type')

width = 42
height = 40
total = width * height
universe = [False] * total

#add_blinker(universe, 4, 5, '|')
#add_blinker(universe, 5, 5, '-')
#----
add_blinker(universe, 3, 5, '|')
add_block(universe, 9, 9)
add_block(universe, 8, 5)
add_ship(universe, 32, 1)
#----
#add_beacon(universe, 20, 18, '/')

draw(universe, width, height)
print(len(universe))

for year in range(0, 200):
    universe = evolve(universe, width, height)
    draw(universe, width, height)
    time.sleep(1/30)