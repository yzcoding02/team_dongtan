"""
시작할때 +,-,* (덧셈, 뺄셈, 곱셈, 나눗셈)중 무엇을 할지 선택하고
각 부호에 밪게 덧셈은 1 뺄셈은 2 곱셈은 3 나눗셈은 4 를 치고
예를들어
ex) 더해지는수(x) enter 더하는수(y)
처럼 써준뒤 enter을 치면 값을 계산 해 준다.
"""
# Define the calculator functions
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


# Take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == "1":
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == "2":
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == "3":
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == "4":
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input")
