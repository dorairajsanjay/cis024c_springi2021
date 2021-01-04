import sys

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2


def calculate(n1,n2,operator):

    if operator == '+':
        return add(n1,n2)
    elif operator == '-':
        return subtract(n1,n2)
    elif operator == '*':
        return multiply(n1,n2)
    elif operator == '/':
        return divide(n1,n2)
    else:
        print("Unsupported Operator")
        return None

n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
operator = str(sys.argv[3])

result = calculate(n1,n2,operator)

print("Result:",result)