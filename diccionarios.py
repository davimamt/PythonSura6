#Los diccionarios son variables espciales que me permiten almacenar multiples datps de diferente tipo en una sola variable

empelado = {
    'nombre': "David",
    'ceudula': "684654",
    'cargo': "Analista de datos",
    'salario':5700000,
    'horasTrabajadas':240,
    'aplicaSubsidioTransporte':False,
    'deudas':[1500000,800000]
}


#print(empelado)
#print(empelado['deudas'][1])


#Recorriendo un diccionario:

for observadorAtributo, observadorValor in empelado.items():
    print(observadorAtributo)
    print(observadorValor)
    