# variables, data-types, strings, comments, escape-sequence, typecasting
# user-input, if-else, match-case statements

# student name
# student roll no.
# registration no.
# age
# class


# compare the age with 18
# if age is less than 18 student is not eligible for voting 
# if age is equal to and greater than 18 than student is eligible for voting

# 4 voting machines
# 1-5 ---- 1 voting machine ----  case 1
# 5-10 ---- 2 voting machine ----  case 2
# 10-15 --- 3 voting machine ---3 
# 15-20 --- 4 voting machine ---4


# starting of program

# title
print("\n\n")
title = "---- \" Welcome to the school portal \" ----"
print(title.center(100))
print("\n")

# details
print("Enter your details but make sure that roll no. is only in between 1-20".center(50))
print("\n")

#input
studentname = input("Enter your name : ")
age = int(input("Enter your age : "))
rollno = int(input("Enter your roll no : "))
if(rollno>20):
    print("!!!Plz enter valid roll number")
class1 = input("Enter your class : ")
regid = int(input("Enter your registeration id : "))

# voting eligibility
print("\n")
vote = "---- Your voting status ----"
print(vote.center(100))
print("\n")
if(age<18):
    print('"You are not eligible for voting"')
else:
    print('"You are eligible for voting"')


# alotement of voting machine
if(rollno > 0 and rollno <= 5):
    vot = 1
elif(rollno > 5 and rollno <= 10):
    vot = 2
elif(rollno > 10 and rollno <= 15):
    vot = 3
elif(rollno > 15 and rollno <= 20):
    vot = 4

print("\n")
voting = "--- Your aloted voting machine is here ---"
print(voting.center(100))
print("\n")
match vot:
    case _ if(rollno > 0 and rollno <= 5):
        print('"First Voting machine aloted."')
    case 2:
        print('"Second Voting machine aloted."')
    case 3:
        print('"Third Voting machine aloted."')
    case 4:
        print('"Fourth Voting machine aloted."')

print("\n")

print(' "Your details are : " ')
print("Your name is ", studentname)
print("Your class is ", class1)
print("Your roll number is ", rollno)
print("Your registeration number is ", regid)

print("\n")

thankyou = '----- " thankyou so much for visiting " -----'
print(thankyou.center(100))
