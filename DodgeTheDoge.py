#Dodge The Doge
#2/4/18
#Conceptualized and Created by Chidi Ewenike and Daniel Ramsey
#Developed using Mac, using CodeRunner and Python IDLE with Pygame Library
#HackPoly 2018

import turtle
import os
import math
import random
import sys
#pygame used for the sound block, that is commemnted out below
#import pygame

#This block of code is supposed to play spongebob, but my python crashes if it runs
#pygame.init()
#pygame.mixer.init()
#sounda= pygame.mixer.Sound("SpongeBob_Song.wav")
#sounda.play()

#Global variables allow variables to be used in loops, definitions, and statements
global level  #for keeping track of levels, start at level 1
level = 1
global explodeBool 
global explosion
global Gameover #for keeping track of Gameover condition
Gameover = False

#Spongebob theme song plays once and doesnt repeats
os.system("afplay SpongeBob_Song.wav&") #song plays

#Creates instructions for the game located at the bottom of the screen

Start_pen = turtle.Turtle()
Start_pen.speed(0)
Start_pen.color("white")
Start_pen.penup()
Start_pen.setposition(0, 270)
Startstring = "Avoid doge! Get to the bottom for next level!"
Start_pen.write(Startstring, False, align="center", font=("Arial", 20, "normal"))
Start_pen.hideturtle()

#Prints the initial level the user is on 
level_pen = turtle.Turtle()
level_pen.clear()
level_pen.speed(0)
level_pen.color("white")
level_pen.penup()
level_pen.setposition(-280, 0)
levelstring = "Level: %s" %level
level_pen.write(levelstring, False, align="left", font=("Arial", 14, "normal"))
level_pen.hideturtle()


