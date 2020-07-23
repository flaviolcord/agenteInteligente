

    
def salvaDadosDesempenho(lista_caminho, tipo_busca, step_busca):
    passos_ate_comida = len(lista_caminho)
    with open(('desempenho_passos_'+tipo_busca+'.txt'), "a") as myfile:
        myfile.write(str(passos_ate_comida)+'\n')
    with open(('desempenho_busca_'+tipo_busca+'.txt'), "a") as myfile:
        myfile.write(str(step_busca)+'\n')    
