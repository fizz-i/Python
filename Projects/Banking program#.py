#Banking program
#show balance 
#Deposit
#withdraw

def show_balance(balance):
    print(f"Your balance is {balance:.2f}")

def deposit():
    amount = float(input("Enter the amount to deposit: "))

    if amount < 0 :
        print("That is invalid")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter the amount to be withdrawn: "))

    if amount > balance:
        print("You do not have that much in your account.")
        return 0
    elif amount < 0 :
        print("INVALID!!")
        return 0
    else:
        return amount

def main():
    balance = 0 

    while True:
        print("------Banking Program------")
        print("How can we help you?")
        print("1. Deposit")
        print("2. Withdrawal")
        print("3. Show balance")
        print("4. Exit")
        inp = int(input("Enter your choice(1, 2, 3, 4): "))
        if inp == 3:
            show_balance(balance)
        elif inp == 2:
            balance -= withdraw(balance)
        elif inp == 1:
            balance += deposit()
        elif inp == 4:
            print("Goodbye!!")
            break
        else:
            print("invalid input")

if __name__ == "__main__":
    main()
