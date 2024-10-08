import pandas as pd
from fuzzy_logic import valor_min_PRESSAO, valor_medio_PRESSAO, valor_max_PRESSAO
from fuzzy_logic import valor_min_VELOCIDADE, valor_medio_VELOCIDADE, valor_max_VELOCIDADE
from fuzzy_rules import aplicar_freio, liberar_freio
from defuzzification import centroide

# Caminho da planilha de entrada
input_xlsx = 'F:\\Univali\\IA\\Trab_fuzzy_v2\\dados_freio.xlsx'

# Caminho da planilha para salvar os resultados
output_xlsx = 'F:\\Univali\\IA\\Trab_fuzzy_v2\\resultados_freio.xlsx'

# Função para processar os dados fuzzy e salvar os resultados
def processar_dados_fuzzy():
    # Ler os dados de entrada
    df_dados_freio = pd.read_excel(input_xlsx)
    
    # Lista para armazenar os resultados
    resultados_freio = []

    # Processar cada linha da planilha
    for _, entrada in df_dados_freio.iterrows():
        pressao_pedal = entrada['Pressao_Pedal']
        velocidade_roda = entrada['Velocidade_Roda']
        velocidade_carro = entrada['Velocidade_Carro']
        
        # Aplicar regras fuzzy e calcular o centroide
        resultado_aplicar_freio = aplicar_freio(pressao_pedal, velocidade_roda, velocidade_carro)
        resultado_liberar_freio = liberar_freio(pressao_pedal, velocidade_roda, velocidade_carro)
        resultado_centroide = centroide(resultado_aplicar_freio, resultado_liberar_freio)
        
        # Armazenar o resultado
        resultados_freio.append([pressao_pedal, velocidade_roda, velocidade_carro, resultado_aplicar_freio, resultado_liberar_freio, resultado_centroide])

    # Criar um DataFrame com os resultados
    df_resultados_freio = pd.DataFrame(resultados_freio, columns=['Pressao_Pedal', 'Velocidade_Roda', 'Velocidade_Carro', 'Aplicar_Freio', 'Liberar_Freio', 'Centroide'])

    # Salvar os resultados no Excel
    df_resultados_freio.to_excel(output_xlsx, index=False)
    print(f"Resultados salvos em: {output_xlsx}")

if __name__ == '__main__':
    processar_dados_fuzzy()
