
# Simple Calculator
print("Welcome to simple calculator.")
print("I will add/subtract/multiple/divide any two numbers you provide.")
first_input = input("Enter in first number: ")
second_input = input("Enter in second number: ")
operation = input("Would you like to add/subtract/multiple/divide: ")

# explicitly convert string type to float type
first_number = float(first_input)
second_number = float(second_input)


def CalcAdd ():
    if operation == "add":
        result = first_number + second_number
    return print(result)
def CalcSubtract():
    if operation == "subtract":
        result = first_number - second_number
    return print(result)
def CalcMultiply():
    if operation == "multiply":
        result = first_number * second_number
    return print(result)
def CalcDivide():
    if operation == "divide":
        result = first_number / second_number
    return print(result)
