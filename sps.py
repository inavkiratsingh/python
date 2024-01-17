import random


def check(c, u):
    if c == u:
        return 0
    elif c == 1 and u == 0:
        return -1
    elif c == 2 and u == 1:
        return -1
    elif c == 0 and u == 2:
        return -1
    else:
        return 1

i = 0

print("Enter 0 for stone 1 for paper 2 for sessor\nYou have only five chances - \n")
user_won = 0

while (i < 5):
    comp = random.randint(0, 2)
    user = int(input())
               
    print("You : " + str(user))
    print("Computer : " + str(comp))

    score = check(comp, user)

    if score == -1:
        print("Computer Wins")
    elif score == 1:
        print("You Win")
        user_won += 1
    else:
        print("Draw")
    i += 1
if(user_won != 0):
    print("\n\nCongratulations !!!!!\n")
    print("You won --\"" + str(user_won) + "\"-- times")
else:
    print("\n\nYou lose every time\nBest of luck for next time.....")
    