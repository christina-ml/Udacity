import time
import random

#def play_game():
#starts the game

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)

def intro():
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause("Time to make some moves.")

def first_choices():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("Enter 3 to go down to the river.")

def field():
    print_pause("Now you are back onto the field.")
    # Just in case the player wants to go back out to the field.

# def house():
    # If the player wants to go back to the house.

def dragon():

    print_pause("Enter 1 to fight the dragon.")
    print_pause("Enter 2 to run away.")
    print_pause("Enter 3 to hide until the dragon goes away.")

    # To determine the next moves for the player. 

def effectiveness(health):
    health = random.randint(0,100)
    if health < 101:
        print_pause("a little scratch") 
    elif health < 50:
        print_pause("Gasping for air")
    elif health < 30:
        print_pause("Not quite finished")
    elif health < 10:
        print_pause("Death")
    print_pause(health)


intro() 
health = []
first_choices() 

while True:
    response = input("Please take your pick. Choice number 1 or 2 or 3?")
    if "1" in response:
        print_pause("You go knock on the door of the house.")
        print_pause("Suddenly, you see a big dragon with wings that's ready to attack you!")
        dragon()
        break

    elif "2" in response:
        print_pause("You peer into the cave.")
        print_pause("You find the weapons and tools necessary to fight off the enemies.")
        print_pause("Now you are back out onto the field.")
        break
    elif "3" in response:
        print_pause("You go down to the river to regain health.")
        print_pause("You gain 15 points in health.")
        print_pause("Now your health is full.")
    else:
        print_pause("Please choose between 1 or 2 or 3.")

while True:
    response = input("Choose between the 3.")
    if "1" in response:
        print_pause("You stab the dragon with your dagger!")
        print_pause("The dragon's health is down 5 points.")
        effectiveness(health)
        
    
    if "2" in response: 
        print_pause("You ran away. You are back out onto the field.")
    if "3" in response:
        print_pause("You have hidden successfully. The dragon has left.")



# for the first choice: need to use the "def effectiveness" to progress the game forward.
# for the second choice: need to have the three choices repeat, and THEN choose between 1, 2, or 3.
# for the third choice: fix the elif "3" in  response: define the response to make progress to the game.

# Added an empty list for health (should be at the start of your code somewhere)
# Made health visible.  Need to fix everything inside def effectiveness(health) so that the
# random.randint number can actually be used. health < 80 means the random number has to be 
# less than 80 to show up...


        


