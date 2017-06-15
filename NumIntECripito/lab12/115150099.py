#!/usr/bin/python2
# Laboratorio 12 : Bruno Hryniewicz dos Santos Cruz
def fatora(a):
    fator=2
    #iniciando uma lista
    fatores=[]
    fatoresnew=[]
    i=0
    while fator<=a:
        if a%fator==0:
            a=a/fator
            fatores.append(fator)
        else:
            fator=fator+1
        i=i +1
    i=0
    #excluindo o zero usado para iniciar a lista
    cont=1
    while i<len(fatores)-1:
        if fatores[i]==fatores[i+1]:
            cont=cont+1
        else:
            print fatores[i],cont
            fatoresnew.append(fatores[i])
            fatoresnew.append(cont)
            cont=1
        i=i+1
    # tratando o caso dos ultimo print
    print fatores[i],cont
    fatoresnew.append(fatores[i])
    fatoresnew.append(cont)
    return fatoresnew
def mdc(a,b):
    r=a%b
    #se resto ==0 parar a recursao
    if r==0:
        return b
    #se nao, devolve b como a, e b como a modulo b (resto) 
    else:
        return mdc (b,a%b)
def Gauss ():
    p=input()
    g=1
    fatoresnew=fatora(p-1)
    geradores=[]
    for i in range (0,len(fatoresnew),2):
        a=2
        while (a**((p-1)/fatoresnew[i]))%(p) ==1:
            a+=1
        h=(a**((p-1)/(fatoresnew[i]**fatoresnew[i+1]))) % p
        g=((g*h)%p)
        print fatoresnew[i],a,h
    print g
    for i in range (1,p):
        a=mdc(i,p-1)
        if a==1:
            geradores.append(int(g**i%p))
    geradores.sort()
    print geradores





#recebendo a quantidade de numeros
x=input()
#loop principal
for i in range (x):
    #recebendo numeros
    Gauss()
    print '---'

