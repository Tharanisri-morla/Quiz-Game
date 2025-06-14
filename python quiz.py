questions =( "where we do python  ",
            "Which of the following is the datatype",
            "find the valid variable",
            "find the funtion of math package in python",
            "how we represent the tuple")
options = (("A.command prommpt","B.vscode","C.sql","D.Oracel"),
           ("A.INT","B.none","C.pi","D.sin"),
           ("A._1","B.a_avg","1","@"),
           ("A.time","B.Date","C.pow()","D.year"),
           ("A.{}","B.[]","C.()","D.{]"))
answers = ("B","A","B","C","C")
guesses = []
score = 0
question_num = 0
for question in questions:
    print(question)
    print("--------------")
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A,B,C,D) : ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        print("~ CORRECT ANSWER ~") 
    else:
            print("INCORRECT ANSWER!!!!")
            print(f"The correct answer is {answers[question_num]}")
    question_num+=1
print("-----------------------")
print("RESULTS")
print("----------------------")
print("answers:",end="")
for answer in answers:
     print(answer,end="")
print()
print("guesses:",end="")
for guess in guesses:
     print(guess, end="")
print()

score=int(score/len(questions)*100)
print(f"Your score is:{score}%")
