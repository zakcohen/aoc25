
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

def part2():
    pass

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()