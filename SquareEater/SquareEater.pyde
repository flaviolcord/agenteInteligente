from collections import deque

from AgenteModule import *
from ComidaModule import *
from ObstaculoModule import *
from PontoCaminhoModule import *
from TipoBuscaModule import *

import random


#######################################################################


tamanhoFonte = 50
distanciamentoMargemSuperior = 50

tamanhoCelulaGrid = 20
quantidadeLinhasColunasGrid = 45
quantidadeObstaculos = 300

tempoDelay = 50

caminhoParaComida = []

#tipoBusca = TipoBusca.LARGURA
#tipoBusca = TipoBusca.PROFUNDIDADE
tipoBusca = TipoBusca.CUSTOUNIFORME
#tipoBusca = TipoBusca.ESTRELA
#tipoBusca = TipoBusca.GULOSA

#######################################################################


def setup():
    
    size(quantidadeLinhasColunasGrid * tamanhoCelulaGrid, quantidadeLinhasColunasGrid * tamanhoCelulaGrid)
    
    inicializaObstaculos()
    inicializaAgente()
    inicializaComida()
    
    atualizaTela()
    

def draw():
    
    atualizaTela()

    global caminhoParaComida
    global visitadas
    
    if (agente.caminhando == False):
        #atualizaTela()
        caminhoParaComida, visitadas = agente.encontraCaminho(comida, tipoBusca)
        mostraExpansao(visitadas)
        comida.atualiza()
        agente.atualiza()
        agente.caminhando = True
        delay(tempoDelay)

    if agente.caminhando:
        mostraExpansao(visitadas)
        agente.caminhaAteComida(comida, caminhoParaComida)
        mostraCaminho(caminhoParaComida)
        comida.atualiza()
        agente.atualiza()
#        atualizaTela()
        delay(tempoDelay)
    
    if agente.comeuComida:
        inicializaComida()
        agente.comeuComida = False
 #       atualizaTela()
        delay(tempoDelay)
    
    '''
    caminhoParaComida = agente.encontraCaminho(comida, tipoBusca)
    delay(2000)
    
    mostraCaminho(caminhoParaComida)
    comida.atualiza()
    agente.atualiza()
    
    agente.caminhaAteComida(comida)   
    
    inicializaComida()
    delay(tempoDelay)
    '''
    
    
    
#######################################################################


def inicializaAgente():
    global agente
    posicaoCentral = round((quantidadeLinhasColunasGrid + 1)/2) - 1
    agente = Agente(posicaoCentral, posicaoCentral, tamanhoCelulaGrid, listaDeObstaculos, quantidadeLinhasColunasGrid)
    

def inicializaComida():
    global comida
    comida = geraComida()
    
    
def geraComida():
    
    linha = random.randint(0, quantidadeLinhasColunasGrid - 1)
    coluna = random.randint(0, quantidadeLinhasColunasGrid - 1)
    
    while((linha == agente.linha and coluna == agente.coluna) or existeObstaculo(linha, coluna)):
        linha = random.randint(0, quantidadeLinhasColunasGrid - 1)
        coluna = random.randint(0, quantidadeLinhasColunasGrid - 1)
    
    return Comida(linha, coluna, tamanhoCelulaGrid)

    
def inicializaObstaculos():
    global listaDeObstaculos
    listaDeObstaculos = geraObtaculos()
    

def geraObtaculos():
    
    listaDeObstaculos = deque()
    
    for x in range(quantidadeObstaculos):
    
       linha = random.randint(0, quantidadeLinhasColunasGrid - 1)
       coluna = random.randint(0, quantidadeLinhasColunasGrid - 1)
       
       obstaculo = Obstaculo(linha, coluna, tamanhoCelulaGrid)
       
       posicaoCentral = round((quantidadeLinhasColunasGrid + 1)/2) - 1
       
       if(obstaculo.linha == posicaoCentral and obstaculo.coluna == posicaoCentral): continue
       
       listaDeObstaculos.append(obstaculo)
       
    return listaDeObstaculos;

       
def existeObstaculo(linha, coluna):
        
    for obstaculo in listaDeObstaculos:
        if(obstaculo.linha == linha and obstaculo.coluna == coluna): return True
        
    return False


def mostraCaminho(caminho):
    
    for ponto in caminho:
        pontoCaminho = PontoCaminho(ponto[0], ponto[1], tamanhoCelulaGrid)
        pontoCaminho.atualiza()



def mostraExpansao(visitadas):
    
    for ponto in visitadas:
        pontoExpansao = PontoExpansao(ponto.linha, ponto.coluna, tamanhoCelulaGrid)
        pontoExpansao.atualiza()


def atualizaTela():
    
    background(255, 204, 0)
    
    atualizaObstaculos()
    
    mostraCaminho(caminhoParaComida)
    
    comida.atualiza()
    agente.atualiza()
    
    atualizaQuantidadeComida()
    

def atualizaObstaculos():
    for obstaculo in listaDeObstaculos:
        obstaculo.atualiza()


def atualizaQuantidadeComida():
    
    fill(255, 255, 255);
    
    textSize(tamanhoFonte)
    text(str(agente.quantidadeComida), 10, distanciamentoMargemSuperior)
