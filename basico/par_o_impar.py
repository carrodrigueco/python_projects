while True:
    numero=input(">>> Buenos dias ingrese el numero que desee verificar...")
    try:
        try:
            explode=numero.index(".")
        except:
            explode=0
        if explode==0:
            numero=int(numero)
        else:
            print(">>> El numero ingresado es un decimal, se le quitaran los decimales...")
            numero=float(numero)
    except:
        print(">>> Error lo ingresado no es un numero...")
        continue
    if numero%2==0:
        print(">>>El numero ingresado es un numero par...")
    else:
        print(">>>El numero ingresado es un numero impar...")
    while True:
        deci=input(">>> Desea ingresar otro numero...[1.Si 2.No]")
        try:
            deci=int(deci)
        except:
            print(">>> Error al ingresar su eleccion...")
            continue
        break
    if deci==2:
        break