#While loop loops for each level player enters, until the game is over
#Contents of the while loop contain the creation code for the border, ground pieces, explosion, player, doge bomb, player movement
while not Gameover:
        
        #Creates a blackbackground 
        wn = turtle.Screen()
        wn.bgpic("background.gif")
        wn.bgcolor("black")
        win = True
        
        
        explodeBool = False
        explosionCounter = 0
        xPlayerBlockPos = 0  #Default value
        yCurr = 0
        
        #All of these images must be in the same folder of this file, and are required for the images 
        turtle.register_shape("Ground.gif")
        turtle.register_shape("dogebomb.gif")
        turtle.register_shape("UK.gif")
        turtle.register_shape("Explode.gif")

        #Creates the explosion image
        explosion = turtle.Turtle()
        explosion.speed(0) 
        explosion.penup() 
        explosion.shape("Explode.gif")

        #Border Creation
        border_pen = turtle.Turtle() #Creates a pen shape
        border_pen.speed(0) #Draws border as fast as it can
        border_pen.color("black")
        border_pen.penup() #So that pen will not draw border from middle to edge of screen
        border_pen.setposition(-200, -300) #Center was 0,0 pixels
        border_pen.pendown() #places pen down so that it can draw border
        border_pen.pensize(1) #3 pixels wide
        border_pen.fd(400) #forward 600 pixels
        border_pen.lt(90)    #left 90 degrees
        border_pen.fd(600) #forward 600 pixels
        border_pen.lt(90)    #left 90 degrees
        border_pen.fd(400) #forward 600 pixels
        border_pen.lt(90)    #left 90 degrees
        border_pen.fd(600) #forward 600 pixels
        border_pen.hideturtle() #we hide turtle because we dont need it anymore

        #Player creation
        player = turtle.Turtle()
        player.shape("UK.gif")
        player.penup()  #We are not draawing a line
        player.speed(0) #We want to create it as fast as possible
        player.setposition(-160, 163)
        player.setheading(90) #turns the triangle head 90 degrees upright

        #Ground turtles for Column 1
        
        Ground00 = turtle.Turtle() #Creates a pen shape
        Ground00.shape("Ground.gif")
        Ground00.penup()  #We are not draawing a line
        Ground00.speed(0) #We want to create it as fast as possible
        Ground00.setposition(-160, 95)

        Ground10 = turtle.Turtle() #Creates a pen shape
        Ground10.shape("Ground.gif")
        Ground10.penup()  #We are not draawing a line
        Ground10.speed(0) #We want to create it as fast as possible
        Ground10.setposition(-160, 25)
                
        Ground20 = turtle.Turtle() #Creates a pen shape
        Ground20.shape("Ground.gif")
        Ground20.penup()  #We are not draawing a line
        Ground20.speed(0) #We want to create it as fast as possible
        Ground20.setposition(-160, -45)

        Ground30 = turtle.Turtle() #Creates a pen shape
        Ground30.shape("Ground.gif")
        Ground30.penup()  #We are not draawing a line
        Ground30.speed(0) #We want to create it as fast as possible
        Ground30.setposition(-160, -115)

        Ground40 = turtle.Turtle() #Creates a pen shape
        Ground40.shape("Ground.gif")
        Ground40.penup()  #We are not draawing a line
        Ground40.speed(0) #We want to create it as fast as possible
        Ground40.setposition(-160, -185)

        #Ground turles for column 2

        Ground01 = turtle.Turtle() #Creates a pen shape
        Ground01.shape("Ground.gif")
        Ground01.penup()  #We are not draawing a line
        Ground01.speed(0) #We want to create it as fast as possible
        Ground01.setposition(-80, 95)

        Ground11 = turtle.Turtle() #Creates a pen shape
        Ground11.shape("Ground.gif")
        Ground11.penup()  #We are not draawing a line
        Ground11.speed(0) #We want to create it as fast as possible
        Ground11.setposition(-80, 25)
                
        Ground21 = turtle.Turtle() #Creates a pen shape
        Ground21.shape("Ground.gif")
        Ground21.penup()  #We are not draawing a line
        Ground21.speed(0) #We want to create it as fast as possible
        Ground21.setposition(-80, -45)

        Ground31 = turtle.Turtle() #Creates a pen shape
        Ground31.shape("Ground.gif")
        Ground31.penup()  #We are not draawing a line
        Ground31.speed(0) #We want to create it as fast as possible
        Ground31.setposition(-80, -115)

        Ground41 = turtle.Turtle() #Creates a pen shape
        Ground41.shape("Ground.gif")
        Ground41.penup()  #We are not draawing a line
        Ground41.speed(0) #We want to create it as fast as possible
        Ground41.setposition(-80, -185)

        #Ground turtles for column 3

        Ground02 = turtle.Turtle() #Creates a pen shape
        Ground02.shape("Ground.gif")
        Ground02.penup()  #We are not draawing a line
        Ground02.speed(0) #We want to create it as fast as possible
        Ground02.setposition(0, 95)

        Ground12 = turtle.Turtle() #Creates a pen shape
        Ground12.shape("Ground.gif")
        Ground12.penup()  #We are not draawing a line
        Ground12.speed(0) #We want to create it as fast as possible
        Ground12.setposition(0, 25)
                
        Ground22 = turtle.Turtle() #Creates a pen shape
        Ground22.shape("Ground.gif")
        Ground22.penup()  #We are not draawing a line
        Ground22.speed(0) #We want to create it as fast as possible
        Ground22.setposition(0, -45)

        Ground32 = turtle.Turtle() #Creates a pen shape
        Ground32.shape("Ground.gif")
        Ground32.penup()  #We are not draawing a line
        Ground32.speed(0) #We want to create it as fast as possible
        Ground32.setposition(0, -115)

        Ground42 = turtle.Turtle() #Creates a pen shape
        Ground42.shape("Ground.gif")
        Ground42.penup()  #We are not draawing a line
        Ground42.speed(0) #We want to create it as fast as possible
        Ground42.setposition(0, -185)

        #Ground turtles for column 4

        Ground03 = turtle.Turtle() #Creates a pen shape
        Ground03.shape("Ground.gif")
        Ground03.penup()  #We are not draawing a line
        Ground03.speed(0) #We want to create it as fast as possible
        Ground03.setposition(80, 95)

        Ground13 = turtle.Turtle() #Creates a pen shape
        Ground13.shape("Ground.gif")
        Ground13.penup()  #We are not draawing a line
        Ground13.speed(0) #We want to create it as fast as possible
        Ground13.setposition(80, 25)
                
        Ground23 = turtle.Turtle() #Creates a pen shape
        Ground23.shape("Ground.gif")
        Ground23.penup()  #We are not draawing a line
        Ground23.speed(0) #We want to create it as fast as possible
        Ground23.setposition(80, -45)

        Ground33 = turtle.Turtle() #Creates a pen shape
        Ground33.shape("Ground.gif")
        Ground33.penup()  #We are not draawing a line
        Ground33.speed(0) #We want to create it as fast as possible
        Ground33.setposition(80, -115)

        Ground43 = turtle.Turtle() #Creates a pen shape
        Ground43.shape("Ground.gif")
        Ground43.penup()  #We are not draawing a line
        Ground43.speed(0) #We want to create it as fast as possible
        Ground43.setposition(80, -185)

        #Ground turtles for column 5
        Ground04 = turtle.Turtle() #Creates a pen shape
        Ground04.shape("Ground.gif")
        Ground04.penup()  #We are not draawing a line
        Ground04.speed(0) #We want to create it as fast as possible
        Ground04.setposition(160, 95)

        Ground14 = turtle.Turtle() #Creates a pen shape
        Ground14.shape("Ground.gif")
        Ground14.penup()  #We are not draawing a line
        Ground14.speed(0) #We want to create it as fast as possible
        Ground14.setposition(160, 25)
                
        Ground24 = turtle.Turtle() #Creates a pen shape
        Ground24.shape("Ground.gif")
        Ground24.penup()  #We are not draawing a line
        Ground24.speed(0) #We want to create it as fast as possible
        Ground24.setposition(160, -45)

        Ground34 = turtle.Turtle() #Creates a pen shape
        Ground34.shape("Ground.gif")
        Ground34.penup()  #We are not draawing a line
        Ground34.speed(0) #We want to create it as fast as possible
        Ground34.setposition(160, -115)

        Ground44 = turtle.Turtle() #Creates a pen shape
        Ground44.shape("Ground.gif")
        Ground44.penup()  #We are not draawing a line
        Ground44.speed(0) #We want to create it as fast as possible
        Ground44.setposition(160, -185)

        playerspeed = 15 #may need to tweek based on system speed or how player works
        
        levelPosArray = [5, 5, 5, 5, 5]   #Keeps track of 5 ground pieces in 5 columns. Value decrements by 1 if ground is destoryed by bomb in respective column. 
        
        xPlayerBlockPos = 0 #intilization

        os.system("afplay DO_YOU_KNOW_THE_WAY.wav&")
                
        #Function - player goes left, able to do this in one line as well
        def move_left():
                os.system("afplay Click.wav&")  #audio plays for moving left
                global xPlayerBlockPos # x-index position of the player [0-4]
                global yCurr           # y -position of the player (pixel)
                if xPlayerBlockPos > 0: # checks to see if player is within the border
                        xPlayerBlockPos -= 1
                player.setx(-160 + (xPlayerBlockPos * 80))     #player moves left by 80
                yCurr = -300 + 80 + 33 + (70 * levelPosArray[xPlayerBlockPos]) # -300 ground, 80 bunker, 33 adjustments, 70 is height of each block
                player.sety(yCurr)
                
        #Function - player goes right
        def move_right():
                os.system("afplay Click.wav&")
                global xPlayerBlockPos
                global yCurr
                if xPlayerBlockPos < 4:
                        xPlayerBlockPos += 1
                player.setx(-160 + (xPlayerBlockPos * 80))
                yCurr = -300 + 80 + 33 + (70 * levelPosArray[xPlayerBlockPos])
                player.sety(yCurr)

        #function - keyboard binding
        turtle.listen()
        turtle.onkey(move_left, "Left")  #When left key is pushed, I call on function move_left
        turtle.onkey(move_right, "Right") #When right key is pushed, I call on function move_right

        def XPosCalculator(xVal):  #Sets player/bomb in the middle of each of the 5 columns
                return -160 + (xVal * 80)
                
        #Able to use more than one bomb, but choose to only use one for time reasons
        bombs = []  #list of bombs

        numberOfBombs = 1 #only one bomb created

        for i in range(numberOfBombs):     #makes each bomb in list a turtle object
                bombs.append(turtle.Turtle())

        for bomb in bombs:        #makes all bombs (in this case 1 bomb) into a doge emoji
                bomb.shape("dogebomb.gif")
                bomb.penup()
                bomb.speed(0)
                xBombPos = random.randint(0,4)  #xBombPos is an index between 0 and 4
                bomb.setposition(XPosCalculator(xBombPos), 300)

        def HeightMax(xVal):   #Makes player go down into the whole (-300 is lowest point, 80 is bunker, 70 is each ground sqaure by pixels)
                return -300 + 80 + (70 * levelPosArray[xVal])
        
        def ImagePosCalc(x,y):   #function for removing a ground piece calulate XY or (Column)(Row)
                        return (x*10) + y

        def ImageRemove():          #Hides
                y = 5 - (levelPosArray[xBombPos])  #Find y or Column
                imageVal = ImagePosCalc(y,xBombPos) #Calulates integer XY, correlating to (Column)(Row) of ground

                if (imageVal == 0):
                        Ground00.hideturtle()

                elif (imageVal == 1):
                        Ground01.hideturtle()

                elif (imageVal == 2):
                        Ground02.hideturtle()

                elif (imageVal == 3):
                        Ground03.hideturtle()

                elif (imageVal == 4):
                        Ground04.hideturtle()

                elif (imageVal == 10):
                        Ground10.hideturtle()

                elif (imageVal == 11):
                        Ground11.hideturtle()

                elif (imageVal == 12):
                        Ground12.hideturtle()

                elif (imageVal == 13):
                        Ground13.hideturtle()

                elif (imageVal == 14):
                        Ground14.hideturtle()

                elif (imageVal == 20):
                        Ground20.hideturtle()

                elif (imageVal == 21):
                        Ground21.hideturtle()

                elif (imageVal == 22):
                        Ground22.hideturtle()

                elif (imageVal == 23):
                        Ground23.hideturtle()

                elif (imageVal == 24):
                        Ground24.hideturtle()

                elif (imageVal == 30):
                        Ground30.hideturtle()

                elif (imageVal == 31):
                        Ground31.hideturtle()

                elif (imageVal == 32):
                        Ground32.hideturtle()

                elif (imageVal == 33):
                        Ground33.hideturtle()

                elif (imageVal == 34):
                        Ground34.hideturtle()

                elif (imageVal == 40):
                        Ground40.hideturtle()

                elif (imageVal == 41):
                        Ground41.hideturtle()

                elif (imageVal == 42):
                        Ground42.hideturtle()

                elif (imageVal == 43):
                        Ground43.hideturtle()

                elif (imageVal == 44):
                        Ground44.hideturtle()
                        
        #Main function
        while win: 
                if (explodeBool):  #moves explosion to wherever the bomb hits the ground
                        explosionCounter += 1 
                        if explosionCounter == 10:
                                explosion.hideturtle()
                                explosionBool = False
                                explosionCounter = 0
                        
                for bomb in bombs:     #Speed of the bombs falling in the y direction
                        yBombPos = bomb.ycor()
                        yBombPos -= (level*.5) * 4
                        bomb.sety(yBombPos)
                
                #Checks if the bomb hit the player piece
                if ((yBombPos - HeightMax(xPlayerBlockPos) <= 40) and ((xBombPos == xPlayerBlockPos))):
                        player.hideturtle()   #hides player
                        explosion.setposition(XPosCalculator(xBombPos), HeightMax(xBombPos) + 80)  #Sets bomb positioning to area where player is hit
                        explosion.showturtle() #shows the explosion
                        os.system("afplay Pop.wav&") 
                        explodeBool = True  # hides the turtles, ready to be located at next position where bomb hits ground or player
                        bomb.hideturtle()
                        Gameover = True     #Exits program while loop and ends the program
                        break
                        
                 #Main function for removing the image of bomb when hits ground and resets bomb to the top
                elif (yBombPos - HeightMax(xBombPos)) <= 20:    
                        ImageRemove()
                        if levelPosArray[xBombPos] > 0:
                                levelPosArray[xBombPos] -= 1
                        bomb.hideturtle()
                        os.system("afplay Pop.wav&")
                        explosion.setposition(XPosCalculator(xBombPos), HeightMax(xBombPos) + 80)
                        explosion.showturtle()
                        explodeBool = True
                        xBombPos = random.randint(0,4)
                        bomb.setposition(XPosCalculator(xBombPos), 300)
                        bomb.showturtle()
                        
                #Checks if player is at the ground level in the bunker
                elif (levelPosArray[xPlayerBlockPos] <= 0):
                        yCurr -= 80
                        player.sety(yCurr)
                        print("Next Level!")
                        win = False    #Means that you actually do win and you will proceed to level two 
                        level_pen.clear()  
                        #Displays what level you are in on the left side of the computer
                        level += 1
                        levelstring = "Level: %s" %level
                        level_pen.clear()
                        level_pen.write(levelstring, False, align="left", font=("Arial", 14, "normal"))

