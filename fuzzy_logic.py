# Funções para fuzzificação

def valor_min_PRESSAO(x, a=0, b=50):
    res_min = (b-x)/(b-a)
    return max(res_min, 0)

def valor_medio_PRESSAO(x, a=30, b=50, c=70):
    aux1 = (x-a) / (b-a)
    aux2 = (c-x) / (c-b)
    return max(min(aux1, aux2), 0)

def valor_max_PRESSAO(x, a=50, b=100):
    res_max = (a-x)/(a-b)
    return max(res_max, 0)

def valor_min_VELOCIDADE(x, a=0, b=60):
    res_min = (b-x)/(b-a)
    return max(res_min, 0)

def valor_medio_VELOCIDADE(x, a=20, b=50, c=80):
    aux1 = (x-a) / (b-a)
    aux2 = (c-x) / (c-b)
    return max(min(aux1, aux2), 0)

def valor_max_VELOCIDADE(x, a=40, b=100):
    res_max = (a-x)/(a-b)
    return max(res_max, 0)
