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