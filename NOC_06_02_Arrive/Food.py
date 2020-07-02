# The "Food" class

import random 

class Food():

    def __init__(self, x, y):
        self.position = PVector(x, y)
        self.r = 20

    def display(self):
        photo = loadImage("2.png")
        image(photo, self.position.x, self.position.y, photo.width / 4, photo.height / 4)
    
    def update(self, agentPosition):
        
        foodPosition = self.position
        agentEat = False

        if(abs(agentPosition.y - foodPosition.y) < 1 and abs(agentPosition.y - foodPosition.y) <  1):
            agentEat = True
            
        return agentEat
        
        
            
        
            
        
        
        
    

    

    
