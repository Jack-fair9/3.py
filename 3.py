
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
    result = first_number + second_number
    return result
def CalcSubtract():
    result = first_number - second_number
    return result
def CalcMultiply():
    result = first_number * second_number
    return result
def CalcDivide():
    result = first_number / second_number
    return result

if operation == "add":
    result = CalcAdd()
elif operation == "subtract":
    result = CalcSubtract()
elif operation == "multiply":
    result = CalcMultiply()
elif operation == "divide":
    result = CalcDivide()