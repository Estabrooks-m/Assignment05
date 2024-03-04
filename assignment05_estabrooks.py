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
        
    def factorial(self, num1):
        num= 1
        for i in range (1, num1+1):
            num = num * i
        fact= print(num1, "! =", num)
        return(fact)
            
        
    def count(self, num1):
        for i in range (0, num1+1):
            count= print (i, "", end= "")
        return(count)
        
    def hypot(self, num1, num2):
        hypot= (num1**2 + num2**2)**.5
        t= round(hypot, 3)
        triangle= print("Hypotenuse= ", t)
        return (triangle)
        
    def area(self, num1, num2):
        a= num1 * num2
        area= round (a, 3)
        rect= print("Area =", area)
        return (rect)
        
    def power(self, num1, num2):
        p= num1 ** num2
        power= round(p, 3)
        num= print(num1, "to the power", num2, "is", power)
        return (num)
        
    def Type(self, arg):
        if isinstance(arg, str):
            argument= print(arg, "is a str")
        elif isinstance(arg, int):
            argument= print(arg, "is an int")
        elif isinstance (arg, float):
            argument= print(arg, "is a float")
        else:
            argument= print("Argument is not a str, int, or float")
            
        return (argument)
    
        
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
    
    while (pick != 1 and pick != 2 and pick != 3 and pick != 4 and pick != 5 and pick != 6 and pick != 7 and pick !=8 and pick !=9):
        pick= int(input("Invalid input try again "))

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
            op= input("Invalid input try again ")
        send= BasicMathOperations()
        print(send.performOp(num1, num2, op))           
              
    elif (pick == 3):
        num1= float(input("Pick a number "))
        num= BasicMathOperations()
        print(num.square(num1))
    
    elif (pick == 4):
        num1= int(input("Pick a number "))
        num= BasicMathOperations()
        print(num.factorial(num1))
        
    elif (pick == 5):
        num1= int(input("Pick a number "))
        num= BasicMathOperations()
        print(num.count(num1))
    
    elif (pick ==6):
        num1= float(input("Pick a number "))
        num2= float(input("Pick another number "))
        num= BasicMathOperations()
        print(num.hypot(num1,num2))
    
    elif (pick== 7):
        num1= float(input("Pick a number "))
        num2= float(input("Pick another number "))
        num= BasicMathOperations()
        print(num.area(num1,num2))
    elif (pick== 8):
        num1= float(input("Pick a number "))
        num2= int(input("To what power do you want to compute "))
        num= BasicMathOperations()
        print(num.power(num1,num2))
    
    elif (pick == 9):
        argu= input("Enter an value ")
        arg= BasicMathOperations()
        print(arg.Type(argu))
    
        
    end= print("")
    return(end)        
    
main()
        
