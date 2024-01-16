print('''
               .---._
           .--(. '  .).--.      . .-.
        . ( ' _) .)` (   .)-. ( ) '-'
       ( ,  ).        `(' . _)
     (')  _________      '-'
     ____[_________]                                         ________
     \__/ | _ \  ||    ,;,;,,                               [________]
     _][__|(")/__||  ,;;;;;;;;,   __________   __________   _| LILI |_
    /             | |____      | |          | |  ___     | |      ____|
   (| .--.    .--.| |     ___  | |   |  |   | |      ____| |____      |
   /|/ .. \~~/ .. \_|_.-.__.-._|_|_.-:__:-._|_|_.-.__.-._|_|_.-.__.-._|
+=/_|\ '' /~~\ '' /=+( o )( o )+==( o )( o )=+=( o )( o )+==( o )( o )=+=
='=='='--'==+='--'===+'-'=='-'==+=='-'+='-'===+='-'=='-'==+=='-'=+'-'===+
''')
print("Welcome to The Train Adventure.")
print("Your mission is to get control of the train, to divert to kitten island.")

direction = input("You're standing in the middle of the train, do you choose to go left or right? \n")
if direction == "left":
    print("You are on the right track, head into the carriage full of daddy snacks!")

    snack_time = input("You've got the munchies, do you a) stop for a snack or b) continue your kitten journey? \n")
    if snack_time == "b":
        print("\n Sticking with the task at hand, we like to see it. Carry on my sweet. Go get them kitties")
        doors = input(
            "You've reached the end carriage of the train - theres three doors to choose from. Choose from: blue, red or black \n")
        if doors == "red":
            print(
                "You burst through the door of the drivers carriage, ready for a challenge to take control. You walk up to the drivers seat and spot Lola Puss - shes the driver and shes already on her way to kitten island to play. You take over and let her nap on your lap whilst you pick up the pace to get you both there. You Win!")
        elif doors == "blue":
            print(
                "You've picked the wrong door and fallen into Man City's ground. They are beating Liverpool 2-0. Game Over!")
        elif doors == "black":
            print(
                "You had so much promise, it was only a door that you had to choose. You've ended up getting off the train and instead of fun on kitten island you are at a farmers market, looking at endless trinkets in a neverending loop. Game Over!")
        else:
            print("Theres no door that colour, cheater. You lose, Game over!")
    else:
        print(
            "NOOOOO, you started with the one snack and just couldn't stop. nom nom nom nom nom. Time for a nap and you missed your chance to get to the beautiful land of the kittens. Game Over!")
else:
    print("Soz you fucked it, theres some snakes in this carriage and you've become the snack! Game Over!")

