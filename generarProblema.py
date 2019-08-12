import pygame
import random

def generarProblema(nivel):
#Devuelve una tupla con todo lo necesario para imprimir el problema en pantalla con su resultado y resultados falsos
#Los while del final son para asegurarse que no salga el resultado como opcion falsa y que no se repitan falsos
    op=random.choice("+-*") #Con el "/" se crashea, hay que arreglarlo
    if nivel == "facil":
        num1 = int(random.randrange(1,11,1))
        num2 = int(random.randrange(1,11,1))
    elif nivel == "medio":
        num1 = int(random.randrange(1,101,1))
        num2 = int(random.randrange(1,101,1))
    else:
        num1 = int(random.randrange(1,500,2))
        num2 = int(random.randrange(1,500,2))                    
    if (num1 < num2 and op == "-") or (num1<num2 and op == "/") or (num1 % num2 != 0 and op == "/"):
        devolver = generarProblema(nivel)
    else:
        resCorrecto = eval(str(num1)+op+str(num2))
        falso1 = falsear(num1,num2,op)
        while falso1 == resCorrecto:
            falso1 = falsear(num1,num2,op)
        falso2 = falsear(num1,num2,op)
        while falso1 == falso2 or falso2 == resCorrecto:
            falso2 = falsear(num1,num2,op)
        falso3 = falsear(num1,num2,op)
        while falso1 == falso3 or falso2 == falso3 or falso3 == resCorrecto:
            falso3 = falsear(num1,num2,op)
        devolver = (resCorrecto,num1,num2,op,falso1,falso2,falso3)
    return devolver

def generarProblemaEspecial(nivel):
#No se que vamos a hacer de problema especial
    pass

def falsear(x,y,op):
#Funcion auxiliar para devolver valores falsos
    num1 = x + int(random.randrange(-3,3))
    num2 = y + int(random.randrange(-3,3))
    return eval(str(num1)+op+str(num2))

