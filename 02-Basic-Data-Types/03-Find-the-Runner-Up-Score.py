#!/bin/python3

# Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

def main():
    n = int(input())
    arr = map(int, input().split())

    runner_up_score = sorted(list(set(arr)))[-2]
    print(runner_up_score)

if __name__ == '__main__':
    main()