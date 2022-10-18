input(">>> Calculador de propinas...Press Enter to continue...")
factura=-1
opcion_propina=-1
deci=-1
numero_personas=1
lst=[0.18, 0.2, 0.25]
while True:
    if factura==-1:
        factura=input(">>> Ingrese la factura total por favor...")
        try:
            factura=float(factura)
        except:
            print(">>> Error lo ingresado debe ser un numero...")
            factura=-1
            continue

    if opcion_propina==-1:
        opcion_propina=input(">>> Cuanto es el porcentaje de propina que desea calcular...[1.18%"+" 2.20%"+" 3.25%]")
        try:
            opcion_propina=int(opcion_propina)
        except:
            print(">>> Error la debe ser una de las opciones...")
            opcion_propina=-1
            continue

    if deci==-1:
        deci=input(">>> Desea calcular para mas de una persona?...[1.Si 2.No]")
        try:
            deci=int(deci)
        except:
            print(">>> Error al ingresar su eleccion...")
            deci=-1
            continue

    if deci==1:
        numero_personas=input(">>> Para cuantas personas desea calcular?...")
        try:
            numero_personas=int(numero_personas)
        except:
            print("Error el numero de personas debe ser un entero...")
            continue
    propina=factura*(lst[opcion_propina-1])
    propina=round(propina,2)
    print(f">>> La propina aplicando el {int(lst[opcion_propina-1]*100)}% es {propina}$, que contabiliza un total de {round(factura+propina,2)}, entre {numero_personas} personas...")
    break
