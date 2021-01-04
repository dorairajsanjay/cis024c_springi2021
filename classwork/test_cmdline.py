
import sys

if len(sys.argv) != 3:
    print("Please use the following syntax:")
    print("python test_cmdline.py <number1> <number2>")
    sys.exit(-1)
    
try:
    n1 = float(sys.argv[1])
    n2 = float(sys.argv[2])
except ValueError as error:
    print("Please enter numerical values for the numbers")
    sys.exit(-1)
    
result = n1 + n2

print("Addition result:", result)
    
