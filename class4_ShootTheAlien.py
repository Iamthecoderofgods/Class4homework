#Shoot the alien
# Import the Pygame Zero Library
import pgzrun
from random import randint
# Pygame Standard for deciding the title of your game window 
TITLE = "Venom shooter"
# Pygame Standard for deciding the width and height for your game window in pixels
HEIGHT = 500
WIDTH = 500
# variable to store the message displayed on your screen
message="Max"

# Actor is built-in object in pgzero
venom = Actor("venom")
# interacts with other actors, move around on screen
# Similar to Sprite in Scratch
#alien.pos = 50,50
r = 120
b = 130
g = 140


# Default function which will be called to update the screen
def draw():
  #screen is another built-in object
  screen.fill(color=(r,g,b))
  venom.draw()
  screen.draw.text(message,(400,50))
#  place_alien()

  
def place_alien():
  venom.pos=(randint(0,WIDTH),randint(0,HEIGHT))

place_alien()

def on_mouse_down(pos):
  #print("Hello World")
  global message,r,g,b
  if venom.collidepoint(pos):
    place_alien()
    message="Amazingg"
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)

  else:
    message="try again"


  
# This method needs to be called to start processing
pgzrun.go()