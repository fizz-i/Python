x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
op = input("what do u want to do with these?(+,-,*,/): ")
if op == "+":
    print(x+y)
elif op == "-":
    print(x-y)
elif op == "*":
    print(x*y)
elif op == "/":
    print(x/y)
else:
    print("Invalid input")