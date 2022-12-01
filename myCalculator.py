class cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def sub(self):
        return self.a-self.b
a=int(4)
b=int(2)
obj=cal(a,b)
choice=int(1)
print("0. Exit")
print("1. Add")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
while choice!=0:
   
    if choice==1:
        print("Adding two numbers with values as 4, 2 ")
        print("Result: ",obj.add())
        choice = 2 
    elif choice==2:
        print("Subtracting two numbers with values as 4, 2 ")
        print("Result: ",obj.sub())
        choice = 3
    elif choice==3:
        print("Multiplying two numbers with values as 4, 2 ")
        print("Result: ",obj.mul())
        choice = 4
    elif choice==4:
        print("Dividing two numbers with values as 4, 2 ")
        print("Result: ",round(obj.div(),2))
        choice=0
    elif choice==0:
        print("Exiting!")
    else:
        print("Invalid choice!!")
    
print()
