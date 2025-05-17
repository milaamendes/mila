import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def calculate_clv(transacoes):
    df = transacoes.groupby('cliente_id')['valor'].sum().reset_index()
    df.columns = ['cliente_id', 'clv']
    return {
        "labels": df['cliente_id'].astype(str).tolist(),
        "values": df['clv'].round(2).tolist()
    }

def run_kmeans(clientes):
    variaveis = ['frequencia_compras', 'total_gasto', 'ultima_compra', 'renda_mensal', 'idade']
    scaler = StandardScaler()
    dados_normalizados = scaler.fit_transform(clientes[variaveis])
    kmeans = KMeans(n_clusters=3, random_state=0).fit(dados_normalizados)
    clientes['cluster'] = kmeans.labels_
    nomes = {0: 'Econômico', 1: 'Premium', 2: 'Frequente'}
    clientes['perfil'] = clientes['cluster'].map(nomes)
    return {
        "x": clientes['frequencia_compras'].tolist(),
        "y": clientes['total_gasto'].tolist(),
        "labels": clientes['perfil'].tolist()
    }

def prepare_campanha_data(campanhas):
    campanhas['taxa_conversao'] = campanhas['conversao'] / campanhas['alcance']
    a = campanhas.groupby('atributo_principal')['taxa_conversao'].mean().reset_index()
    b = campanhas.groupby('nome_campanha')['taxa_conversao'].mean().reset_index()
    return {
        "atributos": a['atributo_principal'].tolist(),
        "taxas_por_atributo": a['taxa_conversao'].round(2).tolist(),
        "campanhas": b['nome_campanha'].tolist(),
        "taxas_por_campanha": b['taxa_conversao'].round(2).tolist()
    }
