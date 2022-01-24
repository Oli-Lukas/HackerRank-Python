#!/bin/python3

# Link: https://www.hackerrank.com/challenges/py-if-else/problem

def main():
    n = int(input().strip())

    weird = (n % 2 == 1) or ((n % 2 == 0) and (n >= 6 and n <= 20))

    print('Weird') if weird else print('Not Weird')

if __name__ == '__main__':
    main()