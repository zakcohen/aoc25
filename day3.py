
def part1():
    with open('static/day3.txt', 'r') as file:
        maxPower = 0
        for line in file:
            bank = line.strip()
            maxFirstDigit = max(bank[:-1])
            firstDigitIndex = bank.index(maxFirstDigit)
            maxSecondDigit = max(bank[firstDigitIndex+1:])
            maxJoltage = int(maxFirstDigit + maxSecondDigit)
            maxPower += maxJoltage
        print("part 1: ", maxPower)
        print("================================================")

def maxJoltage(remainingBank, remainingCells):
    if remainingCells == 0:
        return ""
    nextDigit = max(remainingBank) if remainingCells == 1 else max(remainingBank[:-(remainingCells - 1)])
    nextDigitIndex = remainingBank.index(nextDigit)
    return nextDigit + maxJoltage(remainingBank[nextDigitIndex+1:], remainingCells - 1)

def part2():
    with open('static/day3.txt', 'r') as file:
        maxPower = 0
        for line in file:
            bank = line.strip()
            maxPower += int(maxJoltage(bank, 12))
        print("part 2: ", maxPower)
        print("================================================")

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()