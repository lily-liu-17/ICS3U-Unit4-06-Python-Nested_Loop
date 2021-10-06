#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Oct 2021
# This program will print all possible combinations of RGB


def main():
    # this program will print all possible combinations of RGB
    # peocess & output
    for counterR in range(256):
        for counterG in range(256):
            for counterB in range(256):
                print("RGB ({0}, {1}, {2})".format(counterR, counterG, counterB))

    print("\nDone.")


if __name__ == "__main__":
    main()
