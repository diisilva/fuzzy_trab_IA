import pandas as pd
from faker import Faker
import random

# Caminho do arquivo Excel para salvar os dados gerados
dados_freio_xlsx = 'F:\\Univali\\IA\\Trab_fuzzy_v2\\dados_freio.xlsx'

# Função para gerar pseudodados de entrada para o sistema de freio
def gerar_dados_freio(num_dados=50):
    fake = Faker()
    dados_freio = []

    for _ in range(num_dados):
        # Gera pressão no pedal (0 a 100%)
        pressao_pedal = round(random.uniform(0, 100), 2)

        # Gera velocidade da roda (0 a 150 km/h)
        velocidade_roda = round(random.uniform(0, 150), 2)

        # Gera velocidade do carro (0 a 150 km/h)
        velocidade_carro = round(random.uniform(0, 150), 2)

        # Adiciona os dados na lista
        dados_freio.append({
            'Pressao_Pedal': pressao_pedal,
            'Velocidade_Roda': velocidade_roda,
            'Velocidade_Carro': velocidade_carro
        })

    return dados_freio

# Função para salvar os dados gerados em um arquivo Excel
def salvar_dados_excel(dados, caminho_arquivo):
    df = pd.DataFrame(dados)
    df.to_excel(caminho_arquivo, index=False)
    print(f"Dados de entrada salvos em: {caminho_arquivo}")

# Gerar os dados e salvar
dados_freio = gerar_dados_freio(num_dados=50)
salvar_dados_excel(dados_freio, dados_freio_xlsx)
