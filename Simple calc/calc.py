class Calc:
    def add(self,a,b):
        return a+b 
    
    def sub(self,a,b):
        if b>a:
            raise Exception("B cannot be greater than A")
        return a-b
        