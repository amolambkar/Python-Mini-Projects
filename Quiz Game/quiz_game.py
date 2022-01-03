'''
author - Amol Ambkar
Program - Quiz Game Project

'''
from questions import questions
import random
que_list = [i for i in range(1,len(questions)+1)]

que_asked = 0
user_score = 0
while que_asked < 5:
    que_num = random.choice(que_list)

    print(questions[que_num]["Question"])
    num = 1
    for option in questions[que_num]["Options"]:
        print(str(num)+". "+option)
        num +=1

    print("Please Choose Correct Option..")
    try:
        user_choice = int(input())
    except:
        print("Please Choose Valid Option")
        print("-"*30)
        continue

    if user_choice == questions[que_num]["Answer"]:
        print("Answer is right.")
        user_score += 1
    else:
        print("Answer is wrong.")

    que_asked += 1
    que_list.remove(que_num)
    print("-"*30)
    

print("Your score is :",user_score,"/5")
