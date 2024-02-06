def add(a, k):
    return a + k

def sub(a, k):
    return a - k

def mul(a, k):
    return a * k

def div(a, k):
    return a / k

print("Select the Operation: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("Enter # for Termination")

while True:
    choice = input("Enter the Choice: ")

    if choice == '#':
        print("Program has Ended.")
        break

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Enter valid numbers.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", sub(num1, num2))

        elif choice == '3':
            print(num1, "x", num2, "=", mul(num1, num2))

        elif choice == '4':
            if num2 != 0:
                print(num1, "/", num2, "=", div(num1, num2))
            else:
                print("Cannot divide by zero.")

    else:
        print("Invalid input. Enter a valid choice.")
