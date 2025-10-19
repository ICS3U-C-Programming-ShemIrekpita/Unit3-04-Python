#!/usr/bin/env python3
# Created by: Shem
# Created on: 10/19/2025
# This program asks the user to enter an integer and tells them if it is positive, negative, or zero.

def main():
    # Input: Ask the user to enter an integer
    number = int(input("Enter a Number: "))

    # Process and Output: Check if the number is positive, negative, or zero
    if number > 0:
        print(str(number) + " is a positive number.")
    elif number < 0:
        print(str(number) + " is a negative number.")
    else:
        print(str(number) + " is just zero!")


# This ensures the program starts
if __name__ == "__main__":
    main()
