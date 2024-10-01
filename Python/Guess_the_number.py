num = 19
number_of_guesses = 0
while (number_of_guesses == 0):
    guess = int(input("enter a number" ))
    guesses = number_of_guesses + 1
    
    if guess==num:
        print("congratulation you guess the no.")
        break

    elif guess>num:
        print("the number you entered is greater")
        
    elif guess<num:
        print("the number you entered is lesser")
    
    
