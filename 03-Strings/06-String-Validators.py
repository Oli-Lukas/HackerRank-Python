#!/bin/python3

# Link: https://www.hackerrank.com/challenges/string-validators/problem

# def hasAlphaNumeric(string):
#     string_list = list(string)
#     for character in string_list:
#         if character.isalnum():
#             return True
#     return False

# def hasAlphabetical(string):
#     string_list = list(string)
#     for character in string_list:
#         if character.isalpha():
#             return True
#     return False

# def hasDigits(string):
#     string_list = list(string)
#     for character in string_list:
#         if character.isdigit():
#             return True
#     return False

# def hasLowercase(string):
#     string_list = list(string)
#     for character in string_list:
#         if character.islower():
#             return True
#     return False

# def hasUppercase(string):
#     string_list = list(string)
#     for character in string_list:
#         if character.isupper():
#             return True    
#     return False

def main():
    string = input()

    # print(hasAlphaNumeric(string))
    # print(hasAlphabetical(string))
    # print(hasDigits(string))
    # print(hasLowercase(string))
    # print(hasUppercase(string))
    
    print(any([character.isalnum() for character in string]))
    print(any([character.isalpha() for character in string]))
    print(any([character.isdigit() for character in string]))
    print(any([character.islower() for character in string]))
    print(any([character.isupper() for character in string]))

if __name__ == '__main__':
    main()