# Import a library of functions called 'pygame'
import pygame
from main_functions import *

# Initialize the game engine
pygame.init()

#call main routine
size = [1300, 600] # Define size of windows
size[0] = int(input("Ancho de la ventana: "))
size[1] = int(input("Alto de la ventana: "))
main2(size)