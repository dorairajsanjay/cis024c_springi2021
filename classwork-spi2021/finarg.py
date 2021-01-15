

import sys
import mfc

p = float(sys.argv[1])
if p == 0:
    print("Exiting Program.")

n = float(sys.argv[2])
r = float(sys.argv[3])

type_of_trans = sys.argv[4]
if type_of_trans.lower() == "s":
    print("Simple Interest:", mfc.calculate_simple_interest(p,n,r))
elif type_of_trans.lower() == "c":
    print("Compound Interest:", mfc.calculate_compound_interest(p,n,r))
else:
    print("Invalid command. Try again...")
