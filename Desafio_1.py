import pandas as pd
import numpy as np

dados_vendas_clientes = pd.read_json('Pandas - Transformação e manipulação de dados\desafio1_dados_vendas_clientes.json')
dados_vendas_clientes = pd.json_normalize(dados_vendas_clientes['dados_vendas'])

colunas = list(dados_vendas_clientes.columns)
dados_vendas_clientes = dados_vendas_clientes.explode(colunas[1:])
dados_vendas_clientes.reset_index(inplace=True, drop=True)
dados_vendas_clientes['Valor da compra'] = dados_vendas_clientes['Valor da compra'].apply(lambda x: x.replace('R$','').replace(',','.').strip())
dados_vendas_clientes['Valor da compra'] = dados_vendas_clientes['Valor da compra'].astype(np.float64)
dados_vendas_clientes['Cliente'] = dados_vendas_clientes['Cliente'].str.lower().str.replace('ã', 'a')
dados_vendas_clientes['Cliente'] = dados_vendas_clientes['Cliente'].str.replace('[^a-z ]', ' ', regex=True).str.strip()
dados_vendas_clientes['Data de venda'] = pd.to_datetime(dados_vendas_clientes['Data de venda'])
subset = dados_vendas_clientes.groupby(dados_vendas_clientes['Cliente'])['Valor da compra'].sum()
print(f'A partir da lista abaixo, conseguimos selecionar o cliente com a maior compra na semana: \n{subset}')
