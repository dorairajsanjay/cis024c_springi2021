# subtract method
def subtract(n1,n2):
   return n1 - n2

# add method
def add(n1,n2):
   return n1 + n2

# calculate method
def calculate(n1,n2,operator="+"):
   if operator == "+":
      return add(n1,n2)

   elif operator == "-":
      return subtract(n1,n2)
   else:
      return "Unsupported Operator"

print("Result:",calculate(2,3))
