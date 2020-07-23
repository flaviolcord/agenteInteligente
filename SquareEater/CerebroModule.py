from collections import deque
from CelulaModule import *
from TipoBuscaModule import *
from Desempenho import *

class Cerebro(): 
    
    def __init__(self, listaDeObstaculos, quantidadeLinhasColunasGrid):
        
        self.comida = None
        
        self.quantidadeLinhasColunasGrid = quantidadeLinhasColunasGrid
        
        self.listaDeCelulas = deque()
        self.celulasParaVisitar = deque()
        self.celulasExpandidas = deque()
        
        self.listaDeObstaculos = listaDeObstaculos
        
        
    def encontraCelula(self, linha, coluna):
        
        for celula in self.listaDeCelulas:
            if(celula.linha == linha and celula.coluna == coluna): return celula
            
            
    def busca(self, linhaInicial, colunaInicial, comida, tipoBusca):
        
        if(tipoBusca == TipoBusca.LARGURA): return self.buscaLargura(linhaInicial, colunaInicial, comida, 'largura')
        elif(tipoBusca == TipoBusca.GULOSA): return self.buscaGulosa(linhaInicial, colunaInicial, comida, 'gulosa')
        elif(tipoBusca == TipoBusca.ESTRELA): return self.buscaEstrela(linhaInicial, colunaInicial, comida, 'estrela')
        elif(tipoBusca == TipoBusca.PROFUNDIDADE): return self.buscaProfundidade(linhaInicial, colunaInicial, comida, 'profundidade')
        elif(tipoBusca == TipoBusca.CUSTOUNIFORME): return self.buscaCustoUniforme(linhaInicial, colunaInicial, comida, 'custo_uniforme')
        
        
    def buscaLargura(self, linhaInicial, colunaInicial, comida, nome):
        cont=0
        
        self.listaDeCelulas = deque()
        self.configuraCelulas()
        
        self.comida = comida
        
        self.celulasParaVisitar = deque()
        self.celulasExpandidas = deque()
        
        celulaInicial = self.encontraCelula(linhaInicial, colunaInicial)
        
        self.celulasParaVisitar.append(celulaInicial)
        
        celula = self.celulasParaVisitar.popleft()
        
        
        try:
            
            while(not self.solucao(celula)):
                self.expande(celula)
                celula = self.celulasParaVisitar.popleft()
                cont+=1
                #mostraExpansao(celula, comida, colunaInicial, linhaInicial, self.quantidadeLinhasColunasGrid, self.listaDeObstaculos)
        except:
            return []
    
        return self.geraCaminhoParaComida(celula, nome, cont), self.celulasExpandidas
    
    
    def buscaProfundidade(self, linhaInicial, colunaInicial, comida, nome):
        cont=0
        self.listaDeCelulas = deque()
        self.configuraCelulas()
        
        self.comida = comida
        
        self.celulasParaVisitar = deque()
        self.celulasExpandidas = deque()
        
        celulaInicial = self.encontraCelula(linhaInicial, colunaInicial)
        
        self.celulasParaVisitar.append(celulaInicial)
        
        celula = self.celulasParaVisitar.popleft()
        
        try:
            
            while(not self.solucao(celula)):
                self.expandeProfundidade(celula)
                celula = self.celulasParaVisitar.popleft()
                cont+=1
                #mostraExpansao(celula, comida, colunaInicial, linhaInicial, self.quantidadeLinhasColunasGrid, self.listaDeObstaculos)
        except:
            return []
        
        return self.geraCaminhoParaComida(celula, nome, cont), self.celulasExpandidas
    
    
    def buscaGulosa(self, linhaInicial, colunaInicial, comida, nome):
        cont=0
        
        self.listaDeCelulas = deque()
        self.configuraCelulas()
        
        self.comida = comida
        
        self.celulasParaVisitar = deque()
        self.celulasExpandidas = deque()
        
        celulaInicial = self.encontraCelula(linhaInicial, colunaInicial)
        
        self.celulasParaVisitar.append(celulaInicial)
        
        celula = self.celulasParaVisitar.popleft()
        
        try:
            
            while(not self.solucao(celula)):
                
                self.expande(celula)
                
                listaCustos = []
                
                for celulaParaVisitar in self.celulasParaVisitar:
                    distancia = dist(celulaParaVisitar.linha, celulaParaVisitar.coluna, self.comida.linha, self.comida.coluna)
                    listaCustos.append(distancia)
                    cont+=1
                    
                melhorCusto = sorted(listaCustos)[0]
                
                celulaParaVisitar = None
                
                for celulaCandidata in self.celulasParaVisitar:
                    
                    distancia = dist(celulaCandidata.linha, celulaCandidata.coluna, self.comida.linha, self.comida.coluna)
                    cont+=1
                    
                    if(distancia == melhorCusto):
                        celulaParaVisitar = celulaCandidata;
                        break
                    
                celula = celulaParaVisitar
                
                #mostraExpansao(celula, comida, colunaInicial, linhaInicial, self.quantidadeLinhasColunasGrid, self.listaDeObstaculos)

                self.celulasParaVisitar.remove(celulaParaVisitar)
                
        except:
            return []
    
        return self.geraCaminhoParaComida(celula, nome, cont), self.celulasExpandidas
    
    
    def buscaCustoUniforme(self, linhaInicial, colunaInicial, comida, nome):
        cont=0
        
        self.listaDeCelulas = deque()
        self.configuraCelulas()
        
        self.comida = comida
        
        self.celulasParaVisitar = deque()
        self.celulasExpandidas = deque()
        
        celulaInicial = self.encontraCelula(linhaInicial, colunaInicial)
        
        self.celulasParaVisitar.append(celulaInicial)
        
        celula = self.celulasParaVisitar.popleft()
        
        try:
            
            while(not self.solucao(celula)):
                
                self.expande(celula)
                
                listaCustos = []
                
                for celulaParaVisitar in self.celulasParaVisitar:
                    distancia = dist(celulaParaVisitar.linha, celulaParaVisitar.coluna, linhaInicial, colunaInicial)
                    listaCustos.append(distancia)
                    cont+=1
                    
                melhorCusto = sorted(listaCustos)[0]
                
                celulaParaVisitar = None
                
                for celulaCandidata in self.celulasParaVisitar:
                    
                    distancia = dist(celulaCandidata.linha, celulaCandidata.coluna, linhaInicial, colunaInicial)
                    cont+=1
                    
                    if(distancia == melhorCusto):
                        celulaParaVisitar = celulaCandidata;
                        break
                    
                celula = celulaParaVisitar   
                
                #mostraExpansao(celula, comida, colunaInicial, linhaInicial, self.quantidadeLinhasColunasGrid, self.listaDeObstaculos)
                
                self.celulasParaVisitar.remove(celulaParaVisitar)
                    
        except:
            return []
    
        return self.geraCaminhoParaComida(celula, nome, cont), self.celulasExpandidas
    
    
    def buscaEstrela(self, linhaInicial, colunaInicial, comida, nome):
        cont=0
        
        self.listaDeCelulas = deque()
        self.configuraCelulas()
        
        self.comida = comida
        
        self.celulasParaVisitar = deque()
        self.celulasExpandidas = deque()
        
        celulaInicial = self.encontraCelula(linhaInicial, colunaInicial)
        
        self.celulasParaVisitar.append(celulaInicial)
        
        celula = self.celulasParaVisitar.popleft()
        
        try:
            
            while(not self.solucao(celula)):
                
                self.expande(celula)
                
                listaCustos = []
                
                for celulaParaVisitar in self.celulasParaVisitar:
                    
                    distancia1 = dist(celulaParaVisitar.linha, celulaParaVisitar.coluna, self.comida.linha, self.comida.coluna)
                    distancia2 = dist(celulaParaVisitar.linha, celulaParaVisitar.coluna, linhaInicial, colunaInicial)
                    
                    distancia = distancia1 + distancia2
                    
                    listaCustos.append(distancia)
                    cont+=1
                    
                melhorCusto = sorted(listaCustos)[0]
                
                celulaParaVisitar = None
                
                for celulaCandidata in self.celulasParaVisitar:
                    
                    distancia1 = dist(celulaCandidata.linha, celulaCandidata.coluna, self.comida.linha, self.comida.coluna)
                    distancia2 = dist(celulaCandidata.linha, celulaCandidata.coluna, linhaInicial, colunaInicial)
                    
                    distancia = distancia1 + distancia2
                    cont+=1
                    
                    if(distancia == melhorCusto):
                        celulaParaVisitar = celulaCandidata;
                        break
                    
                celula = celulaParaVisitar
            
                #mostraExpansao(celula, comida, colunaInicial, linhaInicial, self.quantidadeLinhasColunasGrid, self.listaDeObstaculos)

                self.celulasParaVisitar.remove(celulaParaVisitar)
                
        except:
            return []
    
        return self.geraCaminhoParaComida(celula, nome, cont), self.celulasExpandidas
    
    
    def solucao(self, celula):
        return (celula.linha == self.comida.linha and celula.coluna == self.comida.coluna)
    
    
    def expande(self, celula):
        
        self.celulasExpandidas.append(celula)
        
        if(celula.esquerda is not None): self.atualizaListaBusca(celula.esquerda, celula)
        if(celula.direita is not None): self.atualizaListaBusca(celula.direita, celula)
        if(celula.cima is not None): self.atualizaListaBusca(celula.cima, celula)
        if(celula.baixo is not None): self.atualizaListaBusca(celula.baixo, celula)
        
                
    def atualizaListaBusca(self, celula, pai):
        
        if(not self.celulaJaExpandida(celula) and not self.celulaJaMarcadaVisita(celula)): 
            celula.pai = pai
            self.celulasParaVisitar.append(celula)
            
            
    def expandeProfundidade(self, celula):
        
        self.celulasExpandidas.append(celula)
        
        if(celula.esquerda is not None): self.atualizaListaBuscaProfundidade(celula.esquerda, celula)
        if(celula.direita is not None): self.atualizaListaBuscaProfundidade(celula.direita, celula)
        if(celula.cima is not None): self.atualizaListaBuscaProfundidade(celula.cima, celula)
        if(celula.baixo is not None): self.atualizaListaBuscaProfundidade(celula.baixo, celula)
        
                
    def atualizaListaBuscaProfundidade(self, celula, pai):
        
        if(not self.celulaJaExpandida(celula) and not self.celulaJaMarcadaVisita(celula)): 
            celula.pai = pai
            self.celulasParaVisitar.appendleft(celula)
            
        
    def celulaJaExpandida(self, celula):
        
        for celulaExpandida in self.celulasExpandidas:
            if(celulaExpandida.linha == celula.linha and celulaExpandida.coluna == celula.coluna): return True
        
        return False
    
    
    def celulaJaMarcadaVisita(self, celula):
            
        for celulaMarcada in self.celulasParaVisitar:
            if(celulaMarcada.linha == celula.linha and celulaMarcada.coluna == celula.coluna): return True
        
        return False
    
    
    def geraCaminhoParaComida(self, celulaSolucao, nome, cont):
    
        celulaParteDoCaminho = celulaSolucao
            
        caminhoInverso = []
        caminhoInverso.append([celulaParteDoCaminho.linha, celulaParteDoCaminho.coluna])
        
        while celulaParteDoCaminho.pai is not None:
            celulaParteDoCaminho = celulaParteDoCaminho.pai
            caminhoInverso.append([celulaParteDoCaminho.linha, celulaParteDoCaminho.coluna])
        
        salvaDadosDesempenho(list(reversed(caminhoInverso)),nome, cont)
        return list(reversed(caminhoInverso))
    
    
    def configuraCelulas(self):
    
        self.listaDeCelulas = deque()
        
        for linha in range(self.quantidadeLinhasColunasGrid):
            for coluna in range(self.quantidadeLinhasColunasGrid): self.listaDeCelulas.append(Celula(linha, coluna))
            
        for linha in range(self.quantidadeLinhasColunasGrid):
            
            for coluna in range(self.quantidadeLinhasColunasGrid):
                
                celula = self.encontraCelula(linha, coluna)
            
                if(coluna == 0 or self.existeObstaculo(linha, coluna - 1)): celula.esquerda = None
                else: celula.esquerda = self.encontraCelula(linha, coluna - 1)
                
                if(coluna == self.quantidadeLinhasColunasGrid - 1 or self.existeObstaculo(linha, coluna + 1)): celula.direita = None
                else: celula.direita = self.encontraCelula(linha, coluna + 1)
                
                if(linha == 0 or self.existeObstaculo(linha - 1, coluna)): celula.cima = None
                else: celula.cima = self.encontraCelula(linha - 1, coluna)
                
                if(linha == self.quantidadeLinhasColunasGrid - 1 or self.existeObstaculo(linha + 1, coluna)): celula.baixo = None
                else: celula.baixo = self.encontraCelula(linha + 1, coluna)
                
            
    def existeObstaculo(self, linha, coluna):
        for obstaculo in self.listaDeObstaculos:
            if(obstaculo.linha == linha and obstaculo.coluna == coluna): return True
        return False

        
    
    
