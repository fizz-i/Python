#python slot machine

import random
import time
symbols = ("🐯", "💀", "😂", "💦", "👻")

def spin_row(balance):
    spin = random.choices(symbols, k=3)
    for i in spin:
        print(f"| {i} ", end="|")
    print()
    
    if spin[0] == spin[1] == spin[2]:
        balance += 100
        print("Congratulations You Won 100!!!!!")
    else:
        print("Sorry you LOST!!")

def print_row(balance):
    print("************************************")
    print("Spining....")
    time.sleep(3)
    spin_row(balance)
    print()
    print("************************************")

def get_payout(balance):
    cont = input("Would you like to continue?(y/n): ").lower()
    if cont == "y":
        main()
    elif cont == "n":
        print("Have a nice day!!")
        print(f"Your balance is {balance}")
        
    balance = balance

def main():
    balance = 100  
    while balance > 0:
        print("************************************")
        print("Welcome to Python Slot Machine")
        print("Symbols: 🐯, 💀, 😂, 💦, 👻")
        print("************************************\n")


        betamount = float(input("How much would you like to bet? "))
        
        if betamount > balance or betamount <0:
            
            print(f"You cannot bet more than what you have or less than zero, that is {balance}")
            continue
        
        elif betamount <= balance: 
            
            balance -= betamount

            print(f"your left out balance is {balance:.2f}")
            print_row(balance)
            print()
        
            cont = input("Would you like to continue?(y/n): ").lower()
            if cont == "y":
                main()
            elif cont == "n":
                print("Have a nice day!!")
                print(f"Your balance is {balance}")
                break

        else:
            print("Invalid")



if __name__ == "__main__":
    main()