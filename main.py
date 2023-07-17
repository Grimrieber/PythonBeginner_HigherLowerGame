from art import logo, vs
from game_data import data
import random
import os


print(logo)

game_count = 0
score = 0
game_should_continue = True



def format_data(account):
    '''Format the account data into printable format'''
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]

    return(f"{account_name}, a {account_desc}, from {account_country}")

def check_answer(guess, a_followers, b_followers, score):
    '''check choice A to B'''
    if guess == 'a':
        if a_followers > b_followers:
            print("Correct")
            score += 1
        else:
            print("Incorrect")
    elif guess == "b":
        if a_followers < b_followers:
            print("Correct")
            score += 1
        else:
            print("Incorrect")
    else: 
        print("not a suitable choice.")
    return score






while game_should_continue:
    game_count +=1
    accounts_a = random.choice(data)
    accounts_b = random.choice(data)

    while accounts_a == accounts_b:
        accounts_b = random.choice(data)

    print(f"Compare A: {format_data(accounts_a)}")
    print(vs)
    print(f"Compare b: {format_data(accounts_b)}")
    
    guess = input("Who has more followers? Type 'A' or 'B'").lower()

    score = check_answer(guess, accounts_a["follower_count"], accounts_b["follower_count"], score)
    print(f"You have got {score} out of {game_count}")
    game_should_continue = str(input("Continue? Yes or No").lower())
    if game_should_continue == "no" or game_should_continue =='':
        game_should_continue = False
    os.system('clear')
    print(logo)





