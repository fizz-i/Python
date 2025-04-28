temp = float(input("Enter your temperature(in celcius): "))
converion = input("Which unit do you want to convert it to?(kelvin(k), farenheit(f)) ")

calc1 = (temp * 9/5)+32
calc2 = temp + 273

if converion == "k":
    print(calc2)
elif converion == "f":
    print(calc1)
else:
    print("invalid input")