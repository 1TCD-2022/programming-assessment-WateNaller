"""
Filename: AssessmentYEAH.py
Author: Nate Waller
Date:7/7/2021
Description: This is a multichoice quiz on sports
"""
import random
RUGBY_QUESTIONS = ["Who won the 2011 Rugby World Cup?","What is it called when you pass to your teammate who is infront of you?","Is a head-high tackle a penalty?","Finish the rugby players name... Richie Mc___","How long is a rugby field?"]
BASKETBALL_QUESTIONS = ["How many points is a free throw worth?","What number was Michael Jordan?","Where is Yao Ming from?","What is LeBrons last name?","Finish the team... Oklahoma City _______?"]
VOLLEYBALL_QUESTIONS = ["What team does Yuji Nishida play for?","How many hits is a team allowed before getting it over the net?","How many players are on the court per team?","What is it called when after a point, someone hits the ball over the net to start the round outside of the court?","How many points does a set go to?"]
MIXTURE = RUGBY_QUESTIONS+BASKETBALL_QUESTIONS+VOLLEYBALL_QUESTIONS

QUESTION_ANSWERS = ["the all blacks","all blacks","new zealand","nz","forward pass","a forward pass","yes","caw","100m","100 meters","100meters"]
VALID_ANSWER = ["1","2","3","4","5"]
choice = 0
one_to_five = [1,2,3,4,5]


while not choice in VALID_ANSWER:
    choice = input("""Welcome to my quiz!
Please select what you would like to do.
1. Rugby
2. Basketball
3. Volleyball
4. A Mixture
5. Exit

Please select from 1-5""")

# repeat the question until they put in a valid option (1-5).

if choice == "1":
    number_of_questions = int(input("How many questions would you like? Please enter 1-5"))
    while not number_of_questions in one_to_five:
        number_of_questions = int(input("How many questions would you like? Please enter 1-5"))
    questions =(random.sample(RUGBY_QUESTIONS,number_of_questions))

# code for asking  1 question
    if number_of_questions == 1:
        answer = input(questions[0])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")

# code for asking  2 questions       
    elif number_of_questions == 2:
        answer = input(questions[0])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[1])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")

# code for asking  3 questions
    elif number_of_questions == 3:
        answer = input(questions[0])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[1])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[2])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")

# code for asking  4 questions      
    elif number_of_questions == 4:
        answer = input(questions[0])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[1])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[2])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[3])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")

# code for asking  5 questions
    elif number_of_questions == 5:
        answer = input(questions[0])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[1])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[2])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[3])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[4])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")

            
    else:
        number_of_questions = int(input("How many questions would you like? Please enter 1-5"))
    


elif choice == "2":
    number_of_questions = int(input("How many questions would you like? Please enter 1-5"))
    while not number_of_questions in one_to_five:
        number_of_questions = int(input("How many questions would you like? Please enter 1-5"))
    questions =(random.sample(BASKETBALL_QUESTIONS,number_of_questions))

# code for asking  1 question
    if number_of_questions == 1:
        answer = input(questions[0])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")

# code for asking  2 questions       
    elif number_of_questions == 2:
        answer = input(questions[0])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[1])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")

# code for asking  3 questions
    elif number_of_questions == 3:
        answer = input(questions[0])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[1])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[2])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")

# code for asking  4 questions      
    elif number_of_questions == 4:
        answer = input(questions[0])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[1])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[2])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[3])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")

# code for asking  5 questions
    elif number_of_questions == 5:
        answer = input(questions[0])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[1])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[2])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[3])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[4])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")

            
    else:
        number_of_questions = int(input("How many questions would you like? Please enter 1-5"))

elif choice == "3":
    number_of_questions = int(input("How many questions would you like? Please enter 1-5"))
    while not number_of_questions in one_to_five:
        number_of_questions = int(input("How many questions would you like? Please enter 1-5"))
    questions =(random.sample(VOLLEYBALL_QUESTIONS,number_of_questions))

# code for asking  1 question
    if number_of_questions == 1:
        answer = input(questions[0])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")

# code for asking  2 questions       
    elif number_of_questions == 2:
        answer = input(questions[0])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[1])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")

# code for asking  3 questions
    elif number_of_questions == 3:
        answer = input(questions[0])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[1])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[2])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")

# code for asking  4 questions      
    elif number_of_questions == 4:
        answer = input(questions[0])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[1])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[2])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[3])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")

# code for asking  5 questions
    elif number_of_questions == 5:
        answer = input(questions[0])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[1])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[2])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[3])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[4])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")

            
    else:
        number_of_questions = int(input("How many questions would you like? Please enter 1-5"))

elif choice == "4":
    number_of_questions = int(input("How many questions would you like? Please enter 1-5"))
    while not number_of_questions in one_to_five:
        number_of_questions = int(input("How many questions would you like? Please enter 1-5"))
    questions =(random.sample(MIXTURE,number_of_questions))

# code for asking  1 question
    if number_of_questions == 1:
        answer = input(questions[0])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")

# code for asking  2 questions       
    elif number_of_questions == 2:
        answer = input(questions[0])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[1])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")

# code for asking  3 questions
    elif number_of_questions == 3:
        answer = input(questions[0])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[1])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[2])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")

# code for asking  4 questions      
    elif number_of_questions == 4:
        answer = input(questions[0])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[1])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[2])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[3])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")

# code for asking  5 questions
    elif number_of_questions == 5:
        answer = input(questions[0])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[1])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[2])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[3])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")
        answer = input(questions[4])
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
        else:
            print("Incorrect sorry")

            
    else:
        number_of_questions = int(input("How many questions would you like? Please enter 1-5"))

else: #it must be 5
    print("Goodbye!")

