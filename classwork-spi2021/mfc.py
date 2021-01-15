
def calculate_simple_interest(principal, years, rate):
    
    return (principal * years * rate)/100

def calculate_compound_interest(principal, years, rate):
    
    return principal * (1+rate/years)**((rate/100)*years)
