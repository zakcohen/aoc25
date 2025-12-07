from grid import Grid

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


def part2():
    pass

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()