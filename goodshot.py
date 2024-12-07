import pgzrun
import random
TITLE ="good shot game by Munachiso"
WIDTH = 500
HEIGHT = 500

score = 0

alien = Actor("ninja4.png")
message = ""
def draw():
    screen.clear()
    screen.fill("green")
    alien.draw()
    screen.draw.text(message,(300,300),fontsize = 30)
    screen.draw.text(str(score),(10,10),fontsize = 40)


def placing_the_alien():
    alien.x = random.randint(50,450)
    alien.y = random.randint(50,450)

def on_mouse_down(pos):
    global message
    global score
    if alien.collidepoint(pos):
        message = "Good shot!"
        score = score+1
    
        placing_the_alien()
    
    else:
        message = "You missed the shot"
        score = score-2

placing_the_alien()


pgzrun.go()