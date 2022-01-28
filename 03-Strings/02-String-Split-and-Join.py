#!/bin/python3

# Link: https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    # Write your code here
    
    # return '-'.join(line.split())
    return line.replace(' ', '-')

def main():
    line = input()
    result = split_and_join(line)
    print(result)

if __name__ == '__main__':
    main()