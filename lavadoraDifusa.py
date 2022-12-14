from skfuzzy import control as ctrl
import skfuzzy as fuzzy
import numpy as np

class lavadoraDifusa:
    #definición de las variables de entrada
    grado_suciedad = ctrl.Antecedent(np.arange(0, 101, 1),'grado_suciedad')
    nivel_suciedad = ctrl.Antecedent(np.arange(0, 101, 1),'nivel_suciedad')
    tipo_ropa = ctrl.Antecedent(np.arange(0, 101, 1),'tipo_ropa')
    #definición de las variables de salida
    tiempo_lavado = ctrl.Consequent(np.arange(0, 61, 1),'tiempo_lavado')
    #definición los conjuntos difusos
    nombre_gradoS = ['Bajo','Medio','Alto'] # etiquetas lingüisticas a utilizar por una variable
    nombre_nivelS = ['NoGraso','Medio','Graso']
    #incorporamos etiquetas de los conjuntos difusos a las variables
    grado_suciedad.automf(names=nombre_gradoS)
    nivel_suciedad.automf(names=nombre_nivelS)
    #grado_suciedad.view()
    #nivel_suciedad.view()
    #universo del discurso para la variable tiempo de lavado
    tiempo_lavado['muy_corto'] = fuzzy.trimf(tiempo_lavado.universe,[0, 8, 12])
    tiempo_lavado['corto'] = fuzzy.trimf(tiempo_lavado.universe,[8, 12, 20])
    tiempo_lavado['medio'] = fuzzy.trimf(tiempo_lavado.universe,[12, 20, 40])
    tiempo_lavado['largo'] = fuzzy.trimf(tiempo_lavado.universe,[20, 40, 60])
    tiempo_lavado['muy_largo'] = fuzzy.trimf(tiempo_lavado.universe,[40, 60, 60])
    #tiempo_lavado.view()
    #definiremos las reglas del Sistema difuso de la lavadora
    #R1: IF grado suciedad es Alto AND nivel de suciedad es Graso THEN tiempo de lavado es Muy largo.
    r1 = ctrl.Rule(grado_suciedad['Alto'] & nivel_suciedad['Graso'],tiempo_lavado['muy_largo'])
    #R2: IF grado suciedad es Medio AND nivel de suciedad es Graso THEN tiempo de lavado es Largo.
    r2 = ctrl.Rule(grado_suciedad['Medio'] & nivel_suciedad['Graso'],tiempo_lavado['largo'])
    #R3: IF grado suciedad es Bajo AND nivel de suciedad es Graso THEN tiempo de lavado es Medio.
    r3 = ctrl.Rule(grado_suciedad['Bajo'] & nivel_suciedad['Graso'],tiempo_lavado['medio'])
    #R4: IF grado suciedad es Alto AND nivel de suciedad es Medio THEN tiempo de lavado es Largo.
    r4 = ctrl.Rule(grado_suciedad['Alto'] & nivel_suciedad['Medio'],tiempo_lavado['largo'])
    #R5: IF grado suciedad es Medio AND nivel de suciedad es Medio THEN tiempo de lavado es Medio.
    r5 = ctrl.Rule(grado_suciedad['Medio'] & nivel_suciedad['Medio'],tiempo_lavado['medio'])
    #R6: IF grado suciedad es Bajo AND nivel de suciedad es Medio THEN tiempo de lavado es Medio.
    r6 = ctrl.Rule(grado_suciedad['Bajo'] & nivel_suciedad['Medio'],tiempo_lavado['medio'])
    #R7: IF grado suciedad es Alto AND nivel de suciedad es No Graso THEN tiempo de lavado es Medio.
    r7 = ctrl.Rule(grado_suciedad['Alto'] & nivel_suciedad['NoGraso'],tiempo_lavado['medio'])
    #R8: IF grado suciedad es Medio AND nivel de suciedad es No Graso THEN tiempo de lavado es Corto.
    r8 = ctrl.Rule(grado_suciedad['Medio'] & nivel_suciedad['NoGraso'],tiempo_lavado['corto'])
    #R9: IF grado suciedad es Bajo AND nivel de suciedad es No Graso THEN tiempo de lavado es Muy corto.
    r9 = ctrl.Rule(grado_suciedad['Bajo'] & nivel_suciedad['NoGraso'],tiempo_lavado['muy_corto'])
    
    #asignar las reglas al sistema de control difuso definiendo una variable
    lavado_ctrl = ctrl.ControlSystem([r1,r2,r3,r4,r5,r6,r7,r8,r9])
    lavado = ctrl.ControlSystemSimulation(lavado_ctrl)
    
    def lavado_fuzzy(gradoS_Fuzzy, nivelS_Fuzzy):
        lavadoraDifusa.lavado.input['grado_suciedad'] = gradoS_Fuzzy
        lavadoraDifusa.lavado.input['nivel_suciedad'] = nivelS_Fuzzy
        #computar el sistema difuso respecto a las variables de entrada
        lavadoraDifusa.lavado.compute()
        lavadoraDifusa.tiempo_lavado.view(sim=lavadoraDifusa.lavado)
        return lavadoraDifusa.lavado.output['tiempo_lavado']