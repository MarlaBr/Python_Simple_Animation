# Marla Boeer
# Summer 2016

# need time to move things
from graphics import *
import time

# constants
WIDTH = 600
HEIGHT = 400
RADIUS = 25
DX = 3
DY = 3
SPEED = 1/60

def main():
    global DX, DY

    win = GraphWin('Pool Table', WIDTH, HEIGHT)# window
    win.setBackground('powder blue')
    
    ball = Circle(Point(WIDTH/2, HEIGHT/2), RADIUS)# ball
    ball.setFill('tan1')
    ball.draw(win)
    
    win.getMouse()# click to start

    while True:
        ball.move(DX,DY)
        time.sleep(SPEED)

        center = ball.getCenter()# see if ball hit wall
        current_x = center.getX()
        current_y = center.getY()
        
        if current_x >= WIDTH - RADIUS or current_x <= 0 + RADIUS: # bounce x
            DX = -DX
        if current_y >= HEIGHT - RADIUS or current_y <= 0 + RADIUS: # bounce y
            DY = -DY

        #if win.checkMouse(): break
        
    
main()

