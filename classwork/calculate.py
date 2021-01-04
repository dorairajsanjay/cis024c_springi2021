
def add_numbers(number1, number2):
    return number1 + number2

def subtract_numbers(number1, number2):
    return number1 - number2

def multiply_numbers(number1, number2):
    return number1 * number2

def divide_numbers(number1, number2):
    return number1/number2

def Calculate(number1, number2, operator = '+'):
    
    if operator == '+':
        return add_numbers(number1, number2)
    elif operator == '-':
        return subtract_numbers(number1, number2)
    elif operator == '*':
        return multiply_numbers(number1, number2)
    elif operator == '/':
        return divide_numbers(number1, number2)
    else:
        print("Unrecognized Operator:", operator)
        return None
