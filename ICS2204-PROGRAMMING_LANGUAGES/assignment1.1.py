#! /usr/bin/python3
"""
Author: Javan Odhiambo Otieno
Reg: sct211-0098/2022
"""

def simple_addition_calculator():
    name = input("Enter your name: ").capitalize()
    print(f"Welcome {name} to the addition calculator")
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    try:
        sum = eval(f"{num1} + {num2}")
        print(f"The sum of {num1} and {num2} is {sum}.")   
    except NameError as e:
        print("You did not provide numbers.")

if __name__ == "__main__":
    simple_addition_calculator()
