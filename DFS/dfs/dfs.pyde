import random
from collections import deque

# Configuração da exibição do quantitativo comido
tamanhoFonte = 50
distanciamentoMargemSuperior = 50

quantidadeObstaculos = 300

# Configurações da Grid (Ambiente do Agente)
tamanhoCelulaGrid = 20
quantidadeLinhasColunasGrid = 41 # Grid Quadrada (número de linhas = número de colunas)
refreshDelay = 500 # Taxa de atualização da grid em milissegundos

listaDeObstaculos = deque()

# Para guardar a posição da comida e evitar que sejam geradas uma em cima da outra
linhaComida = 0
colunaComida = 0

from celula import Celula
from agente import Agente
from comida import Comida
from obstaculo import Obstaculo
from pontoCaminho import PontoCaminho

# Executado uma única vez. No início
def setup():
    
    # Criando a Grid
    size(quantidadeLinhasColunasGrid * tamanhoCelulaGrid, quantidadeLinhasColunasGrid * tamanhoCelulaGrid) 
    
    # Inicia com o player no centro do ambiente e uma fruta em um local aleatório, além dos obstáculos
    inicializaAgente()
    inicializaComida()
    inicializaObstaculos()
    
    linhaComida = comida.linha
    colunaComida = comida.coluna
    
    atualizaTela() # Exibe a tela com agente e comida
    
def mostraCaminho(caminho):
    
    for ponto in caminho:
        pontoCaminho = PontoCaminho(ponto[0], ponto[1])
        pontoCaminho.atualiza()
    

# Executado constantemente
def draw():
    
    if(not agente.procurandoCaminho):
        
        agente.encontraCaminho()
        atualizaTela()
        agente.procurandoCaminho = True
        
    else:
        
        inicializaComida()
        agente.encontraCaminho()
        atualizaTela()
    
    
########################################

def inicializaAgente():
        
    posicaoCentral = round((quantidadeLinhasColunasGrid + 1)/2) - 1 # Calculando a posição da célula central da Grid
    
    global agente
    agente = Agente(posicaoCentral, posicaoCentral)


def inicializaComida():
    global comida
    comida = geraComida()
    
    
def geraComida():
    
    linha = random.randint(0, quantidadeLinhasColunasGrid - 1)
    coluna = random.randint(0, quantidadeLinhasColunasGrid - 1)
    
    # Evita que uma comida seja gerada na mesma posição anterior ou em cima do agente
    while((linha == linhaComida and coluna == colunaComida) or (linha == agente.linha and coluna == agente.coluna)):
        linha = random.randint(0, quantidadeLinhasColunasGrid - 1)
        coluna = random.randint(0, quantidadeLinhasColunasGrid - 1)
    
    return Comida(linha, coluna)


def inicializaObstaculos():
    
    for _ in xrange(quantidadeObstaculos):
    
       linha = random.randint(0, quantidadeLinhasColunasGrid - 1)
       coluna = random.randint(0, quantidadeLinhasColunasGrid - 1)
       
       obstaculo = Obstaculo(linha, coluna)
       
       # Evita obstáculos no mesmo lugar que o agente e que a comida
       if(obstaculo.linha == comida.linha and obstaculo.coluna == comida.coluna): continue
       if(obstaculo.linha == agente.linha and obstaculo.coluna == agente.coluna): continue
       
       listaDeObstaculos.append(obstaculo)


def atualizaTela(): # Atualiza a tela de tempos em tempos para redesenhar os elementos
    
    background(255, 204, 0) # Limpa a tela recolorindo o background
    
    atualizaObstaculos()
    
    mostraCaminho(agente.caminho)
    
    comida.atualiza()
    agente.atualiza()
    
    atualizaQuantidadeComida()
    

def atualizaObstaculos():
    
    for obstaculo in listaDeObstaculos:
        obstaculo.atualiza()


def atualizaQuantidadeComida():
    
    fill(255, 255, 255);
    
    textSize(tamanhoFonte)
    text(str(agente.quantidadeComida), 10, distanciamentoMargemSuperior)
