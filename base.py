import pandas as pd
import numpy as np
import json

df = pd.read_csv('base_score_credito.csv')

def distancia_euclidiana(usuario1, usuario2):
    return np.linalg.norm(usuario1 - usuario2)

def similaridade(distancia):
    de = distancia
    sim = 1/(1+de)
    return sim

def obter_similares(cliente_id):
    colunas = ['salario_ano','casa_propria','carro','scode_credito','grupo']
    usuario1 = df.loc[df['cliente'] == cliente_id].iloc[0][colunas]
    resultados = []
    df_group = df[df['grupo'] == usuario1['grupo']]
    for index, row in df_group.iterrows():
        if row['cliente'] != cliente_id:
            usuario2 = row[colunas]
            distancia = distancia_euclidiana(usuario1, usuario2)
            sim = similaridade(distancia)
            resultados.append({
                'cliente_comparado': row['cliente'],
                'similaridade': sim
            })
    print(len(df_group))
    df_temp = pd.DataFrame(resultados)
    df_temp = df_temp.sort_values(by='similaridade', ascending=False)
    return json.loads(df_temp[:3].to_json())

def recomendacao_produtos(cliente_alvo, cliente_similar):
    colunas = ['casa_propria', 'seguro_residencia', 'carro', 'seguro_auto', 'cartao','seguro_cartao', 'poupanca', 'renda_fixa', 'credito_pessoal', 'scode_credito']
    produtos_recomentadados = []
    usuario1 = df.loc[df['cliente'] == cliente_alvo].iloc[0][colunas]
    usuario2 = df.loc[df['cliente'] == cliente_similar].iloc[0][colunas]
    for coluna in colunas:
        if usuario2[coluna] >= 1:
            if usuario1[coluna] == 0:
                produtos_recomentadados.append(coluna)
    return produtos_recomentadados