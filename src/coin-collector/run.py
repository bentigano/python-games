import pgzrun

from random import randint

WIDTH = 400
HEIGHT = 400

score = 0
game_over = False

fox = Actor("fox") # options are fox or hedgehog
fox.pos = 100,100

coin = Actor("coin")
coin.pos = 200,200

def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10,10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Final Score: " + str(score), topleft=(10,10), fontsize=60)

# place the coin at a random location
def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def time_up():
    global game_over
    game_over = True

# this runs automatically (from pygame) ~60 times per second
def update():
    global score

    # the higher the number, the faster the collector will move (default = 2)
    if keyboard.left:
        fox.x = fox.x - 4
    elif keyboard.right:
        fox.x = fox.x + 4
    elif keyboard.up:
        fox.y = fox.y - 4
    elif keyboard.down:
        fox.y = fox.y + 4
    
    coin_collected = fox.colliderect(coin)

    if coin_collected:
        score = score + 10
        place_coin()

# run a method (time_up) after a specified number of seconds
# increase this number for more playing time
clock.schedule(time_up, 10.0)
place_coin()

pgzrun.go()