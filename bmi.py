#!/bin/python
def gather_info():
    height = float(raw_input("Enter your height: "))
    weight = float(raw_input("Enter your weight: "))
    unit = raw_input("is the above metrices in metric or imperial? ").lower().strip()
    return(height, weight, unit)
def calculate_bmi(height, weight, unit="metric"):
    if unit == "metric":
        bmi = (weight/(height ** 2))
    else:
        bmi = 703 * (weight/(height * 2))
    print("your BMI is %s  " %bmi)

while True:
    height, weight, unit = gather_info()
    if unit.startswith("i"):
        calculate_bmi(height, weight, unit)
        break
    elif unit.startswith("m"):
        calculate_bmi(height, weight)
        break
    else:
        print("Unit can either be in imperial or metric")
