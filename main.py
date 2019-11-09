# Created by Dawid Twardowski

from calculator import Calculator

calculator = Calculator()

print("Welcome!")
operation = input("Please select operation (+, -, *, /) : ")
x = input("Please select first number (0-359) : ")
y = input("Please select second number (0-359) : ")

print(calculator.calc(int(x), operation, int(y)))

print("\nCya o/")
