#----PARTE B-DICCIONARIOS EN PYTHON----

#Punto 11

ponderado = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10}

#Punto 12

simbolos=["♥","♦","♣","♠"]

#Punto 13

def combinar(dicc,lista):
    baraja={}
    cont=1
    for valor in dicc:
        for i in lista:
            baraja.setdefault(valor+" "+i,cont)
        if cont<10:
            cont+=1
    return baraja

baraja = combinar(ponderado,simbolos)

#Punto 14

from random import randint

def revolver(diccionario):
    dic_new=[]
    for llave in diccionario:
        valor=diccionario.get(llave)
        indice=randint(0,20)
        dic_new.insert(indice,(llave,valor))
    dic_new=dict(dic_new)
    return dic_new

baraja = revolver(baraja)

#Punto 15

cartas_jugador=[]
cartas_tallador=[]

#Punto 16

baraja_original=baraja.copy()

def repartir(baraja,cartas):
    llaves=[f for f in baraja]
    valores=[baraja[f] for f in baraja]
    nbaraja={}
    if len(cartas)==0:
        for i in range(2):
            indice=randint(0,len(llaves)-1)
            cartas.append(llaves.pop(indice))
            valores.pop(indice)
    else:
        indice=randint(0,len(llaves)-1)
        cartas.append(llaves.pop(indice))
        valores.pop(indice)
    
    for i in range(len(llaves)):
        nbaraja[llaves[i]]=valores[i]
    return nbaraja
    return cartas

#Punto 17

def sumar_cartas(cartas,baraja_original):
    acum=0
    ases=False
    for i in baraja_original:
        for x in range(len(cartas)):
            if "A" == cartas[x][0]:
                ases=True
            elif i==cartas[x]:
                acum=acum+baraja_original.get(i)
            
    if ases:
        if (acum+11)>=22:
            acum=1+acum
        else:
            acum=acum+11
    return acum

#Punto 18

def mostrar(cartas,total,tp_jugador):
    print("╔═══════════════════════════════════════════╗")
    print("  El {} posee el siguiente mazo:".format(tp_jugador))
    print(" ",cartas,"\n  Acumulado: ",total)
    print("╚═══════════════════════════════════════════╝")

#Punto 19 y 20

#Las proximas lineas de codigo controlan las mecanicas del juego
cont_tallador=1
cont_rondas=1
contg_jugador=0             #Número de rondas ganadas por el jugador
contg_tallador=0            #Número de rondas ganadas por el tallador 
ganador=False             #Evaluar si hay blackjack            
perdedor=False            #Evaluar si el jugador pierde en alguno de sus turnos.
jugador=True

while True:
    #Las proximas lineas de codigo se evaluan al jugador.
    print("\033[3;37;40m \nRonda #{}\033[0;37;40m \n".format(cont_rondas))

    cont=0                        
    while jugador:
        baraja=repartir(baraja,cartas_jugador)
        total_jugador=sumar_cartas(cartas_jugador,baraja_original)

        if total_jugador==21:
            mostrar(cartas_jugador,total_jugador,"jugador")
            if cont==0:
                print("\033[1;37;40m Ganador Jugador.\033[0;37;40m \n")
                contg_jugador+=1
                ganador=True
                jugador=False
            else:
                continuar=input("¿Desea más cartas?\n(SI/NO): ")
        elif total_jugador>21:
            mostrar(cartas_jugador,total_jugador,"jugador")
            print("\033[1;37;40m El jugador ha perdido.\n Juego Finalizado.\033[0;37;40m \n")
            contg_tallador+=1
            perdedor=True
            jugador=False
        else:
            mostrar(cartas_jugador,total_jugador,"jugador")
            continuar=input("¿Desea más cartas?\n(SI/NO): ")
        if continuar.lower()=="si":
            cont+=1
            continue
        elif continuar.lower()=="no":
            jugador=False
        else:
            raise TypeError("Error al digitar respuesta.")

    if ganador or perdedor:
        ganador=False                
        perdedor=False            
        jugador=True
    else:
        #Las proximas lineas de codigo se encargan de evaluar al tallador.
        while True:
            print("\nTallador: Intento {}".format(cont_tallador))
            baraja=repartir(baraja,cartas_tallador)
            total_tallador=sumar_cartas(cartas_tallador,baraja_original)

            if total_tallador==21 and total_jugador!=total_tallador:
                mostrar(cartas_tallador,total_tallador,"tallador")
                print("Acumulado Tallador:{}      Acumulado Jugador:{}".format(total_tallador,total_jugador))
                print("\033[1;37;40m Ganador Tallador.\033[0;37;40m \n")
                contg_tallador+=1
                break
            elif total_jugador==total_tallador:
                mostrar(cartas_tallador,total_tallador,"tallador")
                print("Acumulado Tallador:{}      Acumulado Jugador:{}".format(total_tallador,total_jugador))
                print("\033[1;37;40m Ganador Tallador.\033[0;37;40m \n")
                contg_tallador+=1
                break
            elif total_tallador>total_jugador and total_tallador<=21:
                mostrar(cartas_tallador,total_tallador,"tallador")
                print("Acumulado Tallador:{}      Acumulado Jugador:{}".format(total_tallador,total_jugador))
                print("\033[1;37;40m Ganador Tallador.\033[0;37;40m \n")
                contg_tallador+=1
                break
            elif total_tallador>21:
                mostrar(cartas_tallador,total_tallador,"tallador")
                print("Acumulado Tallador:{}      Acumulado Jugador:{}".format(total_tallador,total_jugador))
                print("\033[1;37;40m Ganador Jugador.\n Juego Finalizado\033[0;37;40m \n")
                contg_jugador+=1
                break
            else:
                mostrar(cartas_tallador,total_tallador,"tallador")
            cont_tallador+=1
    print("\033[3;37;40m # Rondas ganadas por el jugador: {}.\n # Rondas ganadas por el tallador: {}.\033[0;37;40m \n".format(contg_jugador,contg_tallador))
    
    next_round=input("¿Desea seguir jugando?\n(SI/NO): ")
    if next_round.lower()=="si":            #Reset de todas las variables
        cartas_jugador.clear()
        total_jugador=0
        cartas_tallador.clear()
        total_tallador=0
        baraja = combinar(ponderado,simbolos)
        baraja = revolver(baraja)
        baraja_original=baraja.copy()
        cont_rondas+=1
        ganador=False                
        perdedor=False            
        jugador=True
        cont_tallador=0
        continue
    elif next_round.lower()=="no":
        break
    else:
        raise TypeError("Error al digitar respuesta.")