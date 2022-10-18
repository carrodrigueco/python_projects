from random import randint
import time
numero = -1
intentos = 1
print(">>> Bienvenido a adivina el numero <<<")
time.sleep(1)
while True:

    if numero == -1:
        print(">>> Estoy pensando en un numero entero entre 1 y 50...")
        time.sleep(1)
        numero = randint(1, 50)

    jugador = input(">>> ¡Adivina el numero en que estoy pensado!...")
    try:
        jugador = int(jugador)
    except:
        print(">>> Error lo ingresado no es un numero(No se aceptan decimales)...")
        continue
    if jugador < 1 or jugador > 50:
        print(">>> Error el numero debe estar entre 1 y 50...")
        continue

    if numero == jugador:
        print(f">>> ¡Acertaste el numero era {numero}, Felicidades!...El numero de intentos fue {intentos}...")
    else:
        print(">>> Nop, ese no es el numero...")
        time.sleep(1)
        while True:
            deci = input(">>> Desea seguir intentando?...[1.Si 2.No]")
            try:
                deci = int(deci)
            except:
                print(">>> Error al ingresar su eleccion...")
                continue
            break
        if deci == 2:
            print(f">>> Como te rendiste con solo {intentos} intentos?...")
            break
        else:
            intentos += 1