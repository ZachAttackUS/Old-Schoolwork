import random

class Game():

    def start():
        global point
        lettervalue = random.randint(3, 9)
        answer = input("What is a " + str(lettervalue) +  " letter word?")
        list1 = []
        for i in answer:
            if i != " ":
                list1.append(answer)
        if len(list1) == lettervalue:
            point = point +1
            print("Good Job!")
            print("You have " + str(point) + " points")
            Game.start()


        else:
            print("You Lose!")
            print("You ended with " + str(point) + " points")
            yesList = ("yes","yeah","sure", "definitely", "y", "ye", "yah","yeah", " yes", " yeah", " sure", " definitely", " y", " ye", " yah", " yeah")
            restart = input("Do you want to try again?")
            if restart in yesList:
                point = 0
                Game.start()
            else:
                print("Game Over!")



point = 0
Game.start()