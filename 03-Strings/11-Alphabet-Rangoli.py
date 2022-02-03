#!/bin/python3

# Link: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

import string

alphabet_list = list(string.ascii_lowercase)

def print_rangoli(size):
    width = (4 * size) - 3
    number_of_lines = (2 * size) - 1

    # First part
    for line in range((number_of_lines // 2) + 1):
        line_content = get_string_pattern(size - 1, line)
        print(line_content.center(width, '-'))

    # Second part
    for line in range((number_of_lines // 2) - 1, -1, -1):
        line_content = get_string_pattern(size - 1, line)
        print(line_content.center(width, '-'))

def letters(my_list, position, count):
    if count > 0:
        my_list.append(alphabet_list[position])
        letters(my_list, position - 1, count - 1)
        my_list.append(alphabet_list[position])
    
    elif count == 0:
        my_list.append(alphabet_list[position])

def get_string_pattern(initial_position, count):
    my_list = []

    letters(my_list, initial_position, count)

    string = '-'.join(my_list)

    return string

def main():
    number = int(input())
    print_rangoli(number)

if __name__ == '__main__':
    main()