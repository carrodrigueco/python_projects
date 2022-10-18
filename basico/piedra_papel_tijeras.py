from random import randint
import time
print(">>> Bienvenido a Piedra, Papel o Tijeras <<<")

while True:

    jugador=input(">>> Escoge...[1.Piedra 2.Papel 3.Tijeras]")
    try:
        jugador=int(jugador)
        if jugador!=1 and jugador!=2 and jugador!=3:
            print(">>> Error al escoger...")
            continue
    except:
        print(">>> Error al escoger...")
        continue
    print(">>> Ahora la computadora escogera...")
    time.sleep(1)

    pc=randint(1,3)
    if pc==1:
        mensaje="Piedra"
    if pc==2:
        mensaje="Papel"
    else:
        mensaje="Tijera"    
    print(f">>> La computadora a escogido {mensaje}")
    time.sleep(1)

    if jugador==pc:
        resultado="Empataron"
    elif (jugador==1 and pc==3) or (jugador==2 and pc==1) or (jugador==3 and pc==2):
        resultado="Ganaste"
    else:
        resultado="Perdiste"
    print(f">>> El resultado del enfrentamiento es que {resultado}...Gracias por jugar")
    
    while True:
        deci=input(">>> Desea volver a jugar?...[1.Si 2.No]")
        try:
            deci=int(deci)
        except:
            print(">>> Error al ingresar su eleccion...")
            continue
        break
    if deci==2:
        break


