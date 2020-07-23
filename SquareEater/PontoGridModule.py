class PontoGrid(object):
    
    def __init__(self, linha, coluna, cor, tamanhoCelula):
        
        self.linha = linha
        self.coluna = coluna
        self.tamanhoCelula = tamanhoCelula
        
        self.corpo = createShape(RECT, 0, 0, tamanhoCelula, tamanhoCelula)
        self.corpo.setFill(cor)
        
        
    def atualiza(self):
        shape(self.corpo, self.coluna * self.tamanhoCelula, self.linha * self.tamanhoCelula)
