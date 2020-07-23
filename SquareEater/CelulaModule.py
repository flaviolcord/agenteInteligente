class Celula():
    
    def __init__(self, linha, coluna):
        
        self.pai = None
        
        self.esquerda = None
        self.direita = None
        self.cima = None
        self.baixo = None
        
        self.linha = linha
        self.coluna = coluna
