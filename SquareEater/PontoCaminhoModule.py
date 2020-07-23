from PontoGridModule import *

class PontoCaminho(PontoGrid): 
    
    def __init__(self, linha, coluna, tamanhoCelula):
        PontoGrid.__init__(self, linha, coluna, color(211, 211, 211), tamanhoCelula)
        
        
        
class PontoExpansao(PontoGrid): 
    
    def __init__(self, linha, coluna, tamanhoCelula):
        PontoGrid.__init__(self, linha, coluna, color(75,0,130), tamanhoCelula)
