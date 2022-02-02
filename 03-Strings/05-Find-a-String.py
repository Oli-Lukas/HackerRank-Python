#!/bin/python3

# Link: https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    count = 0

    for i in range(len(string)):
        if (string[i:].startswith(sub_string)):
            count += 1

    # find_result = 1
    # while find_result != -1:
    #     find_result = string.find(sub_string)

    #     if find_result != -1:
    #         count += 1
    #         string = string[find_result + 1:]

    return count

def main():
    string = input()
    sub_string = input()

    count = count_substring(string, sub_string)
    print(count)

if __name__ == '__main__':
    main()