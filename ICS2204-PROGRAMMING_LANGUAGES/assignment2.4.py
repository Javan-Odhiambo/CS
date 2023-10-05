#! /usr/bin/python3
"""
Author: Javan Odhiambo Otieno
Reg: sct211-0098/2022
"""

def main():
    year_to_test = int(input("Enter the year: "))
    is_leap_year_text = f"{year_to_test} is a leap year"
    is_not_leap_year_text = f"{year_to_test} is not a leap year"

    if year_to_test % 4 == 0:
        print(is_leap_year_text)
    else:
        print(is_not_leap_year_text)

if __name__ == "__main__":
    main()
