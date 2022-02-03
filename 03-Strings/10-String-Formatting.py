#!/bin/python3

# Link: https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    # padded_width = len('{0:b}'.format(number))
    padded_width = number.bit_length()

    for count in range(1, number + 1):
        print('{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}'.format(count, width = padded_width))

def main():
    number = int(input())
    print_formatted(number)

if __name__ == '__main__':
    main()