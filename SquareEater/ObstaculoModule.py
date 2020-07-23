from PontoGridModule import *

class Obstaculo(PontoGrid):
    
    def __init__(self, linha, coluna, tamanhoCelula):
        PontoGrid.__init__(self, linha, coluna, color(0, 0, 0), tamanhoCelula)
