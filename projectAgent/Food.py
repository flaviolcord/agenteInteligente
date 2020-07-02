# The "Food" class

import random 

class Food():
    
    def __init__(self, x, y):
        self.position = PVector(x, y)

    def display(self):
        #carrega imagem da banana
        photo = loadImage("banana.png")
        image(photo, self.position.x, self.position.y, photo.width / 3, photo.height / 3)
    
    def update(self, agentPosition):
        
        foodPosition = self.position
        agentEat = False

        #analisa se o agente encontrou o alvo
        if(abs(agentPosition.y - foodPosition.y) < 0.5 and abs(agentPosition.y - foodPosition.y) <  0.5):
            agentEat = True
            
        return agentEat
        
        
            
        
            
        
        
        
    

    

    
