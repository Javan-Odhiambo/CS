#! /usr/bin/python3
"""
Author: Javan Odhiambo Otieno
Reg: sct211-0098/2022
"""

from datetime import date

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1

    if today.month > birth_date.month or (today.month == birth_date.month and today.day >= birth_date.day):
        months = today.month - birth_date.month
        days = today.day - birth_date.day
    else:
        months = (12 - birth_date.month) + today.month
        if today.day < birth_date.day:
            months -= 1
            days = birth_date.day - today.day
        else:
            days = today.day - birth_date.day

    return age, months, days

 
def main():
    name = input("Enter your name: ").capitalize()
    print(f"Welcome {name} to the age calculator")

    year = int(input("Enter the birth year: "))
    month = int(input("Enter the birth month: "))
    day = int(input("Enter the birth day: "))

    birth_date = date(year, month, day)
    years, months, days  = calculate_age(birth_date)

    print(f"Age: {years} years, {months} months, {days} days")

if __name__ == "__main__":
    main()
