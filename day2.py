
def part1():
    with open('static/day2.txt', 'r') as file:
        for line in file:
            line = line.strip()

            invalidCount = 0
            ranges = line.split(',')
            for numRange in ranges:
                numRange = numRange.split('-')
                invalidCount += sum([num for num in range(int(numRange[0]), int(numRange[1]) + 1) if invalid(num)])
            print("part 1: ", invalidCount)
            print("================================================")

def invalid(num):
    strNum = str(num)
    midPoint = len(strNum) // 2
    return strNum[:midPoint] == strNum[midPoint:]

def part2():
    pass

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()