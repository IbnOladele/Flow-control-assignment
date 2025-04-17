try:   #Exception handling for invalid or wrong input
    x = float(input("first number: "))  #first number
    y = float(input("second number: "))  #second number
except ValueError:     #catch wrong input error
    print("Please enter a valid number")  #error response
operation = input("Enter operation (+, -, *, /, **, //): ")  #operation to perform
if operation not in ['+', '-', '*', '/', '**', '//']:   #check if operation is valid
    print("Invalid operation")
else:
    if operation == '+':   #addition
        result = x + y
    elif operation == '-':  #subtraction
        result = x - y
    elif operation == '*':    #multiplication
        result = x * y
    elif operation == '/':    #division
        if y != 0:  #check if second number is not zero
            result = x / y
        else:
            result = "Cannot divide by zero"   #detect division by zero
    elif operation == '**':    #exponential or raised to the power
        result = x ** y
    elif operation == '//':     #Xth root of Y
        if y != 0:    #check if second number is not zero
            result = x // y
        else:
            result = "Cannot divide by zero"    #detect division by zero
print(result)   #Display result