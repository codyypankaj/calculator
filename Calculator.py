a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

choice = input("Enter operation (+, -, *, /): ")

if choice == "+":
    print("Result:", a + b)

elif choice == "-":
    print("Result:", a - b)

elif choice == "*":
    print("Result:", a * b)

elif choice == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid operation")