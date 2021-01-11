# guess the secret number
# oop - vježba

import datetime
import json
import random

class Result():
    def __init__(self, attempts, player_name, date):
        self.attempts = attempts
        self.player_name = player_name
        self.date = date

# pokretanje igre (izbor A)
def play_game():
    secret = random.randint(1, 30)
    attempts = 0
    score_list = get_score_list()

    player_name = input("Unesite ime: ")

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret:
            # klasa Result
            result = Result(attempts = attempts, player_name = player_name, date = str(datetime.datetime.now()))

            score_list.append(result.__dict__)

            with open("score_list.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")


# čitanje score liste
def get_score_list():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
    return score_list

# ispis svih igrača (izbor B)
def get_scores():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
    for score_dict in score_list:
        print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date") + ", Player name: " + score_dict["player_name"])

# sortiranje liste (izbor C)
def get_top_scores():
    score_list = get_score_list()
    new_score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]
    return new_score_list

# izbornik
while True:
    selection = input("Would you like to A) play a new game, B) see score list C) see the best scores, or D) quit? ")

    if selection.upper() == "A":
        play_game()
    elif selection.upper() == "B":
        for score_dict in get_top_scores():
            result = Result(attempts = score_dict.get("attempts"), player_name = score_dict.get("player_name", "Anonymous"), date = score_dict.get("date"))

            print("Player: {name}; Attempts: {attempts}; Date: {date}".format(name = result.player_name, attempts = result.attempts, date = result.date))
    elif selection.upper() == "C":
        get_scores()
    elif selection.upper() == "D":
        break
    else:
        print("Enter correct letter (A, B, C or D)!")