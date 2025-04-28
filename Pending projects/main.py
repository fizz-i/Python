import json
import random

records = {}
uniq = []




def uniq_id():
    new_id = random.randint(1000,9999)
    if new_id in uniq:
        new_id = random.randint(1000,9999)
    elif new_id not in uniq:
        uniq.append(new_id)
        return new_id

def check():
    pass


def account(account_no):
    pass

def balance(balance):
    pass

def withdraw():
    pass

def add():
    pass


def new_account():
    name = input("Please enter your name: ")
    account_no = uniq_id()
    print("Your new account has been generated:")
    print(f"with account name {name} and account number {account_no}")
    
    records.update({account_no : name})
    with open("records.json", "w", encoding="utf-8") as write_file:
        json.dump(records, write_file, indent=4)

x=0
print(records)
while x == 0:
    
    print("-----------------------")
    print("HOW CAN WE HELP YOU?")
    print("1. Widthdraw money")
    print("2. Add money")
    print("3. Account details")
    print("4. Make a new account")
    print("5. exit")
    print("-----------------------")
    inp = input("Enter your choice(1/2/3/4): ")

    if inp == "5":
        x=1
    elif inp == "1":
        withdraw()
        continue
    elif inp == "2":
        add() 
        continue
    elif inp=="3":
        account()
        continue
    elif inp =="4":
        new_account()
        continue
    else:
        print("please enter a valid choice")
        continue