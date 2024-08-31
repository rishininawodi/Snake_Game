import pygame
import sys
import os
import random 
import math

pygame.init()
pygame.display.set_caption("snake game")
pygame.font.init()
random.speed()

#declare global constatnt definition
speed = 0.30
SNAKE_SIZE = 9
APPLE_SIZE = SNAKE_SIZE
SEPERATION =10
SCREEN_HEIGHT = 600
SCREEN_WIDTH= 800
FPS = 25
KEY = {"UP":1 ,"DOM":2 , "LEFT":3 ,"RIGHT":4}

#initiallize screen
screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_HEIGHT),pygame.HWSURFACE)

#HWSURFACE stands for hardware surface refere to using memory on the video card for storing

#Resources
score_font=pygame.font.Font(None,38)
score_numb_font = pygame.font.Font(None,28)
game_over_font = pygame.font.Font(None,46)
play_again_font = score_numb_font
score_msg = score_font.render("Score : ",1,pygame.Color("green"))
score_msg_size = score_font.size("Score")
background_color = pygame.Color(0,0,0)    # we will fill background color as black
black = pygame.Color(0,0,0)

