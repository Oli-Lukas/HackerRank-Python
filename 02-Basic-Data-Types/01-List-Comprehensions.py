#!/bin/python3

# Link: https://www.hackerrank.com/challenges/list-comprehensions/problem

def main():
    x, y, z, n = (int(input()) for _ in range(4))

    coordinates = [[i, j, k] for i in range(0, x+1) for j in range(0, y+1) for k in range(0, z+1)]
    allowed_coordinates = [list_element for list_element in coordinates if sum(list_element) != n]

    print(allowed_coordinates)

if __name__ == '__main__':
    main()