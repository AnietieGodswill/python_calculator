# Addition 
def add(x, y):
    return x+y
#Subtraction
def sub(x, y):
    return x-y
#Multiplication
def multiply(x, y):
    return x*y
#Divides
def div(x, y):
    return x/y

#Call Print Action
print("Select The Operation To Perform")
print("1. Add")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = int(input("Enter The Choice (1/2/3/4): "))
    num1 = float(input("Enter Number First"))
    num2 = float(input("Enter Number Second:"))

    if choice == 1:
                print(num1, "+", num2, "=", add(num1, num2))

    elif choice == 2:
                print(num1, "-", num2, "=", sub(num1, num2))

    elif choice == 3:
                print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == 4:
                print(num1, "/", num2, "=", div(num1, num2))
    else:   
        print("Invalid Output")