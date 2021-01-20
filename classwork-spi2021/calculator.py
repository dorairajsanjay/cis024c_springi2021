
class Calculator:
    
    def __init__(self):
        self.last_result = 0
        
    def add(self,n1,n2):
        self.last_result = n1+n2
        return self.last_result

    def multiply(self,n1,n2):
        self.last_result = n1*n2
        return self.last_result

    def show_last_result(self):
        print("Last result:",self.last_result)
