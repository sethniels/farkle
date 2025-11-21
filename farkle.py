#!/bin/python

import argparse

def PositiveInt (num):
    intval = int(num)
    if intval <= 0:
        raise ValueError(f"{num} is not a positive integer")
    return intval

def dice_combo_generator (numdice : int):
    curr_combo = [1] * numdice
    all_sixes = [6] * numdice
    while curr_combo != all_sixes:
        yield curr_combo
        curr_combo[0] += 1
        for i, die in enumerate(curr_combo):
            if die > 6:
                curr_combo[i+1] += 1
                curr_combo[i] = 1
    yield curr_combo


def farkle (numdice : int):
    for dice_combo in dice_combo_generator(numdice):
        print(dice_combo)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculates the probability "
            "of outcomes for the game Farkle")
    parser.add_argument("numdice", type=PositiveInt, help="The number of dice "
            "to roll")
    args = parser.parse_args()

    farkle(**vars(args))
