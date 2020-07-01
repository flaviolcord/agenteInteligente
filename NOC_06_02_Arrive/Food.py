# The "Food" class

import random 

class Food():

    def __init__(self, x, y):
        self.position = PVector(x, y)
        self.r = 20

    def display(self):
        fill(127)
        noStroke()
        strokeWeight(1)
        with pushMatrix():
            translate(self.position.x, self.position.y)
            rotate(0)
            rect(0, 0, self.r, self.r)
    
    def update(self, agentPosition):
        
        foodPosition = self.position
        agentEat = False

        if(abs(agentPosition.y - foodPosition.y) < 0.8 and abs(agentPosition.y - foodPosition.y) <  0.8):
            agentEat = True
            
        return agentEat
        
        
            
        
            
        
        
        
    

    

    
