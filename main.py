# Display art
from art import logo,vs
from game_data import data
import random
score = 0
person_a = random.choice(data)
while True :
    print(logo)
    print(f"Your current score is {score}")

    #Ganarete a random account from the game data

    person_b = random.choice(data)

    while person_a == person_b:
        person_b = random.choice(data)

    #Format the account data into printable format

    print("Compare A:")
    print(person_a['name'])
    print(f"{person_a['description']}, from {person_a['country']}.\n")

    print(vs)
    print()

    print("Against B:")
    print(person_b['name'])
    print(f"{person_b['description']}, from {person_b['country']}.\n")

    #Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    #Get follower count of each account
    a_followers = person_a['follower_count']
    b_followers = person_b['follower_count']

    #Use if statement to check if user is correct
    correct_answer = ""
    if a_followers > b_followers:
        correct_answer = "A"
    else:
        correct_answer = "B"

    #Give user feedback on their guess
    if guess == correct_answer:
        print("You're right!")
    else:
        print("Sorry, that's wrong.")

    #score keeping
    if guess == correct_answer:
        person_a=person_b
        score += 1
    else:
        print(f"The answer was {correct_answer}, Your score is {score}")
        break









