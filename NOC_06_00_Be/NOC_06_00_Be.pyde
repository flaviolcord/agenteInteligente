# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Modified by Filipe Calegario

# Draws a "vehicle" on the screen

# Implements Craig Reynold's autonomous steering behaviors
# One vehicle "seeks"
# See: http://www.red3d.com/cwr/

from Vehicle import Vehicle
from Food import Food.py

def setup():
    global vehicle, food
    size(640, 360)
    velocity = PVector(0, 0)
    vehicle = Vehicle(width / 2, height / 2, velocity)
    food = Food(width / 3, height / 2, 0)

def draw():
    background(255)
    mouse = PVector(mouseX, mouseY)
    vehicle.update()
    vehicle.display()
    food.update()
    food.display()
    
