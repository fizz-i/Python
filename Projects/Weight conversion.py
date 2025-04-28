w = float(input("Enter your weight: "))
ops = input("In what unit would u like to convert to your weight?(lbs/kg) : ")
if ops == "kg":
    print(f"In kilograms your weight would be: {w*0.453592}")
elif ops == "lbs":
    print(f"In pounds your weight would be: {w/0.453592}")
else:
    print("Invalid operator")