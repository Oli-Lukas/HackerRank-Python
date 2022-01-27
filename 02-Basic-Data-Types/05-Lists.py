#!/bin/python3

# Link: https://www.hackerrank.com/challenges/python-lists/problem

def main():
    my_list = []
    n = int(input())

    for _ in range(n):
        command = input()

        splitted_command = command.split()
        command = splitted_command[0]
        arguments = splitted_command[1:]

        if command != 'print':
            command += '('+ ','.join(arguments) +')'
            eval('my_list.'+ command)
        else:
            print(my_list)

if __name__ == '__main__':
    main()