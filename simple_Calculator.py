#function for addition
def add(a,b):
    return a+b

#function for subtraction
def subtract(a,b):
    return a-b

#function for multiplication
def multiply(a,b):
    return a*b

#function for division
def divide(a,b):
    if b==0:
        print("Error: Number is not allow to divided by zero!!")
    return a/b

#taking two numbers for performing  operations from user as a input
number1=float(input("Enter the first number: "))
number2=float(input("Enter the Second number: "))

#choices that user wants to select for operation they wants
print("Select the options: ")
print("1. Addition ")
print("2. Subtraction ")
print("3. Multiplication ")
print("4. Division ")
print("Exit")

while(True):
    choice=int(input("Enter Your choice from (1 , 2, 3, 4, 5 =>) :"))
    if choice in (1,2,3,4,5):
        if choice==1:
            print("Addition of two numbers that is, ",number1 ,"and" , number1 ,"are equals to: ",add(number1,number2) )

        elif choice==2:   
            print("Subtraction of two numbers that is, ",number1 ,"and" , number1 ,"are equals to: ",subtract(number1,number2) )
            
        elif choice==3:   
            print("Multiplication of two numbers that is, ",number1 ,"and" , number1 ,"are equals to: ",multiply(number1,number2) )

        elif choice==4:   
            print("Division of two numbers that is, ",number1 ,"and" , number1 ,"are equals to: ",divide(number1,number2) )

        elif choice==5:   
            print("Thank You !!")
            exit()
    else:
        print("Invalid Choice")        
                        
