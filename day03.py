import sys


def new_coord(coord, direction):
    x, y = coord
    if direction == '>':
        x += 1
    elif direction == '<':
        x -= 1
    elif direction == '^':
        y += 1
    else:
        y -= 1

    return x, y


if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as f:
        directions = f.read().strip()

    coord = (0, 0)
    visited = {coord}
    for d in directions:
        coord = new_coord(coord, d)
        visited.add(coord)

    print(len(visited))

    santa = (0, 0)
    robot = (0, 0)
    visited = {(0, 0)}
    for i, d in enumerate(directions):
        if i % 2 == 0:
            santa = new_coord(santa, d)
            visited.add(santa)
        else:
            robot = new_coord(robot, d)
            visited.add(robot)

    print(len(visited))
