from grid import Grid
from point import Point

def part1():
    grid = Grid()
    with open('static/day4.txt', 'r') as file:
        for line in file:
            line = line.strip()
            grid.data.append(line)
    accessibleRolls = 0
    for x in range(grid.width()):
        for y in range(grid.height()):
            if grid.get(x, y) == '@':
                neighborRollCount = 0
                for neighbor in grid.get_neighbors_8(x,y):
                    if grid.get(neighbor.x, neighbor.y) == '@':
                        neighborRollCount += 1
                if neighborRollCount < 4:
                    accessibleRolls += 1
    print("part 1: ", accessibleRolls)
    print("================================================")

def getAccessibleRolls(grid):
    accessibleRolls = []
    for x in range(grid.width()):
        for y in range(grid.height()):
            if grid.get(x, y) == '@':
                neighborRollCount = 0
                for neighbor in grid.get_neighbors_8(x,y):
                    if grid.get(neighbor.x, neighbor.y) == '@':
                        neighborRollCount += 1
                if neighborRollCount < 4:
                    accessibleRolls.append(Point(x, y))
    return accessibleRolls

def part2():
    grid = Grid()
    with open('static/day4.txt', 'r') as file:
        for line in file:
            line = line.strip()
            grid.data.append(list(line))

    removedRolls = 0
    while True:
        rolls = getAccessibleRolls(grid)
        if len(rolls) == 0:
            break
        for roll in rolls:
            grid.set(roll.x, roll.y, '.')
            removedRolls += 1
        rolls.clear()
    print("part 2: ", removedRolls)
    print("================================================")

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()