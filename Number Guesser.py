# importing random
import random
# starting the program
def Number_Guesser():
    Continue = True
    if Continue == True:
        print('Welcome to Number Guesser')
        print('I will choose a random number from 1 to 100')
        print('Please guess what number I am thinking of')
        Ans = random.randint(1,100)
        Guess = input('Please enter your guess')
        if Guess == Ans:
            print('You are correct!')
        else:
            print('You are incorrect, please try again')
        Con = input ('Would you like to continue? Y/N')
        if Con =='Y':
         Continue == True
        else:
            if Con == 'N':
                Continue == False