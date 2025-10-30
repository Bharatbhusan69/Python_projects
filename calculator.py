print("Choose any operation: +, -, *, /, //, %")

a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /, //, %): ")
b = float(input("Enter second number: "))

if op == '+':
    result = a + b
    print("Result:", result)

elif op == '-':
    result = a - b
    print("Result:", result)

elif op == '*':
    result = a * b
    print("Result:", result)

elif op == '/':
    if b != 0:
        result = a / b
        print("Result:", result)
    else:
        print("Error")

elif op == '//':
    if b != 0:
        result = a // b
        print("Result:", result)
    else:
        print("Error")

elif op == '%':
    if b != 0:
        result = a % b
        print("Result:", result)
    else:
        print("Error")

else:
    print("error- Please choose from +, -, *, /, //, %")
