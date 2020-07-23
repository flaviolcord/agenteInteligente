from PontoGridModule import *
from CerebroModule import *

class Agente(PontoGrid): 
    
    
    def __init__(self, linha, coluna, tamanhoCelula, listaDeObstaculos, quantidadeLinhasColunasGrid):
        
        PontoGrid.__init__(self, linha, coluna, color(220, 20, 60), tamanhoCelula)
        
        self.comeuComida = False
        self.caminhando = False
        self.quantidadeComida = 0
        self.caminho = []
        self.contador = 0
        
        self.cerebro = Cerebro(listaDeObstaculos, quantidadeLinhasColunasGrid)
        
        
    def encontraCaminho(self, comida, tipoBusca):
        self.caminho = self.cerebro.busca(self.linha, self.coluna, comida, tipoBusca)
        return self.caminho
    
    
    def caminhaAteComida(self, comida, lista):
        
        self.caminhando = True
        
        if self.contador < len(lista):
            ponto = lista[self.contador]
            self.linha = ponto[0]
            self.coluna = ponto[1]
            self.contador += 1
    
        if (self.contador > (len(lista)-1)):
            self.contador = 0
            self.comeuComida = True
            self.caminhando = False
            self.quantidadeComida += 1 
