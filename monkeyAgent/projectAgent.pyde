# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Seeking "vehicle" follows the mouse position

# Implements Craig Reynold's autonomous steering behaviors
# One vehicle "seeks"
# See: http://www.red3d.com/cwr/

from Monkey import Monkey
from Food import Food
import random 


def setup():
    global monkey, bg
    size(700, 490)
    bg = loadImage("Ambiente.jpg")
    
    #Defini valores iniciais para o agente(posição e velocidade)
    velocity = PVector(0, 0)
    monkey = Monkey(width / 2, height / 2)
    
    #Inicia a posição do primeiro alvo
    initializeFood()

def draw():
    background(bg)
    
    #atualiza a posição do alvo e a sua imagem
    positionFood = PVector(food.position.x, food.position.y)
    food.display()
    
    #envia para o agente a posição do alvo 
    monkey.arrive(positionFood)
    monkey.update()
    monkey.display()
    
    #Analaisa se o agente encontrou o alvo
    #caso tenha encontrado soma +1 
    if food.update(monkey.position):
        initializeFood()
        monkey.numberFood += 1
        
    #Plota na tela q quantidade de alvos coletados
    numberFoodScreen(monkey.numberFood)
 
#Função para atualizar a posição do alvo
def initializeFood():
    
    global food
    
    food_x = random.randint(0,620)
    food_y = random.randint(0,340)
    
    food = Food(food_x, food_y)
    
#Função simples para plotar os valores na tela
def numberFoodScreen(numberFood):
    
    font = createFont("Georgia", 16)
    textFont(font, 20)
    fill(0, 0, 0)
    text("Quant:", 5, 20)
    text(numberFood, 75, 20)
    
    
