class Obstaculo(): 
    
    def __init__(self, linha, coluna):
        
        self.linha = linha
        self.coluna = coluna
        
        # Obstáculo = Quadrado Preto
        self.corpo = createShape(RECT, 0, 0, tamanhoCelulaGrid, tamanhoCelulaGrid)
        self.corpo.setFill(color(0, 0, 0))
        
    def atualiza(self): # Atualiza posição na tela
        shape(self.corpo, self.coluna * tamanhoCelulaGrid, self.linha * tamanhoCelulaGrid)
