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
                        