def main():

    #problem1()
    #problem2()
    #problem3()
    problem4()


    #Problem 1:
#Create a function with two variables.
#One should equal “My name is: “ and the other should equal your actual name.
#Print the two variables in one print message.

def problem1():
    myNameis = "My name is: "
    myActualName= "Leighton"
    print(myNameis + myActualName)


    #Problem 2:
#Create a function to ask the user to enter the extra credit they earned.
#If they entered less than 5 print “That’s not enough extra credit.”
#If they entered more than 20 print “That’s too much extra credit”.

def problem2():
    credit = int(input("How much was your extra credit"))
    if (credit < 5):
        print("That's not enough extra credit")
    elif (credit > 20):
        print("That's too much credit")


    #Problem 3:
#Create a function to ask a user to enter a password.
#Ask user to reenter password.
#Check to see if they are correct.

def problem3():
    password= input("Please enter your password")
    password2= input("Please enter password again to verify")
    if (password == password2):
        print("Thank you")
    else:
        print("Passwords do not match")

    #Problem 4:
#Create a function to ask for two card numbers.
#If it equals 21 print BLACKJACK!, if it’s greater than 21 print BUST!,
#if it’s less than 21 print “The total is [THE TOTAL]”

def problem4():
    cardNumber1= int (input("Please enter a card number"))
    cardNumber2= int (input("Please enter a 2nd card"))
    if (cardNumber1 + cardNumber2 == 21):
        print ("BLACK JACK")
    elif (cardNumber1 + cardNumber2 > 21):
        print ("BUST")
    else:
        print("The total is " + str(cardNumber2 + cardNumber1))

if __name__ == '__main__':
    main()