#Stops the sound when player is hit, it is commented out because program crashes if not commented out. 
#sounda.stop()
                        
#if program while loop is broked, game outputs game over and thank you for playing
print("Game Over")
GameOver_pen = turtle.Turtle()
GameOver_pen.speed(0)
GameOver_pen.color("black")
GameOver_pen.penup()
GameOver_pen.setposition(0, -50)
GameOverstring = "Game Over"
GameOver_pen.write(GameOverstring, False, align="center", font=("Arial", 25, "normal"))
GameOver_pen.hideturtle()

GameOver1_pen = turtle.Turtle()
GameOver1_pen.speed(0)
GameOver1_pen.color("black")
GameOver1_pen.penup()
GameOver1_pen.setposition(0, -75)
GameOverstring1 = "Thank you for playing!"
GameOver1_pen.write(GameOverstring1, False, align="center", font=("Arial", 25, "normal"))
GameOver1_pen.hideturtle()

Game1_pen = turtle.Turtle()
Game1_pen.speed(0)
Game1_pen.color("black")
Game1_pen.penup()
Game1_pen.setposition(0, -125)
Gamestring1 = "Highscore: Level %s" %level
Game1_pen.write(Gamestring1, False, align="center", font=("Arial", 25, "normal"))
Game1_pen.hideturtle()

delay = input("We did it! - HackPoly 2018")

