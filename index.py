import pygame
from pygame.locals import *
import random

pygame.init()

# Colours
WHITE     = (255,255,255)
BLACK     = (0,0,0)
ORANGE    = (220,100,0)
BROWN     = (180,80,50)
YELLOW    = (240,200,20)
RED       = (200,10,10)
BLUE      = (10,200,10)
GREEN     = (10,10,200)
GREY	  = (50,50,50)
SKYBLUE   = (125,220,240)
colors    = ["white", "black", "orange", "brown", "yellow", "red", "blue", "green"]
color_map = { "white"   : WHITE,
              "black"   : BLACK,
              "orange"  : ORANGE,
              "brown"   : BROWN,
              "yellow"  : YELLOW,
              "red"     : RED,
              "blue"    : BLUE,
              "green"   : GREEN }


# Global Variables
disp_width  = 550
disp_height = 700
hidden_code = []

# GameDisplay
gameDisplay = pygame.display.set_mode((disp_width, disp_height))
pygame.display.set_caption('Mastermind')

clock = pygame.time.Clock()


def drawPeg(x,y):
    pygame.draw.circle(gameDisplay, BLACK, (x,y), 24)
    pygame.draw.circle(gameDisplay, WHITE, (x,y), 21)
    pygame.draw.circle(gameDisplay, BLACK, (x,y), 8)


def drawPegs():
    y = 575
    for i in range(10):
        x = 150
        font = pygame.font.SysFont ("arial", 30)
        putText(str(i+1), (x-110,y-50,100,100), font, BLACK)
        for j in range(4):
            drawPeg(x,y)
            x += 50

        y -= 50

def drawColorBar():
    pygame.draw.rect(gameDisplay, BLACK, (448,118,54,464))
    pygame.draw.rect(gameDisplay, WHITE, (450,120,50,460))
    x,y = 475,175
    for i in range(8):
        pygame.draw.circle(gameDisplay, BLACK, (x,y), 17)
        pygame.draw.circle(gameDisplay, color_map[colors[i]], (x,y), 15)
        y += 50

def drawCheckbox(x,y):
    pygame.draw.rect(gameDisplay, BLACK, (x,y+7,44,36), 2)
    pygame.draw.circle(gameDisplay, BLACK, (x+15,y+7+13), 5)
    pygame.draw.circle(gameDisplay, BLACK, (x+15,y+7+26), 5)
    pygame.draw.circle(gameDisplay, BLACK, (x+30,y+7+13), 5)
    pygame.draw.circle(gameDisplay, BLACK, (x+30,y+7+26), 5)

def drawCheckboxes():
    x,y = 350,550
    for i in range(10):
        drawCheckbox(x,y)
        y -= 50

def putText(text,rect,font,color):
    rect = pygame.Rect(rect)
    textSurf = font.render(text, True, color)
    textRect = textSurf.get_rect()
    textRect.center = (rect.centerx,rect.centery)
    gameDisplay.blit(textSurf, textRect)


def placeHiddenCode():
    x,y = 165,50
    for color in hidden_code:
        pygame.draw.circle(gameDisplay, BLACK, (x,y), 17)
        pygame.draw.circle(gameDisplay, color_map[color], (x,y), 15)
        x += 40

def hideCode():
    pygame.draw.rect(gameDisplay, GREY, (125,30,200,50))
    font = pygame.font.SysFont ("comicsansms", 30)
    putText("MASTERMIND", (125,30,200,50), font, WHITE)

def drawCheckButton():
    pygame.draw.rect(gameDisplay, BLACK, (149,624,152,52))
    pygame.draw.rect(gameDisplay, SKYBLUE, (150,625,150,50))
    font = pygame.font.SysFont ("comicsansms", 40)
    putText("CHECK", (150,625,150,50), font, BLACK)

def unhideCode():
    pass

# Main Gameloop
def mainloop():

    cur_guess = 1

    exit = False

    while not exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

        gameDisplay.fill(WHITE)
        drawPegs()
        drawColorBar()
        drawCheckboxes()
        placeHiddenCode()
        hideCode()
        drawCheckButton()

        font = pygame.font.SysFont ("comicsansms", 35)
        putText(">", (0,574-cur_guess*50,100,100), font, BLACK)

        pygame.display.update()
        clock.tick(10)

    pygame.quit()
    quit()

# main
def main():
    global hidden_code
    hidden_code = random.sample (colors, 4)
    mainloop()

if __name__ == "__main__":
    main()
