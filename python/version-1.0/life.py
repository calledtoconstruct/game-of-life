
def neighbors(universe, width, height, x, y):
    minx = 0
    maxx = width - 2
    miny = 0
    maxy = height - 2
    count = 0
    if x > minx and y > miny and is_alive(universe, width, x - 1, y - 1):
        count = count + 1
    if x > minx and is_alive(universe, width, x - 1, y):
        count = count + 1
    if x > minx and y < maxy and is_alive(universe, width, x - 1, y + 1):
        count = count + 1
    if y > miny and is_alive(universe, width, x, y - 1):
        count = count + 1
    if y < maxy and is_alive(universe, width, x, y + 1):
        count = count + 1
    if x < maxx and y > miny and is_alive(universe, width, x + 1, y - 1):
        count = count + 1
    if x < maxx and is_alive(universe, width, x + 1, y):
        count = count + 1
    if x < maxx and y < maxy and is_alive(universe, width, x + 1, y + 1):
        count = count + 1
    return count
    
def evolve(universe, width, height):
    total = width * height
    next = [True] * total
    for y in range(0, height - 1):
        for x in range(0, width - 1):
            position = y * width + x
            alive = universe[position]
            count = neighbors(universe, width, height, x, y)
            if alive and count < 2:
                next[position] = False
            if alive and count > 3:
                next[position] = False
            if alive == False and count != 3:
                next[position] = False
    return next

def is_alive(universe, width, x, y):
    position = y * width + x
    return universe[position]
