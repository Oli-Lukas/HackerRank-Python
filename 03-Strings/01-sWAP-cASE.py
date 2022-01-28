#!/bin/python3

# Link: https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    new_string = ''.join([character.upper() if character.islower() else character.lower() for character in s])

    return new_string

def main():
    string = input()
    print(swap_case(string))

if __name__ == '__main__':
    main()