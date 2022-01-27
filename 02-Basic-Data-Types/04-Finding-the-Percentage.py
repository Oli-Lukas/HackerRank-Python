#!/bin/python3

# Link: https://www.hackerrank.com/challenges/finding-the-percentage/problem

def main():
    n = int(input())
    student_marks = {}

    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    
    query_name = input()
    
    marks = student_marks[query_name]
    average = sum(marks) / len(marks)
    print("%.2f"%average)



if __name__ == '__main__':
    main()