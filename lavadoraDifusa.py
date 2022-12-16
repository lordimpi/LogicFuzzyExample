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
    nombre_gradoS = ['MuyBajo','Bajo','MedioSucio','Alto','MuyAlto'] # etiquetas lingüisticas a utilizar por una variable
    nombre_nivelS = ['NoGraso','PocoGraso','MedioGraso','Graso','MuyGraso']
    nombre_tipoR = ['Fina','Media','Gruesa']
    #incorporamos etiquetas de los conjuntos difusos a las variables
    # grado_suciedad.automf(names=nombre_gradoS)
    # nivel_suciedad.automf(names=nombre_nivelS)

    grado_suciedad.automf(names=nombre_gradoS)
    nivel_suciedad.automf(names=nombre_nivelS)
    tipo_ropa.automf(names=nombre_tipoR)

    grado_suciedad['MuyBajo'] = fuzzy.trimf(grado_suciedad.universe,[0, 0, 25])
    grado_suciedad['Bajo'] = fuzzy.trimf(grado_suciedad.universe,[0, 25, 50])
    grado_suciedad['MedioSucio'] = fuzzy.trimf(grado_suciedad.universe,[25, 50, 75])
    grado_suciedad['Alto'] = fuzzy.trimf(grado_suciedad.universe,[50, 75, 100])
    grado_suciedad['MuyAlto'] = fuzzy.trimf(grado_suciedad.universe,[75, 100, 100])

    nivel_suciedad['NoGraso'] = fuzzy.trimf(nivel_suciedad.universe,[0, 0, 25])
    nivel_suciedad['PocoGraso'] = fuzzy.trimf(nivel_suciedad.universe,[0, 25, 50])
    nivel_suciedad['MedioGraso'] = fuzzy.trimf(nivel_suciedad.universe,[25, 50, 75])
    nivel_suciedad['Graso'] = fuzzy.trimf(nivel_suciedad.universe,[50, 75, 100])
    nivel_suciedad['MuyGraso'] = fuzzy.trimf(nivel_suciedad.universe,[75, 100, 100])

    tipo_ropa['Gruesa'] = fuzzy.trimf(tipo_ropa.universe,[0, 25, 50])
    tipo_ropa['Media'] = fuzzy.trimf(tipo_ropa.universe,[25, 50, 75])
    tipo_ropa['Fina'] = fuzzy.trimf(tipo_ropa.universe,[50, 75, 100])

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
    # #R1: IF grado suciedad es Alto AND nivel de suciedad es Graso THEN tiempo de lavado es Muy largo.
    # r1 = ctrl.Rule(grado_suciedad['Alto'] & nivel_suciedad['Graso'],tiempo_lavado['muy_largo'])
    # #R2: IF grado suciedad es Medio AND nivel de suciedad es Graso THEN tiempo de lavado es Largo.
    # r2 = ctrl.Rule(grado_suciedad['Medio'] & nivel_suciedad['Graso'],tiempo_lavado['largo'])
    # #R3: IF grado suciedad es Bajo AND nivel de suciedad es Graso THEN tiempo de lavado es Medio.
    # r3 = ctrl.Rule(grado_suciedad['Bajo'] & nivel_suciedad['Graso'],tiempo_lavado['medio'])
    # #R4: IF grado suciedad es Alto AND nivel de suciedad es Medio THEN tiempo de lavado es Largo.
    # r4 = ctrl.Rule(grado_suciedad['Alto'] & nivel_suciedad['Medio'],tiempo_lavado['largo'])
    # #R5: IF grado suciedad es Medio AND nivel de suciedad es Medio THEN tiempo de lavado es Medio.
    # r5 = ctrl.Rule(grado_suciedad['Medio'] & nivel_suciedad['Medio'],tiempo_lavado['medio'])
    # #R6: IF grado suciedad es Bajo AND nivel de suciedad es Medio THEN tiempo de lavado es Medio.
    # r6 = ctrl.Rule(grado_suciedad['Bajo'] & nivel_suciedad['Medio'],tiempo_lavado['medio'])
    # #R7: IF grado suciedad es Alto AND nivel de suciedad es No Graso THEN tiempo de lavado es Medio.
    # r7 = ctrl.Rule(grado_suciedad['Alto'] & nivel_suciedad['NoGraso'],tiempo_lavado['medio'])
    # #R8: IF grado suciedad es Medio AND nivel de suciedad es No Graso THEN tiempo de lavado es Corto.
    # r8 = ctrl.Rule(grado_suciedad['Medio'] & nivel_suciedad['NoGraso'],tiempo_lavado['corto'])
    # #R9: IF grado suciedad es Bajo AND nivel de suciedad es No Graso THEN tiempo de lavado es Muy corto.
    # r9 = ctrl.Rule(grado_suciedad['Bajo'] & nivel_suciedad['NoGraso'],tiempo_lavado['muy_corto'])
    
    #RTF:
    rtf1 = ctrl.Rule(grado_suciedad['MuyBajo'] & nivel_suciedad['NoGraso'] & tipo_ropa['Fina'] , tiempo_lavado['muy_corto'])
    rtf2 = ctrl.Rule(grado_suciedad['MuyBajo'] & nivel_suciedad['PocoGraso'] & tipo_ropa['Fina'] , tiempo_lavado['muy_corto'])
    rtf3 = ctrl.Rule(grado_suciedad['MuyBajo'] & nivel_suciedad['MedioGraso'] & tipo_ropa['Fina'] , tiempo_lavado['corto'])
    rtf4 = ctrl.Rule(grado_suciedad['MuyBajo'] & nivel_suciedad['Graso'] & tipo_ropa['Fina'] , tiempo_lavado['corto'])
    rtf5 = ctrl.Rule(grado_suciedad['MuyBajo'] & nivel_suciedad['MuyGraso'] & tipo_ropa['Fina'] , tiempo_lavado['corto'])
    rtf6 = ctrl.Rule(grado_suciedad['Bajo'] & nivel_suciedad['NoGraso'] & tipo_ropa['Fina'] , tiempo_lavado['muy_corto'])
    rtf7 = ctrl.Rule(grado_suciedad['Bajo'] & nivel_suciedad['PocoGraso'] & tipo_ropa['Fina'] , tiempo_lavado['muy_corto'])
    rtf8 = ctrl.Rule(grado_suciedad['Bajo'] & nivel_suciedad['MedioGraso'] & tipo_ropa['Fina'] , tiempo_lavado['corto'])
    rtf9 = ctrl.Rule(grado_suciedad['Bajo'] & nivel_suciedad['Graso'] & tipo_ropa['Fina'] , tiempo_lavado['corto'])
    rtf10 = ctrl.Rule(grado_suciedad['Bajo'] & nivel_suciedad['MuyGraso'] & tipo_ropa['Fina'] , tiempo_lavado['medio'])
    rtf11 = ctrl.Rule(grado_suciedad['MedioSucio'] & nivel_suciedad['NoGraso'] & tipo_ropa['Fina'] , tiempo_lavado['muy_corto'])
    rtf12 = ctrl.Rule(grado_suciedad['MedioSucio'] & nivel_suciedad['PocoGraso'] & tipo_ropa['Fina'] , tiempo_lavado['corto'])
    rtf13 = ctrl.Rule(grado_suciedad['MedioSucio'] & nivel_suciedad['MedioGraso'] & tipo_ropa['Fina'] , tiempo_lavado['medio'])
    rtf14 = ctrl.Rule(grado_suciedad['MedioSucio'] & nivel_suciedad['Graso'] & tipo_ropa['Fina'] , tiempo_lavado['medio'])
    rtf15 = ctrl.Rule(grado_suciedad['MedioSucio'] & nivel_suciedad['MuyGraso'] & tipo_ropa['Fina'] , tiempo_lavado['largo'])
    rtf16 = ctrl.Rule(grado_suciedad['Alto'] & nivel_suciedad['NoGraso'] & tipo_ropa['Fina'] , tiempo_lavado['muy_corto'])
    rtf17 = ctrl.Rule(grado_suciedad['Alto'] & nivel_suciedad['PocoGraso'] & tipo_ropa['Fina'] , tiempo_lavado['corto'])
    rtf18 = ctrl.Rule(grado_suciedad['Alto'] & nivel_suciedad['MedioGraso'] & tipo_ropa['Fina'] , tiempo_lavado['medio'])
    rtf19 = ctrl.Rule(grado_suciedad['Alto'] & nivel_suciedad['Graso'] & tipo_ropa['Fina'] , tiempo_lavado['largo'])
    rtf20 = ctrl.Rule(grado_suciedad['Alto'] & nivel_suciedad['MuyGraso'] & tipo_ropa['Fina'] , tiempo_lavado['largo'])
    rtf21 = ctrl.Rule(grado_suciedad['MuyAlto'] & nivel_suciedad['NoGraso'] & tipo_ropa['Fina'] , tiempo_lavado['corto'])
    rtf22 = ctrl.Rule(grado_suciedad['MuyAlto'] & nivel_suciedad['PocoGraso'] & tipo_ropa['Fina'] , tiempo_lavado['medio'])
    rtf23 = ctrl.Rule(grado_suciedad['MuyAlto'] & nivel_suciedad['MedioGraso'] & tipo_ropa['Fina'] , tiempo_lavado['largo'])
    rtf24 = ctrl.Rule(grado_suciedad['MuyAlto'] & nivel_suciedad['Graso'] & tipo_ropa['Fina'] , tiempo_lavado['largo'])
    rtf25 = ctrl.Rule(grado_suciedad['MuyAlto'] & nivel_suciedad['MuyGraso'] & tipo_ropa['Fina'] , tiempo_lavado['muy_largo'])

    #RTM
    rtm1 = ctrl.Rule(grado_suciedad['MuyBajo'] & nivel_suciedad['NoGraso'] & tipo_ropa['Media'] , tiempo_lavado['muy_corto'])
    rtm2 = ctrl.Rule(grado_suciedad['MuyBajo'] & nivel_suciedad['PocoGraso'] & tipo_ropa['Media'] , tiempo_lavado['corto'])
    rtm3 = ctrl.Rule(grado_suciedad['MuyBajo'] & nivel_suciedad['MedioGraso'] & tipo_ropa['Media'] , tiempo_lavado['corto'])
    rtm4 = ctrl.Rule(grado_suciedad['MuyBajo'] & nivel_suciedad['Graso'] & tipo_ropa['Media'] , tiempo_lavado['corto'])
    rtm5 = ctrl.Rule(grado_suciedad['MuyBajo'] & nivel_suciedad['MuyGraso'] & tipo_ropa['Media'] , tiempo_lavado['corto'])
    rtm6 = ctrl.Rule(grado_suciedad['Bajo'] & nivel_suciedad['NoGraso'] & tipo_ropa['Media'] , tiempo_lavado['corto'])
    rtm7 = ctrl.Rule(grado_suciedad['Bajo'] & nivel_suciedad['PocoGraso'] & tipo_ropa['Media'] , tiempo_lavado['corto'])
    rtm8 = ctrl.Rule(grado_suciedad['Bajo'] & nivel_suciedad['MedioGraso'] & tipo_ropa['Media'] , tiempo_lavado['corto'])
    rtm9 = ctrl.Rule(grado_suciedad['Bajo'] & nivel_suciedad['Graso'] & tipo_ropa['Media'] , tiempo_lavado['corto'])
    rtm10 = ctrl.Rule(grado_suciedad['Bajo'] & nivel_suciedad['MuyGraso'] & tipo_ropa['Media'] , tiempo_lavado['medio'])
    rtm11 = ctrl.Rule(grado_suciedad['MedioSucio'] & nivel_suciedad['NoGraso'] & tipo_ropa['Media'] , tiempo_lavado['corto'])
    rtm12 = ctrl.Rule(grado_suciedad['MedioSucio'] & nivel_suciedad['PocoGraso'] & tipo_ropa['Media'] , tiempo_lavado['medio'])
    rtm13 = ctrl.Rule(grado_suciedad['MedioSucio'] & nivel_suciedad['MedioGraso'] & tipo_ropa['Media'] , tiempo_lavado['medio'])
    rtm14 = ctrl.Rule(grado_suciedad['MedioSucio'] & nivel_suciedad['Graso'] & tipo_ropa['Media'] , tiempo_lavado['medio'])
    rtm15 = ctrl.Rule(grado_suciedad['MedioSucio'] & nivel_suciedad['MuyGraso'] & tipo_ropa['Media'] , tiempo_lavado['largo'])
    rtm16 = ctrl.Rule(grado_suciedad['Alto'] & nivel_suciedad['NoGraso'] & tipo_ropa['Media'] , tiempo_lavado['corto'])
    rtm17 = ctrl.Rule(grado_suciedad['Alto'] & nivel_suciedad['PocoGraso'] & tipo_ropa['Media'] , tiempo_lavado['medio'])
    rtm18 = ctrl.Rule(grado_suciedad['Alto'] & nivel_suciedad['MedioGraso'] & tipo_ropa['Media'] , tiempo_lavado['largo'])
    rtm19 = ctrl.Rule(grado_suciedad['Alto'] & nivel_suciedad['Graso'] & tipo_ropa['Media'] , tiempo_lavado['largo'])
    rtm20 = ctrl.Rule(grado_suciedad['Alto'] & nivel_suciedad['MuyGraso'] & tipo_ropa['Media'] , tiempo_lavado['muy_largo'])
    rtm21 = ctrl.Rule(grado_suciedad['MuyAlto'] & nivel_suciedad['NoGraso'] & tipo_ropa['Media'] , tiempo_lavado['medio'])
    rtm22 = ctrl.Rule(grado_suciedad['MuyAlto'] & nivel_suciedad['PocoGraso'] & tipo_ropa['Media'] , tiempo_lavado['largo'])
    rtm23 = ctrl.Rule(grado_suciedad['MuyAlto'] & nivel_suciedad['MedioGraso'] & tipo_ropa['Media'] , tiempo_lavado['largo'])
    rtm24 = ctrl.Rule(grado_suciedad['MuyAlto'] & nivel_suciedad['Graso'] & tipo_ropa['Media'] , tiempo_lavado['muy_largo'])
    rtm25 = ctrl.Rule(grado_suciedad['MuyAlto'] & nivel_suciedad['MuyGraso'] & tipo_ropa['Media'] , tiempo_lavado['muy_largo'])

    #RTG
    rtg1 = ctrl.Rule(grado_suciedad['MuyBajo'] & nivel_suciedad['NoGraso'] & tipo_ropa['Gruesa'] , tiempo_lavado['corto'])
    rtg2 = ctrl.Rule(grado_suciedad['MuyBajo'] & nivel_suciedad['PocoGraso'] & tipo_ropa['Gruesa'] , tiempo_lavado['corto'])
    rtg3 = ctrl.Rule(grado_suciedad['MuyBajo'] & nivel_suciedad['MedioGraso'] & tipo_ropa['Gruesa'] , tiempo_lavado['corto'])
    rtg4 = ctrl.Rule(grado_suciedad['MuyBajo'] & nivel_suciedad['Graso'] & tipo_ropa['Gruesa'] , tiempo_lavado['medio'])
    rtg5 = ctrl.Rule(grado_suciedad['MuyBajo'] & nivel_suciedad['MuyGraso'] & tipo_ropa['Gruesa'] , tiempo_lavado['largo'])
    rtg6 = ctrl.Rule(grado_suciedad['Bajo'] & nivel_suciedad['NoGraso'] & tipo_ropa['Gruesa'] , tiempo_lavado['corto'])
    rtg7 = ctrl.Rule(grado_suciedad['Bajo'] & nivel_suciedad['PocoGraso'] & tipo_ropa['Gruesa'] , tiempo_lavado['corto'])
    rtg8 = ctrl.Rule(grado_suciedad['Bajo'] & nivel_suciedad['MedioGraso'] & tipo_ropa['Gruesa'] , tiempo_lavado['medio'])
    rtg9 = ctrl.Rule(grado_suciedad['Bajo'] & nivel_suciedad['Graso'] & tipo_ropa['Gruesa'] , tiempo_lavado['largo'])
    rtg10 = ctrl.Rule(grado_suciedad['Bajo'] & nivel_suciedad['MuyGraso'] & tipo_ropa['Gruesa'] , tiempo_lavado['largo'])
    rtg11 = ctrl.Rule(grado_suciedad['MedioSucio'] & nivel_suciedad['NoGraso'] & tipo_ropa['Gruesa'] , tiempo_lavado['corto'])
    rtg12 = ctrl.Rule(grado_suciedad['MedioSucio'] & nivel_suciedad['PocoGraso'] & tipo_ropa['Gruesa'] , tiempo_lavado['medio'])
    rtg13 = ctrl.Rule(grado_suciedad['MedioSucio'] & nivel_suciedad['MedioGraso'] & tipo_ropa['Gruesa'] , tiempo_lavado['medio'])
    rtg14 = ctrl.Rule(grado_suciedad['MedioSucio'] & nivel_suciedad['Graso'] & tipo_ropa['Gruesa'] , tiempo_lavado['largo'])
    rtg15 = ctrl.Rule(grado_suciedad['MedioSucio'] & nivel_suciedad['MuyGraso'] & tipo_ropa['Gruesa'] , tiempo_lavado['muy_largo'])
    rtg16 = ctrl.Rule(grado_suciedad['Alto'] & nivel_suciedad['NoGraso'] & tipo_ropa['Gruesa'] , tiempo_lavado['corto'])
    rtg17 = ctrl.Rule(grado_suciedad['Alto'] & nivel_suciedad['PocoGraso'] & tipo_ropa['Gruesa'] , tiempo_lavado['medio'])
    rtg18 = ctrl.Rule(grado_suciedad['Alto'] & nivel_suciedad['MedioGraso'] & tipo_ropa['Gruesa'] , tiempo_lavado['largo'])
    rtg19 = ctrl.Rule(grado_suciedad['Alto'] & nivel_suciedad['Graso'] & tipo_ropa['Gruesa'] , tiempo_lavado['muy_largo'])
    rtg20 = ctrl.Rule(grado_suciedad['Alto'] & nivel_suciedad['MuyGraso'] & tipo_ropa['Gruesa'] , tiempo_lavado['muy_largo'])
    rtg21 = ctrl.Rule(grado_suciedad['MuyAlto'] & nivel_suciedad['NoGraso'] & tipo_ropa['Gruesa'] , tiempo_lavado['medio'])
    rtg22 = ctrl.Rule(grado_suciedad['MuyAlto'] & nivel_suciedad['PocoGraso'] & tipo_ropa['Gruesa'] , tiempo_lavado['medio'])
    rtg23 = ctrl.Rule(grado_suciedad['MuyAlto'] & nivel_suciedad['MedioGraso'] & tipo_ropa['Gruesa'] , tiempo_lavado['largo'])
    rtg24 = ctrl.Rule(grado_suciedad['MuyAlto'] & nivel_suciedad['Graso'] & tipo_ropa['Gruesa'] , tiempo_lavado['muy_largo'])
    rtg25 = ctrl.Rule(grado_suciedad['MuyAlto'] & nivel_suciedad['MuyGraso'] & tipo_ropa['Gruesa'] , tiempo_lavado['muy_largo'])

    #asignar las reglas al sistema de control difuso definiendo una variable    

    # lavado_ctrl = ctrl.ControlSystem([r1,r2,r3,r4,r5,r6,r7,r8,r9])
    # lavado = ctrl.ControlSystemSimulation(lavado_ctrl)

    lavado_ctrl = ctrl.ControlSystem([rtg1,rtg2,rtg3,rtg4,rtg5,rtg6,rtg7,rtg8,rtg9,rtg10,rtg11,rtg12,rtg13,rtg14,rtg15,rtg16,rtg17,rtg18,rtg19,rtg20,rtg21,rtg22,rtg23,rtg24,rtg25,rtm1,rtm2,rtm3,rtm4,rtm5,rtm6,rtm7,rtm8,rtm9,rtm10,rtm11,rtm12,rtm13,rtm14,rtm15,rtm16,rtm17,rtm18,rtm19,rtm20,rtm21,rtm22,rtm23,rtm24,rtm25,rtf1,rtf2,rtf3,rtf4,rtf5,rtf6,rtf7,rtf8,rtf9,rtf10,rtf11,rtf12,rtf13,rtf14,rtf15,rtf16,rtf17,rtf18,rtf19,rtf20,rtf21,rtf22,rtf23,rtf24,rtf25])
    lavado = ctrl.ControlSystemSimulation(lavado_ctrl)

    lavado_ctrl_tg = ctrl.ControlSystem([rtg1,rtg2,rtg3,rtg4,rtg5,rtg6,rtg7,rtg8,rtg9,rtg10,rtg11,rtg12,rtg13,rtg14,rtg15,rtg16,rtg17,rtg18,rtg19,rtg20,rtg21,rtg22,rtg23,rtg24,rtg25])
    lavadoTg = ctrl.ControlSystemSimulation(lavado_ctrl_tg)
    lavado_ctrl_tm = ctrl.ControlSystem([rtm1,rtm2,rtm3,rtm4,rtm5,rtm6,rtm7,rtm8,rtm9,rtm10,rtm11,rtm12,rtm13,rtm14,rtm15,rtm16,rtm17,rtm18,rtm19,rtm20,rtm21,rtm22,rtm23,rtm24,rtm25])
    lavadoTm = ctrl.ControlSystemSimulation(lavado_ctrl_tm)
    lavado_ctrl_tf = ctrl.ControlSystem([rtf1,rtf2,rtf3,rtf4,rtf5,rtf6,rtf7,rtf8,rtf9,rtf10,rtf11,rtf12,rtf13,rtf14,rtf15,rtf16,rtf17,rtf18,rtf19,rtf20,rtf21,rtf22,rtf23,rtf24,rtf25])
    lavadoTf = ctrl.ControlSystemSimulation(lavado_ctrl_tf)

    def lavado_fuzzy(gradoS_Fuzzy, nivelS_Fuzzy, tipo_ropa_Fuzzy):

        lavadoraDifusa.lavado.input['grado_suciedad'] = gradoS_Fuzzy
        lavadoraDifusa.lavado.input['nivel_suciedad'] = nivelS_Fuzzy
        lavadoraDifusa.lavado.input['tipo_ropa'] = tipo_ropa_Fuzzy    
        #computar el sistema difuso respecto a las variables de entrada
        lavadoraDifusa.lavado.compute()
        lavadoraDifusa.tiempo_lavado.view(sim=lavadoraDifusa.lavado)
        return lavadoraDifusa.lavado.output['tiempo_lavado']

        # if tipo_ropa_Fuzzy == :
        #     lavadoraDifusa.lavadoTf.input['grado_suciedad'] = gradoS_Fuzzy
        #     lavadoraDifusa.lavadoTf.input['nivel_suciedad'] = nivelS_Fuzzy
        #     lavadoraDifusa.lavadoTf.input['tipo_ropa'] = tipo_ropa_Fuzzy    
        #     #computar el sistema difuso respecto a las variables de entrada
        #     lavadoraDifusa.lavadoTf.compute()
        #     lavadoraDifusa.tiempo_lavado.view(sim=lavadoraDifusa.lavadoTf)
        #     return lavadoraDifusa.lavadoTf.output['tiempo_lavado']

        # if tipo_ropa_Fuzzy == lavadoraDifusa.tipo_ropa['Gruesa'].label:
        #     lavadoraDifusa.lavadoTg.input['grado_suciedad'] = gradoS_Fuzzy
        #     lavadoraDifusa.lavadoTg.input['nivel_suciedad'] = nivelS_Fuzzy
        #     lavadoraDifusa.lavadoTg.input['tipo_ropa'] = nivel_ropa_Fuzzy    
        #     #computar el sistema difuso respecto a las variables de entrada
        #     lavadoraDifusa.lavadoTg.compute()
        #     lavadoraDifusa.tiempo_lavado.view(sim=lavadoraDifusa.lavadoTg)
        #     return lavadoraDifusa.lavadoTg.output['tiempo_lavado']
        # elif tipo_ropa_Fuzzy == lavadoraDifusa.tipo_ropa['Media'].label:
        #     lavadoraDifusa.lavadoTm.input['grado_suciedad'] = gradoS_Fuzzy
        #     lavadoraDifusa.lavadoTm.input['nivel_suciedad'] = nivelS_Fuzzy
        #     lavadoraDifusa.lavadoTm.input['tipo_ropa'] = nivel_ropa_Fuzzy    
        #     #computar el sistema difuso respecto a las variables de entrada
        #     lavadoraDifusa.lavadoTm.compute()
        #     lavadoraDifusa.tiempo_lavado.view(sim=lavadoraDifusa.lavadoTm)
        #     return lavadoraDifusa.lavadoTm.output['tiempo_lavado']
        # elif tipo_ropa_Fuzzy == lavadoraDifusa.tipo_ropa['Fina'].label:
        #     lavadoraDifusa.lavadoTf.input['grado_suciedad'] = gradoS_Fuzzy
        #     lavadoraDifusa.lavadoTf.input['nivel_suciedad'] = nivelS_Fuzzy
        #     lavadoraDifusa.lavadoTf.input['tipo_ropa'] = nivel_ropa_Fuzzy    
        #     #computar el sistema difuso respecto a las variables de entrada
        #     lavadoraDifusa.lavadoTf.compute()
        #     lavadoraDifusa.tiempo_lavado.view(sim=lavadoraDifusa.lavadoTf)
        #     return lavadoraDifusa.lavadoTf.output['tiempo_lavado']