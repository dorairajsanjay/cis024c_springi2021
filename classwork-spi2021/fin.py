
import mfc

while True:
    
    try:
    
        # get user gross salary
        p = float(input("Please enter the principal(Enter 0 to stop):"))
        if p == 0:
            print("Exiting Program.")
            break
            
        n = float(input("Please enter the time period in years:"))
        r = float(input("Please enter the interest rate:"))
        
        # what type of computation does the user want to do
        while True:
            type_of_trans = input("Enter S for Simple Interest and C for Compound Interest:")
            if type_of_trans.lower() == "s":
                print("Simple Interest:", mfc.calculate_simple_interest(p,n,r))
                break
            elif type_of_trans.lower() == "c":
                print("Compound Interest:", mfc.calculate_compound_interest(p,n,r))
                break
            else:
                print("Invalid command. Try again...")
                continue
            
        # compute net salary
        net_salary = compute_net_salary(gross_salary,tax_rate)

    except Exception as err:
            
        print("Exception:",err)
        print("Please try again:")
