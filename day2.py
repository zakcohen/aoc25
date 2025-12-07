import textwrap

def part1():
    invalidCount = 0
    for numRange in ranges():
        invalidCount += sum([num for num in numRange if invalid(num)])
    print("part 1: ", invalidCount)
    print("================================================")

def ranges():
    with open('static/day2.txt', 'r') as file:
        for line in file:
            line = line.strip()
            ranges = line.split(',')
            for numRange in ranges:
                numRange = numRange.split('-')
                yield range(int(numRange[0]), int(numRange[1]) + 1)

def invalid(num):
    strNum = str(num)
    midPoint = len(strNum) // 2
    return strNum[:midPoint] == strNum[midPoint:]

def invalidPart2(num):
    strNum = str(num)
    for pieceLength in range(1, len(strNum) // 2 + 1):
        pieces = textwrap.wrap(strNum, pieceLength)
        if len(pieces) >= 2 and all(piece == pieces[0] for piece in pieces):
            return True
    return False


def part2():
    invalidCount = 0
    for numRange in ranges():
        invalidCount += sum([num for num in numRange if invalidPart2(num)])
    print("part 2: ", invalidCount)
    print("================================================")

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()