#!/bin/python3

# Link: https://www.hackerrank.com/challenges/designer-door-mat/problem

def drawDoorMat(height, width):
    center = (height // 2) + 1

    # pattern = [('.|.' * (2 * i + 1)).center(m, '-') for i in range(n // 2)]
    # print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
    
    # draws first part
    for line in range(1, (height // 2) + 1):
        drawning_width = (line * 2) - 1
        drawning = drawning_width * '.|.'

        print(drawning.center(width, '-'))
    
    # draws center
    print('WELCOME'.center(width, '-'))

    # draws second part
    for line in range((height // 2), 0, -1):
        drawning_width = (line * 2) - 1
        drawning = drawning_width * '.|.'

        print(drawning.center(width, '-'))

def main():
    height, width = map(int, input().strip().split())

    drawDoorMat(height, width)

if __name__ == '__main__':
    main()