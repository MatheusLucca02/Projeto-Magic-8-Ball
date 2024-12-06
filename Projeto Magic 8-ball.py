# Import random
import random
# Declare Variables and do the loop for play more
total_control = True
while total_control == True:

    control = True
    while control == True:

        random_number = random.randint(1, 11)
        name = input(" What's your name ?")
        question = input(" What do you wanna asks ?")
        answer = ""

# Here i'm doing the control of name

        if name == "" and question == "":
            print(" Try to do any questions :)")
        else:
            control = False
# The if for the random numbers
    if name == "":
        print("Question: " + question + "?")
    else:
        print(name + " asks: " + question+"?")

    if random_number == 1:
        answer = " Yes - definitely "
        print("Magic 8-Ball's answer: " + answer)
    elif random_number == 2:
        answer = " It is decidedly so "
        print("Magic 8-Ball's answer: " + answer)
    elif random_number == 3:
        answer = " Without a doubt "
        print("Magic 8-Ball's answer: " + answer)
    elif random_number == 4:
        answer = "Reply hazy, try again "
        print("Magic 8-Ball's answer: " + answer)
    elif random_number == 5:
        answer = "Ask again later "
        print("Magic 8-Ball's answer: " + answer)
    elif random_number == 6:
        answer = " Better not tell you now "
        print("Magic 8-Ball's answer: " + answer)
    elif random_number == 7:
        answer = " My sources say no "
        print("Magic 8-Ball's answer: " + answer)
    elif random_number == 8:
        answer = " Outlook not so good "
        print("Magic 8-Ball's answer: " + answer)
    elif random_number == 9:
        answer = "Very doubtful "
        print("Magic 8-Ball's answer: " + answer)
    elif random_number == 10:
        answer = " For sure "
        print("Magic 8-Ball's answer: " + answer)
    elif random_number == 11:
        answer = " I dont think so "
        print("Magic 8-Ball's answer: " + answer)
    else:
        print("Error")
# Here i'm doing the control for the loop, if a player wanna play more
    again = input(" Wanna try again(y/n) ?")
    if again == "y" or again == "Y":
        total_control = True
    else:
        total_control = False
