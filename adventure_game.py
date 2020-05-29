import time
import random


def print_pause(str):
    print(str)
    time.sleep(1)


def intro():

    print_pause("\nYou find yourself standing in an open field.")
    print_pause("It is filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairie is somewhere around here.")
    print_pause("It has been terrifying the nearby village.\n")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but rather small) dagger")


def field(items):
    print("\nEnter 1 to knock on the door of the house.")
    print("Enter 2 to peer into the cave.")
    choice = choose()
    if choice == '1':
        house(items)
    if choice == '2':
        cave(items)


def choose():
    while True:
        choice = input("What would you like to do?  Enter 1 or 2:  ")
        if choice == '1' or choice == '2':
            return choice


def play_again():
    print("GAME OVER\n")
    while True:
        choice = input("\nWould you like to play again? y/n \n")
        if choice == 'y':
            play_game()
        if choice == 'n':
            exit()


def fight(items):
    if 'sword' in items:
        print_pause("\nYou pull out your new bad boy magical weapon.")
        print_pause("It bursts out a glow of fantastical energy!")
        print_pause("The evil fairie cowers in fright...")
        print_pause("Beacue the power of your new toy is too much!")
        print_pause("The fairie flies off, never to be seen again.")
        print_pause("You have ridden the village of it's evil foe.")
        print_pause("You are victorious!")
        play_again()

    else:
        print_pause("\nYour feeble dagger is no match for the fairie.")
        print_pause("It easily disembowels you and feeds on your intestines.")
        print_pause("You have died most gruesomely...")
        print_pause("..and the village has not been saved...")
        play_again()


def house(items):
    print_pause("\nYou approach the door of the house.")
    print_pause("You are about to knock when the door opens...")
    print_pause("and out steps a wicked fairie!")
    print_pause("Eep! This is the wicked fairie's house!")
    print_pause("The wicked fairie attacks you!")
    if 'sword' not in items:
        print_pause("You feel a bit under-prepared for this.")
        print_pause("...you only having a tiny dagger...")
    print("\nEnter 1 to Fight!")
    print("Enter 2 to flee...")
    choice = choose()
    if choice == '1':
        fight(items)
    if choice == '2':
        print_pause("\nYou run back to the field for safety.")
        print_pause("Luckily you don't seem to have been followed.")
        field(items)


def cave(items):
    swords = ["sword of Obolisk",
              "axe of Giant's Bane", "Grim Repear's Scytch"]
    sword = random.choice(swords)

    print_pause("\nYou peer cautiously into the cave")
    print_pause("It turns out to be a very small cave.")
    if sword in items:
        print_pause("You've been here before and gotten all the good stuff.")
        print_pause("It's just an empty cave now.")
    else:
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You found the legendary " + sword + "!")
        print_pause("You toss your silly old dagger to the ground.")
        print_pause("This " + sword + " is your new bad boy toy!")
        items.append('sword')
    print_pause("You walk back out to the field")
    field(items)


def play_game():
    items = []
    intro()
    field(items)


play_game()
