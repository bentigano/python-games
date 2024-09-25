import pgzrun

from random import randint
fruit = Actor("apple") # options are apple, orange, or pineapple

def draw(): # Pygame will call automatically call draw() as often as it needs to
    screen.clear()
    fruit.draw()

def place_fruit():
    fruit.x = randint(10, 800)
    fruit.y = randint(10, 600)

def on_mouse_down(pos): # Pygame event hook (called automatically on mouse down/click)
    if fruit.collidepoint(pos):
        print("Good Shot!")
        place_fruit()
    else:
        print("You missed!")
        quit()

place_fruit()

pgzrun.go()