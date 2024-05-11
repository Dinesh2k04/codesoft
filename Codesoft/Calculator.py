def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("Error! Division by zero ")

def main():
    print("Simple Calculator")
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number ")
            continue
        print("\nArithemtic Operations:")
        print("1. Addition(+) ")
        print("2. Subtraction(-) ")
        print("3. Multiplication(*) ")
        print("4. Division(/) ")
        choice = int(input("Select Arithemtic Operations 1 or 2 or 3 or 4 : "))

        if choice in ( 1, 2, 3, 4 ):
            if choice == 1:
                result = add(num1, num2)
            elif choice == 2:
                result = subtract(num1, num2)
            elif choice == 3:
                result = multiply(num1, num2)
            elif choice == 4:
                result = divide(num1, num2)
                if isinstance(result, str):
                    print(result)
                    continue
            print(f"Result: {result}")
        else:
            print("Entered choice is Invalid. Please choose a valid choice!")
            continue
        answer = input("Would you like to perform another calculation? (yes/no): ")
        if answer.lower() not in ('yes', 'y'):
            print("Exiting program.")
            break 
if __name__ == "__main__":
    main()
