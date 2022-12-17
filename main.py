from lavadoraDifusa import *

def parametros_computo_lavado(grado_suciedad, nivel_suciedad, tipo_ropa):
    if grado_suciedad < 0.0 or grado_suciedad > 100:
        raise Exception ("Invalido el grado de suciedad: %lf"%grado_suciedad)
    if nivel_suciedad < 0.0 or nivel_suciedad > 100:
        raise Exception ("Invalido el nivel de suciedad: %lf"%nivel_suciedad)
    if tipo_ropa < 0.0 or tipo_ropa > 100:
        raise Exception ("Invalido el tipo de ropa: %lf"%tipo_ropa)
    valor_lavado = lavadoraDifusa.lavado_fuzzy(grado_suciedad,nivel_suciedad,tipo_ropa)
    return valor_lavado

if __name__ == "__main__":
    grado_suciedad = float (input("ingrese un grado de suciedad entre [0-100]: "))
    nivel_suciedad = float (input("ingrese un nivel de suciedad entre [0-100]: "))
    tipo_ropa = float (input("ingrese un tipo de ropa entre [0-100]: "))
    tiempo_lavado = parametros_computo_lavado(grado_suciedad, nivel_suciedad, tipo_ropa)
    print(tiempo_lavado)
    input("Pulse una tecla para finalizar...")