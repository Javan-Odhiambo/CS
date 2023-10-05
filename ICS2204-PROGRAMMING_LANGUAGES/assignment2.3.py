#! /usr/bin/python3
"""
Author: Javan Odhiambo Otieno
Reg: sct211-0098/2022
"""

def main():
    NORMAL_BMI_MIN = 18
    NORMAL_BMI_MAX = 24.9

    height_in_m = float(input("Enter your height in meters: "))
    weight_in_kg = float(input("Enter your weight in kilograms: "))
    BMI = weight_in_kg / (height_in_m ** 2)

    if BMI < NORMAL_BMI_MIN:
        BMI_results = "underweight"
    elif BMI > NORMAL_BMI_MAX:
        BMI_results = "overweight"
    else:
        BMI_results = "normal weight"

    print(f"You are {BMI_results} with a BMI of {round(BMI, 1)}")

if __name__ == "__main__":
    main()
