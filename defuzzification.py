def centroide(aplicar_freio, liberar_freio):
    if liberar_freio < aplicar_freio:
        num = liberar_freio * 5
        den = liberar_freio
    else:
        num = aplicar_freio * 5
        den = aplicar_freio
    
    for i in range(10, 100, 5):
        valor1 = i / 100
        if valor1 >= liberar_freio:
            break
        elif valor1 >= aplicar_freio:
            break

    for valor in range(10, 101, 5):
        if valor1 <= 1.1:
            num = num + (valor * valor1)
            den = den + valor1
        valor1 = valor1 + 0.05

    return num / den
