#
#Edward McBride
#CIS103 : Introduction to Programming
#Edward McBride
#Date: 9/18/24
#Description:
#This script is a calculator script that will calculate different functions and return the answers. The user will input
#the numbers and receive the correct answers.

#This function adds two numbers
def add(x,y):
    return x+y
#This function subtracts two numbers
def subtract(x,y):
    return x-y
#This function multiplies two numbers
def multiply(x,y):
    return x*y
#This function divides two numbers
def divide(x,y):
    return x/y
#This function produces the answer to expoenential problems
def exponentiation(x,y):
    return x**y
#This function produces the answer to modulus problems
def modulus(x,y):
    return x%y
#This function produces the answer to square root a number
def squareroot(sqrtx):
    return sqrtx
print('Select Operation.')
print('1.Add')
print('2.Subtract')
print('3.Multiply')
print('4.Divide')
print('5.exponentation')
print('6.modulus')
print('7.Square Root')
while True:
    choice = input('Enter choice(1/2/3/4/5/6/7):')
    #take input from the user
    #check if choice is one of the four options
    if choice in ('1','2','3','4','5','6','7'):
        try:
            num1 = float(input('Enter first number:'))
            num2 = float(input('Enter second number:'))
        except ValueError:
            print('Invalid input. Please enter a number.')
            continue
        if choice == '1':
            print(num1,'+', num2, '=', add(num1, num2))
        elif choice == '2':
            print(num1, '-', num2, '=', subtract(num1, num2))
        elif choice == '3':
            print(num1, '*', num2, '=', multiply(num1, num2))
        elif choice == '4':
            print(num1, '/', num2, '=', divide(num1, num2))
        elif choice == '5':
            print(num1,'**', num2, '=', exponentiation(num1, num2))
        elif choice == '6':
            print(num1,'%', num2, '=', modulus(num1, num2))
        elif choice == '7':
            print(num1,'sqrt', num1, '=', squareroot(num1))

        #This will check if the user wants another calculation
        #It will also break the loop if answer is no
        next_calculation = input('Lets do next calculation? (yes/no):')
        if next_calculation == 'no':
            break
        if next_calculation == 'yes':
            continue
        else:
            print('Invalid Input')
        #calculator will continue in a loop



