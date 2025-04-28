#quiz game
questions = ("How many hours are there in a day?",
             "What is the number of alphabets in the english language?",
             "How are you?",
             "How many days in a year?")
options = (("A.32" , "B.23" , "C.24" , "D.12 "),
           ("A.24" , "B.25" , "C.26" , "D.28 "),
           ("A.Fine" , "B.Good" , "C.bad" , "D.One must imagine sisyphus happy "),
           ("A.366" , "B.376" , "C.365" , "D.364 "))
answers = ("C", "C","D","C")
guesses = []
x= 0
score = 0
for i in questions:
    print("--------------------")
    print(i)
    for option in options[x]:
        print(option)
    guess = input("Answer(A/B/C/D): ").upper()
    guesses.append(guess)
    if guess == answers[x]:
        score+=1
        print("Correct")
    else:
        print("Incorrect!")
        print(f"{answers[x]} is the correct answer")

    x+=1

print(f"You got {score} questions correct")


