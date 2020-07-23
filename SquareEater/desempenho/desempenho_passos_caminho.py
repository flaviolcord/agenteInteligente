


# importar
import pandas as pd 

# 
uniforme = pd.read_csv('desempenho_passos_custo_uniforme.txt', header=None)
estrela = pd.read_csv('desempenho_passos_estrela.txt', header=None)
largura = pd.read_csv('desempenho_passos_largura.txt', header=None)
profund = pd.read_csv('desempenho_passos_profundidade.txt', header=None)
gulosa = pd.read_csv('desempenho_passos_gulosa.txt', header=None)

len(estrela)
len(uniforme) 
len(largura) 
len(profund)
len(gulosa)

# selecionar casos aleatorios
estrela = estrela.sample(100).reset_index()
uniforme = uniforme.sample(100).reset_index()
largura = largura.sample(100).reset_index()
profund = profund.sample(100).reset_index()
gulosa = gulosa.sample(100).reset_index()

# nomear coluna de busca
estrela['tipo_de_busca'] = 'estrela'
uniforme['tipo_de_busca'] = 'custo uniforme'
largura['tipo_de_busca'] = 'largura'
profund['tipo_de_busca'] = 'profundidade'
gulosa['tipo_de_busca'] = 'gulosa'

# combinar casos
data = pd.concat([estrela, uniforme, largura, profund, gulosa])

# remover coluna index
data.drop('index', axis=1, inplace=True)
data.columns=['passos_ate_comida', 'tipos_de_busca']

#===================
# visualizacao
#=======================

from plotnine import * 

data = data[data['tipos_de_busca'] != 'profundidade']

# ggplot heatmap
ggplot(date_volume, aes('review_collect_week', 'review_collect_hour')) + geom_tile(aes(fill='freq'))\
    + scale_fill_gradientn(colors=['#9ebcda','#8c6bb1','#88419d','#6e016b']) \
    + ggtitle("Volume de 'Reviews' por hora do dia e dia da semana ")


(
    ggplot(data, aes(x='tipos_de_busca', y='passos_ate_comida'))
    + geom_boxplot(aes(x='tipos_de_busca', y='passos_ate_comida'))
)


