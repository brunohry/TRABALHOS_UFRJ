#!/usr/bin/python2
# Laboratorio 11.1 : Bruno Hryniewicz dos Santos Cruz

def mdc(a,b):
    while True:
        if b==0:
            return a
        #se nao, devolve b como a, e b como a modulo b (resto) 
        else:
            aux=a
            a=b
            b=aux%b


def totiente (n):
    lista=[]
    for i in range (1,n):
        a =  mdc(i,n)
        if a==1:
            lista.append(i)
    return lista


def geraSubgrupo ():
    n = input ()
    grup=totiente(n)
    print grup
    for i in grup:
        lista=[i]
        cont =0
        while lista[cont] != 1:
            lista.append (lista[cont]*i%n)
            cont+=1
        lista.sort()
        print lista

#recebendo a quantidade de numeros
x=input()
#loop principal
for i in range (x):
    #recebendo numeros
    geraSubgrupo()
    print'---'

