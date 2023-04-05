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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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
#Write your code below this line 👇
d1 = input("You've entered a hallway, you see the floor cracked up in front of you, obviously dangerous and a spike wall following you from behind, theres a door to your 'left' and your 'right'. Which way to you want to go?\n").lower()

if d1 == "right":
    d2 = input("You enter the right door and fall down a hole, as you land and get up you are now in a dark cave, you see a mining cart on some rails, do you 'get in' the cart? or 'walk' down the rails?\n").lower()
    if d2 == "walk":
        d3 = input("As you follow the rails you arrive to a pool of lava, your only option is to walk either 'left' or 'right', which way do you go?\n").lower()
        if d3 == "left":
            d4 = input("You arrive to a flat wall with three doors, a 'red' door, a 'blue' door and a 'yellow' door. Which door do you enter?\n").lower()
            if d4 == "yellow":
                print("You have found the treasure!!!! Its a chest full of rare hentai. Congratulations!!")
            elif d4 == "blue":
                print("You enter the blue door, as you close the door behind you everything turns pitch black.. You hear a sinister laugh before you faint. It was Bill Harrington and you just got raped to death.")
            elif d4 == "red":
                print("You enter the red door, and you seam to lack common sense because red is usualy the color of the enemy, and guess what. Every single enemy you have has materialized infront of you into one big blobb monster. It consumes you whole and you die.")
            else:
                print("Well, here we go again with not being able to follow instructions... a higher being punishes you by dropping a Hercules aircraft carrier ontop of your head for being disobediant. You die.")
        elif d3 == "right":
            print("You continue your way to the right and come across a ceiling full of vampire bats who smells you and sucks you dry, not in the good way.. You die. ")
        else:
            print("You seam to have forgotten how to follow instructions, you walk into the lava and you guessed it! Died.")

    elif d2 == "get in":
        print("The cart starts moving with increasing speed, as it gathers enough momentum to be too fast to jump of the rails end and you fall down a pool of lava. You died")
    else:
        print("You seam to have a stroke while reading the question and faint and with no one around to help you, guess what.. You died")
elif d1 == "left":
    print("You entered a room full of hungry hamsters, they eat you and you die.")
else:
    print("You fucking idiot, didn't you read? Well.. you died... obviously..")