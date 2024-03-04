# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:59:04 2024

@author: Estabrooks
"""
class BasicMathOperations:
    def __init__(self):
        pass
    def greet(self, first, last):
        greet= (f"Welcome {first} {last}")
        return (greet)
        
    def add(self, num1, num2):
        num= num1 + num2
        add= print(num1, "+", num2, "=", num)
        return (add)
             
    def performOp(self, num1, num2, oper):
        if (oper == "+"):
            num= num1 + num2
            calc= print(num1, "+", num2, "=", num)
        elif (oper == "-"):
            num= num1 - num2
            calc= print(num1, "-", num2, "=", num)
        elif (oper =="*"):
            num= num1 * num2
            calc= print(num1, "*", num2, "=", num)
        elif(oper== "/"):
            num= num1/num2
            calc= print(num1, "/", num2, "=", num)
        return (calc)
        
    def square(self, num1):
        num= num1**2
        return(num)        
        
    #def factorial(self, num1):
        
    #def count(self, num1):
        
    #def hypot(self, num1, num2):
        
    #def area(self, num1, num2):
        
    #def power(self, num1):
        
    #def Type(self, arg):
        
def main():
    #Get user name and welcome them
    first= str(input("Enter your first name "))
    last= str(input("Enter your last name "))
    name= BasicMathOperations()
    print(name.greet(first, last))
    
    #have user pick which operation they would like to perform
    pick= int(input("Would you like to: Add numbers (1), perform an operation (2), square a number (3),"
          "Take a factorial (4), display all number from 0 to your number (5), find a hypotenbuse (6),"
          "Find the area of a rectangle (7), take the power of a numer (8), or find the argument type (9) "))
    
    if (pick == 1):
        num1= int(input("Pick a number "))
        num2= int(input("Pick another number "))
        num= BasicMathOperations()
        print(num.add(num1,num2))
        
    elif (pick== 2):
        num1= float(input("Pick a number "))
        num2= float(input("Pick another number "))
        print("You can add (+), subtract (-), multiply (*) or divide (/)")
        op=str((input("Which one do you want to do ")))
        while (op != "+" and op != "-" and op != "*" and op != "/"):
            op= input("Invalid input try again")
        send= BasicMathOperations()
        print(send.performOp(num1, num2, op))           
              
    elif (pick == 3):
        num1= float(input("Pick a number "))
        num= BasicMathOperations()
        print(num.square(num1))
        
    
main()
        
