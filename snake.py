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
