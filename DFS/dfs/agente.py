class Agente(): 
    
    def __init__(self, linha, coluna):
        
        # Para busca em largura
        self.caminho = []
        self.celulasParaVisitar = deque()
        self.celulasExpandidas = deque()
        
        self.comeuComida = False
        self.encontrouObstaculo = False
        self.procurandoCaminho = False
        
        self.quantidadeComida = 0
        
        self.linha = linha
        self.coluna = coluna
        
        # Agente = Quadrado Vermelho
        self.corpo = createShape(RECT, 0, 0, tamanhoCelulaGrid, tamanhoCelulaGrid)
        self.corpo.setFill(color(220, 20, 60))
        
    def caminhaAte(self, comida):
        
        linhaOk = False
        colunaOk = False
        
        for ponto in caminho:
            self.linha = ponto[0]
            self.coluna = ponto[1]
        
        # Caminha pelas colunas até que a coluna seja igual a da fruta
        if(self.coluna == comida.coluna): colunaOk = True
            
        # Caminha pelas linhas até que a linha seja igual a da fruta
        if(self.linha == comida.linha): linhaOk = True
            
        # Se player e fruta estão na mesma linha e coluna, então a fruta foi comida
        if(linhaOk and colunaOk): self.comeuComida = True
        else: self.comeuComida = False
        
        if(self.comeuComida): self.quantidadeComida += 1; # Atualizando o quantitativo comido
        
    def encontraCaminho(self):
        
        print("A COMIDA ESTA EM " + str(comida.linha + 1) + ", " + str(comida.coluna + 1))
        print("")
        
        self.procurandoCaminho = True
        
        self.caminho = []
        self.celulasParaVisitar = deque()
        self.celulasExpandidas = deque()
        
        self.caminho = self.buscaEmLargura() # Encontra o caminho utilizando busca em largura
        
    def buscaEmLargura(self):
    
        # Configurando a primeira celula para iniciar a busca em profundidade
        celulaInicial = self.configuraCelula(self.linha, self.coluna, None)
        self.celulasParaVisitar.append(celulaInicial)
        
        celula = self.celulasParaVisitar.popleft() # Pega o primeiro item da lista de células para visitar (FIFO)
        
        print("INDO PARA CELULA " + str(celula.linha + 1) + ", " + str(celula.coluna + 1))
    
        try:
            
            while(not self.solucao(celula)):
            
                print("NAO EH SOLUCAO")
                print("")
                
                self.expande(celula)
                
                print("PROXIMAS PARA VISITAR: ")
                
                for celulaParaVisitar in self.celulasParaVisitar: 
                    print(str(celulaParaVisitar.linha + 1) + ", " + str(celulaParaVisitar.coluna + 1))
                    
                celula = self.celulasParaVisitar.popleft() # Se não houver mais celulas para visitar, ocorrerá um erro
                
                print("INDO PARA CELULA " + str(celula.linha + 1) + ", " + str(celula.coluna + 1))
                
        except:
            print("NAO TEM SOLUCAO!")
            return []
            
        print("EH SOLUCAO!")
        rota = self.geraCaminhoParaComida(celula)
        print("ROTA GERADA!")
        
        return rota # Encontra a solução a partir da célula destino

    def existeObstaculo(self, linha, coluna):
    
        for obstaculo in listaDeObstaculos:
            if(obstaculo.linha == linha and obstaculo.coluna == coluna): return True
            
        return False
        
    def solucao(self, celula):
        return (celula.linha == comida.linha and celula.coluna == comida.coluna)

    def geraCaminhoParaComida(self, celula):
        
        caminhoInverso = []
        
        celulaParteDoCaminho = celula
        
        caminhoInverso.append([celulaParteDoCaminho.linha, celulaParteDoCaminho.coluna])
        
        while celulaParteDoCaminho.pai is not None:
            celulaParteDoCaminho = celulaParteDoCaminho.pai
            caminhoInverso.append([celulaParteDoCaminho.linha, celulaParteDoCaminho.coluna])
        
        return list(reversed(caminhoInverso)) # Inverte porque o caminho parte da comida até o agente. Precisa ser o contrário
        
 
    def expande(self, celula):
        
        self.celulasExpandidas.append(celula)
        
        if(celula.esquerda is not None): self.atualizaListaBusca(self.configuraCelula(celula.esquerda.linha, celula.esquerda.coluna, celula))
        if(celula.direita is not None): self.atualizaListaBusca(self.configuraCelula(celula.direita.linha, celula.direita.coluna, celula))
        if(celula.cima is not None): self.atualizaListaBusca(self.configuraCelula(celula.cima.linha, celula.cima.coluna, celula))
        if(celula.baixo is not None): self.atualizaListaBusca(self.configuraCelula(celula.baixo.linha, celula.baixo.coluna, celula))

    def atualizaListaBusca(self, celula):
        if(not self.celulaJaExpandida(celula) and not self.celulaJaMarcadaVisita(celula)): self.celulasParaVisitar.append(celula)
    
    def celulaJaExpandida(self, celula):
        
        for celulaExpandida in self.celulasExpandidas:
            if(celulaExpandida.linha == celula.linha and celulaExpandida.coluna == celula.coluna): return True
        
        return False

    def celulaJaMarcadaVisita(self, celula):
        
        for celulaMarcada in self.celulasParaVisitar:
            if(celulaMarcada.linha == celula.linha and celulaMarcada.coluna == celula.coluna): return True
        
        return False
    
    def configuraCelula(self, linha, coluna, pai):
        
        celula = Celula(linha, coluna)
        
        celula.pai = pai
        
        if(coluna == 0 or self.existeObstaculo(linha, coluna - 1)): celula.esquerda = None
        else: celula.esquerda = Celula(linha, coluna - 1)
        
        if(coluna == quantidadeLinhasColunasGrid - 1 or self.existeObstaculo(linha, coluna + 1)): celula.direita = None
        else: celula.direita = Celula(linha, coluna + 1)
        
        if(linha == 0 or self.existeObstaculo(linha - 1, coluna)): celula.cima = None
        else: celula.cima = Celula(linha - 1, coluna)
        
        if(linha == quantidadeLinhasColunasGrid - 1 or self.existeObstaculo(linha + 1, coluna)): celula.baixo = None
        else: celula.baixo = Celula(linha + 1, coluna)
        
        return celula
        
    def atualiza(self): # Atualiza posição na tela
        shape(self.corpo, self.coluna * tamanhoCelulaGrid, self.linha * tamanhoCelulaGrid)
