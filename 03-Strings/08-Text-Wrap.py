#!/bin/python3

# Link: https://www.hackerrank.com/challenges/text-wrap/problem

def wrap(string, max_width):
    count = 0
    new_string = ''

    for character in string:
        new_string += character
        count += 1

        if count == max_width:
            new_string += '\n'
            count = 0
    
    return new_string
    # return '\n'.join([string[i:i+max_width] for i in range(0, len(string), max_width)])


def main():
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

if __name__ == '__main__':
    main()