import pandas as pd
import numpy as np

dados_locacao_imoveis = pd.read_json('Pandas - Transformação e manipulação de dados\desafio2_locacao_imoveis.json')
dados_locacao_imoveis = pd.json_normalize(dados_locacao_imoveis['dados_locacao'])

colunas = list(dados_locacao_imoveis.columns)
dados_locacao_imoveis = dados_locacao_imoveis.explode(colunas[1:])
dados_locacao_imoveis.reset_index(inplace=True, drop=True)
dados_locacao_imoveis['valor_aluguel'] = dados_locacao_imoveis['valor_aluguel'].apply(lambda x: x.replace('$','').replace(',','.').replace('reais','').strip())
dados_locacao_imoveis['valor_aluguel'] = dados_locacao_imoveis['valor_aluguel'].astype(np.float64)
dados_locacao_imoveis['apartamento'] = dados_locacao_imoveis['apartamento'].str.replace('(blocoAP)', '')
dados_locacao_imoveis['datas_combinadas_pagamento'] = pd.to_datetime(dados_locacao_imoveis['datas_combinadas_pagamento'], format='%d/%m/%Y')
dados_locacao_imoveis['datas_de_pagamento'] = pd.to_datetime(dados_locacao_imoveis['datas_de_pagamento'], format='%d/%m/%Y')
dados_locacao_imoveis['atraso'] = (dados_locacao_imoveis['datas_de_pagamento'] - dados_locacao_imoveis['datas_combinadas_pagamento']).dt.days
media_atraso = dados_locacao_imoveis.groupby(['apartamento'])['atraso'].mean()
print(f'A média de atraso para cada apartamento é: \n{media_atraso}')
