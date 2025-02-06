import random
#display the welcome message
print("Welcome to the Chore Designator.")
#prompt the user to enter the chore and save in appropriately named variable
choreName = input("What is the chore that needs to be completed?: ")
#promt for the first user's name and save in an approprately named variable 
user1 = input("Enter the name of the first user: ")
#promt for the second user's name and save in an approprately name variable 
user2 = input("Enter the name of the second user: ")
print("Time to play a game to determine whether " + user1 + " or " + user2 + " will complete the chore: " + choreName)
print("Whoever guesses the secret number FIRST will be exempt from doing the chore.")
print("May the odds be ever in your favor. BEGIN!!!")

#Complete the code for the decider function
def decider(user1, user2):
    randNum = random.randint(1,11)
    decision = 0
#write the code to complete the while loop
    while decision == 0:
#prompt each user to enter a number between 1 and 10 and save the input
        guess1 = int(input(f"{user1} enter your guess between 1 and 10: "))
        guess2 = int(input(f"{user2} enter your guess between 1 and 10: "))
#using each uer's guess, determine who loses
        if guess1 == randNum:
            print(user2, "you lose. You have to complete the chore of", choreName)
            decision = 1
            
        elif guess2 == randNum:
            print(user2, "you lose. You have to complete the chore of", choreName)
            decision = 1
            
        else:
            print("Neither guesses were correct. Try again!")
            decision = 0
            
        
    


#call the decider function with the approprate parameters and save retrun value return decider(user1, user2)
decider(user1, user2)
#display who won with an appropriate message (see sample output)

