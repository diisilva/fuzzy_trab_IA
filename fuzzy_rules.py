from fuzzy_logic import valor_min_PRESSAO, valor_medio_PRESSAO, valor_max_PRESSAO
from fuzzy_logic import valor_min_VELOCIDADE, valor_max_VELOCIDADE

def aplicar_freio(pressao_pedal, velocidade_roda, velocidade_carro):
    # Regra 1: Pressão no pedal média -> aplicar freio
    aplicar = valor_medio_PRESSAO(pressao_pedal)
    
    # Regra 2: Pressão no pedal alta + velocidade alta -> aplicar freio
    aux1 = valor_max_PRESSAO(pressao_pedal)
    aux2 = valor_max_VELOCIDADE(velocidade_carro)
    aux3 = valor_max_VELOCIDADE(velocidade_roda)
    aplicar += min(aux1, aux2, aux3)
    
    return aplicar

def liberar_freio(pressao_pedal, velocidade_roda, velocidade_carro):
    # Regra 3: Pressão no pedal alta + velocidade carro alta + velocidade roda baixa -> liberar freio
    aux1 = valor_max_PRESSAO(pressao_pedal)
    aux2 = valor_max_VELOCIDADE(velocidade_carro)
    aux3 = valor_min_VELOCIDADE(velocidade_roda)
    liberar = min(aux1, aux2, aux3)
    
    # Regra 4: Pressão no pedal baixa -> liberar freio
    liberar += valor_min_PRESSAO(pressao_pedal)
    
    return liberar
