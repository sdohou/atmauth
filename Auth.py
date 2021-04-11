import random

#Datetime object- current date and time
from datetime import datetime 
now = datetime.now()

#Account info
acctBalance = 1500

#dictionary
database = {} 

# Initializing the system (Welcome Page)
def init():
    print("\n ********* Welcome to Python Bank ********* \n")
    dt_string()
    haveAccount = int(input("\nDo you have account with us: 1 (Yes) 2 (No) \n"))

    if(haveAccount == 1):
        login()

    elif(haveAccount == 2):
        register()

    else:
        print("You have selected an invalid option.")
        init()

# Login
# - account number & password

def login():
    
    print("********* Login ***********")

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password? \n")

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)
               
                
    print('Invalid account or password')
    login()
    
# Register
# - First name, last name, email, password

def register():

    print("****** Register for an Account *******")

    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    email = input("What is your email address? \n")
    password = input("Create your password: \n")

    accountNumber = generateAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password ]

    print("Your account has been created.")
    print("=== ===== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe.")
    print("=== ===== ====== ===== ===")

    login()

# Bank operations
def bankOperation(user):
    
    print("Hello %s %s " % ( user[0], user[1] ) )
    
    selectedOption = int(input("\nWhat would you like to do? (1) Deposit (2) Withdrawal (3) Exit Session (4) Logout  \n"))

    if(selectedOption == 1):
        depositOperation()

    elif(selectedOption == 2):
        withdrawalOperation()
        
    elif(selectedOption == 3):
        exit()
        
    elif(selectedOption == 4):
        logout()
        
    else:
      print("Invalid option selected.")  
    bankOperation(user)      


def depositOperation():
    
    print("****** Make a Deposit ******")
    print('Your account balance is: \n', int(acctBalance))
    cashDeposit = input('How much would you like to deposit? \n')
    sum = int(acctBalance) + int(cashDeposit)
    print('Transaction complete. Your balance is now: ', sum)
    exit()


def withdrawalOperation():
    
    print("****** Make a Withdrawal ******")
    print('Your account balance is: \n', int(acctBalance))
    withdrawal = input('How much would you like to withdraw? \n')
    print('Transaction complete. Please take your cash.\n')
    endBalance = int(acctBalance) - int(withdrawal)
    print('Your balance is now: ', endBalance)
    exit()

# - Generate user account
def generateAccountNumber():
    return random.randrange(1111111111,9999999999)

def exit():
    print('Session complete. Welcome back to the Main Menu.')
    
def logout():
    print('Thank you for choosing Python Bank. See you next time!')
    login()

# Datetime function
def dt_string():
    dt_string = now.strftime("%B %d, %Y %H:%M")
    print(dt_string)
    
  #### ACTUAL BANKING SYSTEM #####

init()
  
