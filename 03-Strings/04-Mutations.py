#!/bin/python3

# Link: https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    my_list = list(string)
    my_list[position] = character
    new_string = ''.join(my_list)
    return new_string
    # return (string[:position] + character + string[position+1:])

def main():
    string = input()
    index, character = input().split()

    new_string = mutate_string(string, int(index), character)
    print(new_string)

if __name__ == '__main__':
    main()