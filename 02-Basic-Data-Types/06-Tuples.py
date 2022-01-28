#!/bin/python3

# Link: https://www.hackerrank.com/challenges/python-tuples/problem

def main():
    n = int(input())
    integer_list = map(int, input().split())

    t = tuple(integer_list)
    print(hash(t))

if __name__ == '__main__':
    main()