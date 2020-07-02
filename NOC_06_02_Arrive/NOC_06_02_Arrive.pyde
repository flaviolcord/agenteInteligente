# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Seeking "vehicle" follows the mouse position

# Implements Craig Reynold's autonomous steering behaviors
# One vehicle "seeks"
# See: http://www.red3d.com/cwr/

from Vehicle import Vehicle
from Food import Food
import random 



def setup():
    global v
    size(700, 400)
    velocity = PVector(0, 0)
    v = Vehicle(width / 2, height / 2)
    
    initializeFood()

def draw():
    background(255)
    
    # Draw an ellipse at the mouse position
    #fill(127)
    #stroke(200)
    #strokeWeight(2)
    #ellipse(mouse.x, mouse.y, 48, 48)
    
    positionFood = PVector(food.position.x, food.position.y)

    # Call the appropriate steering behaviors for our agents
    food.display()
    v.arrive(positionFood)
    v.update()
    v.display()
    if food.update(v.position):
        initializeFood()
        v.numberFood += 1
        println(v.numberFood)
    numberFoodScreen(v.numberFood)
    
    #photo = loadImage("fruit.png")
    #image(photo, 20, 20, photo.width / 10, photo.height / 10)
        

    #newPosition = food.update(v.position)
    
    #print("NewPosition.x = ", newPosition.x)
    
    #food.update()
    
def initializeFood():
    
    global food
    
    food_x = random.randint(0,620)
    food_y = random.randint(0,340)
    
    food = Food(food_x, food_y)
    
def numberFoodScreen(numberFood):
    
    font = createFont("Georgia", 16)
    textFont(font, 20)
    fill(0, 0, 0)
    text("Quant:", 5, 20)
    text(numberFood, 75, 20)
    
    
