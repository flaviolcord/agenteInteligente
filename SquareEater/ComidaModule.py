from PontoGridModule import *

class Comida(PontoGrid):
     
    def __init__(self, linha, coluna, tamanhoCelula):
        PontoGrid.__init__(self, linha, coluna, color(60, 179, 113), tamanhoCelula)
