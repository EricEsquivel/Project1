"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random
import sys

def start_game():
  
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player. done
    2. Store a random number as the answer/solution. done
    3. Continuously prompt the player for a guess. done
      a. If the guess greater than the solution, display to the player "It's lower". done
      b. If the guess is less than the solution, display to the player "It's higher". done
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number. done
    5. Let the player know the game is ending, or something that indicates the game is over. done
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    print("""
================================================

WELCOME TO THE NUMBER GUESSING GAME!
GUESS THE NUMBER 0-10!

=================================================
""")

again = "yes"
    
def end_game():
    print(f"""
Congrats! You beat {difficulty} difficulty! The answer was {randomnumber}.
You took {attempts} attempts. Thanks for playing!
""")
    


# Kick off the program by calling the start_game function.
start_game()


while again.lower() == "yes":

    randomnumber = random.randint(0, 10)
    number = -1 #if number was 0 and randomnumber was 0, the game would finish instantly
    attempts = 0
    try:
        difficulty = input("Pick your difficulty! Hard means you only have 4 attempts! Normal means you have infinite attempts! (HARD/NORMAL) ")
        if difficulty.lower() != "hard" and difficulty.lower() != "normal":
            raise ValueError("That's not a proper difficulty!")
    except ValueError as err:
        print(err)
    #HARD DIFFICULTY    
    if difficulty.lower() == "hard":
        print("You have chosen the hard difficulty!")
        while number != randomnumber:
            if attempts < 4:
                print(number) # uncomment this line and the one below to check ur number and the random number generated (USE FOR TESTING PURPOSES), program runs w/o it
                print(randomnumber)
                try:
                    number = int(input("Enter a number: "))
                except ValueError:
                    print("Enter an integer! No attempts taken off. Try again!")
                    continue
                if number > 10:
                    print("Number outside range. No attempts taken. Try again.")
                    continue
                if randomnumber > number:
                    print("It's higher!")
                elif randomnumber < number:
                    print("It's lower!")
                attempts += 1
            else:
                print(f"FAIL! You took more than 4 attempts! The answer was {randomnumber}.")
                again = input("Would you like to play again? (YES/NO) ")
                if again.lower() == "yes":
                    break
                    continue
                else:
                    sys.exit("Thanks for playing!")
        if number == randomnumber:
            end_game()
            again = input("Would you like to play again? (YES/NO) ")
            if again.lower() == "yes":
                continue
            else:
                sys.exit()
    #NORMAL DIFFICULTY    
    elif difficulty.lower() == "normal":
        print("You have chosen the normal difficulty!")
        while number != randomnumber:
            #print(number) # uncomment this line and the one below to check ur number and the random number generated (USE FOR TESTING PURPOSES)
            #print(randomnumber)
            try:
                number = int(input("Enter a number: "))
            except ValueError as err:
                print("Enter an integer! No attempts taken off. Try again!")
                continue
            if number > 10:
                print("Number outside range. No attempts taken. Try again.")
                continue
            if randomnumber > number:
                print("It's higher!")
            elif randomnumber < number:
                print("It's lower!")
            attempts += 1
        end_game()
        again = input("Would you like to play again? (YES/NO) ")
        if again.lower() == "yes":
            continue
        else:
            sys.exit()