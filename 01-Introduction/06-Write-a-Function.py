#!/bin/python3

# Link: https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):
    leap = False

    # Write your logic here.
    divided_by_400 = (year % 400 == 0)
    divided_by_100 = (year % 100 == 0)
    divided_by_4   = (year % 4   == 0)
    
    leap = True if divided_by_400 or (divided_by_4 and not divided_by_100) else False

    return leap

def main():
    year = int(input())

    print(is_leap(year))

if __name__ == '__main__':
    main()