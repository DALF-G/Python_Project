import math
from turtle import rt
print("Welcome to the online banking application")
def signin():
    global name # username
    global pin # password
    global cb # current balance
    name = str(input("Please create your user name"))
    pin = str(input("Please create your 6 digit pin"))
    if len(pin)==6:
        pin = pin
    else:
        print("The pin has to be 6 digits")   
        newpin = str(input("Please create your 6 digit pin")) 
        if len(newpin) !=6:
            print("the pin has to be 6 digits")
            signin()
        else:
            pin = newpin  
    print("Thanks for creating your bank account")

def forgotpin():
    recoverpin = str(input("Please create your new 6 digit pin"))   
    if len(recoverpin) !=6:
        print("The pin has to be in 6 digits") 
        forgotpin()
    else:
        print("The new pi has been stored, please log in") 
        pin = recoverpin
        login()

def depositinterest(p,r,t):
    # A = pe^(rt) which is the formula for calculating the compound interest
    p = float(p)
    r = float(r)
    t = float(t)
    rt = r * t
    e = math.exp(rt)
    #calculations
    a = p * e # Future value of your investment  
    return a      
def login():
    # name1 represent username
    # pin1 represent user's pin 
    name1 = str(input("Please enter your username"))
    pin1 = str(input("Please enter your pin"))
    # check if the name and pin match
    if name1 == name and pin1 == pin:
        print("Welcome to the online banking application" + "" + name)
        print("Please choose the menu down here")
        listmenu =["1-Deposit","2-Withdraw","3-Transfer","4-Check Balance","5-Deposit interest rate","6-Calculate compound interest rate"]
        for b in listmenu:
            print(b)
        choose = int(input("Please enter the number of your chose"))
        d = 0 # d represents deposit
        w = 0 # w represents withdraw
        cb = 0 # cb represents current balance
        if choose ==1:
            d = int(input("Enter the amount of your deposit"))
            cb = d
            print("Your account balance is" + "" + str(cb))

        elif choose ==2:
            w = int(input("Enter the amount of money that you want to withdraw"))
            if w > cb:
                print("Your current balance is not sufficient for this transaction")
                login()
            else:
                cb = d-w 
                print(str(w) +""+ "has been withdrawn from your account" +""+ "and your current balance is" +""+ str(cb)) 
        elif choose ==3:
            dest = str(input("Please enter the account number of your destination in 8 digits"))
            if len(dest) == 8:
                amount = int(input("Please enter the amount of money you want to transfer"))
                if amount > cb:
                    print("Your current balance is not sufficient for this transaction")
                    login()
                else:
                    cb = d - amount
                    print("The transaction of" + "" + str(amount) +""+ "has been transfered to" + "" + str(dest) + " "+ "your current balance is" + str(cb))

            else:
                print("The transaction has been rejected since the destination account number is invalid") 


        elif choose ==4:
            print("Your current balance is" + "" + str(cb))

        elif choose ==5:
            if d > 50000:
                rate = 3
            elif d > 30000:
                rate =2
            else:
                rate =1.5
            print("Your current deposit interest rate is"+ "" + str(rate) + " %")

        elif choose ==6:
            listoption = ["1-calculate your deposit compound interest based on your CB","2-Calculate your deposit compound interest based on your deposit input"]
            for n in listoption:
                print(n)
            choice = int(input("Please enter your choice from the options above"))
            if choice ==1:
                timing = str(input("How many years you want to invest your money?"))
                if d > 50000:
                    ratex = 3/100
                elif d > 30000:
                    ratex =2/100
                else:
                    ratex = 1.5/100
                print("Your current balance in" + "" + "timing" +""+ "years will be")
                print(depositinterest(cb,ratex,timing)) 
            elif choice ==2:
                timing1 = str(input("How many years you want to invest your money?"))
                money = str(input("Please enter the ammount of money you would like to deposit")) 
                money = int(money)
                if d > 50000:
                    ratex = 3/100
                elif d > 30000:
                    ratex =2/100
                else:
                    ratex = 1.5/100
                print("Your current balance in" + "" + "timing" +""+ "years will be")
                print(depositinterest(money,ratex,timing)) 

        else:
            print("Option is not availabe,back to main menu")
            login()                 

    else:
        print("Either your username or pin is wrong,did you create your account?") 
        list1 = ["1-Yes","2-No"]  
        for i in list1:
            print(i)
        inp = int(input("Enter your choice below")) 
        if inp == 1:
            list2 = ["1-do you want to attempt to log in again?","2-you forgot your Pin"]
            for e in list2:
                print(e)
            theanswer = str(input("please enter your choice"))
            theanswer = int(theanswer)
            if theanswer ==1:
                login()
            elif theanswer == 2:
                forgotpin()
            else:
                print("Option is not available")  
                login() 

        elif inp ==2:
            print("please create your account") 
            signin()                  

def mainmenu():
    optionone = int(input("choose 1 to sign in and choose 2 to log in"))
    if optionone == 1:
        signin()
    elif optionone ==2:
        login()
    else:
        print("Option not available")
        mainmenu()
    exit()    

def exit():
    answer = str(input("Do you want to conduct transaction? Yes or No")) 
    if answer =="Yes":
        login()
    elif answer =="No":
        print("Thank you for using this App")
    else:
        print("Option is not Available")
        mainmenu()
mainmenu()





