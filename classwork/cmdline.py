
import argparse
import calc3

parser = argparse.ArgumentParser()

parser.add_argument('n1', type=int,help='first number')
parser.add_argument('n2',  type=int,help='second number')
parser.add_argument('--operator', default="-", help='operators')

args = parser.parse_args()

print(args.n1, args.n2, args.operator)

print("Result:",calc3.calculate(args.n1, args.n2, args.operator))
