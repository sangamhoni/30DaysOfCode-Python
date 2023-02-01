from calc_art import logo
import os

def adds(n1, n2):
    return n1+n2

def subtracts(n1, n2):
    return n1-n2

def multiplies(n1, n2):
    return n1*n2

def divides(n1, n2):
    return round(n1/n2, 1)

operations={
    '+': adds,
    '-': subtracts,
    '*': multiplies,
    '/': divides
}

def calculator():
    continue_or_not=True

    print(logo)
    num1=float(input("What's the number: "))
    for symbol in operations:
        print(symbol)
    while continue_or_not==True:
        operation_symbol=input("Pick an operation: ")
        num2=float(input("What's the next number: "))

        calculation_function=operations[operation_symbol]
        answer=calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # continue_or_not=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:  ").lower()
        more_calc=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:  ").lower()
        if more_calc=='y':
            num1=answer
        elif more_calc=='n':
            continue_or_not=False
            os.system('cls')
            calculator()
        else:
            break

calculator()



