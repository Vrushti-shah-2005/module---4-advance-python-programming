try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = num1 / num2
    print(f"The result is: {result}")

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numeric values.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
