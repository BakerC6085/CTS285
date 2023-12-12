# Creating the Dataman Project
def Dataman():
    print('Welcome to the Dataman')
    print('Please choose the program you with to play')
    print('1 Answer Checker')
    print('2 Memory Bank')
    print('3 Number Guesser')
    Chosen = input("Please choose 1, 2, or 3")
    if Chosen == '1':
        Answer_Checker()
    else:
        if Chosen == '2':
            Memory_Bank()
        else:
            if Chosen == '3':
                Number_Guesser()
            else:
                print('Please enter 1,2, or 3 only')
                
# Making the Function for Answer Checker
def Answer_Checker():
    Continue = True
    if Continue ==  True:
        # welcome message for answer checker
        print('Welcome to Answer Checker!')
        # Getting the input from the user for the program
        Num1 = input('Please Enter First Number')
        Equi = input('Please Enter Equiation Type +, -, *, or /')
        Num2 = input('Please Enter Second Number')
        Ans = input('Please Enter Answer')
        # Checking what equation to do
        if Equi == '+':
            Result = Num1 + Num2
        else:
            if Equi == '-':
                Result = Num1 - Num2
            else:
                if Equi == '*':
                    Result = Num1 * Num2
                else:
                    if Equi == '/':
                        Result == Num1 / Num2
                    else:
                        print('Please Enter a correct equiation symbol')
        # Checking Answer against the typed in answer                
        if Result == Ans:
            print('Your Answer is Correct')
        else:
            print('Your Answer is incorrect')
            Replay = input('Do you wish to continue? Y or N')
            if Replay == 'Y':
                Continue = True
            else:
                if Replay == 'N':
                    Continue = False
                else:
                    print('Please enter only Y or N')

# Making the program of memory bank
def Memory_Bank():
    # starting loop
    Continue = True
    if Continue == True:
        print('Welcome to Memory Bank')
        Type = input('Please Enter 1 to store questions or 2 to answer questions')
        # getting the problems that need to be stored
        if Type == '1':
            print('Please enter 5 problems to store')
            Num11 = input("Please enter the first number of the equation")
            Equi1 = input('Please Enter Equiation Type +, -, *, or /')
            Num12 = input('Please Enter Second Number')
            # Checking what equation to do
            if Equi1 == '+':
                Result1 = Num11 + Num12
            else:
                if Equi1 == '-':
                    Result1 = Num11 - Num12
                else:
                    if Equi1 == '*':
                        Result1 = Num11 * Num12
                    else:
                        if Equi1 == '/':
                            Result1 == Num11 / Num12
                        else:
                            print('Please Enter a correct equiation symbol')
            Num21 = input("Please enter the first number of the equation")
            Equi2 = input('Please Enter Equiation Type +, -, *, or /')
            Num22 = input('Please Enter Second Number')
            # Checking what equation to do
            if Equi2 == '+':
                Result2 = Num21 + Num22
            else:
                if Equi2 == '-':
                    Result2 = Num21 - Num22
                else:
                    if Equi2 == '*':
                        Result2 = Num21 * Num22
                    else:
                        if Equi2 == '/':
                            Result2 == Num21 / Num22
                        else:
                            print('Please Enter a correct equiation symbol')
            Num31 = input("Please enter the first number of the equation")
            Equi3 = input('Please Enter Equiation Type +, -, *, or /')
            Num32 = input('Please Enter Second Number')
            # Checking what equation to do
            if Equi3 == '+':
                Result3 = Num31 + Num32
            else:
                if Equi3 == '-':
                    Result3 = Num31 - Num32
                else:
                    if Equi3 == '*':
                        Result3 = Num31 * Num32
                    else:
                        if Equi3 == '/':
                            Result3 == Num31 / Num32
                        else:
                            print('Please Enter a correct equiation symbol')
            Num41 = input("Please enter the first number of the equation")
            Equi4 = input('Please Enter Equiation Type +, -, *, or /')
            Num42 = input('Please Enter Second Number')
            # Checking what equation to do
            if Equi4 == '+':
                Result4 = Num41 + Num42
            else:
                if Equi3 == '-':
                    Result4 = Num41 - Num42
                else:
                    if Equi4 == '*':
                        Result4 = Num41 * Num42
                    else:
                        if Equi4 == '/':
                            Result4 == Num41 / Num42
                        else:
                            print('Please Enter a correct equiation symbol')
            Num51 = input("Please enter the first number of the equation")
            Equi5 = input('Please Enter Equiation Type +, -, *, or /')
            Num52 = input('Please Enter Second Number')
            # Checking what equation to do
            if Equi4 == '+':
                Result5 = Num51 + Num52
            else:
                if Equi5 == '-':
                    Result5 = Num51 - Num52
                else:
                    if Equi5 == '*':
                        Result5 = Num51 * Num52
                    else:
                        if Equi5 == '/':
                            Result5 == Num51 / Num52
                        else:
                            print('Please Enter a correct equiation symbol')
        else:
            if Type == '2':
                # Getting the inputed answers for the problems
                print('Please Answer these 5 questions')
                print(*Num11, ' '*Equi1, ' '*Num12, '=')
                print(*Num21, ' '*Equi2, ' '*Num22, '=')
                print(*Num31, ' '*Equi3, ' '*Num32, '=')
                print(*Num41, ' '*Equi4, ' '*Num42, '=')
                print(*Num51, ' '*Equi5, ' '*Num52, '=')
                Ans1 = input('Enter the answer for question 1')
                if Result1 == Ans1:
                    print('Your Answer is Correct')
                else:
                    print('Your Answer is incorrect')
                Ans2 = input('Enter the answer for question 2')
                if Result2 == Ans2:
                    print('Your Answer is Correct')
                else:
                    print('Your Answer is incorrect')
                Ans3 = input('Enter the answer for question 3')
                if Result3 == Ans3:
                    print('Your Answer is Correct')
                else:
                    print('Your Answer is incorrect')
                Ans4 = input('Enter the answer for question 4')
                if Result4 == Ans4:
                    print('Your Answer is Correct')
                else:
                    print('Your Answer is incorrect')
                Ans5 = input('Enter the answer for question 5')
                if Result5 == Ans5:
                    print('Your Answer is Correct')
                else:
                    print('Your Answer is incorrect')
                Con = input('Would you like to continue? Y/N')
                if Con =='Y':
                 Continue == True
                else:
                    if Con == 'N':
                        Continue == False

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