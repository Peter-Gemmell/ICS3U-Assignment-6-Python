#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on May 2022
# This program calculates perimeter of a square using function

import math


def perimeter_square(length):
    # this function calculates perimeter of a square

    # calculation
    perimeter = length * 4

    # output
    return perimeter


def main():
    # gets input from user & outputs perimeter

    # inputs
    length_string = input("Enter the length of the side of a square in cm : ")

    try:
        length_side = float(length_string)
        if length_side > 0:
            perimeter_square_rounded = round(perimeter_square(length_side), 2)
            print(
                "The perimeter of a square with a side of {} cm is {} cm\u00B2".format(
                    length_side, perimeter_square_rounded
                )
            )
        else:
            print("Negative number entered, please try again.")

    except Exception:
        print("Invalid input, please try again.")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
