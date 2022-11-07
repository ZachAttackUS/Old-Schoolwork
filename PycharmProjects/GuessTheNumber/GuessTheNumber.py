import random


class Game():

    def setUpNumberAndAsk():
        GuessNumber = str(random.randint(0,100))
        print(GuessNumber)
        Useranswer = str(input("Guess the Number"))
        if Useranswer == GuessNumber:
            Game.guessequalUser()
        elif Useranswer > GuessNumber:
            Game.sayLower()
            Game.Guessagain()
            if Useranswer == GuessNumber:
                Game.guessequalUser()
            elif Useranswer > GuessNumber:
                Game.sayLower()
                Game.Guessagain()
                if Useranswer == GuessNumber:
                    Game.guessequalUser()
                elif Useranswer > GuessNumber:
                    Game.sayLower()
                    Game.Guessagain()
                    if Useranswer == GuessNumber:
                        Game.guessequalUser()
                    elif Useranswer > GuessNumber:
                        Game.sayLower()
                        Game.Guessagain()
                    elif Useranswer < GuessNumber:
                        Game.sayHigher()
                        Game.Guessagain()
                elif Useranswer < GuessNumber:
                    Game.sayHigher()
                    Game.Guessagain()
                    if Useranswer == GuessNumber:
                        Game.guessequalUser()
                    elif Useranswer > GuessNumber:
                        Game.sayLower()
                        Game.Guessagain()
                    elif Useranswer < GuessNumber:
                        Game.sayHigher()
                        Game.Guessagain()
            elif Useranswer < GuessNumber:
                Game.sayHigher()
                Game.Guessagain()
                if Useranswer == GuessNumber:
                    Game.guessequalUser()
                elif Useranswer > GuessNumber:
                    Game.sayLower()
                    Game.Guessagain()
                    if Useranswer == GuessNumber:
                        Game.guessequalUser()
                    elif Useranswer > GuessNumber:
                        Game.sayLower()
                        Game.Guessagain()
                    elif Useranswer < GuessNumber:
                        Game.sayHigher()
                        Game.Guessagain()
                elif Useranswer < GuessNumber:
                    Game.sayHigher()
                    Game.Guessagain()
                    if Useranswer == GuessNumber:
                        Game.guessequalUser()
                    elif Useranswer > GuessNumber:
                        Game.sayLower()
                        Game.Guessagain()
                    elif Useranswer < GuessNumber:
                        Game.sayHigher()
                        Game.Guessagain()
        elif Useranswer < GuessNumber:
            Game.sayHigher()
            Game.Guessagain()
            if Useranswer == GuessNumber:
                Game.guessequalUser()
            elif Useranswer > GuessNumber:
                Game.sayLower()
                Game.Guessagain()
                if Useranswer == GuessNumber:
                    Game.guessequalUser()
                elif Useranswer > GuessNumber:
                    Game.sayLower()
                    Game.Guessagain()
                    if Useranswer == GuessNumber:
                        Game.guessequalUser()
                    elif Useranswer > GuessNumber:
                        Game.sayLower()
                        Game.Guessagain()
                    elif Useranswer < GuessNumber:
                        Game.sayHigher()
                        Game.Guessagain()
                elif Useranswer < GuessNumber:
                    Game.sayHigher()
                    Game.Guessagain()
                    if Useranswer == GuessNumber:
                        Game.guessequalUser()
                    elif Useranswer > GuessNumber:
                        Game.sayLower()
                        Game.Guessagain()
                    elif Useranswer < GuessNumber:
                        Game.sayHigher()
                        Game.Guessagain()
            elif Useranswer < GuessNumber:
                Game.sayHigher()
                Game.Guessagain()
                if Useranswer == GuessNumber:
                    Game.guessequalUser()
                elif Useranswer > GuessNumber:
                    Game.sayLower()
                    Game.Guessagain()
                    if Useranswer == GuessNumber:
                        Game.guessequalUser()
                    elif Useranswer > GuessNumber:
                        Game.sayLower()
                        Game.Guessagain()
                    elif Useranswer < GuessNumber:
                        Game.sayHigher()
                        Game.Guessagain()
                elif Useranswer < GuessNumber:
                    Game.sayHigher()
                    Game.Guessagain()
                    if Useranswer == GuessNumber:
                        Game.guessequalUser()
                    elif Useranswer > GuessNumber:
                        Game.sayLower()
                        Game.Guessagain()
                    elif Useranswer < GuessNumber:
                        Game.sayHigher()
                        Game.Guessagain()

    def guessequalUser():
        print("You did it! Wow I'm impressed!")

    def Guessagain():
        Useranswer = input("Guess the number again")

    def sayHigher():
        print("You guessed too low!")
        
    def sayLower():
        print("You guessed too high!")


Game.setUpNumberAndAsk()