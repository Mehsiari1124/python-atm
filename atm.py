print("Welcome to UnionBank ATM")
restart = ('y')
chances = 3
balance = 5000

while chances >= 0:
    pin = int(input("Please enter your 4 digit Pin: "))
    if pin == (0000):
        print("Pin successfully entered\n")
        while restart not in('n', 'NO', 'no', 'N'):
            print("1) Balance Inquiry")
            print("2) Withdraw")
            print("3) To Pay In")
            print("4) To return your card")
            print("5) Exit\n")
            option = int(input("Enter your transaction: "))
            if option == 1:

            
                print("\nYour balance is P",balance)
                restart = input("\nWould you like to do another transaction?")
                if restart in ('n', 'NO', 'no', 'N'):
                    print("Thank You")
                    break

            elif option == 2:
                    option2 = ('y')
                    withdraw1 = int(input("Enter Amount to withdraw: "))
                    if withdraw1 in [100, 200, 500, 1000]:
                        balance = balance - withdraw1
                        print("\nYour balance now is P",balance)
                        restart = input("would you like to go back?")
                        if restart in ('n', 'NO', 'no', 'N'):
                            print('thank you')
                            break
                    elif withdraw1 != [100, 200, 500, 1000]:
                        print("Invalid amount, please enter a new amount\n")
                        restart = ('y')
                    elif withdraw1 == 1:
                        withdraw1 = int(input("Pease entered your desired amount"))

            elif option == 3:
                    Pay_in = int(input("How much would you like to pay in:"))
                    balance = balance + Pay_in
                    print("Your balance is P",balance)
                    if restart in ('n', 'NO', 'no', 'N'):
                        print('thank you')
                        break
            
            elif option == 4:
                 print("Please wait while your Card is Returned...")
                 print("Thank You for using our service...")
                 break
            elif option == 5:
                 exit()

            else:
                 print("Please enter a correct number...")
                 restart = 'Y'
            
    elif pin != ('0000'):
         print("Incorrect PIN...")
         chances = chances - 1
         if chances == 0:
              print("No more tries...")
              break



