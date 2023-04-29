#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

greet_programmer()

def greet(name="Plane"):
    print(f"Hello, {name}!")

greet("Plane")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default("programmer")

def add(num1, num2):
    result = num1 + num2
    return result

add(1, 3)

def halve(number):
    result = float(number / 2)
    return result

halve(10)
