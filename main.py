from lavadoraDifusa import *

def parametros_computo_lavado(grado_suciedad, nivel_suciedad, tipo_ropa, nivel_ropa_Fuzzy):
    if grado_suciedad < 0.0 or grado_suciedad > 100:
        raise Exception ("Invalido el grado de suciedad: %lf"%grado_suciedad)
    if nivel_suciedad < 0.0 or nivel_suciedad > 100:
        raise Exception ("Invalido el nivel de suciedad: %lf"%nivel_suciedad)
    if nivel_ropa_Fuzzy < 0.0 or nivel_ropa_Fuzzy > 100:
        raise Exception ("Invalido el tipo de ropa: %lf"%nivel_ropa_Fuzzy)
    valor_lavado = lavadoraDifusa.lavado_fuzzy(grado_suciedad,nivel_suciedad,tipo_ropa,nivel_ropa_Fuzzy)
    return valor_lavado

if __name__ == "__main__":
    grado_suciedad = float (input("ingrese un grado de suciedad entre [0-100]: "))
    nivel_suciedad = float (input("ingrese un nivel de suciedad entre [0-100]: "))
    tipo_ropa = input("ingrese un tipo de ropa (Gruesa, Media, Fina): ")
    nivel_ropa_Fuzzy = 0.0
    if tipo_ropa.lower() == "gruesa":
        nivel_ropa_Fuzzy = float (input("ingrese un nivel de ropa Gruesa entre [0-100]: "))
    elif tipo_ropa.lower() == "media":
        nivel_ropa_Fuzzy = float (input("ingrese un nivel de ropa Media entre [0-100]: "))
    elif tipo_ropa.lower() == "fina":
        nivel_ropa_Fuzzy = float (input("ingrese un nivel de ropa Fina entre [0-100]: "))
    tiempo_lavado = parametros_computo_lavado(grado_suciedad, nivel_suciedad, tipo_ropa, nivel_ropa_Fuzzy)
    print(tiempo_lavado)
    input()