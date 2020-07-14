class PontoCaminho(): 
    
    def __init__(self, linha, coluna):
        
        self.linha = linha
        self.coluna = coluna
        
        # Ponto do Caminho = Quadrado Cinza
        self.corpo = createShape(RECT, 0, 0, tamanhoCelulaGrid, tamanhoCelulaGrid)
        self.corpo.setFill(color(211, 211, 211))
        
    def atualiza(self): # Atualiza posição na tela
        shape(self.corpo, self.coluna * tamanhoCelulaGrid, self.linha * tamanhoCelulaGrid)
