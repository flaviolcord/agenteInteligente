class TipoBusca:
    
    LARGURA = "LARGURA"
    GULOSA = "GULOSA"
    ESTRELA = "ESTRELA"
    PROFUNDIDADE = "PROFUNDIDADE"
    CUSTOUNIFORME = "CUSTOUNIFORME"
    
    

def mostraExpansao(celula, comida, agente_coluna, agente_linha, grid, listaDeObstaculos):
    # captura posicoes de obstaculos
    obstaculos = [(x.coluna, x.linha) for x in listaDeObstaculos]
    
    # se nao for obstaculo ou o proprio agente, pinta de roxo
    if celula.coluna == agente_coluna and celula.linha == agente_linha:
        print('test')
    else:
        if (celula.coluna,celula.linha) not in obstaculos and (celula.coluna,celula.linha) != (comida.coluna, comida.linha):
            aparece = createShape(RECT, 0, 0, 20, 20)
            aparece.setFill(color(75,0,130))
            shape(aparece, celula.coluna * 20, celula.linha * 20)
            print('disp')

    

def mostraExpansao2(celula, agente_coluna, agente_linha, grid, listaDeObstaculos):
    
    obstaculos = [(x.coluna, x.linha) for x in listaDeObstaculos]

    #mostrar espaco na tela
    aparece = createShape(RECT, 0, 0, grid, grid)
    aparece.setFill(color(75,0,130))
    shape(aparece, celula.coluna * grid, celula.linha * grid)
    # mostra agente
    if celula.coluna == agente_coluna and celula.linha == agente_linha:
        aparece = createShape(RECT, 0, 0, grid, grid)
        aparece.setFill(color(220, 20, 60))
        shape(aparece, celula.coluna * grid, celula.linha * grid)
    # mostra obstaculos
    if (celula.coluna,celula.linha) in obstaculos:
        aparece = createShape(RECT, 0, 0, grid, grid)
        aparece.setFill(color(0, 0, 0))
        shape(aparece, celula.coluna * grid, celula.linha * grid)
             
