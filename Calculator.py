#CALCULATOR CHALLENGE

def add(n1,n2):
    return n1+n2

def substract(n1,n2):
    return n1-n2

def divide(n1,n2):
    return n1/n2

def multiplication(n1,n2):
    return n1*n2

operations = {
    '+':add,
    '-':substract,
    '/':divide,
    '*':multiplication
}

num1=int(input("Enter the first number"))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from  the line above")
num2=int(input("Enter the next number"))
calculation_function = operations[operation_symbol]
answer = calculation_function(num1,num2)
result = calculation_function(answer, num2)
print(f'{num1} {operation_symbol} {num2} = {answer}')

stop = True
while stop==True:
    another_caluclation = input(f"Type 'y' to continue calculation with {answer} or 'n' to exit")
    if another_caluclation=='n':
        stop=False
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from  the line above")
    num2=int(input("Enter the next number"))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    result = calculation_function(answer, num2)
    print(f"{answer} {operation_symbol} {result}")
