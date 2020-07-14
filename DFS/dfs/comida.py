class Comida(): 
    
    def __init__(self, linha, coluna):
        
        self.linha = linha
        self.coluna = coluna
        
        # Comida = Quadrado Verde
        self.corpo = createShape(RECT, 0, 0, tamanhoCelulaGrid, tamanhoCelulaGrid)
        self.corpo.setFill(color(60, 179, 113))
        
    def atualiza(self): # Atualiza posição na tela
        shape(self.corpo, self.coluna * tamanhoCelulaGrid, self.linha * tamanhoCelulaGrid)
