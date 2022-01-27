#!/bin/python3

# Link: https://www.hackerrank.com/challenges/nested-list/problem

def main():
    n = int(input())
    records = [[input(), float(input())] for _ in range(n)]

    students_score = [list_element[1] for list_element in records]
    second_lowest_score = sorted(list(set(students_score)))[1]
    second_lowest_students = [list_element[0] for list_element in records if list_element[1] == second_lowest_score]
    second_lowest_students.sort()

    [print(name) for name in second_lowest_students]

if __name__ == '__main__':
    main()