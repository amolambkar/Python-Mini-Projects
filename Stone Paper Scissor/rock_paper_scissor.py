'''
Author - Amol Ambkar
Program - Rock Paper scissor Game

'''
# Rock vs Paper ==> Paper
# Paper vs Scissor == > Scissor 
# Scissor vs Rock ==> Rock
import random
import time

#choices for user
choices = {
    1 : "Rock",
    2 : "Paper",
    3 : "Scissor"
}

def find_winner(user,comp):
    '''
    Function to return the winner from choices

    Parameters:
    user - User's choice
    comp - Computer's choice

    Return:
    return string ("Tie"/"User"/"Computer") winner

    '''
    if user == comp:
        return "Tie"
    elif (choices[user] == "Rock" and choices[comp] == "Paper") or\
        (choices[user] == "Paper" and choices[comp] == "Scissor") or\
        (choices[user] == "Scissor" and choices[comp] == "Rock"):
        return "Computer"
    else:
        return "User"

print("Rock-Paper-Scissor\n")
print("Rules of game:\n"+
        "1.Rock vs Paper ==> Paper\n"+
        "2.Paper vs Scissor == > Scissor"+
        "3.Scissor vs Rock ==> Rock")

user_win = 0
comp_win = 0
while True:
    print("Please Choose you option number :\n 1.Rock \n 2.Paper \n 3.Scissor")

    try:
        user_choice = int(input())
    except:
        print("Only integers allowed")
        print("-"*30)
        continue

    try:
        print("Your choice :",choices[user_choice])
    except:
        print("Please Choose valid option")
        print("-"*30)
        continue
    
    print("Now its Computer's turn")
    time.sleep(1)
    computer_choice = random.randint(1,3)
    print("Computer's choice :",choices[computer_choice])

    winner = find_winner(user_choice,computer_choice)

    print(choices[user_choice],"vs",choices[computer_choice])

    if winner == "Computer":
        comp_win+=1
        print("Computer is Winner")
    elif winner == "User":
        user_win += 1
        print("You are the winner")
    else:
        print("Match Tie")
        
    print("\n user score :",user_win,"vs Computer Score",comp_win)

    print("-"*30)
