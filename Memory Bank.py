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