#number guessing game
import random

lowerrange = int(input("Enter lowest number : "))
upperrange = int(input("Enter highest number: "))
number = random.randint(lowerrange, upperrange)

while True:
    guess = int(input("Enter your guess: "))

    if guess > upperrange or guess < lowerrange:
        print("You are out of range")
        print(f"the range you picked was {lowerrange} to {upperrange}")
        continue
    elif guess > lowerrange and guess < upperrange:
        print("You are very close!!")
        continue
    elif guess == number + 1 or guess == number + 2 :
        print("You are very very close")
        continue
    elif guess> number or guess< number:
        print("You are getting there!!")
    elif guess == number:
        print(f"Your guess was right {number}")
        break
    elif guess == "":
        print("Can't leave it empty")
        print(f"the range you picked was {lowerrange} to {upperrange}")
