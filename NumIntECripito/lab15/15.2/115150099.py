#!/usr/bin/python2
# Laboratorio 15.2 : Bruno Hryniewicz dos Santos Cruz
from math import sqrt
def PotencializaModulo (base,exp,mod):
    r=1
    a=base
    e=exp
    while e!=0:
        if (e%2)!=0:
            r=(r*a)%mod
            e=(e-1)/2
        else:
            e=e/2
        a=(a*a)%mod
    return r

def InversMulti(a,b):
    #definindo x e y iniciais
    x=[1,0]
    y=[0,1]
    #printando as duas primeiras linhas    #recebendo valor de r para q=0
    r=[b]
    #contador 
    i=0
    while r[i]>0:
        #obtendo e printando de uma linha q, r ,x, y
        q=a/b
        r.append(a%b)
        x.append(x[i]-x[i+1]*q)
        y.append(y[i]-y[i+1]*q)
        #tratando o caso do print quando r==0 
        if r[i+1]==0:
            return x[i+1]
        #andand de linha na tabela (transformando linha atual na linha de cima
        i=i+1
        a=b
        b=r[i]

def Baby (baby,m,g,p):
    for j in range (0,m):
        aux= PotencializaModulo(g,j,p)
        baby.append(aux)
        print j, aux
    return Baby

def BabyAndGigantSteps ():
    g,h,p = input()
    m = int(sqrt((p-1)))+1
    print m
    baby=[]
    Baby(baby,m,g,p)
    gLinha = InversMulti ( g , p )
    t = PotencializaModulo(gLinha, m , p)
    for i  in range (0,m):
        aux = PotencializaModulo(t,i,p)*h %p
        print i, aux
        if baby.count(aux) > 0:
            j=baby.index(aux)
            print i,j
            print i*m+j
            return









    




#recebendo a quantidade de numeros
x=input()
#loop principal
for i in range (x):
	#recebendo numeros
	BabyAndGigantSteps()
	print "---"



