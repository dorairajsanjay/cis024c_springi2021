## this is my calculator

import sys
import argparse

def add(number_list):
    return sum(number_list)

def multiply(number_list):
    product = 1
    for n in number_list:
        product = product * n
        
    return product

x = int(input("Enter the first number:"))
y = int(input("Enter the second number:"))

print("Result:",add(x,y))
