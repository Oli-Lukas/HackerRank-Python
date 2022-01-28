#!/bin/python3

# Link: https://www.hackerrank.com/challenges/whats-your-name/problem

def print_full_name(first, last):
    fullname = first +' '+ last
    print("Hello %s! You just delved into python."% (fullname))

    # print(f"Hello {first} {last}! You just delved into python.")

def main():
    first_name = input()
    last_name  = input()

    print_full_name(first_name, last_name)

if __name__ == '__main__':
    main()