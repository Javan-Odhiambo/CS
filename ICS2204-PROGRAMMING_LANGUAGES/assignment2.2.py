#! /usr/bin/python3

"""
Author: Javan Odhiambo Otieno
Reg: sct211-0098/2022
"""

def main():
    TIP_OPTIONS = [10, 12, 15]
    bill_amount = int(input("Enter the total bill amount: "))

    tip_percentage = int(input(r"Enter the tip percentage either 10%, 12% or 15%: ")) / 100

    number_of_people = int(input("Enter the number of people: "))

    amount_per_person = round((bill_amount + (bill_amount * tip_percentage)) / number_of_people, 2)

    print(f"Each person should pay {amount_per_person}")

if __name__ == "__main__":
    main()
