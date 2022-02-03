#!/bin/python3

# Link: https://www.hackerrank.com/challenges/capitalize/problem

def solve(string):
    return ' '.join([word.capitalize() for word in string.split()])
    # return ' '.join(map(str.capitalize, string.split()))

def main():
    string = input()
    result = solve(string)
    print(result)

if __name__ == '__main__':
    main()