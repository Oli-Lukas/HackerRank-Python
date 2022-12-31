#!/bin/python3

# Link: https://www.hackerrank.com/challenges/capitalize/problem

def solve(string: str) -> str:
    wordlist = []

    for word in string.split(' '):
        wordlist.append(word.capitalize())
    
    return ' '.join(wordlist)

def main() -> None:
    string = input()
    result = solve(string)
    print(result)

if __name__ == '__main__':
    main()