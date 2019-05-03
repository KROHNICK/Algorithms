#!/usr/bin/python

import sys


def making_change(amount, denominations):
    ways_to_get_amount = [0]*(amount+1)
    ways_to_get_amount[0] = 1
    for denomination in denominations:
        for i in range(denomination, amount+1):
            ways_to_get_amount[i] += ways_to_get_amount[i-denomination]
    return ways_to_get_amount[amount]


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
