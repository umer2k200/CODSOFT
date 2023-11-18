def add(first_no,second_no):
    return first_no+second_no

def sub(first_no,second_no):
    return first_no-second_no

def mul(first_no,second_no):
    return first_no*second_no

def div(first_no,second_no):
    return first_no/second_no

def mod(first_no,second_no):
    return first_no%second_no

def exp(first_no,second_no):
    return first_no**second_no

def Calculator_operations(first_no,second_no,operation):
    if operation==1:
        print("Addition of ",first_no," and ",second_no," is ",add(first_no,second_no))
    elif operation==2:
        print("Subtraction of ",first_no," and ",second_no," is ",sub(first_no,second_no))
    elif operation==3:
        print("Multiplication of ",first_no," and ",second_no," is ",mul(first_no,second_no))
    elif operation==4:
        if second_no != 0:
            print("Division of ",first_no," and ",second_no," is ",div(first_no,second_no) )
        else:
            print("Divisor is equal to 0. Division by zero is not possible")
        """check mod and division with same numbers and set diviiosn to int"""
    elif operation==5:
        if second_no != 0:
            print("Modulus of ",first_no," and ",second_no," is ",mod(first_no,second_no))
        else:
            print("Divisor is equal to 0. Division by zero is not possible")
    elif operation==6:
        print("Exponent of ",first_no," and ",second_no," is ",exp(first_no,second_no))
    else:
        print("Invalid operation")

print("-----------------------------------------------")
print("         WELCOME TO THE CALCULATOR")
print("-----------------------------------------------")
print("Operations: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Exponent")
flag =True
again_flag = False
while(flag):
    try:
        if again_flag==True:
            first_no=float(input("Enter the first number again: "))
            flag =False
        else:
            first_no=float(input("Enter the first number: "))
            flag =False
    except ValueError:
        print("This is not a number! ")
        again_flag=True

flag = True
again_flag= False
while(flag):
    try:
        if again_flag==True:
            second_no=float(input("Enter the second number again: "))
            flag =False
        else:
            second_no=float(input("Now, Enter the second number: "))
            flag =False
    except ValueError:
        print("This is not a number! ")
        again_flag=True

flag = True
again_flag= False
while(flag):
    try:
        if again_flag==True:
            operation=int(input("Enter the operation again: "))
            Calculator_operations(first_no,second_no,operation)
            flag =False
        else:
            operation=int(input("Enter the operation: "))
            Calculator_operations(first_no,second_no,operation)
            flag =False
    except ValueError:
        print("This is not a number! ")
        again_flag=True
        
print("-----------------------------------------------")
print("       THANK YOU FOR USING CALCULATOR")
print("-----------------------------------------------")
