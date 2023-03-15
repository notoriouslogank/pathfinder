import argparse
import random

parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description="Rolls (x) number of n-sided dice.",
)
parser.add_argument(
    "-L", "--droplowest", type=int, help="Drop lowest (x) number of rolls."
)
parser.add_argument(
    "-H", "--drophighest", type=int, help="Drop highest (x) number of rolls."
)
parser.add_argument("-s", "--sum", action="store_true", help="Sum total of rolls.")
parser.add_argument(
    "-n", "--natural", action="store_true", help="Only show results of natural 20 or 1."
)
parser.add_argument(
    "-m", "--multiply", type=int, help="Repeat the same roll (x) times."
)
args = parser.parse_args()

xdy = input("What would you like to roll? [xdy] ")
d = xdy.find("d")
amount = int(xdy[0:d])
sides = int(xdy[d + 1 :])


def roll(amount, sides):
    """Roll (x) number of (y)-sided dice.

    Args:
        multiply (int): roll with the original params (m) times
        natural (bool): only return Nat 1s and Nat 20s
        drophighest (int): removes (x) highest values from the list
        droplowest (int): removes (x) lowest values from the list
        sum (bool): total of all rolls in list

    """
    rolls = []
    for i in range(0, amount):
        rolls.append(random.randint(1, sides))
    if args.multiply:
        print("Rolling [xdy] " + str(args.multiply) + " times.")
        t = int(args.multiply) - 1
        while t >= 0:
            print(rolls)
            t -= 1
            rolls = []
            for i in range(0, amount):
                rolls.append(random.randint(1, sides))
            if args.sum:
                print(f"Total: {sum(rolls)}")

    elif args.natural:
        if max(rolls) == 20:
            print("CRITICAL SUCCESS!")
        elif min(rolls) == 1:
            print("CRITICAL FAILURE!")
        else:
            print(rolls)
    elif args.drophighest:
        print("Dropping highest " + str(args.drophighest) + " roll(s).")
        rolls.sort()
        del rolls[-(args.drophighest) :]
        print(rolls)
    elif args.droplowest:
        print("Dropping lowest " + str(args.droplowest) + " rolls(s).")
        rolls.sort()
        lowest = rolls[0 : (args.droplowest)]
        del rolls[0 : (args.droplowest)]
        print(f"Lowest roll: {lowest}")
        print(rolls)
    elif args.sum:
        print(f"Total: {sum(rolls)}")
    else:
        print(rolls)


def main():
    (roll(amount, sides))


main()
