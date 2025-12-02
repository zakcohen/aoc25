
def part1():
    dial = 50
    zeroCount = 0
    with open('static/day1.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('L'):
                dial -= int(line[1:])
            elif line.startswith('R'):
                dial += int(line[1:])
            dial = dial % 100
            if dial == 0:
                zeroCount += 1
    print("part 1: ", zeroCount)
    print("================================================")

def part2():
    dial = 50
    zeroCount = 0
    with open('static/day1.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('L'):
                for i in range(int(line[1:])):
                    dial -= 1
                    dial = dial % 100
                    if dial == 0:
                        zeroCount += 1
            elif line.startswith('R'):
                for i in range(int(line[1:])):
                    dial += 1
                    dial = dial % 100
                    if dial == 0:
                        zeroCount += 1
            print(dial)
            
    print("part 2: ", zeroCount)
    print("================================================")

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()