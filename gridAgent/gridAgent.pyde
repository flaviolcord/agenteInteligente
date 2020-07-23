import random

# Configurações do Grid (Ambiente do Agente)
tamanhoCelulaGrid = 8
quantidadeLinhasColunasGrid = 101 # Grid Quadrada (número de linhas = número de colunas)

refreshDelay = 5 # Taxa de atualização da tela em milissegundos


########################################


class Agente(): 
    
    def __init__(self, linha, coluna):
        
        self.comeuComida = False
        self.quantidadeComida = 0
        
        self.linha = linha
        self.coluna = coluna
        
        # Agente = Quadrado Vermelho
        self.corpo = createShape(RECT, 0, 0, tamanhoCelulaGrid, tamanhoCelulaGrid)
        self.corpo.setFill(color(220, 20, 60))
        
    def come(self, comida):
        
        linhaOk = False
        colunaOk = False
        
        # Caminha pelas colunas até que a coluna seja igual a da fruta
        if(self.coluna != comida.coluna):
    
            if(self.coluna > comida.coluna): self.coluna = self.coluna - 1
            else: self.coluna += 1
      
        else:
            colunaOk = True
            
        # Caminha pelas linhas até que a linha seja igual a da fruta
        if(self.linha != comida.linha):
    
            if(self.linha > comida.linha): self.linha = self.linha - 1
            else: self.linha += 1
      
        else:
            linhaOk = True
            
        # Se player e fruta estão na mesma linha e coluna, então a fruta foi comida
        if(linhaOk and colunaOk): self.comeuComida = True
        else: self.comeuComida = False
        
        if(self.comeuComida): self.quantidadeComida += 1; # Atualizando o quantitativo comido
        
    def atualiza(self): # Atualiza posição na tela
        shape(self.corpo, self.coluna * tamanhoCelulaGrid, self.linha * tamanhoCelulaGrid)
        

class Comida(): 
    
    def __init__(self, linha, coluna):
        
        self.linha = linha
        self.coluna = coluna
        
        # Comida = Quadrado Verde
        self.corpo = createShape(RECT, 0, 0, tamanhoCelulaGrid, tamanhoCelulaGrid)
        self.corpo.setFill(color(60, 179, 113))
        
    def atualiza(self): # Atualiza posição na tela
        shape(self.corpo, self.coluna * tamanhoCelulaGrid, self.linha * tamanhoCelulaGrid)


########################################


# Executado uma única vez. No início
def setup():
    
    # Criando a Grid
    size(quantidadeLinhasColunasGrid * tamanhoCelulaGrid, quantidadeLinhasColunasGrid * tamanhoCelulaGrid) 
    
    # Inicia com o player no centro do ambiente e uma fruta em um local aleatório
    inicializaAgente()
    inicializaComida()

    atualizaTela() # Atualiza a tela de tempos em tempos para redesenhar os elementos
    
    agente.come(comida) # Come a primeira fruta
    

# Executado constantemente
def draw():
    
    atualizaTela()
    
    if(not agente.comeuComida): 
        agente.come(comida)
        
    else: 
        inicializaComida()
        agente.comeuComida = False 
  
      
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
    
    return Comida(linha, coluna)


def atualizaTela():
    
    background(255, 204, 0) # Limpa a tela deixando-a laranja
    
    comida.atualiza()
    agente.atualiza()
    
    atualizaQuantidadeComida()
        
    delay(refreshDelay) # Aguarda um tempo em milissegundos antes de fazer a próxima atualização
    

def atualizaQuantidadeComida():
    
    textSize(15)
    text("QUANTIDADE COMIDA: " + str(agente.quantidadeComida), 10, 20)
