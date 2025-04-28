menu = {
        "coke" : 80,
        "popcorn" : 350,
        "pizza" : 200, 
        "corn" : 120, 
        "icecream" : 75
}

cart=[]
total=0

print("---------MENU---------")
for item,price in menu.items():
    print(f"{item:10}:  {price} rupees/-")
print("----------------------")

while True:
    i = input("Select your item(q to quit): ").strip().lower()
    cart.append(i)
    if i == "q":
        break
    elif menu.get(i) == None:
        cart.remove(i)
        print(f"{i} is not on the menu")
cart.remove("q")

for i in cart:
    total += menu.get(i)
print(f"Your total is {total}rupees/-")
print("Enjoy your food")
