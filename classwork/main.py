
import calc3
import sys

#print("System Args:", sys.argv)

if len(sys.argv) != 4:
    print("Invalid Number of parameters")
    sys.exit(-1)
    
n1 = float(sys.argv[1])
n2 = float(sys.argv[2])
operator = sys.argv[3]

print("Result in Main:",calc3.calculate(n1,n2,operator))
