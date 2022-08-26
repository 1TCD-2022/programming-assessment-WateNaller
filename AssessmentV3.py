"""
Filename: AssessmentYEAH.py
Author: Nate Waller
Date:7/7/2021
Description: This is a multichoice quiz on sports
"""
import random

RUGBY_QUESTIONS = ["Who won the 2011 Rugby World Cup?",
                   "In Rugby, what is it called when you pass to your teammate\
 who is infront of you?",
                   "In Rugby, is a head-high tackle a penalty?",
                   "Finish the rugby players name... Richie Mc___",
                   "How long is a rugby field?"]
BASKETBALL_QUESTIONS = ["In Basketball, how many points is a free \
throw worth?",
                        "What number did Michael Jordan wear?",
                        "Where is Yao Ming from?",
                        "What is LeBrons last name?",
                        "Finish the basketball team... Oklahoma City _______?"]
VOLLEYBALL_QUESTIONS = ["In Volleyball, what team does Yuji Nishida play for?",
                        "In Volleyball, how many hits is a team allowed before\
 getting it over the net?",
                        "In Volleyball, how many players are on\
the court per team?",
                        "In Volleyball, What is it called when after a point, \
someone hits the ball over the net to start the round outside of the court?",
                        "In Volleyball, how many points does a set go to?"]
MIXTURE = RUGBY_QUESTIONS+BASKETBALL_QUESTIONS+VOLLEYBALL_QUESTIONS

QUESTION_ANSWERS = ["the all blacks", "all blacks", "abs", "new zealand", "nz",
                    "forward pass", "a forward pass", "yes", "caw", "100m",
                    "100 meters", "100meters", "100 metres", "100metres",
                    "1", "23", "china", "james", "thunder",
                    "japan", "jp", "3", "three", "six", "6",
                    "serve", "a serve", "25"]
# Options so they have to input the given options.
VALID_ANSWER = ["1", "2", "3", "4", "5"]
choice = 0
one_to_five = [1, 2, 3, 4, 5]
play_again = False


# Code that loops the whole quiz until they dont want to play
while not play_again:
    number_of_questions = 5
    valid_choice = False
    score = 0
    choice = input("""Welcome to my quiz!
    Please select what you would like to do.
    1. Rugby
    2. Basketball
    3. Volleyball
    4. A Mixture
    5. Exit

    Please select from 1-5""")
    # Code that loops until they give 1 to 5 (so they cant input random things)
    while choice not in VALID_ANSWER:
        choice = input("""Welcome to my quiz!
    Please select what you would like to do.
    1. Rugby
    2. Basketball
    3. Volleyball
    4. A Mixture
    5. Exit

    Please select from 1-5""")

# Code that determines the set of questions going to be asked
    if choice == "1":
        questions = (random.sample(RUGBY_QUESTIONS, number_of_questions))
    elif choice == "2":
        questions = (random.sample(BASKETBALL_QUESTIONS, number_of_questions))
    elif choice == "3":
        questions = (random.sample(VOLLEYBALL_QUESTIONS, number_of_questions))
    elif choice == "4":
        questions = (random.sample(MIXTURE, number_of_questions))
    else:
        # they must have chose to exit
        print("Goodbye!")
        exit()
# code that loops until they choose how many questions they want (1 to 5)
# to stop them from entering random things
    while not(valid_choice):
        try:
            number_of_questions = int(input("How many questions would you like?\
Please enter 1-5"))
            if number_of_questions in one_to_five:
                valid_choice = True
        except ValueError:
            print("Please enter a valid response 1-5")

    # code for asking  1 question
    if number_of_questions == 1:
        answer = input("{}".format(questions[0]))
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
            score = score+1
        else:
            print("Incorrect sorry")
        print("Your score is ", score, "out of", number_of_questions)

    # code for asking  2 questions
    elif number_of_questions == 2:
        answer = input("{}".format(questions[0]))
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
            score = score+1
        else:
            print("Incorrect sorry")
        answer = input("{}".format(questions[1]))
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
            score = score+1
        else:
            print("Incorrect sorry")
        print("Your score is ", score, "out of", number_of_questions)

    # code for asking  3 questions
    elif number_of_questions == 3:
        answer = input("{}".format(questions[0]))
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
            score = score+1
        else:
            print("Incorrect sorry")
        answer = input("{}".format(questions[1]))
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
            score = score+1
        else:
            print("Incorrect sorry")
        answer = input("{}".format(questions[2]))
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
            score = score+1
        else:
            print("Incorrect sorry")
        print("Your score is ", score, "out of", number_of_questions)

    # code for asking  4 questions
    elif number_of_questions == 4:
        answer = input("{}".format(questions[0]))
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
            score = score+1
        else:
            print("Incorrect sorry")
        answer = input("{}".format(questions[1]))
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
            score = score+1
        else:
            print("Incorrect sorry")
        answer = input("{}".format(questions[2]))
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
            score = score+1
        else:
            print("Incorrect sorry")
        answer = input("{}".format(questions[3]))
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
            score = score+1
        else:
            print("Incorrect sorry")
        print("Your score is ", score, "out of", number_of_questions)

    # code for asking  5 questions
    elif number_of_questions == 5:
        answer = input("{}".format(questions[0]))
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
            score = score+1
        else:
            print("Incorrect sorry")
        answer = input("{}".format(questions[1]))
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
            score = score+1
        else:
            print("Incorrect sorry")
        answer = input("{}".format(questions[2]))
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
            score = score+1
        else:
            print("Incorrect sorry")
        answer = input("{}".format(questions[3]))
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
            score = score+1
        else:
            print("Incorrect sorry")
        answer = input("{}".format(questions[4]))
        if answer.lower() in QUESTION_ANSWERS:
            print("Correct! Well done.")
            score = score+1
        else:
            print("Incorrect sorry")
        print("Your score is ", score, "out of", number_of_questions)
    else:
        number_of_questions = int(input("How many questions would you like?\
Please enter 1-5"))
