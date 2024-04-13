from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#function to check user's guess against actual answer
def checkAns(guess,answer,turns):
    """Checks ans against guess returns turns remaining after each guess"""
    if guess>answer:
        print("The guess is too high")
        return turns - 1
    elif guess<answer:
        print("The guess is too low ") 
        return turns - 1 
    elif guess == answer:
        print(f"Correct! The answer is {answer}")

#function to set difficulty
def setDifficulty():
    level = input("Choose a difficulty type 'easy' or 'hard'")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS    

#choose a random number 1-100
def game():
    print("Welcome to the Guessing game!")
    print("I am Thinking of a number between 1-100!")
    answer = randint(1,100)
    print(f"The answer is {answer}")

    turns = setDifficulty()

    
    #repeating as long as attempts left
    guess = 0
    while guess!= answer:
        #Let the use guess a number
        guess = int(input("Make a guesss! "))
        turns = checkAns(guess,answer,turns) # so we update the turns variable 
        print(f"You have {turns} attemps remaining ")
        if turns == 0 :
            print("You Lose no turns left")
            return    
game()
#Track the no of turns and reduce by one if they get it wrong





