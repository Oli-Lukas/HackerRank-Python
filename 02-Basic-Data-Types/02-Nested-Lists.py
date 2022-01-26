#!/bin/python3

# Link: https://www.hackerrank.com/challenges/nested-list/problem

def main():
    n = int(input())
    records = [[input(), float(input())] for _ in range(n)]

    scores = [list_element[1] for list_element in records]
    scores = [score for score in scores if score > min(scores)]

    students = [list_element[0] for list_element in records if list_element[1] == min(scores)]
    students.sort()

    [print(name) for name in students]

if __name__ == '__main__':
    main()