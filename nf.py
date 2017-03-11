import random
def mastermind():
    colours = ["R", "G", "B", "Y", "W", "O"] #R-RED,G-GREEN,B-BLUE,Y-YELLOW,W-WHITE,O-ORANGE
    attempts = 0
    game = True
    s=1
    colour_code = random.sample(colours,4)	
    print ("START GUESSING")	
    while game:
            correct_colour = ""
            guessed_colour = ""
            player_guess=""
            player_guess=raw_input().upper()
            attempts+= 1
            if len(player_guess) != len(colour_code):
                    print ("The secret code needs to have exactly four colors")
                    continue
            for i in range(4):
                    if player_guess[i] not in colours:
                            print ("invalid input")
                            continue
            if correct_colour != "bbbb":
                    for i in range(4):
                            if player_guess[i] == colour_code[i]:
                                    correct_colour += "b"
                            if  player_guess[i] != colour_code[i] and player_guess[i] in colour_code:
                                    guessed_colour += "w"
                    print (correct_colour +  guessed_colour + "\n")		
                    
            if correct_colour == "bbbb":
                    if attempts == 1:
                            print ("You guessed at the first attempt!")
                    else:
                            print ("Well done... You needed " + str(attempts) + " attempts to guess.")
                    game = False
                    
            if attempts >= 1 and attempts <6 and correct_colour != "bbbb":
                    print ("Next attempt: ")
            elif attempts >= 6:
                    print ("You didn't guess! The secret color code was: " + str(colour_code))	

            #To play or not to play
            while game == False:
                    finish_game = input("Do you want to play again (Y/N)?").upper()	
                    attempts = 0
                    if finish_game =="N":
                            print ("Thanks for the game")
                    elif finish_game == "Y":
                            game = True
                            print ("Let's play again.Guess the secret code: ")
