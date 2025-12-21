
def part1():
    freshRanges = []
    freshCount = 0
    with open('static/day5.txt', 'r') as file:
        for line in file:
            line = line.strip()

            if '-' in line:
                freshRange = line.split('-')
                freshRanges.append(range(int(freshRange[0]), int(freshRange[1]) + 1))
            # starts with a number
            elif line.isdigit():
                for freshRange in freshRanges:
                    if int(line) in freshRange:
                        freshCount += 1
                        break

    print("part 1: ", freshCount)
    print("================================================")

                


def part2():
    pass

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()