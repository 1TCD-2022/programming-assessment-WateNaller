"""
Filename: AssessmentYEAH.py
Author: Nate Waller
Date:7/7/2021
Description: This is a multichoice quiz on sports
"""
import random
RUGBY_QUESTIONS = ["Who won the 2011 Rugby World Cup?","What is it called when you pass to your teammate who is infront of you"]
BASKETBALL_QUESTIONS = ["How many points is a free throw worth?","What number was Michael Jordan?","Where is Yao Ming from?","What is LeBrons last name?","Finish the team... Oklahoma City _______?]
VOLLEYBALL_QUESTIONS = ["What team does Yuji Nishida play for?","How many hits is a team allowed before getting it over the net?","How many players are on the court per team?","What is it called when after a point, someone hits the ball over the net to start the round outside of the court?","How many points does a set go to?"]
MIXTURE = RUGBY_QUESTIONS+BASKETBALL_QUESTIONS+VOLLEYBALL_QUESTIONS

QUESTION_ANSWERS = [""]
VALID_ANSWER = ["1","2","3","4","5"]
choice = 0

while not choice in VALID_ANSWER:
    choice = input("""Welcome to my quiz!
Please select what you would like to do.
1. Basketball
2. Volleyball
3. Rugby
4. A Mixture
5. Exit

Please select from 1-5""")

# repeat the question until they put in a valid option (1-5).

if choice == "1":
    number_of_questions = int(input("How many questions would you like?"))
    print(random.sample(RUGBY_QUESTIONS,number_of_questions))

elif choice == "2":
    number_of_questions = int(input("How many questions would you like?"))
    print(random.sample(BASKETBALL_QUESTIONS,number_of_questions))

elif choice == "3":
    number_of_questions = int(input("How many questions would you like?"))
    print(random.sample(VOLLEYBALL_QUESTIONS,number_of_questions))

elif choice == "4":
    number_of_questions = int(input("How many questions would you like?"))
    print(random.sample(MIXTURE,number_of_questions))

else: #it must be 5
    print("Goodbye!")

