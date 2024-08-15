print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go? '
                'Type "left" or "right".\n').lower()
if choice1 == "left":
    choice2 = input("While walking to the left you've came across a debris. ""What do you do? "
                    "Type 'jump' to try jumping over it or 'walk around' to walk around of it.\n").lower()
    if choice2 == "walk around":
        choice3 = input("Now you have come to a lake. There is an island in the middle of the lake."
                        "Type 'swim' to swim across. Type 'wait' to wait for a boat.\n").lower()
        if choice3 == "wait":
            choice4 = input("You arrive at the island. There is a house with 3 doors."
                            "One red, One green. one blue. Which colour do you choose?\n").lower()
            if choice4 == "red":
                print("You entered a room with full of fire. Game Over!")
            elif choice4 == "blue":
                print("You get frozen. Game Over!")
            elif choice4 == "green":
                choice5 = input("You entered a room with an apple on the table. What do you do?"
                                "Type 'eat' to eat the apple or 'throw' to throw it into trash.\n").lower()
                if choice5 == "throw":
                    print("Congratulations. A door with treasure has now opened.")
                elif choice5 == "eat":
                    print("You get poisoned. Game Over!")
                else:
                    print("You have done something you shouldn't! Now you are locked in this room. Game Over!")
            else:
                print("You didn't pick any room. You get kicked out of house. Game Over!")
        else:
            print("You get attacked by an angry trout. Game Over!")
    else:
        print("You sprained your foot. Game Over!")
else:
    print("You fell into a hole. Game Over!")


