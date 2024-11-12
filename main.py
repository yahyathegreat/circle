import math

radius = float(input("Enter radius: "))
print("Circumference:", 2 * math.pi * radius)
number = input("Enter a number: ")
num_digits = len(number) if number.isdigit() else len(number) - 1  
print("Total digits:", num_digits)
